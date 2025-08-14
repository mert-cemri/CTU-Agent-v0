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

### 1. Convert Data (already completed)
```bash
cd sft/LLaMA-Factory/data
python tau_bench_converter.py \
  --input_dir ../../../../data/reward_filtered_sft_data_all_domains.jsonl \
  --output_dir tau_bench/reward_filtered_sft_data_all_domains
```

### 2. Train Models
```bash
cd ../examples/tau_bench

# Train 3B model (recommended)
./train_tau_bench.sh 3b

# Train 7B model  
./train_tau_bench.sh 7b

# Manual training
llamafactory-cli train qwen2_5_3b_lora_sft.yaml
llamafactory-cli train qwen2_5_7b_lora_sft.yaml
```

## Dataset Variants

- `tau_bench_reward_full` - Complete reward-filtered dataset
- `tau_bench_reward_tools` - Tool-calling focused subset

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