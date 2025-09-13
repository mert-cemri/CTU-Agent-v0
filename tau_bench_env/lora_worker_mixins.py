"""
LoRA-compatible worker mixins for CTU-Agent.

This module provides mixin classes that add LoRA-compatible weight broadcasting methods
to SkyRL workers. These methods handle parameter name mapping from LoRA's 'base_model.'
prefix to the original parameter names expected by VLLM inference engines.
"""

import asyncio
import torch
import torch.distributed
from loguru import logger


class LoRAWorkerMixin:
    """
    Mixin class that adds LoRA-compatible weight broadcasting methods.
    
    This mixin should be added to worker classes that need to sync LoRA model weights
    to VLLM inference engines. It provides methods that strip the 'base_model.' prefix
    from parameter names when broadcasting to inference engines.
    """
    
    def _map_lora_parameter_name(self, param_name: str) -> str:
        """
        Map LoRA parameter name to VLLM-compatible name.
        
        LoRA/PEFT wraps models and adds 'base_model.' prefix to parameters,
        but VLLM expects the original parameter names.
        
        Args:
            param_name: Parameter name from LoRA model
            
        Returns:
            str: VLLM-compatible parameter name
        """
        if param_name.startswith("base_model."):
            return param_name[len("base_model."):]
        return param_name
    
    async def broadcast_to_inference_engines_lora(self, inference_engine_client):
        """
        Broadcast model weights to inference engines with LoRA parameter name mapping.
        
        This method is similar to the standard broadcast_to_inference_engines but maps
        LoRA parameter names to be compatible with VLLM inference engines.
        
        Args:
            inference_engine_client: Client for communicating with inference engines
        """
        # Implementation depends on the specific worker type (FSDP or DeepSpeed)
        if hasattr(self, '_broadcast_lora_fsdp'):
            await self._broadcast_lora_fsdp(inference_engine_client)
        elif hasattr(self, '_broadcast_lora_deepspeed'):
            await self._broadcast_lora_deepspeed(inference_engine_client)
        else:
            raise NotImplementedError(
                "LoRA broadcasting not implemented for this worker type. "
                "Worker must implement either _broadcast_lora_fsdp or _broadcast_lora_deepspeed."
            )


class LoRAFSDPWorkerMixin(LoRAWorkerMixin):
    """LoRA-compatible mixin for FSDP workers."""
    
    async def _broadcast_lora_fsdp(self, inference_engine_client):
        """FSDP-specific LoRA weight broadcasting."""
        from torch.distributed.fsdp import StateDictType, ShardedStateDictConfig, FSDP
        
        logger.info("Broadcasting FSDP model weights to inference engines with LoRA parameter mapping")
        
        use_prefix_cache = self.cfg.generator.enable_prefix_caching
        generator_dtype = self._get_generator_dtype()
        cache_reset_task = None
        
        if use_prefix_cache and torch.distributed.get_rank() == 0:
            cache_reset_task = inference_engine_client.reset_prefix_cache()

        torch.cuda.empty_cache()
        
        # Get model state dict
        if hasattr(self.model.model, '_is_root') and self.model.model._is_root:
            FSDP.set_state_dict_type(
                self.model.model,
                state_dict_type=StateDictType.SHARDED_STATE_DICT,
                state_dict_config=ShardedStateDictConfig(),
            )
        params = self.model.model.state_dict()

        for name, param in params.items():
            # Map LoRA parameter name for VLLM compatibility
            vllm_name = self._map_lora_parameter_name(name)
            
            if not self.use_cuda_ipc:
                if torch.distributed.get_rank() == 0:
                    shape = param.shape
                    update_weight_task = asyncio.create_task(
                        inference_engine_client.update_named_weight(
                            {
                                "name": vllm_name,  # Use mapped name
                                "dtype": self.cfg.generator.model_dtype,
                                "shape": shape,
                            }
                        )
                    )

                def gather_and_broadcast(param):
                    if torch.distributed.get_rank() == 0:
                        param = param.to(generator_dtype)
                        torch.distributed.broadcast(param.data, 0, group=self._model_update_group)

                await asyncio.to_thread(gather_and_broadcast, param)
                if torch.distributed.get_rank() == 0:
                    await update_weight_task
            else:
                # CUDA IPC implementation with LoRA mapping
                await self._broadcast_cuda_ipc_lora(inference_engine_client, name, param, vllm_name, generator_dtype)

        if cache_reset_task is not None:
            await cache_reset_task
        torch.cuda.empty_cache()
        torch.distributed.barrier()
        
    def _get_generator_dtype(self):
        """Get generator dtype from config."""
        from skyrl_train.utils.utils import str_to_torch_dtype
        return str_to_torch_dtype(self.cfg.generator.model_dtype)
    
    async def _broadcast_cuda_ipc_lora(self, inference_engine_client, name, param, vllm_name, generator_dtype):
        """Handle CUDA IPC broadcasting with LoRA parameter mapping."""
        from torch.multiprocessing.reductions import reduce_tensor
        from skyrl_train.utils import get_physical_gpu_id
        
        weight = param.data.clone()
        weight = weight.to(generator_dtype)
        ipc_handle = reduce_tensor(weight)

        ipc_handle = {get_physical_gpu_id(): ipc_handle}
        ipc_handle_list = [None] * torch.distributed.get_world_size()
        torch.distributed.all_gather_object(ipc_handle_list, ipc_handle)

        if torch.distributed.get_rank() == 0:
            ipc_handles = {}
            for d in ipc_handle_list:
                ipc_handles.update(d)

            shape = param.shape
            await asyncio.create_task(
                inference_engine_client.update_named_weight(
                    {
                        "name": vllm_name,  # Use mapped name
                        "dtype": self.cfg.generator.model_dtype,
                        "shape": shape,
                        "extras": {
                            "ipc_handles": ipc_handles,
                        },
                    }
                )
            )

        torch.distributed.barrier()
        torch.cuda.synchronize()


class LoRADeepSpeedWorkerMixin(LoRAWorkerMixin):
    """LoRA-compatible mixin for DeepSpeed workers."""
    
    async def _broadcast_lora_deepspeed(self, inference_engine_client):
        """DeepSpeed-specific LoRA weight broadcasting."""
        import deepspeed
        from skyrl_train.utils.utils import str_to_torch_dtype
        from skyrl_train.utils import get_physical_gpu_id
        
        logger.info("Broadcasting DeepSpeed model weights to inference engines with LoRA parameter mapping")
        
        use_prefix_cache = self.cfg.generator.enable_prefix_caching
        generator_dtype = str_to_torch_dtype(self.cfg.generator.model_dtype)
        cache_reset_task = None
        
        if use_prefix_cache and torch.distributed.get_rank() == 0:
            cache_reset_task = inference_engine_client.reset_prefix_cache()

        torch.cuda.empty_cache()
        model = self.model.model.module
        
        for name, param in model.named_parameters():
            # Map LoRA parameter name for VLLM compatibility  
            vllm_name = self._map_lora_parameter_name(name)
            
            if not self.use_cuda_ipc:
                if torch.distributed.get_rank() == 0:
                    shape = param.shape if self.zero_stage != 3 else param.ds_shape
                    update_weight_task = asyncio.create_task(
                        inference_engine_client.update_named_weight(
                            {
                                "name": vllm_name,  # Use mapped name
                                "dtype": self.cfg.generator.model_dtype,
                                "shape": shape,
                            }
                        )
                    )

                def gather_and_broadcast(param):
                    with deepspeed.zero.GatheredParameters([param], enabled=self.zero_stage == 3):
                        if torch.distributed.get_rank() == 0:
                            param = param.to(generator_dtype)
                            torch.distributed.broadcast(param.data, 0, group=self._model_update_group)

                await asyncio.to_thread(gather_and_broadcast, param)
                if torch.distributed.get_rank() == 0:
                    await update_weight_task
            else:
                # CUDA IPC implementation with LoRA mapping
                await self._broadcast_cuda_ipc_deepspeed_lora(
                    inference_engine_client, name, param, vllm_name, generator_dtype
                )

        if cache_reset_task is not None:
            await cache_reset_task
        torch.cuda.empty_cache()
        torch.distributed.barrier()
    
    async def _broadcast_cuda_ipc_deepspeed_lora(self, inference_engine_client, name, param, vllm_name, generator_dtype):
        """Handle DeepSpeed CUDA IPC broadcasting with LoRA parameter mapping."""
        import deepspeed
        from torch.multiprocessing.reductions import reduce_tensor  
        from skyrl_train.utils import get_physical_gpu_id
        
        with deepspeed.zero.GatheredParameters([param], enabled=self.zero_stage == 3):
            weight = param.data.clone()
            weight = weight.to(generator_dtype)
            ipc_handle = reduce_tensor(weight)

            ipc_handle = {get_physical_gpu_id(): ipc_handle}
            ipc_handle_list = [None] * torch.distributed.get_world_size()
            torch.distributed.all_gather_object(ipc_handle_list, ipc_handle)

            if torch.distributed.get_rank() == 0:
                ipc_handles = {}
                for d in ipc_handle_list:
                    ipc_handles.update(d)

                shape = param.shape if self.zero_stage != 3 else param.ds_shape
                await asyncio.create_task(
                    inference_engine_client.update_named_weight(
                        {
                            "name": vllm_name,  # Use mapped name
                            "dtype": self.cfg.generator.model_dtype,
                            "shape": shape,
                            "extras": {
                                "ipc_handles": ipc_handles,
                            },
                        }
                    )
                )

            torch.distributed.barrier()
            torch.cuda.synchronize()