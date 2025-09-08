#!/bin/bash

# Simple VLLM server startup script

# Configuration
MODEL="${1:-Qwen/Qwen2.5-3B-Instruct}"
PORT="${2:-8000}" # Default port 8000
MAX_MODEL_LEN="${3:-8192}" #65536 
GPU_UTIL="${4:-0.35}"
GPU_ID="${5:-0}"  # Default to GPU 0

# bash start_vllm_server.sh mcemri/qwen2.5-3b-rl-cut-agent-v3-step40-v0 8000 65536 0.9 3

echo "=================================================="
echo "         Starting VLLM Server"
echo "=================================================="
echo "Model: $MODEL"
echo "Port: $PORT"
echo "Max Model Length: $MAX_MODEL_LEN"
echo "GPU Memory Utilization: $GPU_UTIL"
echo "GPU ID: $GPU_ID"
echo ""

# # Show GPU status
# echo "Current GPU status:"
# nvidia-smi --query-gpu=index,name,memory.used,memory.total --format=csv,noheader,nounits | \
#     awk -v gpu_id="$GPU_ID" -F', ' 'BEGIN{print "GPU  Name                     Memory (Used/Total)"} 
#                                      {printf "%-3s  %-23s  %s/%s MB", $1, $2, $3, $4; 
#                                       if($1==gpu_id) printf " <- SELECTED"; print ""}'
# echo ""

# # Kill any existing VLLM server on this port
# echo "Checking for existing server on port $PORT..."
# lsof -ti:$PORT | xargs kill -9 2>/dev/null || true
# sleep 2

# Enable long context support
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export CUDA_VISIBLE_DEVICES=$GPU_ID

# Start VLLM server
echo "Starting server on GPU $GPU_ID..."
vllm serve "$MODEL" \
    --port $PORT \
    --max-model-len $MAX_MODEL_LEN \
    --gpu-memory-utilization $GPU_UTIL \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code \
    --disable-log-requests

# Note: Server runs in foreground
# To run in background, add: > vllm.log 2>&1 &

