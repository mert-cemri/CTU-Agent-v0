#!/usr/bin/env python3
"""
Debug script to check what arguments are being passed to Hydra.
This will help identify where the 'source' argument is coming from.
"""

import sys
import os

# Add the project root to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("=== DEBUGGING HYDRA ARGUMENTS ===")
print(f"sys.argv: {sys.argv}")
print(f"len(sys.argv): {len(sys.argv)}")

for i, arg in enumerate(sys.argv):
    print(f"  [{i}]: '{arg}'")
    if arg == "source":
        print(f"    ^^^ FOUND STANDALONE 'source' AT INDEX {i}")
    if "source" in arg and "=" not in arg:
        print(f"    ^^^ FOUND 'source' WITHOUT EQUALS: '{arg}'")

print("=== END DEBUGGING ===")

# Try to run a minimal Hydra example to see what happens
try:
    import hydra
    from omegaconf import DictConfig
    
    config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "training", "configs")
    
    @hydra.main(config_path=config_dir, config_name="tau_bench_config", version_base=None)
    def test_main(cfg: DictConfig) -> None:
        print("Hydra loaded successfully!")
        print(f"Config keys: {list(cfg.keys())}")
    
    test_main()
    
except Exception as e:
    print(f"Error during Hydra parsing: {e}")
    print(f"Error type: {type(e)}")