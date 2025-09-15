#!/usr/bin/env python3
"""
Test the exact format of responses from the conversation you provided.
"""

import json

def test_exact_conversation_responses():
    """Test the exact responses from your conversation."""
    
    print("="*80)
    print("TESTING EXACT CONVERSATION RESPONSES")
    print("="*80)
    
    # These are the EXACT responses from your conversation
    responses_from_conversation = [
        '{"tool_calls": [{"function": {"name": "find_user_id_by_name_zip", "arguments": "{\"first_name\": \"Yusuf\", \"last_name\": \"Rossi\", \"zip\": \"19122\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "get_user_details", "arguments": "{\"user_id\": \"yusuf_rossi_9620\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "get_order_details", "arguments": "{\"order_id\": \"#W2378156\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\"product_id\": \"1656367028\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "get_product_details", "arguments": "{\"product_id\": \"4896585277\"}"}}]}',
        '{"tool_calls": [{"function": {"name": "exchange_delivered_order_items", "arguments": "{\"order_id\": \"#W2378156\", \"item_ids\": [\"1151293680\", \"4983901480\"], \"new_item_ids\": [\"7706410293\", \"7747408585\"], \"payment_method_id\": \"credit_card_9513926\"}"}}]}'
    ]
    
    print(f"Testing {len(responses_from_conversation)} responses from your actual conversation...\n")
    
    all_success = True
    
    for i, response in enumerate(responses_from_conversation):
        print(f"Response {i+1}:")
        print(f"Raw: {response}")
        
        try:
            # Parse outer JSON
            outer_json = json.loads(response)
            print(f"✅ Outer JSON parsed successfully")
            
            # Extract tool call
            tool_call = outer_json["tool_calls"][0]
            function_info = tool_call["function"]
            tool_name = function_info["name"]
            arguments_str = function_info["arguments"]
            
            print(f"✅ Tool name: {tool_name}")
            print(f"✅ Arguments string: {arguments_str}")
            
            # Parse inner arguments JSON
            arguments = json.loads(arguments_str)
            print(f"✅ Arguments parsed: {arguments}")
            
            print(f"✅ Response {i+1} COMPLETELY SUCCESSFUL\n")
            
        except Exception as e:
            print(f"❌ Response {i+1} FAILED: {e}\n")
            all_success = False
    
    print("="*80)
    if all_success:
        print("🎉 ALL CONVERSATION RESPONSES PARSE PERFECTLY!")
        print("Parsing is NOT the issue causing 0 rewards.")
    else:
        print("❌ PARSING ISSUES FOUND IN CONVERSATION RESPONSES")
    print("="*80)
    
    return all_success

if __name__ == "__main__":
    test_exact_conversation_responses()