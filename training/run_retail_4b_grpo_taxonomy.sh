#!/bin/bash

# GRPO + Taxonomy Feedback Training on Retail Domain - 4B Model
# This script trains Qwen3-4B-Instruct-2507 on retail domain with LLM Judge feedback

# Configuration for 4B model
NUM_GPUS=8
NUM_INFERENCE_ENGINES=2  # Same as 8B model for better memory efficiency
TENSOR_PARALLEL_SIZE=4  # Same as 8B model (2 engines × 4 GPUs = 8 total)
EPOCHS=100

# Model Configuration
POLICY_MODEL="Qwen/Qwen3-4B-Instruct-2507"
REF_MODEL="Qwen/Qwen3-4B-Instruct-2507"
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_retail_grpo_taxonomy_v0

# Data Configuration - Using retail domain only
DATA_DIR="data/tau_bench_retail"

# Get the CTU-Agent-v0 root directory
CTU_ROOT="$(dirname "$(dirname "$(realpath "$0")")")"

# Generate timestamp for unique export directories
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Make sure required directories exist
CKPT_DIR="$CTU_ROOT/checkpoints/tau_bench/${MODEL_NAME_SANITIZED}"
EXPORT_DIR="$CTU_ROOT/exports/tau_bench_retail_4b_taxonomy_${TIMESTAMP}"
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

# Enable taxonomy feedback with configurable alpha
export TAXONOMY_FEEDBACK="true"
export TAXONOMY_ALPHA=${TAXONOMY_ALPHA:-"1"}  # Slightly higher weight for 4B model

# Enable VLLM settings (optimized for 4B model)
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

# Training command
cd "$(dirname "$0")"

# Add SkyRL modules to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL_mod/skyrl-train:$(pwd)/../SkyRL_mod/skyrl-gym:$(pwd)/../tau_bench:$(pwd)/../tau_bench_env:$(pwd)/../data_prep:$(pwd)/.."

# Kill any existing Ray processes
ray stop || true

echo "========================================="
echo "Starting 4B GRPO + Taxonomy Training on Retail Domain"
echo "========================================="
echo "Model: $POLICY_MODEL"
echo "Domain: Retail only"
echo "Taxonomy Feedback: ENABLED (alpha=$TAXONOMY_ALPHA)"
echo "WandB Project: tau_bench_retail_grpo_4b_with_taxonomy"
echo "Memory Optimized: YES (4B model - efficient settings)"
echo "Simplified Reward Structure: ENABLED"
echo ""

# Verify OpenAI key is set
if [ "$OPENAI_API_KEY" = "your_openai_api_key" ]; then
    echo "WARNING: OPENAI_API_KEY not set. LLM Judge will not work!"
    echo "Please set: export OPENAI_API_KEY=your_actual_key"
fi

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
  trainer.critic_mini_batch_size=4 \
  trainer.micro_train_batch_size_per_gpu=1 \
  trainer.micro_forward_batch_size_per_gpu=1 \
  trainer.max_prompt_length=16384 \
  trainer.eval_batch_size=4 \
  trainer.eval_before_train=true \
  trainer.eval_interval=10 \
  trainer.policy.optimizer_config.lr=3.0e-7 \
  trainer.policy.optimizer_config.num_warmup_steps=100 \
  trainer.policy.optimizer_config.weight_decay=0.05 \
  trainer.policy.optimizer_config.max_grad_norm=0.5 \
  trainer.policy.optimizer_config.offload_after_step=true \
  trainer.policy.fsdp_config.cpu_offload=true \
  trainer.policy.fsdp_config.reshard_after_forward=true \
  trainer.ref.fsdp_config.cpu_offload=true \
  trainer.critic.fsdp_config.cpu_offload=true \
  trainer.reward.fsdp_config.cpu_offload=true \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.01 \
  trainer.algorithm.eps_clip_low=0.1 \
  trainer.algorithm.eps_clip_high=0.1 \
  trainer.algorithm.value_clip=0.1 \
  trainer.ckpt_interval=10 \
  trainer.hf_save_interval=20 \
  trainer.use_sample_packing=false \
  trainer.gradient_checkpointing=true \
  trainer.gradient_checkpointing_use_reentrant=false \
  generator.max_turns=15 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=3 \
  generator.gpu_memory_utilization=0.75 \
  generator.max_input_length=16384 \
  generator.max_num_batched_tokens=16384 \
  generator.enforce_eager=true \
  generator.enable_prefix_caching=false \
  generator.enable_chunked_prefill=false \
  generator.sampling_params.max_generate_length=512 \
  generator.sampling_params.temperature=0.8 \
  generator.sampling_params.top_p=0.9 \
  +generator.sampling_params.repetition_penalty=1.05 \
  +generator.sampling_params.frequency_penalty=0.5 \
  +generator.sampling_params.presence_penalty=0.1 \
  generator.zero_reward_on_length_threshold=true \
  generator.max_assistant_response_tokens=2048 \
  generator.override_existing_update_group="force_new" \
  generator.use_native_tool_calling=true \
  environment.env_class="tau_bench" \
  environment.skyrl_gym.tau_bench.user_strategy="llm" \
  environment.skyrl_gym.tau_bench.user_model="gpt-4o" \
  environment.skyrl_gym.tau_bench.user_provider="openai" \
  environment.skyrl_gym.tau_bench.max_turns=10 \
  environment.skyrl_gym.tau_bench.use_native_tool_calling=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_FEEDBACK=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_ALPHA=$TAXONOMY_ALPHA \
  environment.skyrl_gym.max_env_workers=10 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_retail_grpo_4b" \
  trainer.run_name="retail_4b_grpo_taxonomy_alpha${TAXONOMY_ALPHA}_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=latest \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
  $@

echo "Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Exports saved to: $EXPORT_DIR"
echo "Taxonomy alpha: $TAXONOMY_ALPHA"