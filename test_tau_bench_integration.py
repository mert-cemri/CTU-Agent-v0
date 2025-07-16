#!/usr/bin/env python3
"""
Test script for tau_bench integration with SkyRL.
This script tests the core components without running full training.
"""

import os
import sys
import json
import tempfile
from pathlib import Path
from omegaconf import DictConfig

# Add project root to path
sys.path.append(str(Path(__file__).parent))

def test_data_conversion():
    """Test the data conversion functionality."""
    print("Testing data conversion...")
    
    # Create sample tau_bench data
    sample_data = {
        "tasks": [
            {
                "annotator": "test_annotator",
                "user_id": "test_user",
                "instruction": "I need to cancel my flight booking",
                "actions": [
                    {"name": "get_user_details", "kwargs": {"user_id": "test_user"}},
                    {"name": "cancel_reservation", "kwargs": {"reservation_id": "ABC123"}}
                ],
                "domain": "airline",
                "complexity": 2,
                "generated_at": "2024-01-01"
            },
            {
                "annotator": "test_annotator",
                "user_id": "test_user_2",
                "instruction": "I want to return an item I bought",
                "actions": [
                    {"name": "get_order_details", "kwargs": {"order_id": "ORDER123"}},
                    {"name": "return_delivered_order_items", "kwargs": {"order_id": "ORDER123"}}
                ],
                "domain": "retail",
                "complexity": 1,
                "generated_at": "2024-01-01"
            }
        ]
    }
    
    # Test data conversion
    try:
        from data_prep.convert_tau_data import convert_task_to_skyrl_format, filter_and_validate_tasks
        
        # Test task validation
        valid_tasks = filter_and_validate_tasks(sample_data["tasks"])
        print(f"✓ Task validation passed: {len(valid_tasks)} valid tasks")
        
        # Test task conversion
        for task in valid_tasks:
            skyrl_task = convert_task_to_skyrl_format(task)
            
            # Verify required fields
            assert "prompt" in skyrl_task
            assert "env_class" in skyrl_task
            assert "reward_spec" in skyrl_task
            assert "extra_info" in skyrl_task
            assert skyrl_task["env_class"] == "tau_bench"
            assert len(skyrl_task["prompt"]) == 2
            assert skyrl_task["prompt"][0]["role"] == "system"
            assert skyrl_task["prompt"][1]["role"] == "user"
            
        print("✓ Data conversion test passed")
        
    except Exception as e:
        print(f"✗ Data conversion test failed: {e}")
        return False
    
    return True


def test_environment_creation():
    """Test the environment creation functionality."""
    print("\nTesting environment creation...")
    
    try:
        from tau_bench_env.env import TauBenchEnv
        from omegaconf import DictConfig
        
        # Test environment configuration
        env_config = DictConfig({
            "user_strategy": "llm",
            "user_model": "gpt-4o-mini",  # Use cheaper model for testing
            "user_provider": "openai",
            "max_turns": 5
        })
        
        extras = {
            "domain": "airline",
            "instruction": "I need to cancel my flight booking",
            "reward_spec": {
                "ground_truth": [
                    {"name": "get_user_details", "kwargs": {"user_id": "test_user"}},
                    {"name": "cancel_reservation", "kwargs": {"reservation_id": "ABC123"}}
                ]
            }
        }
        
        # Create environment (this might fail if API keys are not set)
        env = TauBenchEnv(env_config, extras)
        
        # Test basic properties
        assert env.domain == "airline"
        assert env.instruction == "I need to cancel my flight booking"
        assert len(env.ground_truth_actions) == 2
        assert env.max_turns == 5
        
        print("✓ Environment creation test passed")
        
        # Test initialization
        initial_prompt = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello"}
        ]
        
        # Note: This might fail without proper API keys
        print("  Note: Skipping init test (requires API keys)")
        
    except Exception as e:
        print(f"✗ Environment creation test failed: {e}")
        return False
    
    return True


def test_parser():
    """Test the LLM response parser."""
    print("\nTesting LLM response parser...")
    
    try:
        from tau_bench_env.parser import parse_llm_response
        
        # Sample tools info
        tools_info = [
            {
                "function": {
                    "name": "get_user_details",
                    "description": "Get user details",
                    "parameters": {"type": "object", "properties": {"user_id": {"type": "string"}}}
                }
            },
            {
                "function": {
                    "name": "cancel_reservation",
                    "description": "Cancel reservation",
                    "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string"}}}
                }
            }
        ]
        
        # Test JSON tool call parsing
        json_response = '{"name": "get_user_details", "arguments": {"user_id": "test123"}}'
        action = parse_llm_response(json_response, tools_info)
        assert action.name == "get_user_details"
        assert action.kwargs["user_id"] == "test123"
        
        # Test markdown JSON parsing
        markdown_response = '```json\n{"name": "cancel_reservation", "arguments": {"reservation_id": "ABC123"}}\n```'
        action = parse_llm_response(markdown_response, tools_info)
        assert action.name == "cancel_reservation"
        assert action.kwargs["reservation_id"] == "ABC123"
        
        # Test fallback to respond action
        natural_response = "I can help you with that. Let me check your details."
        action = parse_llm_response(natural_response, tools_info)
        assert action.name == "respond"
        assert "content" in action.kwargs
        
        print("✓ Parser test passed")
        
    except Exception as e:
        print(f"✗ Parser test failed: {e}")
        return False
    
    return True


def test_system_prompts():
    """Test the system prompt generation."""
    print("\nTesting system prompts...")
    
    try:
        from data_prep.prompts import get_domain_system_prompt, create_full_system_prompt, get_all_domains
        
        # Test domain availability
        domains = get_all_domains()
        expected_domains = ["airline", "healthcare", "telecom", "doordash", "retail"]
        
        for domain in expected_domains:
            assert domain in domains, f"Domain {domain} not found"
            
            # Test prompt generation
            prompt = get_domain_system_prompt(domain)
            assert isinstance(prompt, str)
            assert len(prompt) > 0
            
            # Test full prompt generation
            full_prompt = create_full_system_prompt(domain)
            assert isinstance(full_prompt, str)
            assert len(full_prompt) > len(prompt)
            assert "tool" in full_prompt.lower()
        
        print("✓ System prompts test passed")
        
    except Exception as e:
        print(f"✗ System prompts test failed: {e}")
        return False
    
    return True


def main():
    """Run all tests."""
    print("Running tau_bench integration tests...\n")
    
    tests = [
        test_system_prompts,
        test_parser,
        test_data_conversion,
        test_environment_creation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
            failed += 1
    
    print(f"\nTest Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! The tau_bench integration is working correctly.")
        print("\nNext steps:")
        print("1. Set up your API keys (OPENAI_API_KEY, WANDB_API_KEY)")
        print("2. Convert your training data:")
        print("   python -m data_prep.convert_tau_data --input_path tau_bench/data/novel_sft_dataset.json --output_dir $HOME/data/tau_bench")
        print("3. Run training:")
        print("   bash training/run_tau_bench.sh")
    else:
        print("❌ Some tests failed. Please fix the issues before proceeding.")
        sys.exit(1)


if __name__ == "__main__":
    main() 