# Simple parser for VLLM native tool calling
import json
from typing import Union, Dict, Any, List, Optional
from tau_bench.tau_types import Action, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME


def parse_tool_calling_response(response: Union[str, Dict[str, Any]], source: str = "agent") -> Action:
    """
    Parse VLLM tool calling response (OpenAI-compatible format).
    
    Expected format for structured tool calling:
    {
        "tool_calls": [
            {
                "id": "call_xxx",
                "type": "function", 
                "function": {
                    "name": "tool_name",
                    "arguments": "{\"arg1\": \"value1\"}"  # JSON string
                }
            }
        ]
    }
    """
    import os
    
    # Debug logging
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n🔍 SIMPLE PARSER DEBUG:")
        print(f"   Response type: {type(response)}")
        print(f"   Response content: {repr(response)[:200]}...")
    
    # Handle dictionary response (structured tool calling)
    if isinstance(response, dict):
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"   📋 Processing dict response")
            
        # Check for tool_calls in OpenAI format
        if "tool_calls" in response:
            tool_calls = response["tool_calls"]
            
            # Validate structure - tool_calls MUST be a list
            if tool_calls is not None and not isinstance(tool_calls, list):
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"   ⚠️  Malformed tool_calls: {type(tool_calls)} = {repr(tool_calls)[:100]}")
                    print(f"   💬 Falling back to respond action")
                return Action(
                    name=RESPOND_ACTION_NAME,
                    kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                )
            
            if tool_calls and len(tool_calls) > 0:
                # Process first tool call
                tool_call = tool_calls[0]
                
                # Validate tool_call structure - if malformed, fall back to respond
                if not isinstance(tool_call, dict):
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ⚠️  Malformed tool_call: {type(tool_call)} = {tool_call}")
                        print(f"   💬 Falling back to respond action")
                    return Action(
                        name=RESPOND_ACTION_NAME,
                        kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                    )
                
                # Optional fields: id, type
                # Required field: function
                if "function" not in tool_call:
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ⚠️  Tool_call missing 'function' field: {list(tool_call.keys())}")
                        print(f"   💬 Falling back to respond action")
                    return Action(
                        name=RESPOND_ACTION_NAME,
                        kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                    )
                
                func_info = tool_call["function"]
                
                # Validate function structure - if malformed, fall back to respond
                if not isinstance(func_info, dict):
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ⚠️  Malformed function field: {type(func_info)} = {func_info}")
                        print(f"   💬 Falling back to respond action")
                    return Action(
                        name=RESPOND_ACTION_NAME,
                        kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                    )
                
                if "name" not in func_info:
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ⚠️  Function missing 'name' field: {list(func_info.keys())}")
                        print(f"   💬 Falling back to respond action")
                    return Action(
                        name=RESPOND_ACTION_NAME,
                        kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                    )
                
                tool_name = func_info["name"]
                arguments = func_info.get("arguments", {})
                
                # Validate tool name - if malformed, fall back to respond
                if not isinstance(tool_name, str) or len(tool_name) == 0:
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ⚠️  Invalid tool name: {repr(tool_name)}")
                        print(f"   💬 Falling back to respond action")
                    return Action(
                        name=RESPOND_ACTION_NAME,
                        kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                    )
                
                # Parse arguments if they're a JSON string (OpenAI format)
                if isinstance(arguments, str):
                    try:
                        arguments = json.loads(arguments)
                    except json.JSONDecodeError as e:
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"   ⚠️  Failed to parse arguments JSON: {e}")
                            print(f"   📋 Arguments string: {repr(arguments)}")
                        arguments = {}
                
                # Validate final arguments - if malformed, fall back to respond
                if not isinstance(arguments, dict):
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ⚠️  Invalid arguments after parsing: {type(arguments)} = {arguments}")
                        print(f"   💬 Falling back to respond action")
                    return Action(
                        name=RESPOND_ACTION_NAME,
                        kwargs={RESPOND_ACTION_FIELD_NAME: str(response)}
                    )
                
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"   ✅ Found tool call: {tool_name} with args: {arguments}")
                
                return Action(name=tool_name, kwargs=arguments)
        
        # Check for direct content response
        if "content" in response and response["content"]:
            if os.environ.get("DEBUG_PARSER", "0") == "1":
                print(f"   💬 Found content response")
            return Action(
                name=RESPOND_ACTION_NAME,
                kwargs={RESPOND_ACTION_FIELD_NAME: response["content"]}
            )
    
    # Handle string response - try to parse as JSON first for fallback compatibility
    if isinstance(response, str):
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"   📝 Processing string response")
            
        # Clean the response first
        cleaned_response = response.strip()
        
        # Remove model-specific tokens that might interfere
        tokens_to_remove = ['<|im_end|>', '<|endoftext|>', '<|im_start|>']
        for token in tokens_to_remove:
            cleaned_response = cleaned_response.replace(token, '')
        cleaned_response = cleaned_response.strip()
        
        # Try to parse as JSON (fallback for when VLLM returns JSON string instead of structured response)
        if cleaned_response.startswith('{') and 'tool_calls' in cleaned_response:
            try:
                parsed_json = json.loads(cleaned_response)
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"   🔄 Parsed JSON from string, retrying as dict")
                # Recursively call with parsed JSON
                return parse_tool_calling_response(parsed_json, source)
            except json.JSONDecodeError as e:
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"   ❌ Failed to parse JSON from string: {e}")
                    print(f"   📝 Malformed JSON (first 200 chars): {repr(cleaned_response[:200])}")
                pass
        
        # Fallback to respond action
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"   💬 Defaulting to respond action")
        return Action(
            name=RESPOND_ACTION_NAME,
            kwargs={RESPOND_ACTION_FIELD_NAME: cleaned_response}
        )
    
    # Final fallback
    response_text = str(response) if response else ""
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"   🔚 Final fallback to respond")
    return Action(
        name=RESPOND_ACTION_NAME,
        kwargs={RESPOND_ACTION_FIELD_NAME: response_text}
    )