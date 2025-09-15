#!/bin/bash

# GRPO Training on Retail Domain - 3B Model (Vanilla)
# This script trains Qwen2.5-3B-Instruct on retail domain only using standard GRPO

# Configuration
NUM_GPUS=8
NUM_INFERENCE_ENGINES=2
TENSOR_PARALLEL_SIZE=4
EPOCHS=100

# Model Configuration
# Replace this path with your SFT model path
# POLICY_MODEL="mcemri/qwen2.5_3b_alldata_sft_v0"  # e.g., "/root/ckpts/your_sft_model" or "mcemri/qwen2.5_3b_alldata_sft_v0"
POLICY_MODEL="Qwen/Qwen2.5-3B-Instruct"
REF_MODEL="Qwen/Qwen2.5-3B-Instruct"  # Keep vanilla model as reference for KL regularization
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_retail_grpo_vanilla_after_sft_v3

# Data Configuration - Using retail domain only
DATA_DIR="data/tau_bench_retail"

# Get the CTU-Agent-v0 root directory
CTU_ROOT="$(dirname "$(dirname "$(realpath "$0")")")"

# Make sure required directories exist with unique run names
RUN_TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
CKPT_DIR="$CTU_ROOT/checkpoints/tau_bench/${MODEL_NAME_SANITIZED}_${RUN_TIMESTAMP}"
EXPORT_DIR="$CTU_ROOT/exports/tau_bench_retail_${RUN_TIMESTAMP}"
if [ ! -d "$CKPT_DIR" ]; then
    echo "Creating checkpoint directory: $CKPT_DIR"
    mkdir -p $CKPT_DIR
else
    echo "Using existing checkpoint directory: $CKPT_DIR"
fi

# Environment variables
export WANDB_API_KEY=${WANDB_API_KEY:-"your_wandb_api_key"}
export OPENAI_API_KEY=${OPENAI_API_KEY:-"your_openai_api_key"}
export DEBUG_PARSER=0

# Explicitly disable taxonomy feedback
export TAXONOMY_FEEDBACK="false"
export TAXONOMY_ALPHA="0.0"

# VLLM settings for longer tau_bench conversations
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_MAX_MODEL_LEN=8192  # Conservative for memory
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

# PyTorch memory optimization
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128

# Training command
cd "$(dirname "$0")"

# Add SkyRL modules to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL_mod/skyrl-train:$(pwd)/../SkyRL_mod/skyrl-gym:$(pwd)/../tau_bench:$(pwd)/../tau_bench_env:$(pwd)/../data_prep:$(pwd)/.."

# Kill any existing Ray processes
ray stop || true

echo "========================================="
echo "Starting 3B GRPO Training (Vanilla) on Retail Domain"
echo "========================================="
echo "Model: $POLICY_MODEL"
echo "Domain: Retail only"
echo "Taxonomy Feedback: DISABLED"
echo "WandB Project: tau_bench_retail_grpo"
echo "Conservative memory settings enabled"
echo ""

HYDRA_FULL_ERROR=1 python main_tau_bench.py \
  trainer.policy.model.path="$POLICY_MODEL" \
  trainer.ref.model.path="$REF_MODEL" \
  trainer.placement.policy_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.ref_num_gpus_per_node=$NUM_GPUS \
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
  trainer.micro_train_batch_size_per_gpu=1 \
  trainer.micro_forward_batch_size_per_gpu=1 \
  trainer.max_prompt_length=8192 \
  trainer.eval_batch_size=2 \
  trainer.eval_before_train=false \
  trainer.eval_interval=5 \
  trainer.policy.optimizer_config.lr=3.0e-7 \
  trainer.policy.optimizer_config.num_warmup_steps=200 \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.02 \
  trainer.ckpt_interval=5 \
  trainer.hf_save_interval=20 \
  trainer.use_sample_packing=false \
  generator.max_turns=15 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=2 \
  generator.gpu_memory_utilization=0.3 \
  generator.max_input_length=8192 \
  generator.enforce_eager=true \
  generator.sampling_params.max_generate_length=1024 \
  generator.sampling_params.temperature=0.9 \
  generator.sampling_params.top_p=0.9 \
  generator.override_existing_update_group="force_new" \
  generator.use_native_tool_calling=true \
  environment.env_class="tau_bench" \
  environment.skyrl_gym.tau_bench.user_strategy="llm" \
  environment.skyrl_gym.tau_bench.user_model="gpt-4o" \
  environment.skyrl_gym.tau_bench.user_provider="openai" \
  environment.skyrl_gym.tau_bench.max_turns=10 \
  environment.skyrl_gym.tau_bench.use_native_tool_calling=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_FEEDBACK=false \
  environment.skyrl_gym.tau_bench.TAXONOMY_ALPHA=0.0 \
  environment.skyrl_gym.max_env_workers=12 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_retail_grpo" \
  trainer.run_name="retail_3b_grpo_vanilla_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=latest \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
  $@

echo "Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Exports saved to: $EXPORT_DIR"