#!/bin/bash

# Simple script to run tau_bench tests with VLLM

# Set default values
DOMAIN=${1:-"retail"}
MODEL=${2:-"Qwen/Qwen3-8B"}
NUM_TASKS=${3:-5}

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
    --max-tokens 2048

echo ""
echo "Test complete! Check the results/ directory for output."

#   # Test retail domain with 5 tasks
#   python test_model.py --domain retail --num-tasks 5

#   # Test airline with different model
#   python test_model.py --domain airline --model Qwen/Qwen3-8B --num-tasks 10

#   # Test with custom parameters
#   python test_model.py \
#     --domain healthcare \
#     --model Qwen/Qwen3-8B \
#     --user-model gpt-4o \
#     --num-tasks 20 \
#     --start-idx 10 \
#     --temperature 0.5