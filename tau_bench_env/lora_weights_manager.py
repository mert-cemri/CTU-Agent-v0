"""
LoRA-compatible weights manager for CTU-Agent.

This module provides a wrapper around SkyRL's InferenceWeightsManager that handles
LoRA parameter name mapping for VLLM compatibility. When LoRA is used, PEFT wraps
the model and adds 'base_model.' prefix to parameter names, but VLLM expects the
original parameter names.
"""

from typing import List
from skyrl_train.workers.worker import PPORayActorGroup
from skyrl_train.inference_engines.inference_engine_client import InferenceEngineClient
from skyrl_train.weights_manager import InferenceWeightsManager
from ray import ObjectRef
import asyncio
import ray
from skyrl_train.utils import Timer
from loguru import logger


class LoRAInferenceWeightsManager(InferenceWeightsManager):
    """
    LoRA-compatible weights manager that strips 'base_model.' prefix from parameter names.
    
    This class extends the standard InferenceWeightsManager to handle LoRA models where
    PEFT adds 'base_model.' prefix to parameter names, but VLLM inference engines expect
    the original parameter names without this prefix.
    """
    
    def __init__(
        self,
        policy_model: PPORayActorGroup,
        inference_engine_client: InferenceEngineClient,
        colocate_all: bool,
        no_sync: bool = False,
        enable_lora_mapping: bool = True,
    ):
        """
        Initialize LoRA-compatible weights manager.
        
        Args:
            policy_model: PPO Ray actor group for policy model
            inference_engine_client: Client for inference engines
            colocate_all: Whether to colocate all components
            no_sync: Whether to skip weight synchronization
            enable_lora_mapping: Whether to enable LoRA parameter name mapping
        """
        super().__init__(policy_model, inference_engine_client, colocate_all, no_sync)
        self.enable_lora_mapping = enable_lora_mapping
        
    def sync_policy_weights_to_inference_engines(self) -> List[ObjectRef]:
        """Sync policy weights to inference engines with LoRA parameter name mapping."""
        if self.enable_lora_mapping:
            logger.info("Using LoRA-compatible weight sync with parameter name mapping")
            return self.policy_model.async_run_ray_method(
                "pass_through", "broadcast_to_inference_engines_lora", self.inference_engine_client
            )
        else:
            return super().sync_policy_weights_to_inference_engines()

    async def async_sync_policy_weights_to_inference_engines(self):
        """Async sync policy weights to inference engines with LoRA parameter name mapping."""
        if self.enable_lora_mapping:
            logger.info("Using async LoRA-compatible weight sync with parameter name mapping")
            return await self.policy_model.async_run_method(
                "pass_through", "broadcast_to_inference_engines_lora", self.inference_engine_client
            )
        else:
            return await super().async_sync_policy_weights_to_inference_engines()


def create_weights_manager(
    policy_model: PPORayActorGroup,
    inference_engine_client: InferenceEngineClient,
    colocate_all: bool,
    no_sync: bool = False,
    lora_rank: int = 0,
) -> InferenceWeightsManager:
    """
    Factory function to create the appropriate weights manager.
    
    Args:
        policy_model: PPO Ray actor group for policy model
        inference_engine_client: Client for inference engines  
        colocate_all: Whether to colocate all components
        no_sync: Whether to skip weight synchronization
        lora_rank: LoRA rank (>0 means LoRA is enabled)
        
    Returns:
        InferenceWeightsManager: Standard or LoRA-compatible weights manager
    """
    if lora_rank > 0:
        logger.info(f"Creating LoRA-compatible weights manager (LoRA rank: {lora_rank})")
        return LoRAInferenceWeightsManager(
            policy_model=policy_model,
            inference_engine_client=inference_engine_client,
            colocate_all=colocate_all,
            no_sync=no_sync,
            enable_lora_mapping=True,
        )
    else:
        logger.info("Creating standard weights manager (no LoRA)")
        return InferenceWeightsManager(
            policy_model=policy_model,
            inference_engine_client=inference_engine_client,
            colocate_all=colocate_all,
            no_sync=no_sync,
        )