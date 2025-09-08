# Tau-Bench Testing Guide

## Quick Start

### 1. Installation
```bash
cd testing/tau-bench
pip install -e .
export OPENAI_API_KEY="your-api-key"  # For user simulator
```

### 2. Testing Modes

The unified `test.py` script supports three modes:

#### Mode 1: VLLM Testing (Recommended for Local Models)
```bash
# Start VLLM server first
bash start_vllm_server.sh

# Run tests
python test.py --mode vllm \
    --model Qwen/Qwen2.5-3B-Instruct \
    --base-url http://localhost:8000/v1 \
    --env retail
```

#### Mode 2: Standard Testing (For API Models)
```bash
python test.py --mode standard \
    --model gpt-4o \
    --model-provider openai \
    --env airline
```

#### Mode 3: Quick Testing (First 5 Tasks Only)
```bash
python test.py --mode quick \
    --model Qwen/Qwen2.5-3B-Instruct \
    --base-url http://localhost:8000/v1 \
    --env retail
```

## Full Evaluation

### Retail Domain (115 Tasks)
```bash
python test.py --mode vllm \
    --model your-model \
    --base-url http://localhost:8000/v1 \
    --env retail \
    --max-concurrency 4
```

### Airline Domain (50 Tasks)
```bash
python test.py --mode vllm \
    --model your-model \
    --base-url http://localhost:8000/v1 \
    --env airline \
    --max-concurrency 4
```

## Specific Task Testing
```bash
# Test specific task IDs
python test.py --mode vllm \
    --model your-model \
    --base-url http://localhost:8000/v1 \
    --env retail \
    --task-ids 0 1 2 3 4
```

## Output Structure

Results are saved in organized directories:
```
results/
├── retail_20240915_143022/
│   ├── retail_full_results.json          # All results with conversations
│   ├── conversations/
│   │   ├── task_000.json                 # Individual task conversation
│   │   ├── task_001.json
│   │   └── ...
│   └── summary/
│       └── evaluation_summary.json       # Performance metrics
```

## Result Format

Each task result includes:
- `task_id`: Task identifier
- `reward`: Task completion score (0.0-1.0)
- `info`: Task details and metadata
- `traj`: Full conversation trajectory
- `trial`: Trial number for multiple runs

## VLLM Server Configuration

### Memory-Optimized Settings

Based on your GPU and requirements:

#### For 8×A100 80GB (Your Setup)
```bash
# Conservative for training compatibility
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
vllm serve your-model \
    --port 8000 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.3 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code

# Standard for testing only
vllm serve your-model \
    --port 8000 \
    --max-model-len 16384 \
    --gpu-memory-utilization 0.5 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code
```

#### For Different Models
```bash
# 3B Model
--max-model-len 16384 --gpu-memory-utilization 0.5

# 7B Model
--max-model-len 8192 --gpu-memory-utilization 0.4

# 13B Model
--max-model-len 4096 --gpu-memory-utilization 0.3
```

## User Simulator Options

### Strategy Options
- `llm`: Standard LLM-based user (default)
- `react`: User with explicit reasoning
- `verify`: User with verification step
- `reflection`: User with self-reflection

### Example with Different User
```bash
python test.py --mode vllm \
    --model your-model \
    --base-url http://localhost:8000/v1 \
    --env retail \
    --user-model claude-3-5-sonnet-20240620 \
    --user-provider anthropic \
    --user-strategy react
```

## Parallel Testing

Adjust concurrency based on API limits:
```bash
# High concurrency for local models
--max-concurrency 10

# Low concurrency for API models
--max-concurrency 2
```

## Analyzing Results

### View Summary
```bash
cat results/*/summary/evaluation_summary.json | jq .
```

### Count Successful Tasks
```bash
jq '[.[] | select(.reward > 0.9)] | length' results/*/retail_full_results.json
```

### Extract Failed Tasks
```bash
jq '[.[] | select(.reward < 0.9) | {task_id, reward}]' results/*/retail_full_results.json
```

## Common Issues

### Context Length Errors
Increase `--max-model-len` in VLLM server:
```bash
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
vllm serve ... --max-model-len 32768
```

### OOM Errors
Reduce `--gpu-memory-utilization`:
```bash
vllm serve ... --gpu-memory-utilization 0.3
```

### Slow Generation
Increase `--max-concurrency` or use multiple GPUs:
```bash
CUDA_VISIBLE_DEVICES=0,1 vllm serve ... --tensor-parallel-size 2
```

## Comparing Models

Test multiple models and compare:
```bash
# Test base model
python test.py --mode vllm --model Qwen/Qwen2.5-3B-Instruct \
    --base-url http://localhost:8000/v1 --env retail \
    --output-dir results/base_3b

# Test fine-tuned model  
python test.py --mode vllm --model your-finetuned-model \
    --base-url http://localhost:8001/v1 --env retail \
    --output-dir results/finetuned_3b

# Compare results
python compare_results.py results/base_3b results/finetuned_3b
```