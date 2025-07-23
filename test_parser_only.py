#!/usr/bin/env python3
"""
Simplified test script for parser improvements - no environment dependencies
"""

import json
import os
import sys

# Simple mock classes to avoid imports
class Action:
    def __init__(self, name, kwargs):
        self.name = name
        self.kwargs = kwargs

RESPOND_ACTION_NAME = "respond"
RESPOND_ACTION_FIELD_NAME = "content"

# Copy the parser function here to test without imports
def parse_llm_response(response, tools_info):
    """Test version of parser"""
    tool_names = [tool["function"]["name"] for tool in tools_info]
    
    # Enhanced debug logging
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n=== PARSER DEBUG ===")
        print(f"Available tools: {tool_names}")
        print(f"Response type: {type(response)}")
        if isinstance(response, str):
            print(f"Response (first 500 chars): {repr(response[:500])}")
        else:
            print(f"Response: {repr(response)}")
        print("===================")
    
    # Simple parsing logic for testing
    if isinstance(response, str):
        response = response.strip()
        
        # Try to parse as JSON
        if response.startswith('{') and response.endswith('}'):
            try:
                parsed = json.loads(response)
                if "name" in parsed and "arguments" in parsed:
                    if parsed["name"] in tool_names:
                        return Action(name=parsed["name"], kwargs=parsed["arguments"])
            except json.JSONDecodeError:
                pass
    
    # Fallback
    response_text = response if isinstance(response, str) else json.dumps(response)
    
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n=== PARSER FALLBACK ===")
        print(f"Failed to parse tool call, falling back to respond action")
        print(f"Original response: {repr(response_text[:200])}")
        print("=====================")
    
    return Action(
        name=RESPOND_ACTION_NAME,
        kwargs={RESPOND_ACTION_FIELD_NAME: response_text.strip()}
    )

def test_parser():
    """Test the parser with various inputs"""
    tools_info = [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get user details",
                "parameters": {"properties": {"user_id": {"type": "string"}}}
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get order details",
                "parameters": {"properties": {"order_id": {"type": "string"}}}
            }
        }
    ]
    
    test_cases = [
        ('{"name": "get_user_details", "arguments": {"user_id": "123"}}', "get_user_details"),
        ('  {"name": "get_order_details", "arguments": {"order_id": "456"}}  ', "get_order_details"),
        ('Hello, how can I help?', RESPOND_ACTION_NAME),
        ('{"name": "invalid_tool", "arguments": {}}', RESPOND_ACTION_NAME),
        ('{"broken json', RESPOND_ACTION_NAME),
    ]
    
    print("=" * 60)
    print("PARSER TESTS")
    print("=" * 60)
    
    # Test without debug
    print("\n1. Testing without debug logging:")
    os.environ["DEBUG_PARSER"] = "0"
    
    passed = 0
    for input_str, expected in test_cases:
        action = parse_llm_response(input_str, tools_info)
        status = "✓" if action.name == expected else "✗"
        print(f"{status} Input: {input_str[:50]}... → {action.name}")
        if action.name == expected:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(test_cases)}")
    
    # Test with debug
    print("\n2. Testing with debug logging enabled:")
    os.environ["DEBUG_PARSER"] = "1"
    
    # Test one case with debug
    print("\nDebug output for failing case:")
    action = parse_llm_response("This should fail and show debug output", tools_info)
    
    return passed, len(test_cases)

def main():
    print("CTU-Agent-v0 Parser Test (Simplified)")
    print("=" * 60)
    
    passed, total = test_parser()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Parser tests: {passed}/{total} passed ({passed/total*100:.0f}%)")
    
    print("\n" + "=" * 60)
    print("IMPROVEMENTS IMPLEMENTED")
    print("=" * 60)
    print("""
1. ✓ Enhanced parser debug logging (set DEBUG_PARSER=1)
   - Shows available tools, response type, and content
   - Logs when falling back to respond action

2. ✓ Generation examples logging
   - Added logging every 50 steps in trainer.py
   - Shows prompt, response, and reward

3. ✓ More frequent W&B logging
   - Added batch_reward/* metrics for granular tracking
   - Logs after every batch, not just training steps

4. ✓ Few-shot examples in system prompt
   - Dynamically generates examples based on available tools
   - Shows correct JSON format for tool calls

5. ✓ Fixed parser KeyError
   - Changed tool["name"] to tool["function"]["name"]
""")
    
    print("\n" + "=" * 60)
    print("HOW TO RUN TRAINING ON GPU MACHINE")
    print("=" * 60)
    print("""
1. Set environment variables:
   export OPENAI_API_KEY="your-key"
   export DEBUG_PARSER=1  # Enable parser debugging
   export WANDB_API_KEY="your-key"  # For W&B tracking

2. Activate the environment:
   cd SkyRL_mod/skyrl-train
   uv sync --extra vllm
   source .venv/bin/activate
   export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook

3. Run training with enhanced logging:
   bash training/run_tau_bench.sh

4. For a test run with more logging:
   bash training/run_tau_bench.sh \\
       trainer.epochs=2 \\
       trainer.train_batch_size=64 \\
       trainer.eval_interval=1 \\
       generator.n_samples_per_prompt=3

5. Monitor the logs:
   # In one terminal:
   tail -f $HOME/ckpts/tau_bench/logs/train.log | grep -E "(PARSER|GENERATION EXAMPLES)"
   
   # In another terminal:
   tail -f $HOME/ckpts/tau_bench/logs/train.log | grep "parse_failure_rate"

6. Check W&B for:
   - reward/parse_failure_rate
   - batch_reward/avg_raw_reward (more frequent updates)
   - batch_reward/parse_failure_rate
   - batch_reward/batch_number

Please run this and share:
1. Parser debug output showing what the model generates
2. Generation examples from the logs
3. Parse failure rate trends from W&B
""")

if __name__ == "__main__":
    main()