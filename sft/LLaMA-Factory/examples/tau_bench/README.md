# Tau-Bench SFT Training

Train language models on tau_bench multi-turn tool-calling conversations.

## Quick Start

```bash
# Convert data and train 3B LoRA model
./train_tau_bench.sh 3b lora full

# Train 7B QLoRA model on balanced dataset
./train_tau_bench.sh 7b qlora balanced
```

## Configurations

| Model | Method | Dataset | VRAM | Config |
|-------|--------|---------|------|--------|
| Qwen2.5-3B | LoRA | Full | 16GB | `qwen2_5_3b_lora_sft.yaml` |
| Qwen2.5-3B | Full | Full | 24GB | `qwen2_5_3b_full_sft.yaml` |
| Qwen2.5-7B | QLoRA | Balanced | 16-20GB | `qwen2_5_7b_qlora_sft.yaml` |

## Manual Training

```bash
# Convert data first
cd ../../data
python tau_bench_converter.py \
  --input_dir ../../../data/tau_bench_multi \
  --output_dir tau_bench/processed

# Train model
cd ../examples/tau_bench
llamafactory-cli train qwen2_5_3b_lora_sft.yaml
```

## Datasets

- `tau_bench_full` - Complete dataset
- `tau_bench_balanced` - Equal samples per domain
- `tau_bench_tools` - Tool-calling focused
- `tau_bench_{domain}` - Domain-specific

## Evaluation

```bash
# Interactive chat
llamafactory-cli chat --model_name_or_path saves/qwen2_5_3b_tau_bench_lora

# API server
llamafactory-cli api --model_name_or_path saves/qwen2_5_3b_tau_bench_lora
```