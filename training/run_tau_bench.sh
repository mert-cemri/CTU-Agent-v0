#!/bin/bash
# set -x

# # Activate conda environment
# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate ctu

# Tau Bench Training Script
# Train Qwen2.5-3B-Instruct on tau_bench multi-domain conversational AI tasks

# Configuration

NUM_GPUS=8
NUM_INFERENCE_ENGINES=2
TENSOR_PARALLEL_SIZE=4
EPOCHS=50

# Model Configuration - Upgraded to more powerful 3B model
POLICY_MODEL="Qwen/Qwen2.5-3B-Instruct"
REF_MODEL="Qwen/Qwen2.5-3B-Instruct"
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_v1-multi-domain

# Make sure required directories exist
CKPT_DIR="$HOME/ckpts/tau_bench/${MODEL_NAME_SANITIZED}"
DATA_DIR="data/tau_bench_retail"

mkdir -p $DATA_DIR

# Clean up existing checkpoints for fresh start
if [ -d "$CKPT_DIR" ]; then
    echo "Removing existing checkpoints at: $CKPT_DIR"
    rm -rf "$CKPT_DIR"
fi
mkdir -p $CKPT_DIR

# # Environment variables
export WANDB_API_KEY=${WANDB_API_KEY:-"your_wandb_api_key"}
export OPENAI_API_KEY=${OPENAI_API_KEY:-"your_openai_api_key"}
export DEBUG_PARSER=1

# Ray environment variable for UV support
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

# Training command
cd "$(dirname "$0")"

# Add SkyRL modules to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL_mod/skyrl-train:$(pwd)/../SkyRL_mod/skyrl-gym:$(pwd)/../tau_bench:$(pwd)/../tau_bench_env:$(pwd)/../data_prep:$(pwd)/.."

# Kill any existing Ray processes to ensure clean start
ray stop || true

HYDRA_FULL_ERROR=1 CUDA_LAUNCH_BLOCKING=1 python main_tau_bench.py \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
  trainer.policy.model.path="$POLICY_MODEL" \
  trainer.ref.model.path="$REF_MODEL" \
  trainer.placement.policy_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.ref_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.critic_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.reward_num_gpus_per_node=$NUM_GPUS \
  generator.num_inference_engines=$NUM_INFERENCE_ENGINES \
  generator.inference_engine_tensor_parallel_size=$TENSOR_PARALLEL_SIZE \
  trainer.ckpt_path="$CKPT_DIR" \
  trainer.export_path="$HOME/exports/tau_bench" \
  trainer.epochs=$EPOCHS \
  trainer.train_batch_size=128 \
  trainer.policy_mini_batch_size=32 \
  trainer.micro_train_batch_size_per_gpu=1 \
  trainer.micro_forward_batch_size_per_gpu=1 \
  trainer.max_prompt_length=8192 \
  trainer.eval_batch_size=64 \
  trainer.eval_before_train=true \
  trainer.eval_interval=2 \
  trainer.policy.optimizer_config.lr=5.0e-6 \
  trainer.policy.optimizer_config.num_warmup_steps=100 \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.001 \
  trainer.ckpt_interval=10 \
  trainer.hf_save_interval=20 \
  trainer.use_sample_packing=false \
  generator.max_turns=20 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=3 \
  generator.gpu_memory_utilization=0.7 \
  generator.max_input_length=8192 \
  generator.enforce_eager=true \
  generator.sampling_params.max_generate_length=1024 \
  generator.sampling_params.temperature=1.0 \
  generator.sampling_params.top_p=0.9 \
  generator.override_existing_update_group="force_new" \
  generator.use_native_tool_calling=true \
  environment.env_class="tau_bench" \
  environment.skyrl_gym.tau_bench.user_strategy="llm" \
  environment.skyrl_gym.tau_bench.user_model="gpt-4o" \
  environment.skyrl_gym.tau_bench.user_provider="openai" \
  environment.skyrl_gym.tau_bench.max_turns=10 \
  environment.skyrl_gym.tau_bench.use_native_tool_calling=true \
  environment.skyrl_gym.max_env_workers=16 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_rl" \
  trainer.run_name="tau_bench_qwen2_5_3b_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=none \
  $@

echo "Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Exports saved to: $HOME/exports/tau_bench" 

#6 from 20