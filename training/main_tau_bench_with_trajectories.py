# Copyright Sierra

import os
import sys
import ray
import json
import hydra
from pathlib import Path
from datetime import datetime
from omegaconf import DictConfig, OmegaConf
from typing import Dict, List, Any

# Add the project root to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyrl_gym.envs.registration import register
from skyrl_train.entrypoints.main_base import BasePPOExp
from skyrl_train.utils.utils import validate_cfg
from skyrl_train.utils.utils import initialize_ray

# Get the config directory (relative to this file)
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs")


class TauBenchPPOExpWithTrajectories(BasePPOExp):
    """Extended PPO experiment that logs trajectories for test sets."""
    
    def __init__(self, cfg: DictConfig):
        super().__init__(cfg)
        self.trajectory_save_path = None
        self.save_test_trajectories = False
        
        # Check if trajectory saving is enabled
        if hasattr(cfg.trainer, 'save_test_trajectories'):
            self.save_test_trajectories = cfg.trainer.save_test_trajectories
        
        if hasattr(cfg.trainer, 'trajectory_save_path'):
            self.trajectory_save_path = Path(cfg.trainer.trajectory_save_path)
            self.trajectory_save_path.mkdir(parents=True, exist_ok=True)
            print(f"Trajectory logging enabled. Saving to: {self.trajectory_save_path}")
    
    def save_trajectories_to_file(self, trajectories: List[Dict], domain: str, eval_step: int):
        """Save trajectories to a JSON file with proper indexing."""
        if not self.trajectory_save_path or not self.save_test_trajectories:
            return
        
        # Create filename with eval step and domain
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"test_{domain}_trajectories_eval{eval_step:04d}_{timestamp}.json"
        filepath = self.trajectory_save_path / filename
        
        # Prepare trajectory data with metadata
        trajectory_data = {
            "metadata": {
                "domain": domain,
                "eval_step": eval_step,
                "global_step": self.trainer.global_step if hasattr(self, 'trainer') else 0,
                "epoch": self.trainer.epoch if hasattr(self, 'trainer') else 0,
                "timestamp": timestamp,
                "model": str(self.cfg.trainer.policy.model.path),
                "run_name": self.cfg.trainer.run_name,
                "num_trajectories": len(trajectories)
            },
            "trajectories": trajectories
        }
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(trajectory_data, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(trajectories)} {domain} trajectories to: {filepath}")
    
    async def eval(self) -> Dict[str, float]:
        """Override eval to capture and save test trajectories."""
        # Call parent eval
        eval_metrics = await super().eval()
        
        # If we have test datasets and trajectory saving is enabled
        if self.save_test_trajectories and hasattr(self.trainer, 'test_datasets'):
            eval_step = self.trainer.global_step // self.cfg.trainer.eval_interval
            
            # Process test datasets and save trajectories
            for domain, dataset in self.trainer.test_datasets.items():
                if dataset is not None:
                    # Get the trajectories from the last evaluation
                    # This requires accessing the generator output from evaluation
                    if hasattr(self, '_last_test_trajectories'):
                        trajectories = self._last_test_trajectories.get(domain, [])
                        if trajectories:
                            self.save_trajectories_to_file(trajectories, domain, eval_step)
        
        return eval_metrics
    
    async def generate_and_save_trajectories(self, dataset, domain: str):
        """Generate trajectories and save them."""
        # This would need to be integrated with the actual generation process
        # For now, this is a placeholder showing the structure
        pass


@ray.remote(num_cpus=1)
def skyrl_entrypoint(cfg: DictConfig):
    """
    Ray entrypoint for tau_bench training with trajectory logging.
    
    This function runs on a Ray worker and is responsible for:
    1. Setting up the module path
    2. Registering the tau_bench environment
    3. Running the training loop with trajectory logging
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
    
    # Run the training experiment with trajectory logging
    exp = TauBenchPPOExpWithTrajectories(cfg)
    exp.run()


@hydra.main(config_path=config_dir, config_name="tau_bench_config", version_base=None)
def main(cfg: DictConfig) -> None:
    """Main training function with trajectory logging support."""
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