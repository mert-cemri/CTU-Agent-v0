#!/bin/bash

# Simple VLLM server startup script

# Configuration
MODEL="${1:-Qwen/Qwen2.5-3B-Instruct}"
PORT="${2:-8000}" # Default port 8000
MAX_MODEL_LEN="${3:-8192}" #65536 
GPU_UTIL="${4:-0.35}"
GPU_ID="${5:-0}"  # Default to GPU 0

# bash start_vllm_server.sh mcemri/qwen2.5-3b-rl-cut-agent-v3-step40-v0 8000 65536 0.9 3
# bash start_vllm_server.sh mcemri/qwen2.5_3b_alldata_sft_v0-step40-v0 8001 65536 0.9 7
# bash start_vllm_server.sh Qwen/Qwen3-8B 8001 65536 0.9 6
# bash start_vllm_server.sh Qwen/Qwen3-4B-Instruct-2507 8002 65536 0.9 7
# bash start_vllm_server.sh mcemri/qwen2.5-3b-rl-cut-agent-grpo-taxonomy-step80-pure 8000 65536 0.9 0
# python test.py --mode vllm     --model mcemri/qwen2.5-3b-rl-cut-agent-grpo-taxonomy-step80-pure    --base-url http://localhost:8000/v1     --env airline     --max-concurrency 2     --output-dir testing_results/qwen25_3b_grpo_taxonomy_v0_airline
# python test.py --mode vllm     --model mcemri/qwen2.5-3b-rl-cut-agent-grpo-taxonomy-step80-pure    --base-url http://localhost:8000/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen25_3b_grpo_taxonomy_v0_retail

# python test.py --mode vllm     --model mcemri/qwen2.5-7b-rl-cut-agent-grpo-step100-v0    --base-url http://localhost:8000/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen25_7b-rl-cut-agent-grpo-step100_retail
# python test.py --mode vllm     --model mcemri/qwen2.5-7b-rl-cut-agent-grpo-taxonomy-step100-v0    --base-url http://localhost:8001/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen25_7b-rl-cut-agent-grpo-taxonomy-step100_retail
# python test.py --mode vllm     --model mcemri/qwen2.5-7b-rl-cut-agent-grpo-step20-v0    --base-url http://localhost:8002/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen25_7b-rl-cut-agent-grpo-step20_retail
# python test.py --mode vllm     --model mcemri/qwen2.5-7b-rl-cut-agent-grpo-taxonomy-step200-v0    --base-url http://localhost:8003/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen25_7b-rl-cut-agent-grpo-taxonomy-step200_retail
# python test.py --mode vllm     --model mcemri/qwen2.5-7b-multi-domain-rl-grpo-taxonomy-fil-v0    --base-url http://localhost:8004/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen2.5-7b-multi-domain-rl-grpo-taxonomy-fil-v0_retail
# python test.py --mode vllm     --model mcemri/qwen2.5-7b-sft-v1   --base-url http://localhost:8003/v1     --env retail     --max-concurrency 2     --output-dir testing_results/qwen2.5-7b-sft-v1_retail
# python test.py --mode vllm     --model Qwen/Qwen2.5-3B-Instruct  --base-url http://localhost:8005/v1     --env airline     --max-concurrency 2     --output-dir testing_results/qwen2.5-3b-instruct-v1_airline
# python test.py --mode vllm     --model  mcemri/ mcemri/qwen2.5-3b-rl-cut-agent-grpo-pure-step80-v0  --base-url http://localhost:8005/v1     --env airline     --max-concurrency 2     --output-dir testing_results/ mcemri/qwen2.5-3b-rl-cut-agent-grpo-pure-step80-v0_airline


# bash start_vllm_server.sh mcemri/qwen2.5-7b-rl-cut-agent-grpo-step100-v0 8000 65536 0.9 0
# bash start_vllm_server.sh mcemri/qwen2.5-7b-rl-cut-agent-grpo-taxonomy-step100-v0 8001 65536 0.9 1
# bash start_vllm_server.sh mcemri/qwen2.5-7b-rl-cut-agent-grpo-step20-v0 8002 65536 0.9 2
# bash start_vllm_server.sh mcemri/qwen2.5-7b-sft-v1 8003 32768 0.9 3
# bash start_vllm_server.sh mcemri/qwen2.5-7b-multi-domain-rl-grpo-taxonomy-fil-v0 8004 32768 0.9 4
# bash start_vllm_server.sh Qwen/Qwen2.5-3B-Instruct 8005 32768 0.9 5
# bash start_vllm_server.sh mcemri/qwen2.5-7b-sft-multi-domain-rl-grpo-taxonomy-step20-v0 8007 32768 0.9 7
# bash start_vllm_server.sh mcemri/qwen2.5-3b-rl-cut-agent-grpo-pure-step80-v0 8005 32768 0.9 5
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

