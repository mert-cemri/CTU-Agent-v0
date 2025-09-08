# VLLM Testing Guide

## Quick Start

### 1. Start VLLM Server
```bash
# For your fine-tuned 3B model
vllm serve /path/to/qwen2.5-3b-finetuned \
    --port 8000 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes

# For your fine-tuned 7B model (different port)
vllm serve /path/to/qwen2.5-7b-finetuned \
    --port 8001 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes
```

### 2. Test Models
```bash
cd testing/tau-bench

# Install dependencies
pip install -e .

# Test 3B model on 5 retail tasks
python run_vllm.py \
    --model "Qwen/Qwen2.5-3B-Instruct" \
    --base-url "http://localhost:8000/v1" \
    --env retail \
    --task-ids 1 2 3 4 5

# Test 7B model on airline tasks
python run_vllm.py \
    --model "Qwen/Qwen2.5-7B-Instruct" \
    --base-url "http://localhost:8001/v1" \
    --env airline \
    --max-concurrency 2
```

## Files Created

1. **`tau_bench/agents/vllm_agent.py`**: Direct VLLM integration via OpenAI API
2. **`run_vllm.py`**: Standalone script for VLLM model evaluation

## Key Features

- Direct VLLM support without litellm dependency
- OpenAI-compatible API for tool calling
- Concurrent task execution
- Automatic result saving with timestamps
- Success rate metrics

## Expected Performance

- **Untrained models**: Pass rate ~20-30%
- **After SFT**: Pass rate ~40-50%
- **GPT-4o baseline**: Pass rate ~42% (airline), ~60% (retail)

## Troubleshooting

If tool calling fails:
- Ensure VLLM server has `--enable-auto-tool-choice`
- Check model supports tool calling format
- Verify OpenAI client version >= 1.0

## Results Location

Results saved to: `vllm_results/<model>_<domain>_<timestamp>.json`