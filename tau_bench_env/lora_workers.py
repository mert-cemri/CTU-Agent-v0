"""
LoRA-compatible worker classes for CTU-Agent.

This module provides application-layer worker classes that combine SkyRL workers
with LoRA-compatible mixins to handle weight synchronization between LoRA models
and VLLM inference engines.
"""

import ray
from SkyRL_mod.skyrl_train.skyrl_train.workers.fsdp.fsdp_worker import FSDPPolicyWorkerBase
from SkyRL_mod.skyrl_train.skyrl_train.workers.deepspeed.deepspeed_worker import DeepSpeedPolicyWorkerBase
from .lora_worker_mixins import LoRAFSDPWorkerMixin, LoRADeepSpeedWorkerMixin


class LoRAFSDPPolicyWorker(LoRAFSDPWorkerMixin, FSDPPolicyWorkerBase):
    """
    FSDP policy worker with LoRA weight synchronization support.
    
    This class combines the standard FSDP policy worker with LoRA-compatible
    weight broadcasting methods that handle parameter name mapping for VLLM.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class LoRADeepSpeedPolicyWorker(LoRADeepSpeedWorkerMixin, DeepSpeedPolicyWorkerBase):
    """
    DeepSpeed policy worker with LoRA weight synchronization support.
    
    This class combines the standard DeepSpeed policy worker with LoRA-compatible  
    weight broadcasting methods that handle parameter name mapping for VLLM.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Create Ray remote worker classes
LoRAFSDPPolicyWorkerRay = ray.remote(num_gpus=1)(LoRAFSDPPolicyWorker)
LoRADeepSpeedPolicyWorkerRay = ray.remote(num_gpus=1)(LoRADeepSpeedPolicyWorker)


def create_lora_policy_worker(strategy: str):
    """
    Factory function to create the appropriate LoRA-compatible policy worker.
    
    Args:
        strategy: Training strategy ('fsdp' or 'deepspeed')
        
    Returns:
        Ray remote worker class with LoRA support
    """
    if strategy in ('fsdp', 'fsdp2'):
        return LoRAFSDPPolicyWorkerRay
    elif strategy == 'deepspeed':
        return LoRADeepSpeedPolicyWorkerRay
    else:
        raise ValueError(f"Unsupported strategy: {strategy}. Must be 'fsdp', 'fsdp2', or 'deepspeed'.")