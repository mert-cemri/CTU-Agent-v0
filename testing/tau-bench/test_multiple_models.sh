#!/bin/bash

# Test multiple models served on different GPUs

echo "Testing Multiple Models on Tau-Bench"
echo "====================================="

# Model 1: Base Qwen2.5-3B (GPU 0, port 8000)
echo -e "\n[1/3] Testing Base Qwen2.5-3B-Instruct..."
python test_qwen.py \
    --model "Qwen/Qwen2.5-3B-Instruct" \
    --base-url "http://localhost:8000/v1" \
    --env retail \
    --tasks 1 2 3 4 5 \
    --output-dir "qwen_results/base_3b"

# Model 2: Fine-tuned 3B (GPU 1, port 8001)
echo -e "\n[2/3] Testing Fine-tuned 3B Model..."
python test_qwen.py \
    --model "finetuned-3b" \
    --base-url "http://localhost:8001/v1" \
    --env retail \
    --tasks 1 2 3 4 5 \
    --output-dir "qwen_results/finetuned_3b"

# Model 3: Fine-tuned 7B (GPU 2-3, port 8002)
echo -e "\n[3/3] Testing Fine-tuned 7B Model..."
python test_qwen.py \
    --model "finetuned-7b" \
    --base-url "http://localhost:8002/v1" \
    --env retail \
    --tasks 1 2 3 4 5 \
    --output-dir "qwen_results/finetuned_7b"

echo -e "\n====================================="
echo "All tests complete!"
echo ""
echo "Comparing results:"
echo "Base 3B results: qwen_results/base_3b/"
echo "Finetuned 3B results: qwen_results/finetuned_3b/"
echo "Finetuned 7B results: qwen_results/finetuned_7b/"