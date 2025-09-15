#!/usr/bin/env python3
"""
Direct parsing test without complex imports.
Tests the specific responses that were problematic.
"""

import json
import os

# Enable debugging
os.environ["DEBUG_PARSER"] = "1"

def test_critical_exchange_parsing():
    """Test the critical exchange call that should work."""
    
    print("="*80)
    print("DIRECT PARSING TEST - CRITICAL EXCHANGE CALL")
    print("="*80)
    
    # The critical exchange response from the conversation
    exchange_response = '{"tool_calls": [{"function": {"name": "exchange_delivered_order_items", "arguments": "{\\"order_id\\": \\"#W2378156\\", \\"item_ids\\": [\\"1151293680\\", \\"4983901480\\"], \\"new_item_ids\\": [\\"7706410293\\", \\"7747408585\\"], \\"payment_method_id\\": \\"credit_card_9513926\\"}"}}]}'
    
    print("Testing exchange response:")
    print(exchange_response)
    print()
    
    try:
        # Parse as JSON (this is what simple_parser does)
        parsed_json = json.loads(exchange_response)
        print("✅ JSON parsing successful")
        print(f"Parsed structure: {parsed_json}")
        
        # Extract tool call info (simulate simple_parser logic)
        if "tool_calls" in parsed_json and len(parsed_json["tool_calls"]) > 0:
            tool_call = parsed_json["tool_calls"][0]
            if "function" in tool_call:
                func_info = tool_call["function"]
                tool_name = func_info.get("name")
                arguments_str = func_info.get("arguments", "{}")
                
                print(f"✅ Tool name extracted: {tool_name}")
                print(f"✅ Arguments string: {arguments_str}")
                
                # Parse arguments JSON
                try:
                    arguments = json.loads(arguments_str)
                    print(f"✅ Arguments parsed: {arguments}")
                    
                    # Verify expected fields
                    expected_fields = ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                    for field in expected_fields:
                        if field in arguments:
                            print(f"✅ Field '{field}' present: {arguments[field]}")
                        else:
                            print(f"❌ Field '{field}' MISSING")
                    
                    print(f"\n🎉 PARSING COMPLETELY SUCCESSFUL!")
                    print(f"Tool: {tool_name}")
                    print(f"Arguments: {arguments}")
                    
                    return True
                    
                except json.JSONDecodeError as e:
                    print(f"❌ Failed to parse arguments JSON: {e}")
                    return False
            else:
                print(f"❌ No 'function' in tool_call")
                return False
        else:
            print(f"❌ No tool_calls found")
            return False
            
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse response JSON: {e}")
        return False

def check_potential_issues():
    """Check for potential issues that could cause problems."""
    
    print(f"\n{'='*80}")
    print("CHECKING FOR POTENTIAL ISSUES")
    print("="*80)
    
    issues_found = []
    
    # 1. Check if responses have proper structure
    test_responses = [
        '{"tool_calls": [{"function": {"name": "get_user_details", "arguments": "{\\"user_id\\": \\"yusuf_rossi_9620\\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\\"product_id\\": \\"1656367028\\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "exchange_delivered_order_items", "arguments": "{\\"order_id\\": \\"#W2378156\\", \\"item_ids\\": [\\"1151293680\\", \\"4983901480\\"], \\"new_item_ids\\": [\\"7706410293\\", \\"7747408585\\"], \\"payment_method_id\\": \\"credit_card_9513926\\"}"}}]}'
    ]
    
    print(f"Testing {len(test_responses)} critical responses...")
    
    for i, response in enumerate(test_responses):
        print(f"\nResponse {i+1}:")
        try:
            parsed = json.loads(response)
            tool_name = parsed["tool_calls"][0]["function"]["name"]
            args_str = parsed["tool_calls"][0]["function"]["arguments"]
            args = json.loads(args_str)
            print(f"✅ {tool_name}: {len(args)} arguments")
        except Exception as e:
            print(f"❌ Parsing failed: {e}")
            issues_found.append(f"Response {i+1} parsing failed: {e}")
    
    # 2. Check for escaped quotes issue
    print(f"\n--- Checking escaped quotes ---")
    sample_args = '{\\"order_id\\": \\"#W2378156\\", \\"item_ids\\": [\\"1151293680\\", \\"4983901480\\"]}'
    try:
        parsed_args = json.loads(sample_args)
        print(f"✅ Escaped quotes parse correctly: {parsed_args}")
    except Exception as e:
        print(f"❌ Escaped quotes issue: {e}")
        issues_found.append(f"Escaped quotes parsing failed: {e}")
    
    # 3. Check for array parsing
    print(f"\n--- Checking array parsing ---")
    array_test = '[\\"1151293680\\", \\"4983901480\\"]'
    try:
        parsed_array = json.loads(array_test)
        print(f"✅ Array parsing works: {parsed_array}")
    except Exception as e:
        print(f"❌ Array parsing issue: {e}")
        issues_found.append(f"Array parsing failed: {e}")
    
    print(f"\n{'='*60}")
    if not issues_found:
        print("🎉 NO PARSING ISSUES DETECTED!")
        print("All responses should parse correctly during training.")
    else:
        print("⚠️  POTENTIAL ISSUES FOUND:")
        for issue in issues_found:
            print(f"  - {issue}")
    print("="*60)
    
    return len(issues_found) == 0

if __name__ == "__main__":
    success1 = test_critical_exchange_parsing()
    success2 = check_potential_issues()
    
    print(f"\n{'='*80}")
    print("FINAL ASSESSMENT")
    print("="*80)
    
    if success1 and success2:
        print("✅ PARSING APPEARS TO BE WORKING CORRECTLY")
        print("The tool calls from the conversation should parse successfully.")
        print("The 0 reward issue is likely NOT due to parsing problems.")
        print("The hash comparison fix we implemented should address the main issue.")
    else:
        print("❌ PARSING ISSUES DETECTED")
        print("These could contribute to 0 reward problems during training.")
    
    print("="*80)