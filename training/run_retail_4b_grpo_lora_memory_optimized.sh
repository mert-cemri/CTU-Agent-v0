#!/bin/bash

# Memory-Optimized GRPO Training with LoRA on Retail Domain - 4B Model
# This script reduces memory usage through aggressive optimizations

# Memory optimization environment variables
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TORCH_CUDA_MEMORY_FRACTION=0.9

# Configuration for 4B model with LoRA (memory optimized)
NUM_GPUS=8
NUM_INFERENCE_ENGINES=1  # Reduced from 2 to save memory
TENSOR_PARALLEL_SIZE=2   # Reduced from 4 to 2
EPOCHS=100

# Model Configuration
POLICY_MODEL="Qwen/Qwen3-4B-Instruct-2507"
REF_MODEL="Qwen/Qwen3-4B-Instruct-2507"
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_retail_grpo_lora_memory_opt_v0

# LoRA Configuration for 4B model (smaller rank for memory savings)
LORA_RANK=16     # Reduced from 32 to 16
LORA_ALPHA=32    # Reduced from 64 to 32
LORA_DROPOUT=0.05

# Memory-optimized Directory Setup
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
CKPT_DIR="training/outputs/$TIMESTAMP/checkpoints"
EXPORT_DIR="training/exports/$TIMESTAMP"
WANDB_PROJECT="tau_bench_retail_grpo_lora_memory_opt"
WANDB_RUN_NAME="${MODEL_NAME_SANITIZED}_$(date +%m%d_%H%M)"

# Create directories
mkdir -p "$CKPT_DIR"
mkdir -p "$EXPORT_DIR"

echo "=========================================="
echo "Memory-Optimized LoRA GRPO Training - Retail Domain"
echo "Model: $POLICY_MODEL"
echo "LoRA Rank: $LORA_RANK, Alpha: $LORA_ALPHA"
echo "Batch size optimizations: AGGRESSIVE"
echo "Checkpoint: $CKPT_DIR"
echo "Export: $EXPORT_DIR"
echo "=========================================="

# Run from root directory
cd "$(dirname "$0")" || exit 1

# Memory-optimized training command
python training/main_tau_bench.py \
  trainer.placement.policy_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.critic_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.reward_num_gpus_per_node=$NUM_GPUS \
  generator.num_inference_engines=$NUM_INFERENCE_ENGINES \
  generator.inference_engine_tensor_parallel_size=$TENSOR_PARALLEL_SIZE \
  trainer.ckpt_path="$CKPT_DIR" \
  trainer.resume_path=null \
  trainer.export_path="$EXPORT_DIR" \
  trainer.epochs=$EPOCHS \
  trainer.train_batch_size=8 \
  trainer.policy_mini_batch_size=4 \
  trainer.critic_mini_batch_size=4 \
  trainer.micro_train_batch_size_per_gpu=1 \
  trainer.micro_forward_batch_size_per_gpu=1 \
  trainer.max_prompt_length=8192 \
  trainer.eval_batch_size=2 \
  trainer.eval_before_train=false \
  trainer.eval_interval=20 \
  trainer.policy.optimizer_config.lr=1.0e-5 \
  trainer.policy.optimizer_config.num_warmup_steps=50 \
  trainer.policy.optimizer_config.weight_decay=0.01 \
  trainer.policy.optimizer_config.max_grad_norm=1.0 \
  trainer.policy.optimizer_config.offload_after_step=true \
  trainer.policy.fsdp_config.cpu_offload=true \
  trainer.policy.fsdp_config.reshard_after_forward=true \
  trainer.policy.model.lora_rank=$LORA_RANK \
  trainer.policy.model.lora_alpha=$LORA_ALPHA \
  trainer.policy.model.lora_dropout=$LORA_DROPOUT \
  trainer.ref.fsdp_config.cpu_offload=true \
  trainer.critic.fsdp_config.cpu_offload=true \
  trainer.reward.fsdp_config.cpu_offload=true \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.01 \
  trainer.algorithm.eps_clip_low=0.1 \
  trainer.algorithm.eps_clip_high=0.1 \
  trainer.algorithm.value_clip=0.1 \
  trainer.ckpt_interval=20 \
  trainer.hf_save_interval=50 \
  trainer.use_sample_packing=false \
  trainer.gradient_checkpointing=true \
  trainer.gradient_checkpointing_use_reentrant=false \
  generator.max_turns=10 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=2 \
  generator.gpu_memory_utilization=0.7 \
  generator.max_input_length=8192 \
  generator.max_num_batched_tokens=8192 \
  generator.enforce_eager=true \
  generator.enable_prefix_caching=false \
  generator.enable_chunked_prefill=false \
  environment.skyrl_gym.tau_bench.max_turns=10 \
  environment.skyrl_gym.tau_bench.use_native_tool_calling=false \
  wandb.project=$WANDB_PROJECT \
  wandb.name=$WANDB_RUN_NAME

echo "Memory-optimized training completed!"
echo "Checkpoint saved to: $CKPT_DIR"
echo "Model exported to: $EXPORT_DIR"