#!/bin/bash

# Tau-bench testing examples with different configurations
# Uncomment and modify the examples below to run different tests

set -e

# Configuration
export OPENAI_API_KEY="${OPENAI_API_KEY:-your-api-key}"
BASE_URL="${BASE_URL:-http://localhost:8000/v1}"
OUTPUT_BASE="${OUTPUT_BASE:-results}"

echo "=================================================="
echo "         Tau-bench Testing Examples"
echo "=================================================="
echo "Base URL: $BASE_URL"
echo "Output Directory: $OUTPUT_BASE"
echo ""

# Check if OpenAI API key is set
if [ "$OPENAI_API_KEY" = "your-api-key" ]; then
    echo "⚠️  Warning: Set OPENAI_API_KEY for user simulator"
    echo "   export OPENAI_API_KEY='your-actual-key'"
    echo ""
fi

# =============================================================================
# QUICK TESTING (5 tasks only)
# =============================================================================

echo "Example 1: Quick test (5 tasks) - UNCOMMENT TO RUN"
# python test.py --mode quick \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --output-dir $OUTPUT_BASE/quick_retail

# =============================================================================
# SPECIFIC TASK TESTING
# =============================================================================

echo "Example 2: Test specific tasks - UNCOMMENT TO RUN"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --task-ids 0 1 2 3 4 \
#     --max-concurrency 2 \
#     --output-dir $OUTPUT_BASE/specific_tasks

# =============================================================================
# FULL RETAIL EVALUATION (115 tasks)
# =============================================================================

echo "Example 3: Full retail evaluation - UNCOMMENT TO RUN"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --max-concurrency 4 \
#     --output-dir $OUTPUT_BASE/full_retail

# =============================================================================
# FULL AIRLINE EVALUATION (50 tasks)  
# =============================================================================

echo "Example 4: Full airline evaluation - UNCOMMENT TO RUN"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env airline \
#     --max-concurrency 4 \
#     --output-dir $OUTPUT_BASE/full_airline

# =============================================================================
# FINE-TUNED MODEL TESTING (if you have one)
# =============================================================================

echo "Example 5: Test fine-tuned model - UNCOMMENT TO RUN"
# python test.py --mode vllm \
#     --model mcemri/qwen2.5_3b_alldata_sft_v0 \
#     --base-url http://localhost:8001/v1 \
#     --env retail \
#     --max-concurrency 4 \
#     --output-dir $OUTPUT_BASE/finetuned_retail

# =============================================================================
# TEMPERATURE COMPARISON
# =============================================================================

echo "Example 6: Temperature comparison - UNCOMMENT TO RUN"
# echo "Testing with temperature=0.0 (deterministic)"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --temperature 0.0 \
#     --task-ids 0 1 2 3 4 \
#     --output-dir $OUTPUT_BASE/temp_0.0
# 
# echo "Testing with temperature=0.7 (creative)"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --temperature 0.7 \
#     --task-ids 0 1 2 3 4 \
#     --output-dir $OUTPUT_BASE/temp_0.7

# =============================================================================
# DIFFERENT USER SIMULATOR
# =============================================================================

echo "Example 7: Different user simulator - UNCOMMENT TO RUN"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --user-model gpt-4o-mini \
#     --user-strategy react \
#     --task-ids 0 1 2 \
#     --output-dir $OUTPUT_BASE/different_user

# =============================================================================
# MULTIPLE TRIALS (for statistical significance)
# =============================================================================

echo "Example 8: Multiple trials - UNCOMMENT TO RUN"
# for trial in 0 1 2; do
#     echo "Running trial $trial..."
#     python test.py --mode vllm \
#         --model Qwen/Qwen2.5-3B-Instruct \
#         --base-url $BASE_URL \
#         --env retail \
#         --task-ids 0 1 2 3 4 \
#         --trial $trial \
#         --output-dir $OUTPUT_BASE/trial_$trial
# done

# =============================================================================
# STANDARD MODE (using API models like GPT-4)
# =============================================================================

echo "Example 9: API model testing - UNCOMMENT TO RUN"
# python test.py --mode standard \
#     --model gpt-4o \
#     --model-provider openai \
#     --env retail \
#     --task-ids 0 1 2 \
#     --max-concurrency 2 \
#     --output-dir $OUTPUT_BASE/gpt4o_retail

# =============================================================================
# HIGH CONCURRENCY (for fast local models)
# =============================================================================

echo "Example 10: High concurrency testing - UNCOMMENT TO RUN"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url $BASE_URL \
#     --env retail \
#     --max-concurrency 10 \
#     --task-ids $(seq 0 19) \
#     --output-dir $OUTPUT_BASE/high_concurrency

# =============================================================================
# MODEL COMPARISON WORKFLOW
# =============================================================================

echo "Example 11: Model comparison workflow - UNCOMMENT TO RUN"
# echo "Step 1: Test base model"
# python test.py --mode vllm \
#     --model Qwen/Qwen2.5-3B-Instruct \
#     --base-url http://localhost:8000/v1 \
#     --env retail \
#     --task-ids 0 1 2 3 4 \
#     --output-dir $OUTPUT_BASE/base_model
# 
# echo "Step 2: Test fine-tuned model (assuming different port)"
# python test.py --mode vllm \
#     --model your-finetuned-model \
#     --base-url http://localhost:8001/v1 \
#     --env retail \
#     --task-ids 0 1 2 3 4 \
#     --output-dir $OUTPUT_BASE/finetuned_model
# 
# echo "Step 3: Compare results"
# python compare_results.py \
#     $OUTPUT_BASE/base_model \
#     $OUTPUT_BASE/finetuned_model \
#     --output $OUTPUT_BASE/comparison_report.json

# =============================================================================

echo ""
echo "=================================================="
echo "To run an example:"
echo "1. Edit this script and uncomment the desired example"
echo "2. Make sure VLLM server is running:"
echo "   bash start_vllm_server.sh [model] [port] [max_len] [gpu_util] [gpu_id]"
echo "3. Run: bash run_tests.sh"
echo ""
echo "To start VLLM server examples:"
echo "   bash start_vllm_server.sh Qwen/Qwen2.5-3B-Instruct 8000 8192 0.35 0"
echo "   bash start_vllm_server.sh your-model 8001 16384 0.4 1"
echo "=================================================="