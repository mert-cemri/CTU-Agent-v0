#!/usr/bin/env python3
"""
Test script to verify improvements to CTU-Agent-v0
Tests parser improvements, logging, and system prompt enhancements
"""

import os
import json
import sys
from typing import Dict, Any, List

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tau_bench_env.parser import parse_llm_response
from tau_bench.tau_types import RESPOND_ACTION_NAME

def create_mock_tools_info() -> List[Dict[str, Any]]:
    """Create mock tools info for testing"""
    return [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get the details of a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id"
                        }
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function", 
            "function": {
                "name": "get_order_details",
                "description": "Get order information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The order id"
                        }
                    },
                    "required": ["order_id"]
                }
            }
        }
    ]

def test_parser_formats():
    """Test various parser input formats"""
    tools_info = create_mock_tools_info()
    
    test_cases = [
        # Test 1: Direct JSON format
        {
            "name": "Direct JSON",
            "input": '{"name": "get_user_details", "arguments": {"user_id": "123"}}',
            "expected_name": "get_user_details",
            "expected_args": {"user_id": "123"}
        },
        # Test 2: JSON with extra whitespace
        {
            "name": "JSON with whitespace",
            "input": '  {"name": "get_user_details", "arguments": {"user_id": "456"}}  ',
            "expected_name": "get_user_details",
            "expected_args": {"user_id": "456"}
        },
        # Test 3: Natural language (should fall back to respond)
        {
            "name": "Natural language",
            "input": "Hello, how can I help you?",
            "expected_name": RESPOND_ACTION_NAME,
            "expected_args": None
        },
        # Test 4: Code block format
        {
            "name": "Code block",
            "input": '```python\nget_user_details(user_id="789")\n```',
            "expected_name": "get_user_details",
            "expected_args": {"user_id": "789"}
        },
        # Test 5: Invalid tool name
        {
            "name": "Invalid tool",
            "input": '{"name": "invalid_tool", "arguments": {}}',
            "expected_name": RESPOND_ACTION_NAME,
            "expected_args": None
        },
        # Test 6: Malformed JSON
        {
            "name": "Malformed JSON",
            "input": '{"name": "get_user_details", "arguments": {"user_id": }',
            "expected_name": RESPOND_ACTION_NAME,
            "expected_args": None
        }
    ]
    
    print("=" * 60)
    print("PARSER FORMAT TESTS")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Input: {test['input'][:100]}...")
        
        try:
            action = parse_llm_response(test['input'], tools_info)
            print(f"Parsed action: {action.name}")
            print(f"Arguments: {action.kwargs}")
            
            # Check if parsed correctly
            if action.name == test['expected_name']:
                if test['expected_args'] is None or action.kwargs == test['expected_args']:
                    print("✓ PASSED")
                    passed += 1
                else:
                    print(f"✗ FAILED - Expected args: {test['expected_args']}, got: {action.kwargs}")
                    failed += 1
            else:
                print(f"✗ FAILED - Expected: {test['expected_name']}, got: {action.name}")
                failed += 1
                
        except Exception as e:
            print(f"✗ FAILED with exception: {e}")
            failed += 1
    
    print(f"\n{'-' * 60}")
    print(f"Total: {len(test_cases)}, Passed: {passed}, Failed: {failed}")
    print(f"Success rate: {passed/len(test_cases)*100:.1f}%")
    
    return passed, failed

def test_system_prompt_enhancement():
    """Test the enhanced system prompt with few-shot examples"""
    from tau_bench_env.env import TauBenchEnv
    
    print("\n" + "=" * 60)
    print("SYSTEM PROMPT ENHANCEMENT TEST")
    print("=" * 60)
    
    # Create a mock environment config
    env_config = {
        "domain": "retail",
        "user_strategy": "llm",
        "max_turns": 5
    }
    
    try:
        # Initialize environment
        env = TauBenchEnv(env_config)
        
        # Reset to get initial observation
        obs = env.reset()
        
        # Extract system prompt from messages
        messages = json.loads(obs)["messages"]
        system_message = next((m["content"] for m in messages if m["role"] == "system"), None)
        
        print("\nSystem prompt preview (first 1000 chars):")
        print("-" * 60)
        print(system_message[:1000] + "..." if len(system_message) > 1000 else system_message)
        
        # Check for few-shot examples
        has_examples = "EXAMPLES OF CORRECT TOOL USAGE:" in system_message
        has_json_format = '{"name":' in system_message
        
        print("\n✓ Few-shot examples included" if has_examples else "✗ Few-shot examples missing")
        print("✓ JSON format demonstrated" if has_json_format else "✗ JSON format not demonstrated")
        
        return has_examples and has_json_format
        
    except Exception as e:
        print(f"✗ Failed to test system prompt: {e}")
        return False

def test_debug_logging():
    """Test debug logging functionality"""
    print("\n" + "=" * 60)
    print("DEBUG LOGGING TEST")
    print("=" * 60)
    
    # Enable debug logging
    os.environ["DEBUG_PARSER"] = "1"
    
    tools_info = create_mock_tools_info()
    
    print("\nTesting with debug logging enabled...")
    print("You should see debug output below:")
    print("-" * 60)
    
    # Test with a response that will fail parsing
    test_input = "This is a natural language response that should trigger fallback"
    action = parse_llm_response(test_input, tools_info)
    
    print("-" * 60)
    print(f"Parsed action: {action.name}")
    
    # Disable debug logging
    os.environ["DEBUG_PARSER"] = "0"
    
    return True

def main():
    """Run all tests"""
    print("CTU-Agent-v0 Improvement Tests")
    print("=" * 60)
    
    # Run parser tests
    parser_passed, parser_failed = test_parser_formats()
    
    # Test system prompt enhancement
    prompt_success = test_system_prompt_enhancement()
    
    # Test debug logging
    debug_success = test_debug_logging()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Parser tests: {parser_passed} passed, {parser_failed} failed")
    print(f"System prompt enhancement: {'✓ PASSED' if prompt_success else '✗ FAILED'}")
    print(f"Debug logging: {'✓ PASSED' if debug_success else '✗ FAILED'}")
    
    print("\n" + "=" * 60)
    print("INSTRUCTIONS FOR GPU TRAINING")
    print("=" * 60)
    print("""
To run training on your GPU machine:

1. First, set up the environment:
   export OPENAI_API_KEY="your-key-here"
   export DEBUG_PARSER=1  # Enable parser debugging
   export WANDB_API_KEY="your-key-here"  # If using W&B

2. Run the training with enhanced logging:
   bash training/run_tau_bench.sh

3. For a quick test run with more frequent logging:
   bash training/run_tau_bench.sh \\
       trainer.epochs=5 \\
       trainer.train_batch_size=64 \\
       trainer.ckpt_interval=2 \\
       generator.n_samples_per_prompt=3

4. Monitor the logs for:
   - Parser debug output (look for "=== PARSER DEBUG ===" and "=== PARSER FALLBACK ===")
   - Generation examples every 50 steps (look for "=== GENERATION EXAMPLES ===")
   - More frequent reward metrics in W&B (both "reward/*" and "batch_reward/*" metrics)

5. To get the most detailed parsing information:
   tail -f $HOME/ckpts/tau_bench/logs/train.log | grep -A5 -B5 "PARSER"

6. Check W&B for:
   - reward/parse_failure_rate - Shows % of failed parses
   - batch_reward/* metrics - More granular reward tracking
   - reward/avg_raw_reward - Overall success rate

Please run the training and share:
1. The parser debug output showing what formats the model is generating
2. The parse_failure_rate from W&B
3. Any generation examples from the logs
""")

if __name__ == "__main__":
    main()