#!/bin/bash
set -e

# Tau-Bench SFT Training Script
MODEL_SIZE="${1:-3b}"
TRAINING_TYPE="${2:-lora}"
DATASET="${3:-full}"

echo "Training ${MODEL_SIZE} model with ${TRAINING_TYPE} on ${DATASET} dataset"

# Configuration mapping
case "${MODEL_SIZE}_${TRAINING_TYPE}" in
    "3b_lora") CONFIG="qwen2_5_3b_lora_sft.yaml" ;;
    "3b_full") CONFIG="qwen2_5_3b_full_sft.yaml" ;;
    "7b_qlora") CONFIG="qwen2_5_7b_qlora_sft.yaml" ;;
    *)
        echo "Error: Unsupported configuration: ${MODEL_SIZE}_${TRAINING_TYPE}"
        echo "Supported: 3b_lora, 3b_full, 7b_qlora"
        exit 1
        ;;
esac

# Convert data if needed
DATA_DIR="../../data/tau_bench/processed"
if [ ! -f "${DATA_DIR}/tau_bench_${DATASET}.json" ]; then
    echo "Converting data..."
    cd ../../data
    python tau_bench_converter.py \
        --input_dir ../../../data/tau_bench_multi \
        --output_dir tau_bench/processed
    cd ../examples/tau_bench
fi

# Update dataset in config if not 'full'
if [ "${DATASET}" != "full" ]; then
    sed "s/dataset: tau_bench_full/dataset: tau_bench_${DATASET}/g" \
        "${CONFIG}" > "temp_${CONFIG}"
    CONFIG="temp_${CONFIG}"
fi

# Check GPU
echo "GPU Status:"
nvidia-smi --query-gpu=name,memory.free --format=csv,noheader || echo "No GPU detected"

# Run training
echo "Starting training with ${CONFIG}..."
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}
export TOKENIZERS_PARALLELISM=false

llamafactory-cli train "${CONFIG}"

# Cleanup
[ -f "temp_${CONFIG}" ] && rm "temp_${CONFIG}"

echo "Training complete! Model saved to saves/qwen2_5_${MODEL_SIZE}_tau_bench_${TRAINING_TYPE}"