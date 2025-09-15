#!/usr/bin/env python3
"""
Comprehensive test to verify parsing and other potential blockers during training.
This simulates the actual training pipeline more closely.
"""

import os
import sys
import json

# Enable all debugging
os.environ["DEBUG_HASH_COMPARISON"] = "1"
os.environ["DEBUG_PARSER"] = "1"

# Set OpenAI API key if available
if "OPENAI_API_KEY" in os.environ:
    import litellm
    litellm.api_key = os.environ.get("OPENAI_API_KEY")

# Add the project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tau_bench_env.env import TauBenchEnv
from tau_bench_env.parser import parse_llm_response
from tau_bench_env.simple_parser import parse_tool_calling_response

def test_parsing_with_actual_responses():
    """Test parsing with the actual malformed responses from the conversation."""
    
    print("="*80)
    print("COMPREHENSIVE PARSING AND ENVIRONMENT TEST")
    print("="*80)
    
    # Create environment config like in training
    env_config = {
        "use_native_tool_calling": True,  # This is what training uses
        "max_turns": 20
    }
    
    # Environment extras like in training
    extras = {
        "domain": "retail",
        "instruction": "You are Yusuf Rossi in 19122. You received your order #W2378156 and wish to exchange the mechanical keyboard for a similar one but with clicky switches and the smart thermostat for one compatible with Google Home instead of Apple HomeKit. If there is no keyboard that is clicky, RGB backlight, full size, you'd go for no backlight. You are detail-oriented and want to make sure everything is addressed in one go.",
        "reward_spec": json.dumps({
            "method": "action_grounding",
            "ground_truth": [
                {"name": "find_user_id_by_name_zip", "kwargs": {"first_name": "Yusuf", "last_name": "Rossi", "zip": "19122"}},
                {"name": "get_order_details", "kwargs": {"order_id": "#W2378156"}},
                {"name": "get_product_details", "kwargs": {"product_id": "1656367028"}},
                {"name": "get_product_details", "kwargs": {"product_id": "4896585277"}},
                {"name": "exchange_delivered_order_items", "kwargs": {"order_id": "#W2378156", "item_ids": ["1151293680", "4983901480"], "new_item_ids": ["7706410293", "7747408585"], "payment_method_id": "credit_card_9513926"}}
            ]
        })
    }
    
    # Create TauBenchEnv like in training
    env = TauBenchEnv(env_config, extras)
    
    print(f"Environment created successfully:")
    print(f"  Domain: {env.domain}")
    print(f"  Native tool calling: {env.use_native_tool_calling}")
    print(f"  Max turns: {env.max_turns}")
    print(f"  Tools available: {len(env.tools_info)}")
    
    # Test the actual agent responses from the problematic conversation
    agent_responses = [
        # Early in conversation - regular text
        "I'm unable to locate your order or account with the current information provided. To proceed, could you please share more details such as your full name, email address, or zip code? This will help me find your account and locate the correct order for the exchange.",
        
        # Tool calls that should parse correctly
        '{"tool_calls": [{"function": {"name": "find_user_id_by_name_zip", "arguments": "{\\"first_name\\": \\"Yusuf\\", \\"last_name\\": \\"Rossi\\", \\"zip\\": \\"19122\\"}"}}]}',
        
        '{"tool_calls": [{"function": {"name": "get_user_details", "arguments": "{\\"user_id\\": \\"yusuf_rossi_9620\\"}"}}]}',
        
        '{"tool_calls": [{"function": {"name": "get_order_details", "arguments": "{\\"order_id\\": \\"#W2378156\\"}"}}]}',
        
        '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\\"product_id\\": \\"1656367028\\"}"}}]}',
        
        '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\\"product_id\\": \\"4896585277\\"}"}}]}',
        
        # The critical exchange call
        '{"tool_calls": [{"function": {"name": "exchange_delivered_order_items", "arguments": "{\\"order_id\\": \\"#W2378156\\", \\"item_ids\\": [\\"1151293680\\", \\"4983901480\\"], \\"new_item_ids\\": [\\"7706410293\\", \\"7747408585\\"], \\"payment_method_id\\": \\"credit_card_9513926\\"}"}}]}',
        
        # Final response
        "The exchange for your order #W2378156 has been successfully requested! Here are the details..."
    ]
    
    # Initialize environment
    prompt, metadata = env.init([{"role": "user", "content": "I want to exchange items from my recent order."}])
    
    print(f"\nEnvironment initialized. Prompt has {len(prompt)} messages.")
    
    # Test each response
    for i, response in enumerate(agent_responses):
        print(f"\n{'='*60}")
        print(f"TESTING RESPONSE {i+1}")
        print(f"{'='*60}")
        print(f"Response: {response[:100]}...")
        
        try:
            if env.use_native_tool_calling:
                # This is what training actually uses
                parsed_response = json.loads(response) if response.startswith('{') else response
                parsed_action = parse_tool_calling_response(parsed_response, source="agent")
            else:
                # Fallback parser
                parsed_action = parse_llm_response(response, env.tools_info, source="agent")
            
            print(f"✅ PARSING SUCCESS:")
            print(f"   Action: {parsed_action.name}")
            if hasattr(parsed_action, 'kwargs') and parsed_action.kwargs:
                print(f"   Kwargs: {parsed_action.kwargs}")
            
            # Execute the action if it's not a respond action
            if parsed_action.name != "respond":
                print(f"   Executing action...")
                result = env.step(parsed_action)
                print(f"   Result: {result.observation[:100]}...")
                print(f"   Done: {result.done}")
                print(f"   Reward: {result.reward}")
                
                if result.done:
                    print(f"\n🏁 CONVERSATION COMPLETED!")
                    print(f"   Final reward: {result.reward}")
                    break
            
        except Exception as e:
            print(f"❌ PARSING/EXECUTION ERROR:")
            print(f"   Error: {e}")
            print(f"   Type: {type(e).__name__}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*80}")
    print("TEST COMPLETED")
    print(f"{'='*80}")

if __name__ == "__main__":
    test_parsing_with_actual_responses()