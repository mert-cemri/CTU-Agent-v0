#!/bin/bash
set -x

# Tau Bench Training Script
# Train Qwen-7B-Instruct on tau_bench multi-domain conversational AI tasks

# Configuration
DATA_DIR="$HOME/data/tau_bench"
CKPT_DIR="$HOME/ckpts/tau_bench"
NUM_GPUS=8
NUM_INFERENCE_ENGINES=2
TENSOR_PARALLEL_SIZE=4

# Make sure required directories exist
mkdir -p $DATA_DIR
mkdir -p $CKPT_DIR

# Environment variables
export WANDB_API_KEY=${WANDB_API_KEY:-"your_wandb_api_key"}
export OPENAI_API_KEY=${OPENAI_API_KEY:-"your_openai_api_key"}

# Ray environment variable for UV support
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

# Training command
cd "$(dirname "$0")"

uv run --isolated --extra vllm python main_tau_bench.py \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
  trainer.policy.model.path="Qwen/Qwen2.5-7B-Instruct" \
  trainer.ref.model.path="Qwen/Qwen2.5-7B-Instruct" \
  trainer.placement.policy_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.ref_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.critic_num_gpus_per_node=$NUM_GPUS \
  trainer.placement.reward_num_gpus_per_node=$NUM_GPUS \
  generator.num_inference_engines=$NUM_INFERENCE_ENGINES \
  generator.inference_engine_tensor_parallel_size=$TENSOR_PARALLEL_SIZE \
  trainer.ckpt_path="$CKPT_DIR" \
  trainer.export_path="$HOME/exports/tau_bench" \
  trainer.epochs=50 \
  trainer.train_batch_size=256 \
  trainer.policy_mini_batch_size=64 \
  trainer.micro_train_batch_size_per_gpu=1 \
  trainer.micro_forward_batch_size_per_gpu=2 \
  trainer.max_prompt_length=4096 \
  trainer.eval_batch_size=128 \
  trainer.eval_before_train=true \
  trainer.eval_interval=5 \
  trainer.policy.optimizer_config.lr=1.0e-6 \
  trainer.algorithm.use_kl_loss=true \
  trainer.algorithm.kl_loss_coef=0.001 \
  trainer.ckpt_interval=10 \
  trainer.hf_save_interval=20 \
  generator.max_turns=20 \
  generator.use_conversation_multi_turn=true \
  generator.batched=false \
  generator.async_engine=true \
  generator.n_samples_per_prompt=3 \
  generator.gpu_memory_utilization=0.7 \
  generator.sampling_params.max_generate_length=2048 \
  generator.sampling_params.temperature=0.7 \
  generator.sampling_params.top_p=0.9 \
  environment.env_class="tau_bench" \
  environment.skyrl_gym.tau_bench.user_strategy="llm" \
  environment.skyrl_gym.tau_bench.user_model="gpt-4o" \
  environment.skyrl_gym.tau_bench.user_provider="openai" \
  environment.skyrl_gym.tau_bench.max_turns=20 \
  environment.skyrl_gym.max_env_workers=16 \
  trainer.logger="wandb" \
  trainer.project_name="tau_bench_rl" \
  trainer.run_name="tau_bench_qwen7b_$(date +%Y%m%d_%H%M%S)" \
  trainer.resume_mode=latest \
  $@

echo "Training completed!"
echo "Checkpoints saved to: $CKPT_DIR"
echo "Exports saved to: $HOME/exports/tau_bench" 