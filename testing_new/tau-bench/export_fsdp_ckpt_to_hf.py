#!/usr/bin/env python3
"""
Export a sharded FSDP checkpoint to HuggingFace safetensors format.

Example:
  /data/mert/miniconda3/envs/sky/bin/python export_fsdp_ckpt_to_hf.py \
    --ckpt-dir /data/mert/ckpts/.../global_step_120/policy \
    --output-dir /data/mert/ckpts/.../global_step_120/policy/huggingface \
    --base-model Qwen/Qwen3-8B \
    --strategy fsdp2 \
    --lora-rank 64 --lora-alpha 128 --lora-dropout 0.05 \
    --target-modules all-linear \
    --num-gpus 2
"""

import argparse
import os
import re

import hydra
from omegaconf import OmegaConf
import ray
from transformers import AutoTokenizer
from ray.util.placement_group import placement_group

from skyrl_train.entrypoints.main_base import config_dir
from skyrl_train.workers.worker import PPORayActorGroup
from skyrl_train.utils import get_ray_pg_ready_with_timeout


def _infer_world_size(ckpt_dir: str) -> int:
    for name in os.listdir(ckpt_dir):
        match = re.match(r"model_world_size_(\d+)_rank_0\.pt", name)
        if match:
            return int(match.group(1))
    raise FileNotFoundError(
        f"Could not infer world_size from {ckpt_dir}. "
        "Expected a file like model_world_size_2_rank_0.pt"
    )


def _get_policy_worker(strategy: str):
    if strategy in ("fsdp", "fsdp2"):
        from skyrl_train.workers.fsdp.fsdp_worker import PolicyWorker

        return PolicyWorker
    if strategy == "deepspeed":
        from skyrl_train.workers.deepspeed.deepspeed_worker import PolicyWorker

        return PolicyWorker
    raise ValueError(f"Unsupported strategy: {strategy}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export FSDP checkpoint to HF safetensors.")
    parser.add_argument("--ckpt-dir", required=True, help="Path to policy checkpoint dir (contains model_world_size_*).")
    parser.add_argument("--output-dir", required=True, help="Path to write HF model (config + safetensors).")
    parser.add_argument("--base-model", required=True, help="Base model id or local path used for initialization.")
    parser.add_argument("--strategy", default="fsdp2", choices=["fsdp", "fsdp2", "deepspeed"])
    parser.add_argument("--lora-rank", type=int, default=0)
    parser.add_argument("--lora-alpha", type=int, default=16)
    parser.add_argument("--lora-dropout", type=float, default=0.0)
    parser.add_argument("--target-modules", default="all-linear")
    parser.add_argument("--num-gpus", type=int, default=0, help="World size used for the checkpoint.")
    args = parser.parse_args()

    ckpt_dir = os.path.abspath(args.ckpt_dir)
    output_dir = os.path.abspath(args.output_dir)

    inferred_world_size = _infer_world_size(ckpt_dir)
    num_gpus = args.num_gpus or inferred_world_size
    if num_gpus != inferred_world_size:
        raise ValueError(
            f"--num-gpus ({num_gpus}) must match checkpoint world_size ({inferred_world_size})."
        )

    with hydra.initialize_config_dir(config_dir=config_dir, version_base=None):
        cfg = hydra.compose(config_name="ppo_base_config")

    # Allow adding LoRA fields that aren't present in the base config struct.
    OmegaConf.set_struct(cfg, False)

    cfg.trainer.strategy = args.strategy
    cfg.trainer.target_modules = args.target_modules
    cfg.trainer.policy.model.path = args.base_model
    cfg.trainer.policy.model.lora_rank = args.lora_rank
    cfg.trainer.policy.model.lora_alpha = args.lora_alpha
    cfg.trainer.policy.model.lora_dropout = args.lora_dropout
    cfg.trainer.placement.policy_num_gpus_per_node = num_gpus
    cfg.trainer.train_batch_size = max(1, num_gpus)
    cfg.trainer.micro_train_batch_size_per_gpu = 1
    cfg.trainer.policy.sequence_parallel_size = 1

    os.makedirs(output_dir, exist_ok=True)

    ray.init(ignore_reinit_error=True)

    pg = placement_group([{"GPU": num_gpus, "CPU": num_gpus}], strategy="PACK")
    get_ray_pg_ready_with_timeout(pg, timeout=60)

    policy_worker = _get_policy_worker(cfg.trainer.strategy)
    actor_group = PPORayActorGroup(
        cfg=cfg,
        num_nodes=1,
        num_gpus_per_node=num_gpus,
        ray_actor_type=policy_worker,
        pg=pg,
        num_gpus_per_actor=1,
        colocate_all=False,
        sequence_parallel_size=cfg.trainer.policy.sequence_parallel_size,
        record_memory=False,
    )

    # Initialize model from base weights, then load sharded checkpoint.
    ray.get(actor_group.async_init_model(cfg.trainer.policy.model.path))
    # Some environments expose `load_ckpt`, others expose `load_checkpoint`.
    try:
        ray.get(
            actor_group.async_run_ray_method(
                "pass_through",
                "load_ckpt",
                ckpt_dir=ckpt_dir,
                load_optimizer_states=False,
                load_lr_scheduler_states=False,
                load_module_only=True,
            )
        )
    except AttributeError:
        ray.get(
            actor_group.async_run_ray_method(
                "pass_through",
                "load_checkpoint",
                ckpt_dir=ckpt_dir,
                load_optimizer_states=False,
                load_lr_scheduler_states=False,
            )
        )

    tokenizer = AutoTokenizer.from_pretrained(args.base_model, trust_remote_code=True)
    ray.get(
        actor_group.async_run_ray_method(
            "pass_through",
            "save_hf_model",
            export_dir=output_dir,
            tokenizer=tokenizer,
        )
    )

    ray.shutdown()
    print(f"Export complete: {output_dir}")


if __name__ == "__main__":
    main()
