# Qwen2.5-3B-Instruct Testing Guide

## Prerequisites

1. Install dependencies:
```bash
cd testing/tau-bench
pip install -e .
pip install openai  # Required for VLLM client
```

2. Set OpenAI API key for user simulator:
```bash
export OPENAI_API_KEY="your-api-key"
```

## Testing Qwen2.5-3B-Instruct

### Option 1: Using VLLM Server

Start VLLM server with Qwen2.5-3B:
```bash
vllm serve Qwen/Qwen2.5-3B-Instruct \
    --port 8000 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code \
    --max-model-len 8192
```

Test the model:
```bash
# Quick test with 3 retail tasks
python test_qwen.py --env retail --tasks 1 2 3

# Test airline domain
python test_qwen.py --env airline --tasks 1 2 3 4 5

# Test with different temperature
python test_qwen.py --temperature 0.7 --tasks 1 2 3
```

### Option 2: Using Your Fine-tuned Model

Start VLLM with your fine-tuned model:
```bash
vllm serve /path/to/your/finetuned/qwen2.5-3b \
    --port 8000 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --trust-remote-code
```

Test your model:
```bash
python test_qwen.py \
    --model "your-model-name" \
    --env retail \
    --tasks 1 2 3 4 5 6 7 8 9 10
```

## What the Test Does

1. **Special Token Handling**: Automatically cleans Qwen special tokens like `<|im_end|>`, `<|endoftext|>`
2. **Tool Call Parsing**: Handles both native OpenAI format and Qwen's text-based tool calls
3. **Error Recovery**: Gracefully handles parsing errors with fallback responses
4. **Performance Metrics**: Shows success rate, average reward, and per-task analysis

## Expected Results

### Base Qwen2.5-3B (No Fine-tuning)
- Success rate: 20-30%
- May struggle with complex tool compositions
- Good at understanding intent but may fail on tool syntax

### After Fine-tuning on tau_bench data
- Success rate: 40-60%
- Better tool call formatting
- Improved multi-turn conversation handling

### Comparison Baselines
- GPT-4o: ~42% (airline), ~60% (retail)
- Claude-3.5: ~36% (airline), ~63% (retail)

## Troubleshooting

### Issue: "No module named 'openai'"
```bash
pip install openai
```

### Issue: Tool calls not working
Ensure VLLM server started with:
- `--enable-auto-tool-choice`
- `--tool-call-parser hermes`

### Issue: Model runs out of memory
Reduce context length:
```bash
vllm serve Qwen/Qwen2.5-3B-Instruct \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.9
```

### Issue: Special tokens appearing in output
The QwenVLLMAgent automatically handles these, but if issues persist:
```python
# Check agent is cleaning tokens
export DEBUG_PARSER=1
python test_qwen.py --tasks 1
```

## Output Files

Results saved to `qwen_results/` directory:
- `qwen25_3b_retail_YYYYMMDD_HHMMSS.json`: Full conversation traces
- Each file contains task rewards, tool calls, and complete message history

## Performance Optimization

For better performance:
1. Use temperature 0.0 for deterministic tool calling
2. Start with retail domain (easier than airline)
3. Test tasks 1-5 first (simpler scenarios)
4. Fine-tune on tau_bench training data for significant improvement