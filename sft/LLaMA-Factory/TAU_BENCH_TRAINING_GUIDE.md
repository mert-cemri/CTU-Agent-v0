# Tau-Bench Training Guide for LLaMA-Factory

## Available Datasets

After running the converter, you have these datasets registered in `dataset_info.json`:

### Original Domains (Airline, Retail)
- `tau_bench_reward_full` - Complete dataset from all original domains
- `tau_bench_reward_tools` - Tool-calling focused subset

### New Domains (Healthcare, Telecom, DoorDash)  
- `tau_bench_new_domains` - Complete dataset from new domains
- `tau_bench_new_domains_tools` - Tool-calling focused subset

## Training Commands

### 1. Using Standard Script (Limited Options)

```bash
cd sft/LLaMA-Factory

# Train on original domains (default)
./examples/tau_bench/train_tau_bench.sh 3b reward_full

# Train on tools subset
./examples/tau_bench/train_tau_bench.sh 3b reward_tools
```

### 2. Using Custom Script (Flexible)

```bash
cd sft/LLaMA-Factory

# Train on new domains dataset
./examples/tau_bench/train_tau_bench_custom.sh 3b tau_bench_new_domains

# Train on new domains tools subset
./examples/tau_bench/train_tau_bench_custom.sh 3b tau_bench_new_domains_tools

# Train with custom dataset path
./examples/tau_bench/train_tau_bench_custom.sh 3b my_custom_dataset "tau_bench/my_custom_data/data.json"
```

### 3. Direct YAML Modification

Edit `examples/tau_bench/qwen2_5_3b_lora_sft.yaml`:

```yaml
### dataset
dataset: tau_bench_new_domains  # Change this line
template: qwen
cutoff_len: 8192
```

Then run:
```bash
llamafactory-cli train examples/tau_bench/qwen2_5_3b_lora_sft.yaml
```

## Training Both Domain Sets

To train on both original and new domains:

```bash
# Option 1: Train sequentially
./examples/tau_bench/train_tau_bench.sh 3b reward_full
# After completion, continue training:
./examples/tau_bench/train_tau_bench_custom.sh 3b tau_bench_new_domains

# Option 2: Combine datasets first
python3 << EOF
import json

# Load both datasets
with open('data/tau_bench/reward_filtered_sft_data_all_domains/tau_bench_full.json') as f:
    original = json.load(f)
    
with open('data/tau_bench/reward_filtered_sft_data_new_domains/tau_bench_full.json') as f:
    new_domains = json.load(f)

# Combine
combined = original + new_domains

# Save
with open('data/tau_bench/combined_all_domains.json', 'w') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)
    
print(f"Combined dataset: {len(combined)} examples")
EOF

# Then train on combined dataset
./examples/tau_bench/train_tau_bench_custom.sh 3b tau_bench_combined "tau_bench/combined_all_domains.json"
```

## Multi-GPU Training

```bash
# Use specific GPUs
CUDA_VISIBLE_DEVICES=0,1,2,3 ./examples/tau_bench/train_tau_bench_custom.sh 3b tau_bench_new_domains

# Use all GPUs (default)
./examples/tau_bench/train_tau_bench_custom.sh 3b tau_bench_new_domains
```

## After Training

### Merge LoRA Weights

```bash
# For 3B model
llamafactory-cli export \
    --model_name_or_path Qwen/Qwen2.5-3B-Instruct \
    --adapter_name_or_path saves/qwen2_5_3b_tau_bench_lora \
    --template qwen \
    --export_dir merged_models/qwen2.5-3b-tau-new-domains \
    --export_size 4 \
    --export_legacy_format false

# For 7B model
llamafactory-cli export \
    --model_name_or_path Qwen/Qwen2.5-7B-Instruct \
    --adapter_name_or_path saves/qwen2_5_7b_tau_bench_lora \
    --template qwen \
    --export_dir merged_models/qwen2.5-7b-tau-new-domains \
    --export_size 4 \
    --export_legacy_format false
```

### Test Fine-tuned Model

```bash
cd ../../testing/tau-bench

# Serve the merged model
vllm serve merged_models/qwen2.5-3b-tau-new-domains \
    --port 8001 \
    --max-model-len 32768 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes

# Test it
python test_qwen.py \
    --model "qwen2.5-3b-tau-new-domains" \
    --base-url "http://localhost:8001/v1" \
    --env retail
```

## Dataset Summary

| Dataset | Examples | Domains | Focus |
|---------|----------|---------|-------|
| tau_bench_reward_full | ~14,000 | Airline, Retail | All conversations |
| tau_bench_reward_tools | ~8,000 | Airline, Retail | Tool-heavy |
| tau_bench_new_domains | ~10,000 | Healthcare, Telecom, DoorDash | All conversations |
| tau_bench_new_domains_tools | ~6,000 | Healthcare, Telecom, DoorDash | Tool-heavy |

## Tips

1. **Start with tools subset** for faster training and validation
2. **Use new domains** to test generalization
3. **Combine datasets** for comprehensive training
4. **Monitor GPU memory** - reduce batch size if OOM
5. **Save checkpoints frequently** with `save_steps: 500`