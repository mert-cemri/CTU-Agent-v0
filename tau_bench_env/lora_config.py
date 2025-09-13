"""
LoRA configuration utilities for CTU-Agent.

This module provides utilities to determine when LoRA is enabled and configure
the appropriate workers and weights managers based on the training configuration.
"""

from typing import Optional, Tuple
from omegaconf import DictConfig
from loguru import logger


def is_lora_enabled(config: DictConfig) -> bool:
    """
    Check if LoRA is enabled in the training configuration.
    
    Args:
        config: Training configuration
        
    Returns:
        bool: True if LoRA is enabled (lora_rank > 0)
    """
    lora_rank = getattr(config.trainer.policy.model, 'lora_rank', 0)
    return lora_rank > 0


def get_lora_config(config: DictConfig) -> Tuple[int, int, float]:
    """
    Extract LoRA configuration parameters from the training config.
    
    Args:
        config: Training configuration
        
    Returns:
        Tuple[int, int, float]: (lora_rank, lora_alpha, lora_dropout)
    """
    model_config = config.trainer.policy.model
    lora_rank = getattr(model_config, 'lora_rank', 0)
    lora_alpha = getattr(model_config, 'lora_alpha', 16)
    lora_dropout = getattr(model_config, 'lora_dropout', 0.0)
    
    return lora_rank, lora_alpha, lora_dropout


def log_lora_status(config: DictConfig) -> None:
    """
    Log the current LoRA configuration status.
    
    Args:
        config: Training configuration
    """
    if is_lora_enabled(config):
        lora_rank, lora_alpha, lora_dropout = get_lora_config(config)
        logger.info(f"LoRA enabled with rank={lora_rank}, alpha={lora_alpha}, dropout={lora_dropout}")
        logger.info("Using LoRA-compatible workers and weights manager")
    else:
        logger.info("LoRA disabled - using standard workers and weights manager")


def should_use_lora_workers(config: DictConfig) -> bool:
    """
    Determine if LoRA-compatible workers should be used.
    
    Args:
        config: Training configuration
        
    Returns:
        bool: True if LoRA workers should be used
    """
    return is_lora_enabled(config) and config.trainer.strategy in ('fsdp', 'fsdp2', 'deepspeed')


def get_worker_strategy(config: DictConfig) -> str:
    """
    Get the training strategy from configuration.
    
    Args:
        config: Training configuration
        
    Returns:
        str: Training strategy ('fsdp', 'fsdp2', or 'deepspeed')
    """
    return config.trainer.strategy


def validate_lora_config(config: DictConfig) -> None:
    """
    Validate LoRA configuration parameters.
    
    Args:
        config: Training configuration
        
    Raises:
        ValueError: If LoRA configuration is invalid
    """
    if not is_lora_enabled(config):
        return
        
    lora_rank, lora_alpha, lora_dropout = get_lora_config(config)
    
    if lora_rank <= 0:
        raise ValueError(f"LoRA rank must be positive, got {lora_rank}")
    
    if lora_alpha <= 0:
        raise ValueError(f"LoRA alpha must be positive, got {lora_alpha}")
        
    if not 0 <= lora_dropout <= 1:
        raise ValueError(f"LoRA dropout must be between 0 and 1, got {lora_dropout}")
        
    strategy = get_worker_strategy(config)
    if strategy not in ('fsdp', 'fsdp2', 'deepspeed'):
        raise ValueError(f"LoRA not supported for strategy '{strategy}'. Must be 'fsdp', 'fsdp2', or 'deepspeed'.")
    
    logger.info("LoRA configuration validation passed")


class LoRAConfig:
    """
    LoRA configuration container.
    
    This class encapsulates LoRA configuration parameters and provides
    convenient access methods for the training pipeline.
    """
    
    def __init__(self, config: DictConfig):
        """
        Initialize LoRA configuration.
        
        Args:
            config: Training configuration
        """
        self.config = config
        self.enabled = is_lora_enabled(config)
        
        if self.enabled:
            self.rank, self.alpha, self.dropout = get_lora_config(config)
            self.strategy = get_worker_strategy(config)
        else:
            self.rank = 0
            self.alpha = 16
            self.dropout = 0.0
            self.strategy = get_worker_strategy(config)
    
    def __repr__(self) -> str:
        if self.enabled:
            return f"LoRAConfig(enabled=True, rank={self.rank}, alpha={self.alpha}, dropout={self.dropout}, strategy='{self.strategy}')"
        else:
            return f"LoRAConfig(enabled=False, strategy='{self.strategy}')"
    
    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            'enabled': self.enabled,
            'rank': self.rank,
            'alpha': self.alpha,
            'dropout': self.dropout,
            'strategy': self.strategy,
        }