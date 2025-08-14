# Tau-Bench LoRA Training

LoRA fine-tuning for Qwen2.5 models on tau_bench reward-filtered dataset.

## Quick Start

```bash
# Train 3B model (recommended)
./train_tau_bench.sh 3b

# Train 7B model
./train_tau_bench.sh 7b

# Use tool-focused dataset
./train_tau_bench.sh 3b reward_tools
```

## Manual Training

```bash
# 3B model
llamafactory-cli train qwen2_5_3b_lora_sft.yaml

# 7B model  
llamafactory-cli train qwen2_5_7b_lora_sft.yaml
```

## Hardware Requirements

| Model | VRAM | Batch Size | Training Time |
|-------|------|------------|---------------|
| Qwen2.5-3B | 16GB | 2 | 8-12 hours |
| Qwen2.5-7B | 24GB | 1 | 12-18 hours |

## Available Datasets

- `tau_bench_reward_full` - Complete reward-filtered dataset
- `tau_bench_reward_tools` - Tool-calling focused subset

## Evaluation

```bash
# Interactive chat
llamafactory-cli chat --model_name_or_path saves/qwen2_5_3b_tau_bench_lora

# Export merged model
llamafactory-cli export \
    --model_name_or_path Qwen/Qwen2.5-3B-Instruct \
    --adapter_name_or_path saves/qwen2_5_3b_tau_bench_lora \
    --export_dir models/qwen2_5_3b_tau_bench_merged
```