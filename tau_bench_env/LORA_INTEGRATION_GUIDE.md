# LoRA Integration Guide for CTU-Agent

This guide shows how to use the application-layer LoRA solution in CTU-Agent training scripts.

## Overview

The LoRA integration provides:
- **LoRA-compatible workers** that handle weight synchronization between LoRA models and VLLM
- **Parameter name mapping** that strips `base_model.` prefix from LoRA parameters  
- **Drop-in replacement** for standard SkyRL components
- **No modifications** to the core SkyRL codebase

## Key Components

### 1. LoRA Configuration (`lora_config.py`)
- Detects LoRA settings from training config
- Validates LoRA parameters
- Provides utilities for conditional LoRA handling

### 2. LoRA Workers (`lora_workers.py`)
- `LoRAFSDPPolicyWorker`: FSDP policy worker with LoRA support
- `LoRADeepSpeedPolicyWorker`: DeepSpeed policy worker with LoRA support
- Factory function to create appropriate worker type

### 3. LoRA Weights Manager (`lora_weights_manager.py`)  
- `LoRAInferenceWeightsManager`: Handles weight sync with parameter mapping
- Factory function to create standard or LoRA weights manager

### 4. Worker Mixins (`lora_worker_mixins.py`)
- Reusable mixins that add LoRA broadcasting methods
- Separate implementations for FSDP and DeepSpeed

## Usage Example

Here's how to integrate LoRA support into a training script:

```python
import hydra
from omegaconf import DictConfig
from skyrl_train.trainers.ppo_trainer import PPOTrainer
from tau_bench_env import (
    LoRAConfig, 
    validate_lora_config, 
    log_lora_status,
    create_weights_manager,
    create_lora_policy_worker
)

@hydra.main(config_path="training/configs", config_name="tau_bench_config")
def main(cfg: DictConfig):
    # 1. Validate and log LoRA configuration
    validate_lora_config(cfg)
    log_lora_status(cfg)
    
    # 2. Create LoRA configuration object
    lora_config = LoRAConfig(cfg)
    
    # 3. Initialize trainer with conditional LoRA support
    trainer = PPOTrainer(cfg)
    
    # 4. Create appropriate policy worker
    if lora_config.enabled:
        policy_worker_class = create_lora_policy_worker(lora_config.strategy)
    else:
        # Use standard SkyRL workers
        if cfg.trainer.strategy == 'fsdp':
            from SkyRL_mod.skyrl_train.skyrl_train.workers.fsdp.fsdp_worker import PolicyWorker
            policy_worker_class = PolicyWorker
        elif cfg.trainer.strategy == 'deepspeed':
            from SkyRL_mod.skyrl_train.skyrl_train.workers.deepspeed.deepspeed_worker import PolicyWorker  
            policy_worker_class = PolicyWorker
    
    # 5. Initialize policy model with chosen worker
    trainer.init_policy_workers(policy_worker_class)
    
    # 6. Create appropriate weights manager
    weights_manager = create_weights_manager(
        policy_model=trainer.policy_model,
        inference_engine_client=trainer.inference_engine_client,
        colocate_all=cfg.trainer.placement.colocate_all,
        no_sync=cfg.trainer.no_sync,
        lora_rank=lora_config.rank,
    )
    
    # 7. Use weights manager in training loop
    trainer.set_weights_manager(weights_manager)
    trainer.fit()

if __name__ == "__main__":
    main()
```

## Configuration

The LoRA parameters should be configured in your training config:

```yaml
trainer:
  strategy: "fsdp"  # or "deepspeed" 
  policy:
    model:
      path: "Qwen/Qwen2.5-3B-Instruct"
      lora_rank: 32      # >0 enables LoRA
      lora_alpha: 64     # LoRA scaling parameter
      lora_dropout: 0.1  # LoRA dropout rate
```

## How It Works

### 1. Parameter Name Mapping

When LoRA is enabled, PEFT wraps the model and adds `base_model.` prefix to all parameters:
- Original: `model.layers.0.self_attn.q_proj.weight`
- LoRA: `base_model.model.layers.0.self_attn.q_proj.weight`

The LoRA workers detect this and strip the prefix when syncing to VLLM:
```python
def _map_lora_parameter_name(self, param_name: str) -> str:
    if param_name.startswith("base_model."):
        return param_name[len("base_model."):]
    return param_name
```

### 2. Conditional Usage

The system automatically detects LoRA configuration and switches between:
- **LoRA mode**: Uses `LoRAInferenceWeightsManager` and LoRA-compatible workers
- **Standard mode**: Uses standard SkyRL components unchanged

### 3. Broadcasting Methods

LoRA workers implement `broadcast_to_inference_engines_lora()` methods that:
1. Get model parameters (with `base_model.` prefix)
2. Map parameter names for VLLM compatibility
3. Broadcast weights using mapped names
4. Handle both CUDA IPC and standard broadcasting

## Benefits

1. **No SkyRL modifications**: Core SkyRL codebase remains untouched
2. **Drop-in compatibility**: Standard training works unchanged
3. **Automatic detection**: Switches based on `lora_rank > 0`
4. **Full strategy support**: Works with both FSDP and DeepSpeed
5. **Robust error handling**: Validates configuration and provides clear errors

## Testing

Test the LoRA integration with your existing scripts:

```bash
# Standard training (no changes needed)
./training/run_retail_3b_grpo.sh

# LoRA training (automatically detected)
./training/run_retail_4b_grpo_lora.sh
```

The system will automatically log whether LoRA is enabled and which components are being used.

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure `tau_bench_env` is in your Python path
2. **Configuration errors**: Check that LoRA parameters are under `trainer.policy.model`
3. **Worker mismatch**: Ensure strategy matches LoRA worker type ('fsdp' or 'deepspeed')

### Debug Logging

Enable debug logging to see LoRA parameter mapping:
```python
import logging
logging.getLogger('tau_bench_env.lora_worker_mixins').setLevel(logging.DEBUG)
```

This will show parameter name mappings during weight synchronization.