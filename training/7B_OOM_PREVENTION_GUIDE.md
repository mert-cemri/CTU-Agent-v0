# 7B Model OOM Prevention Guide

## Quick Fix

Run the optimized script instead:
```bash
./training/run_multi_domain_7b_optimized.sh
```

## Key Changes to Prevent OOM

### 1. Reduced Batch Sizes
```bash
# Original (OOM)
trainer.train_batch_size=64
trainer.policy_mini_batch_size=16
trainer.eval_batch_size=32

# Optimized (No OOM)
trainer.train_batch_size=32
trainer.policy_mini_batch_size=8
trainer.eval_batch_size=16
```

### 2. Memory Offloading
```bash
# Enable CPU offloading for all models
trainer.policy.fsdp_config.cpu_offload=true
trainer.ref.fsdp_config.cpu_offload=true
trainer.critic.fsdp_config.cpu_offload=true
trainer.reward.fsdp_config.cpu_offload=true

# Reshard after forward pass
trainer.policy.fsdp_config.reshard_after_forward=true

# Offload optimizer states
trainer.policy.optimizer_config.offload_after_step=true
```

### 3. Reduced Context Length
```bash
# Original
export VLLM_MAX_MODEL_LEN=32768
trainer.max_prompt_length=16384

# Optimized for 7B
export VLLM_MAX_MODEL_LEN=16384
trainer.max_prompt_length=16384
```

### 4. Generator Memory Settings
```bash
# Original
generator.gpu_memory_utilization=0.8
generator.n_samples_per_prompt=5
generator.max_num_batched_tokens=24576

# Optimized
generator.gpu_memory_utilization=0.75
generator.n_samples_per_prompt=3
generator.max_num_batched_tokens=16384
```

### 5. Gradient Checkpointing
```bash
# Enable gradient checkpointing
trainer.gradient_checkpointing=true
trainer.gradient_checkpointing_use_reentrant=false
```

### 6. Reduced Workers
```bash
# Original
environment.skyrl_gym.max_env_workers=16

# Optimized
environment.skyrl_gym.max_env_workers=8
```

## Memory Usage Estimates

### 7B Model Memory Requirements

| Configuration | VRAM per GPU | Total VRAM |
|--------------|--------------|------------|
| Original (OOM) | ~50GB | 400GB |
| Optimized | ~35-40GB | 280-320GB |
| With CPU Offload | ~25-30GB | 200-240GB |

### Per-GPU Breakdown (8 A100 80GB)
- Model weights: ~14GB (with tensor parallel=4)
- Optimizer states: ~10-15GB (with offloading)
- Activations: ~5-10GB (with gradient checkpointing)
- KV cache: ~5-10GB (reduced context)

## Monitoring Memory

```bash
# Watch GPU memory in real-time
watch -n 1 nvidia-smi

# Check for OOM in logs
tail -f ~/ckpts/tau_bench/*/logs/*.log | grep -i "out of memory"
```

## If Still Getting OOM

### Option 1: Further Reduce Batch Sizes
```bash
trainer.train_batch_size=16
trainer.policy_mini_batch_size=4
trainer.micro_train_batch_size_per_gpu=1
```

### Option 2: Increase Tensor Parallelism
```bash
generator.inference_engine_tensor_parallel_size=8  # Use all 8 GPUs
generator.num_inference_engines=1  # Only 1 engine
```

### Option 3: Use Fewer GPUs for Training
```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 ./training/run_multi_domain_7b_optimized.sh
```

### Option 4: Switch to 3B Model
```bash
# 3B model uses much less memory
./training/run_multi_domain_3b.sh
```

## Recommended Settings by GPU

### A100 80GB (8 GPUs)
Use the optimized script as-is.

### A100 40GB (8 GPUs)
```bash
# Further reduce memory usage
trainer.train_batch_size=16
trainer.policy_mini_batch_size=4
generator.gpu_memory_utilization=0.65
generator.n_samples_per_prompt=2
```

### V100 32GB (8 GPUs)
Consider using 3B model instead, or:
```bash
# Maximum memory savings
trainer.train_batch_size=8
trainer.policy_mini_batch_size=2
generator.gpu_memory_utilization=0.6
export VLLM_MAX_MODEL_LEN=8192
```

## Testing Before Full Training

Test with 1 epoch first:
```bash
./training/run_multi_domain_7b_optimized.sh trainer.epochs=1
```

If successful, increase epochs gradually.