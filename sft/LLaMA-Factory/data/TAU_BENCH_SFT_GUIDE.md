# Tau-Bench SFT Data Processing Guide

## Overview

Convert tau_bench multi-turn tool-calling conversations to LLaMA-Factory ShareGPT format for supervised fine-tuning.

## Format Conversion

**Input (OpenAI format):**
```json
{
  "messages": [
    {"role": "system", "content": "System prompt"},
    {"role": "user", "content": "User request"},
    {"role": "assistant", "tool_calls": [{"function": {"name": "tool", "arguments": "{}"}}]},
    {"role": "tool", "content": "Result"}
  ],
  "tools": [{"type": "function", "function": {...}}]
}
```

**Output (ShareGPT format):**
```json
{
  "conversations": [
    {"from": "human", "value": "User request"},
    {"from": "function_call", "value": "{\"name\": \"tool\", \"arguments\": {}}"},
    {"from": "observation", "value": "Result"},
    {"from": "gpt", "value": "Response"}
  ],
  "system": "System prompt",
  "tools": "[{\"type\": \"function\", \"function\": {...}}]"
}
```

## Usage

### 1. Convert Data
```bash
cd sft/LLaMA-Factory/data
python tau_bench_converter.py \
  --input_dir ../../../../data/reward_filtered_sft_data_all_domains.jsonl \
  --output_dir tau_bench/reward_filtered_sft_data_all_domains
```

### 2. Train Model
```bash
cd ../examples/tau_bench
llamafactory-cli train qwen2_5_3b_lora_sft.yaml
```

## Dataset Variants

- `tau_bench_full` - Complete dataset
- `tau_bench_balanced` - Equal samples per domain
- `tau_bench_tools` - Tool-calling focused
- `tau_bench_{domain}` - Domain-specific (airline, retail, healthcare, telecom, doordash)

## Validation

Ensure:
- Proper role alternation (human/observation → gpt/function_call)
- Valid JSON in tool calls
- System prompts extracted
- Complete tool descriptions

## Hardware Requirements

| Model | Method | VRAM | Time |
|-------|--------|------|------|
| Qwen2.5-3B | LoRA | 16GB | 8-12h |
| Qwen2.5-3B | Full | 24GB | 24-36h |
| Qwen2.5-7B | QLoRA | 16-20GB | 12-18h |