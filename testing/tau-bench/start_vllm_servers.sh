#!/bin/bash

# Start multiple VLLM servers on different GPUs

echo "Starting VLLM servers on different GPUs..."

# Enable longer context lengths
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

# Kill any existing vllm processes
echo "Stopping existing VLLM servers..."
pkill -f "vllm serve" || true
sleep 2

# Start servers in background
echo "Starting Base Qwen2.5-3B on GPU 0 (port 8000)..."
CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-3B-Instruct \
    --port 8000 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.95 > vllm_gpu0.log 2>&1 &

echo "Starting Fine-tuned 3B on GPU 1 (port 8001)..."
# Replace with your model path
CUDA_VISIBLE_DEVICES=1 vllm serve merged_models/merged-qwen2.5-3b-tau \
    --port 8001 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.95 > vllm_gpu1.log 2>&1 &

echo "Starting Fine-tuned 7B on GPU 2,3 (port 8002)..."
# Replace with your model path
CUDA_VISIBLE_DEVICES=2,3 vllm serve /path/to/your/finetuned-7b \
    --port 8002 \
    --tensor-parallel-size 2 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.95 > vllm_gpu2_3.log 2>&1 &

echo "Waiting for servers to start..."
sleep 10

# Check if servers are running
echo -e "\nChecking server status:"
curl -s http://localhost:8000/health && echo "✓ GPU 0 server (port 8000) is running" || echo "✗ GPU 0 server failed"
curl -s http://localhost:8001/health && echo "✓ GPU 1 server (port 8001) is running" || echo "✗ GPU 1 server failed"
curl -s http://localhost:8002/health && echo "✓ GPU 2-3 server (port 8002) is running" || echo "✗ GPU 2-3 server failed"

echo -e "\nLogs available at:"
echo "  GPU 0: vllm_gpu0.log"
echo "  GPU 1: vllm_gpu1.log"
echo "  GPU 2-3: vllm_gpu2_3.log"

echo -e "\nTo monitor logs:"
echo "  tail -f vllm_gpu0.log"