#!/usr/bin/env python3
"""
Test script to verify TAXONOMY_FEEDBACK configuration is working correctly.
"""

import os
import sys
from pathlib import Path

# Add project paths
sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(__file__).parent / "SkyRL_mod" / "skyrl-train"))
sys.path.append(str(Path(__file__).parent / "SkyRL_mod" / "skyrl-gym"))
sys.path.append(str(Path(__file__).parent / "tau_bench"))
sys.path.append(str(Path(__file__).parent / "tau_bench_env"))

def test_config():
    """Test that configuration loads correctly."""
    print("=" * 60)
    print("Testing TAXONOMY_FEEDBACK Configuration")
    print("=" * 60)
    
    # Test environment variables
    print("\n1. Environment Variables:")
    print(f"   TAXONOMY_FEEDBACK: {os.environ.get('TAXONOMY_FEEDBACK', 'not set')}")
    print(f"   TAXONOMY_ALPHA: {os.environ.get('TAXONOMY_ALPHA', 'not set')}")
    print(f"   OPENAI_API_KEY: {'set' if os.environ.get('OPENAI_API_KEY') else 'not set'}")
    
    # Test config loading
    print("\n2. Testing Config Loading:")
    try:
        from omegaconf import OmegaConf
        
        # Load tau_bench config
        config_path = Path(__file__).parent / "training" / "configs" / "skyrl_gym_config" / "tau_bench.yaml"
        if config_path.exists():
            config = OmegaConf.load(config_path)
            print(f"   Config loaded successfully from: {config_path}")
            print(f"   TAXONOMY_FEEDBACK in config: {config.tau_bench.TAXONOMY_FEEDBACK}")
            print(f"   TAXONOMY_ALPHA in config: {config.tau_bench.TAXONOMY_ALPHA}")
            print(f"   use_native_tool_calling in config: {config.tau_bench.use_native_tool_calling}")
        else:
            print(f"   ERROR: Config file not found at {config_path}")
            return False
    except Exception as e:
        print(f"   ERROR loading config: {e}")
        return False
    
    # Test LLM Judge integration
    print("\n3. Testing LLM Judge Integration:")
    try:
        from tau_bench_env.llm_judge_integration import create_judge_from_config
        
        # Create mock config
        mock_config = {
            'TAXONOMY_FEEDBACK': os.environ.get('TAXONOMY_FEEDBACK', 'false').lower() == 'true',
            'TAXONOMY_ALPHA': float(os.environ.get('TAXONOMY_ALPHA', '1.0'))
        }
        
        judge = create_judge_from_config(mock_config)
        print(f"   Judge created successfully")
        print(f"   Judge enabled: {judge.enabled}")
        print(f"   Judge alpha: {judge.alpha}")
        
        if judge.enabled and not os.environ.get('OPENAI_API_KEY'):
            print("   WARNING: Judge is enabled but OPENAI_API_KEY is not set!")
            
    except Exception as e:
        print(f"   ERROR creating judge: {e}")
        return False
    
    # Test wandb project naming
    print("\n4. Testing WandB Project Naming:")
    try:
        # Simulate tracking initialization
        project_name = "tau_bench_rl"
        
        # Check if taxonomy feedback would modify project name
        taxonomy_enabled = os.environ.get('TAXONOMY_FEEDBACK', 'false').lower() == 'true'
        if taxonomy_enabled:
            modified_name = f"{project_name}_with_taxonomy_feedback"
            print(f"   Original project: {project_name}")
            print(f"   Modified project: {modified_name}")
        else:
            print(f"   Project name: {project_name} (no modification)")
            
    except Exception as e:
        print(f"   ERROR: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    # Test with default values
    print("\nTest 1: Default values (taxonomy disabled)")
    test_config()
    
    # Test with taxonomy enabled
    print("\n\nTest 2: With taxonomy feedback enabled")
    os.environ['TAXONOMY_FEEDBACK'] = 'true'
    os.environ['TAXONOMY_ALPHA'] = '0.5'
    test_config()
    
    print("\n\nTesting complete!")