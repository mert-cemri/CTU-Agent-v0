# Context Length Configuration Guide

## Quick Fix for Context Length Errors

If you see errors like:
```
"This model's maximum context length is 8192 tokens. However, you requested 8209 tokens..."
```

### Solution 1: Increase Context Length (Recommended)

```bash
# Enable long context support
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

# For Qwen2.5-3B (supports up to 32K)
vllm serve Qwen/Qwen2.5-3B-Instruct \
    --port 8000 \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.95 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code

# For Qwen2.5-7B (supports up to 128K but memory intensive)
vllm serve Qwen/Qwen2.5-7B-Instruct \
    --port 8001 \
    --max-model-len 32768 \
    --tensor-parallel-size 2 \
    --gpu-memory-utilization 0.95 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code
```

### Solution 2: Memory-Optimized Settings

Based on your GPU memory:

**For A100 40GB:**
```bash
# 3B model - can handle 32K easily
--max-model-len 32768 --gpu-memory-utilization 0.95

# 7B model - balance context and memory
--max-model-len 16384 --gpu-memory-utilization 0.90
```

**For A100 80GB:**
```bash
# 3B model - go for maximum context
--max-model-len 65536 --gpu-memory-utilization 0.95

# 7B model - comfortable with 32K
--max-model-len 32768 --gpu-memory-utilization 0.95
```

**For V100 32GB:**
```bash
# 3B model
--max-model-len 16384 --gpu-memory-utilization 0.90

# 7B model - need tensor parallelism
--max-model-len 8192 --tensor-parallel-size 2 --gpu-memory-utilization 0.85
```

### Solution 3: Automatic KV Cache Management

```bash
# Let VLLM manage memory automatically
vllm serve Qwen/Qwen2.5-3B-Instruct \
    --port 8000 \
    --max-model-len 32768 \
    --enable-prefix-caching \
    --enable-chunked-prefill \
    --max-num-batched-tokens 32768 \
    --gpu-memory-utilization 0.95 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes
```

## Context Requirements for Tau-Bench

Tau-bench conversations can get long due to:
- Multi-turn conversations (up to 20 turns)
- Tool descriptions and responses
- User simulator responses

**Recommended minimum context lengths:**
- **Retail domain**: 16384 tokens
- **Airline domain**: 16384 tokens
- **Safe for all tasks**: 32768 tokens

## Debugging Context Issues

Check actual context usage:
```bash
# Enable debug mode to see token counts
export DEBUG_PARSER=1
python test_qwen.py --env retail --tasks 1
```

Monitor VLLM memory:
```bash
# Watch GPU memory usage
watch -n 1 nvidia-smi

# Check VLLM logs for OOM errors
tail -f vllm_gpu0.log
```

## Quick Commands

```bash
# Standard setup for tau-bench testing
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

# 3B model with 32K context
CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2.5-3B-Instruct \
    --port 8000 --max-model-len 32768 --gpu-memory-utilization 0.95 \
    --enable-auto-tool-choice --tool-call-parser hermes --trust-remote-code

# Test it
python test_qwen.py --env retail --base-url "http://localhost:8000/v1"
```