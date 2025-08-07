#!/bin/bash
# set -x

# Tau Bench Training Script for Llama-3.1-8B
# Train Meta-Llama-3.1-8B-Instruct on tau_bench multi-domain conversational AI tasks

# Configuration

NUM_GPUS=8
NUM_INFERENCE_ENGINES=2
TENSOR_PARALLEL_SIZE=4
EPOCHS=100

# Model Configuration - Llama-3.1-8B model
POLICY_MODEL="unsloth/Meta-Llama-3.1-8B-Instruct"
REF_MODEL="unsloth/Meta-Llama-3.1-8B-Instruct"
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_v1-multi-domain

# Make sure required directories exist
CKPT_DIR="$HOME/ckpts/tau_bench/${MODEL_NAME_SANITIZED}"
EXPORT_DIR="$HOME/exports/tau_bench/${MODEL_NAME_SANITIZED}"

# Ensure checkpoint directory exists (don't delete existing checkpoints)
if [ ! -d "$CKPT_DIR" ]; then
    echo "Creating checkpoint directory: $CKPT_DIR"
    mkdir -p $CKPT_DIR
else
    echo "Using existing checkpoint directory: $CKPT_DIR"
    echo "Will resume from latest checkpoint if available"
fi

# Ensure export directory exists for eval dumps
mkdir -p $EXPORT_DIR
echo "Evaluation results will be saved to: $EXPORT_DIR/dumped_evals/"

# Environment variables
export WANDB_API_KEY=${WANDB_API_KEY:-"your_wandb_api_key"}
export OPENAI_API_KEY=${OPENAI_API_KEY:-"your_openai_api_key"}
export DEBUG_PARSER=0

# Enable VLLM to use longer context lengths (Llama-3.1 supports 128K)
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_MAX_MODEL_LEN=32768  # Keep at 32K for consistency with training

# Ray environment variable for UV support
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

# Training command
cd "$(dirname "$0")"

# Add SkyRL modules to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL_mod/skyrl-train:$(pwd)/../SkyRL_mod/skyrl-gym:$(pwd)/../tau_bench:$(pwd)/../tau_bench_env:$(pwd)/../data_prep:$(pwd)/.."

# Kill any existing Ray processes to ensure clean start
ray stop || true

# Run training with adjusted parameters for 8B model
# Using the Llama-specific config file
HYDRA_FULL_ERROR=1 CUDA_LAUNCH_BLOCKING=1 python main_tau_bench.py \
  --config-name=tau_bench_llama_config \
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
  trainer.export_path="$HOME/exports/tau_bench/${MODEL_NAME_SANITIZED}" \
  trainer.dump_eval_results=true \
  trainer.epochs=$EPOCHS \
  trainer.train_batch_size=32 \
  trainer.policy_mini_batch_size=8 \
  trainer.micro_train_batch_size_per_gpu=1 \
  trainer.micro_forward_batch_size_per_gpu=1 \
  trainer.max_prompt_length=16384 \
  trainer.eval_batch_size=16 \
  trainer.eval_before_train=true \
  trainer.eval_interval=5 \
  trainer.policy.optimizer_config.lr=2.0e-7 \
  trainer.policy.optimizer_config.num_warmup_steps=200 \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.02 \
  trainer.ckpt_interval=5 \
  trainer.hf_save_interval=20 \
  trainer.use_sample_packing=false \
  generator.max_turns=20 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=5 \
  generator.gpu_memory_utilization=0.65 \
  generator.max_input_length=16384 \
  generator.max_num_batched_tokens=16384 \
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
  environment.skyrl_gym.max_env_workers=16 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_rl" \
  trainer.run_name="tau_bench_llama3_1_8b_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=latest \
  $@

echo "Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Evaluation dumps saved to: $EXPORT_DIR/dumped_evals/"
echo "Each eval step creates a folder with all trajectories and results"

## Key changes for 8B model:
# - Reduced batch sizes: train_batch_size=32 (from 64), policy_mini_batch_size=8 (from 16)
# - Reduced eval_batch_size to 16 (from 32)
# - Reduced GPU memory utilization to 0.65 (from 0.8)
# - Reduced max_num_batched_tokens to 16384 (from 24576)
# - Slightly lower learning rate: 2.0e-7 (from 3.0e-7)
# - Added trajectory logging paths and flags