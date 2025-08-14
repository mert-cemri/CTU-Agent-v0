#!/bin/bash

# Test Qwen2.5-3B-Instruct on all tau-bench tasks

set -e

# Configuration
MODEL="${MODEL:-Qwen/Qwen2.5-3B-Instruct}"
BASE_URL="${BASE_URL:-http://localhost:8000/v1}"
USER_MODEL="${USER_MODEL:-gpt-4o}"
TEMPERATURE="${TEMPERATURE:-0.0}"

echo "=================================================="
echo "    Full Tau-Bench Evaluation for Qwen2.5-3B     "
echo "=================================================="
echo ""
echo "Model: $MODEL"
echo "VLLM URL: $BASE_URL"
echo "User Model: $USER_MODEL"
echo "Temperature: $TEMPERATURE"
echo ""

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "ERROR: OPENAI_API_KEY not set"
    echo "Please run: export OPENAI_API_KEY='your-api-key'"
    exit 1
fi

# Test all retail tasks
echo "Testing RETAIL domain (all tasks)..."
python test_qwen.py \
    --model "$MODEL" \
    --base-url "$BASE_URL" \
    --env retail \
    --temperature $TEMPERATURE \
    --user-model "$USER_MODEL"

echo ""
echo "=================================================="
echo ""

# Test all airline tasks
echo "Testing AIRLINE domain (all tasks)..."
python test_qwen.py \
    --model "$MODEL" \
    --base-url "$BASE_URL" \
    --env airline \
    --temperature $TEMPERATURE \
    --user-model "$USER_MODEL"

echo ""
echo "=================================================="
echo "             All Tests Complete!                  "
echo "=================================================="
echo ""
echo "Results saved in: qwen_results/"
echo ""

# Show summary
echo "Quick Summary:"
ls -lh qwen_results/*.json | tail -2