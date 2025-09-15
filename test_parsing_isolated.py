#!/usr/bin/env python3
"""
Isolated test of parsing with the actual agent responses.
This focuses on potential parsing issues without requiring full environment.
"""

import os
import sys
import json

# Enable parser debugging
os.environ["DEBUG_PARSER"] = "1"

# Add the project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tau_bench_env.parser import parse_llm_response
from tau_bench_env.simple_parser import parse_tool_calling_response

def test_response_parsing():
    """Test parsing of the actual responses from the problematic conversation."""
    
    print("="*80)
    print("ISOLATED PARSING TEST")
    print("="*80)
    
    # Mock tools info (like what retail environment would have)
    tools_info = [
        {
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user ID by name and zip code",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "zip": {"type": "string"}
                    },
                    "required": ["first_name", "last_name", "zip"]
                }
            }
        },
        {
            "function": {
                "name": "get_user_details",
                "description": "Get user details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "function": {
                "name": "get_order_details",
                "description": "Get order details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "function": {
                "name": "get_product_details",
                "description": "Get product details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"}
                    },
                    "required": ["product_id"]
                }
            }
        },
        {
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange delivered order items",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}},
                        "payment_method_id": {"type": "string"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        },
        {
            "function": {
                "name": "think",
                "description": "Think about something",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {"type": "string"}
                    },
                    "required": ["thought"]
                }
            }
        }
    ]
    
    # The actual responses from the problematic conversation
    test_responses = [
        # 1. Regular conversational response
        {
            "response": "I'm unable to locate your order or account with the current information provided. To proceed, could you please share more details such as your full name, email address, or zip code? This will help me find your account and locate the correct order for the exchange.",
            "expected": "respond",
            "description": "Regular conversational response"
        },
        
        # 2. Tool call responses (these should parse correctly)
        {
            "response": '{"tool_calls": [{"function": {"name": "find_user_id_by_name_zip", "arguments": "{\\"first_name\\": \\"Yusuf\\", \\"last_name\\": \\"Rossi\\", \\"zip\\": \\"19122\\"}"}}]}',
            "expected": "find_user_id_by_name_zip",
            "description": "Find user by name and zip"
        },
        
        {
            "response": '{"tool_calls": [{"function": {"name": "get_user_details", "arguments": "{\\"user_id\\": \\"yusuf_rossi_9620\\"}"}}]}',
            "expected": "get_user_details", 
            "description": "Get user details"
        },
        
        {
            "response": '{"tool_calls": [{"function": {"name": "get_order_details", "arguments": "{\\"order_id\\": \\"#W2378156\\"}"}}]}',
            "expected": "get_order_details",
            "description": "Get order details"
        },
        
        {
            "response": '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\\"product_id\\": \\"1656367028\\"}"}}]}',
            "expected": "get_product_details",
            "description": "Get product details 1"
        },
        
        {
            "response": '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\\"product_id\\": \\"4896585277\\"}"}}]}',
            "expected": "get_product_details",
            "description": "Get product details 2"
        },
        
        # 3. Think tool calls
        {
            "response": '{"tool_calls": [{"function": {"name": "think", "arguments": "{\\"thought\\": \\"The user wants to exchange their mechanical keyboard (clicky, no backlight, full size) and smart thermostat (Google Assistant compatible) for new items. I need to verify the item IDs for these options and proceed with the exchange request.\\"}"}}]}',
            "expected": "think",
            "description": "Think tool call"
        },
        
        # 4. The critical exchange call
        {
            "response": '{"tool_calls": [{"function": {"name": "exchange_delivered_order_items", "arguments": "{\\"order_id\\": \\"#W2378156\\", \\"item_ids\\": [\\"1151293680\\", \\"4983901480\\"], \\"new_item_ids\\": [\\"7706410293\\", \\"7747408585\\"], \\"payment_method_id\\": \\"credit_card_9513926\\"}"}}]}',
            "expected": "exchange_delivered_order_items",
            "description": "Exchange order items (CRITICAL)"
        }
    ]
    
    print(f"Testing {len(test_responses)} responses with both parsers...")
    
    all_passed = True
    
    for i, test_case in enumerate(test_responses):
        print(f"\n{'='*60}")
        print(f"TEST {i+1}: {test_case['description']}")
        print(f"{'='*60}")
        print(f"Response: {test_case['response'][:100]}...")
        print(f"Expected action: {test_case['expected']}")
        
        # Test both parsers
        for parser_name, parser_func in [
            ("NATIVE (simple_parser)", parse_tool_calling_response),
            ("LEGACY (complex_parser)", lambda r, s: parse_llm_response(r, tools_info, s))
        ]:
            print(f"\n--- {parser_name} ---")
            try:
                if parser_name.startswith("NATIVE"):
                    # For native parser, need to parse JSON first if it's a string
                    if test_case['response'].startswith('{'):
                        parsed_response = json.loads(test_case['response'])
                        action = parser_func(parsed_response, "agent")
                    else:
                        action = parser_func(test_case['response'], "agent")
                else:
                    # Legacy parser handles strings directly
                    action = parser_func(test_case['response'], "agent")
                
                print(f"✅ SUCCESS: {action.name}")
                if hasattr(action, 'kwargs') and action.kwargs:
                    print(f"   kwargs: {action.kwargs}")
                
                # Check if it matches expected
                if action.name == test_case['expected']:
                    print(f"✅ EXPECTED ACTION MATCH")
                else:
                    print(f"⚠️  ACTION MISMATCH: got {action.name}, expected {test_case['expected']}")
                    if test_case['expected'] != "respond":  # Only flag as error if not conversational
                        all_passed = False
                
            except Exception as e:
                print(f"❌ PARSING FAILED: {e}")
                all_passed = False
                import traceback
                traceback.print_exc()
    
    print(f"\n{'='*80}")
    if all_passed:
        print("🎉 ALL PARSING TESTS PASSED!")
    else:
        print("⚠️  SOME PARSING TESTS FAILED - POTENTIAL BLOCKER IDENTIFIED")
    print(f"{'='*80}")
    
    return all_passed

if __name__ == "__main__":
    test_response_parsing()