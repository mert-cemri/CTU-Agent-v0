# Copyright Sierra

import os
import sys

# Set default training mode early (before any imports that might create environments)
os.environ.setdefault("SKYRL_MODE", "train")

import ray
import hydra
from omegaconf import DictConfig

# Add the project root to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyrl_gym.envs.registration import register
from skyrl_train.entrypoints.main_base import BasePPOExp
from skyrl_train.utils.utils import validate_cfg
from skyrl_train.utils.utils import initialize_ray

# Get the config directory (relative to this file)
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs")


@ray.remote(num_cpus=1)
def skyrl_entrypoint(cfg: DictConfig):
    """
    Ray entrypoint for tau_bench training.
    
    This function runs on a Ray worker and is responsible for:
    1. Setting up the module path
    2. Registering the tau_bench environment
    3. Running the training loop
    """
    # Add the project root to the path for imports (needed for Ray workers)
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.append(project_root)
    
    # Register the tau_bench environment
    # This needs to be done inside the entrypoint task
    register(
        id="tau_bench",
        entry_point="tau_bench_env.env:TauBenchEnv",
    )
    
    # Run the training experiment
    exp = BasePPOExp(cfg)
    exp.run()


@hydra.main(config_path=config_dir, config_name="tau_bench_config", version_base=None)
def main(cfg: DictConfig) -> None:
    """Main training function."""
    # Validate the configuration
    validate_cfg(cfg)
    
    # Ensure OpenAI API key is available
    import os
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY environment variable is required for tau_bench user simulation")
    
    # Initialize Ray cluster (will include OpenAI API key in runtime env)
    initialize_ray(cfg)
    
    # Run the training entrypoint
    ray.get(skyrl_entrypoint.remote(cfg))


if __name__ == "__main__":
    main() 