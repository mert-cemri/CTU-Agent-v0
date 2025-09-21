#!/bin/bash

# PPO + Taxonomy Feedback Training on Retail Domain - 3B Model
# This script trains Qwen2.5-3B-Instruct on retail domain with PPO + LLM Judge feedback

# Configuration
NUM_GPUS=8
NUM_INFERENCE_ENGINES=8  # Must match NUM_GPUS for colocated models
TENSOR_PARALLEL_SIZE=1
EPOCHS=100

# Model Configuration
POLICY_MODEL="Qwen/Qwen2.5-3B-Instruct"
REF_MODEL="Qwen/Qwen2.5-3B-Instruct"
CRITIC_MODEL="Qwen/Qwen2.5-3B-Instruct"  # REQUIRED for PPO
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_retail_ppo_taxonomy_v1

# Data Configuration - Using retail domain only
DATA_DIR="data/tau_bench_retail"

# Get the CTU-Agent-v0 root directory
CTU_ROOT="$(dirname "$(dirname "$(realpath "$0")")")"

# Make sure required directories exist with unique run names
RUN_TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
CKPT_DIR="$CTU_ROOT/checkpoints/tau_bench/${MODEL_NAME_SANITIZED}"
EXPORT_DIR="$CTU_ROOT/exports/tau_bench_retail_ppo_taxonomy_${RUN_TIMESTAMP}"
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
export TAXONOMY_ALPHA=${TAXONOMY_ALPHA:-"0.5"}  # Weight for judge rewards

# VLLM settings for longer tau_bench conversations
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_MAX_MODEL_LEN=22000
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
echo "Starting 3B PPO + Taxonomy Training on Retail Domain"
echo "========================================="
echo "Policy Model: $POLICY_MODEL"
echo "Critic Model: $CRITIC_MODEL"
echo "Domain: Retail only"
echo "Algorithm: PPO with GAE"
echo "Taxonomy Feedback: ENABLED (alpha=$TAXONOMY_ALPHA)"
echo "WandB Project: tau_bench_retail_ppo_with_taxonomy"
echo ""

# Verify OpenAI key is set
if [ "$OPENAI_API_KEY" = "your_openai_api_key" ]; then
    echo "WARNING: OPENAI_API_KEY not set. LLM Judge will not work!"
    echo "Please set: export OPENAI_API_KEY=your_actual_key"
fi

HYDRA_FULL_ERROR=1 python main_tau_bench.py \
  trainer.policy.model.path="$POLICY_MODEL" \
  trainer.ref.model.path="$REF_MODEL" \
  trainer.critic.model.path="$CRITIC_MODEL" \
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
  trainer.update_epochs_per_batch=1 \
  trainer.train_batch_size=16 \
  trainer.policy_mini_batch_size=2 \
  trainer.critic_mini_batch_size=2 \
  trainer.micro_train_batch_size_per_gpu=2 \
  trainer.micro_forward_batch_size_per_gpu=2 \
  trainer.max_prompt_length=17000 \
  trainer.eval_batch_size=8 \
  trainer.eval_before_train=false \
  trainer.eval_interval=5 \
  trainer.policy.optimizer_config.lr=1.0e-6 \
  trainer.policy.optimizer_config.num_warmup_steps=200 \
  trainer.policy.optimizer_config.offload_after_step=true \
  trainer.policy.fsdp_config.cpu_offload=true \
  trainer.policy.fsdp_config.reshard_after_forward=true \
  trainer.ref.fsdp_config.cpu_offload=true \
  trainer.critic.fsdp_config.cpu_offload=true \
  trainer.critic.optimizer_config.lr=5.0e-6 \
  trainer.critic.optimizer_config.num_warmup_steps=200 \
  trainer.reward.fsdp_config.cpu_offload=true \
  trainer.algorithm.advantage_estimator="gae" \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.001 \
  trainer.algorithm.gamma=0.99 \
  trainer.algorithm.lambd=0.95 \
  trainer.algorithm.normalize_reward=true \
  trainer.algorithm.value_clip=0.2 \
  trainer.algorithm.eps_clip_low=0.2 \
  trainer.algorithm.eps_clip_high=0.2 \
  trainer.ckpt_interval=5 \
  trainer.hf_save_interval=20 \
  trainer.use_sample_packing=false \
  trainer.gradient_checkpointing=true \
  trainer.gradient_checkpointing_use_reentrant=false \
  generator.max_turns=16 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=8 \
  generator.gpu_memory_utilization=0.4 \
  +generator.max_model_len=22000 \
  generator.max_input_length=17000 \
  generator.enforce_eager=true \
  generator.sampling_params.max_generate_length=1024 \
  generator.sampling_params.temperature=0.9 \
  generator.sampling_params.top_p=1 \
  +generator.sampling_params.repetition_penalty=1.05 \
  +generator.sampling_params.frequency_penalty=0.5 \
  +generator.sampling_params.presence_penalty=0.1 \
  generator.zero_reward_on_length_threshold=false \
  generator.max_assistant_response_tokens=8192 \
  generator.override_existing_update_group="force_new" \
  generator.use_native_tool_calling=true \
  environment.env_class="tau_bench" \
  environment.skyrl_gym.tau_bench.user_strategy="llm" \
  environment.skyrl_gym.tau_bench.user_model="gpt-4o" \
  environment.skyrl_gym.tau_bench.user_provider="openai" \
  environment.skyrl_gym.tau_bench.max_turns=16 \
  environment.skyrl_gym.tau_bench.use_native_tool_calling=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_FEEDBACK=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_ALPHA="$TAXONOMY_ALPHA" \
  environment.skyrl_gym.max_env_workers=4 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_retail_ppo" \
  trainer.run_name="retail_3b_ppo_taxonomy_alpha${TAXONOMY_ALPHA}_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=latest \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
  $@

echo "Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Exports saved to: $EXPORT_DIR"
echo "Algorithm: PPO with GAE (gamma=0.99, lambd=0.95)"
echo "Taxonomy alpha: $TAXONOMY_ALPHA"