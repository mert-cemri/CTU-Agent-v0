#!/bin/bash

# Test multiple models served on different GPUs

echo "Testing Multiple Models on Tau-Bench"
echo "====================================="

# Model 1: Base Qwen2.5-3B (GPU 0, port 8000)
echo -e "\n[1/4] Testing Base Qwen2.5-3B-Instruct..."
python testing/tau-bench/test_qwen.py \
    --model "Qwen/Qwen2.5-3B-Instruct" \
    --base-url "http://localhost:8000/v1" \
    --env airline \
    --output-dir "testing/tau-bench/qwen_results/base_3b_airline"

# Model 2: Fine-tuned 3B (GPU 1, port 8001)
echo -e "\n[2/4] Testing Fine-tuned 3B Model..."
python testing/tau-bench/test_qwen.py \
    --model "sft/LLaMA-Factory/merged_models/merged-qwen2.5-3b-tau" \
    --base-url "http://localhost:8001/v1" \
    --env airline \
    --output-dir "testing/tau-bench/qwen_results/finetuned_3b_airline"

echo -e "\n[3/4] Testing Fine-tuned 7B Model..."
python testing/tau-bench/test_qwen.py \
    --model "Qwen/Qwen2.5-7B-Instruct" \
    --base-url "http://localhost:8000/v1" \
    --env airline \
    --output-dir "testing/tau-bench/qwen_results/base_7b_airline"

echo -e "\n[4/4] Testing Fine-tuned 7B Model..."
python testing/tau-bench/test_qwen.py \
    --model "sft/LLaMA-Factory/merged_models/merged-qwen2.5-7b-tau" \
    --base-url "http://localhost:8001/v1" \
    --env airline \
    --output-dir "testing/tau-bench/qwen_results/finetuned_7b_airline"

echo -e "\n====================================="
echo "All tests complete!"
echo ""
echo "Comparing results:"
echo "Base 3B results: qwen_results/base_3b/"
echo "Finetuned 3B results: qwen_results/finetuned_3b/"
echo "Finetuned 7B results: qwen_results/finetuned_7b/"