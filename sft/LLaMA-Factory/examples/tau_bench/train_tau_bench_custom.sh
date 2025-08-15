#!/bin/bash
set -e

# Flexible Tau-Bench SFT Training Script
MODEL_SIZE="${1:-3b}"
DATASET_NAME="${2:-tau_bench_reward_full}"
CUSTOM_PATH="${3:-}"

echo "========================================="
echo "Custom Tau-Bench Training Script"
echo "========================================="
echo "Model: Qwen2.5-${MODEL_SIZE}"
echo "Dataset: ${DATASET_NAME}"
echo "Custom path: ${CUSTOM_PATH:-Not specified}"
echo ""

# Configuration mapping
case "${MODEL_SIZE}" in
    "3b") BASE_CONFIG="examples/tau_bench/qwen2_5_3b_lora_sft.yaml" ;;
    "7b") BASE_CONFIG="examples/tau_bench/qwen2_5_7b_lora_sft.yaml" ;;
    *)
        echo "Error: Unsupported model size: ${MODEL_SIZE}"
        echo "Supported: 3b, 7b"
        exit 1
        ;;
esac

# Create temporary config
TEMP_CONFIG="temp_${MODEL_SIZE}_${DATASET_NAME}.yaml"
cp "${BASE_CONFIG}" "${TEMP_CONFIG}"

# Update dataset name in config
sed -i "s/dataset: tau_bench_reward_full/dataset: ${DATASET_NAME}/g" "${TEMP_CONFIG}"

# If custom path provided, add/update it in dataset_info.json
if [ -n "${CUSTOM_PATH}" ]; then
    echo "Adding custom dataset to dataset_info.json..."
    
    # Backup dataset_info.json
    cp data/dataset_info.json data/dataset_info.json.bak
    
    # Add custom dataset entry if not exists
    python3 << EOF
import json

with open('data/dataset_info.json', 'r') as f:
    data = json.load(f)

# Add or update the custom dataset entry
data['${DATASET_NAME}'] = {
    "file_name": "${CUSTOM_PATH}",
    "formatting": "sharegpt",
    "columns": {
        "messages": "conversations",
        "system": "system",
        "tools": "tools"
    },
    "tags": {
        "role_tag": "from",
        "content_tag": "value",
        "user_tag": "human",
        "assistant_tag": "gpt",
        "observation_tag": "observation",
        "function_tag": "function_call"
    }
}

with open('data/dataset_info.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Added dataset '{DATASET_NAME}' with path '{CUSTOM_PATH}'")
EOF
fi

# Check GPU
echo ""
echo "GPU Status:"
nvidia-smi --query-gpu=name,memory.free --format=csv,noheader || echo "No GPU detected"

# Run training
echo ""
echo "Starting training with ${TEMP_CONFIG}..."
echo "Dataset: ${DATASET_NAME}"
sleep 2

export TOKENIZERS_PARALLELISM=false

# Use all available GPUs if not specified
if [ -z "${CUDA_VISIBLE_DEVICES}" ]; then
    echo "Using all available GPUs"
else
    echo "Using GPUs: ${CUDA_VISIBLE_DEVICES}"
fi

llamafactory-cli train "${TEMP_CONFIG}"

# Cleanup
rm -f "${TEMP_CONFIG}"

# Restore original dataset_info.json if we modified it
if [ -f "data/dataset_info.json.bak" ]; then
    echo "Restoring original dataset_info.json..."
    mv data/dataset_info.json.bak data/dataset_info.json
fi

echo ""
echo "Training complete! Model saved to saves/qwen2_5_${MODEL_SIZE}_tau_bench_lora"
echo ""
echo "To merge LoRA weights:"
echo "llamafactory-cli export --model Qwen/Qwen2.5-${MODEL_SIZE^^}B-Instruct \\"
echo "    --adapter_name qwen2_5_${MODEL_SIZE}_tau_bench_lora \\"
echo "    --export_dir merged_models/qwen2.5-${MODEL_SIZE}-tau-${DATASET_NAME}"