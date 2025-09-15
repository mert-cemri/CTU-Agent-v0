#!/bin/bash

# Memory-Optimized GRPO Training with LoRA + Taxonomy on Retail Domain - 4B Model
# Based on working run_retail_4b_grpo_lora_taxonomy.sh with aggressive memory optimizations

# Configuration for 4B model with LoRA (memory optimized)
NUM_GPUS=8
NUM_INFERENCE_ENGINES=1  # Reduced from 2 to save memory  
TENSOR_PARALLEL_SIZE=2   # Reduced from 4 to 2
EPOCHS=100

# LLM Judge Configuration (memory optimized)
TAXONOMY_ALPHA=${TAXONOMY_ALPHA:-1.5}  # Reduced from 2.0 to 1.5 for stability

# Model Configuration
POLICY_MODEL="Qwen/Qwen3-4B-Instruct-2507"
REF_MODEL="Qwen/Qwen3-4B-Instruct-2507"
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_retail_grpo_lora_taxonomy_memory_opt_v0

# LoRA Configuration for 4B model (smaller rank for memory savings)
LORA_RANK=16     # Reduced from 32 to 16
LORA_ALPHA=32    # Reduced from 64 to 32
LORA_DROPOUT=0.05

# Data Configuration - Using retail domain only
DATA_DIR="data/tau_bench_retail"

# Get the CTU-Agent-v0 root directory
CTU_ROOT="$(dirname "$(dirname "$(realpath "$0")")")"

# Generate timestamp for unique export directories
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Make sure required directories exist
CKPT_DIR="$CTU_ROOT/checkpoints/tau_bench/${MODEL_NAME_SANITIZED}"
EXPORT_DIR="$CTU_ROOT/exports/tau_bench_retail_4b_lora_taxonomy_memory_opt_${TIMESTAMP}"
if [ ! -d "$CKPT_DIR" ]; then
    echo "Creating checkpoint directory: $CKPT_DIR"
    mkdir -p $CKPT_DIR
else
    echo "Using existing checkpoint directory: $CKPT_DIR"
fi

# Memory optimization environment variables
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TORCH_CUDA_MEMORY_FRACTION=0.9

# Environment variables
export WANDB_API_KEY=${WANDB_API_KEY:-"your_wandb_api_key"}
export OPENAI_API_KEY=${OPENAI_API_KEY:-"your_openai_api_key"}
export DEBUG_PARSER=0

# Enable taxonomy feedback with LLM Judge
export TAXONOMY_FEEDBACK="true"

# Enable VLLM settings
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

# Training command
cd "$(dirname "$0")"

# Add SkyRL modules to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL_mod/skyrl-train:$(pwd)/../SkyRL_mod/skyrl-gym:$(pwd)/../tau_bench:$(pwd)/../tau_bench_env:$(pwd)/../data_prep:$(pwd)/.."

# Kill any existing Ray processes
ray stop || true

echo "========================================="
echo "Memory-Optimized 4B GRPO Training with LoRA + Taxonomy on Retail Domain"
echo "========================================="
echo "Model: $POLICY_MODEL"
echo "Domain: Retail only"
echo "LoRA Configuration (Memory Optimized):"
echo "  - Rank: $LORA_RANK"
echo "  - Alpha: $LORA_ALPHA"
echo "  - Dropout: $LORA_DROPOUT"
echo "LLM Judge Alpha: $TAXONOMY_ALPHA"
echo "Memory Optimization: LoRA + Aggressive Batch Size Reduction"
echo "WandB Project: tau_bench_retail_grpo_4b_lora_taxonomy_memory_opt"
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
  generator.sampling_params.temperature=0.8 \
  generator.sampling_params.top_p=0.9 \
  +generator.sampling_params.repetition_penalty=1.05 \
  +generator.sampling_params.frequency_penalty=0.5 \
  +generator.sampling_params.presence_penalty=0.1 \
  generator.zero_reward_on_length_threshold=true \
  generator.max_assistant_response_tokens=1024 \
  generator.override_existing_update_group="force_new" \
  generator.use_native_tool_calling=true \
  environment.env_class="tau_bench" \
  environment.skyrl_gym.tau_bench.user_strategy="llm" \
  environment.skyrl_gym.tau_bench.user_model="gpt-4o" \
  environment.skyrl_gym.tau_bench.user_provider="openai" \
  environment.skyrl_gym.tau_bench.max_turns=10 \
  environment.skyrl_gym.tau_bench.use_native_tool_calling=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_FEEDBACK=true \
  environment.skyrl_gym.tau_bench.TAXONOMY_ALPHA="$TAXONOMY_ALPHA" \
  environment.skyrl_gym.max_env_workers=8 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_retail_grpo_4b_lora_taxonomy_memory_opt" \
  trainer.run_name="retail_4b_grpo_lora_taxonomy_memory_opt_r${LORA_RANK}_alpha${TAXONOMY_ALPHA}_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=latest \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
 

echo "Memory-optimized taxonomy LoRA Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Exports saved to: $EXPORT_DIR"
echo "LoRA rank: $LORA_RANK, alpha: $LORA_ALPHA (Memory Optimized)"
echo "LLM Judge alpha used: $TAXONOMY_ALPHA"
echo "Training approach: Parameter-efficient fine-tuning with LoRA adapters + LLM Judge + Aggressive Memory Optimization"