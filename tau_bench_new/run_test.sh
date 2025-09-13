#!/bin/bash

# Simple script to run tau_bench tests with VLLM

# Set default values (can be overridden via command line arguments)
DOMAIN=${1:-"retail"}
MODEL=${2:-"Qwen/Qwen3-8B"}
NUM_TASKS=${3:-5}
MAX_MODEL_LEN=${4:-32768}
TENSOR_PARALLEL=${5:-1}
GPU_MEMORY=${6:-0.8}

# Ensure OpenAI API key is set for user simulation
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Error: OPENAI_API_KEY is not set. This is required for user simulation with gpt-4o."
    echo "Please set it: export OPENAI_API_KEY=your_key_here"
    exit 1
fi

echo "========================================="
echo "Running Tau Bench Test"
echo "========================================="
echo "Domain: $DOMAIN"
echo "Model: $MODEL"
echo "Number of tasks: $NUM_TASKS"
echo "Max model length: $MAX_MODEL_LEN"
echo "Tensor parallel size: $TENSOR_PARALLEL"
echo "GPU memory utilization: $GPU_MEMORY"
echo ""

# Navigate to tau_bench_new directory
cd "$(dirname "$0")"

# Run the test
python test_model.py \
    --domain "$DOMAIN" \
    --model "$MODEL" \
    --user-model "gpt-4o" \
    --num-tasks "$NUM_TASKS" \
    --temperature 0.7 \
    --max-tokens 2048 \
    --max-model-len "$MAX_MODEL_LEN" \
    --tensor-parallel-size "$TENSOR_PARALLEL" \
    --gpu-memory-utilization "$GPU_MEMORY"

echo ""
echo "Test complete! Check the results/ directory for output."

# Usage examples:
#   # Basic usage with defaults
#   bash run_test.sh
#
#   # Custom domain and model
#   bash run_test.sh airline "Qwen/Qwen2.5-3B-Instruct" 10
#
#   # With custom VLLM settings
#   bash run_test.sh retail "Qwen/Qwen3-8B" 5 16384 2 0.9
#
#   # Direct python usage with all parameters
#   python test_model.py \
#     --domain healthcare \
#     --model "Qwen/Qwen2.5-3B-Instruct" \
#     --num-tasks 20 \
#     --max-model-len 16384 \
#     --tensor-parallel-size 2 \
#     --gpu-memory-utilization 0.9 \
#     --temperature 0.5