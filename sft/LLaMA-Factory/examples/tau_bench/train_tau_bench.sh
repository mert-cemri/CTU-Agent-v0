#!/bin/bash
set -e

# Tau-Bench SFT Training Script
MODEL_SIZE="${1:-3b}"
DATASET="${2:-reward_full}"

echo "Training Qwen2.5-${MODEL_SIZE} LoRA model on ${DATASET} dataset"

# Configuration mapping
case "${MODEL_SIZE}" in
    "3b") CONFIG="examples/tau_bench/qwen2_5_3b_lora_sft.yaml" ;;
    "7b") CONFIG="examples/tau_bench/qwen2_5_7b_lora_sft.yaml" ;;
    *)
        echo "Error: Unsupported model size: ${MODEL_SIZE}"
        echo "Supported: 3b, 7b"
        exit 1
        ;;
esac

# Update dataset in config if not default
if [ "${DATASET}" != "reward_full" ]; then
    sed "s/dataset: tau_bench_reward_full/dataset: tau_bench_${DATASET}/g" \
        "${CONFIG}" > "temp_${CONFIG}"
    CONFIG="temp_${CONFIG}"
fi

# Check GPU
echo "GPU Status:"
nvidia-smi --query-gpu=name,memory.free --format=csv,noheader || echo "No GPU detected"

# Run training
echo "Starting training with ${CONFIG}..."
sleep 2


export TOKENIZERS_PARALLELISM=false

# Use all available GPUs if not specified
if [ -z "${CUDA_VISIBLE_DEVICES}" ]; then
    echo "Using all available GPUs"
else
    echo "Using GPUs: ${CUDA_VISIBLE_DEVICES}"
fi

llamafactory-cli train "${CONFIG}"

# Cleanup
[ -f "temp_${CONFIG}" ] && rm "temp_${CONFIG}"

echo "Training complete! Model saved to saves/qwen2_5_${MODEL_SIZE}_tau_bench_lora"