# Simple parser for VLLM native tool calling
import json
from typing import Union, Dict, Any, List, Optional
from tau_bench.tau_types import Action, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME


def parse_tool_calling_response(response: Union[str, Dict[str, Any]], source: str = "agent") -> Action:
    """
    Parse VLLM tool calling response (OpenAI-compatible format).
    
    This is a minimal parser for structured tool calling responses from VLLM
    when using the native tool calling API.
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
        if "tool_calls" in response and response["tool_calls"] is not None:
            tool_calls = response["tool_calls"]
            if len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call:
                    func_info = tool_call["function"]
                    # Ensure func_info is a dict before calling .get()
                    if isinstance(func_info, dict):
                        tool_name = func_info.get("name")
                        arguments = func_info.get("arguments", {})
                    else:
                        # func_info is not a dict, skip this tool call
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"   ⚠️  func_info is not dict: {type(func_info)}")
                        tool_name = None
                        arguments = {}
                    
                    # Parse arguments if they're a JSON string
                    if isinstance(arguments, str):
                        try:
                            arguments = json.loads(arguments)
                        except json.JSONDecodeError:
                            arguments = {}
                    
                    if tool_name:
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