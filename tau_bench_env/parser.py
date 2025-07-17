# Copyright Sierra

import json
import re
from typing import List, Dict, Any, Optional, Union
from tau_bench.types import Action, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME


def parse_llm_response(response: Union[str, Dict[str, Any]], available_tools: List[Dict[str, Any]]) -> Action:
    """
    Parse raw LLM response to extract tool calls and convert to tau_bench Action objects.
    
    Args:
        response: Raw LLM response (string) or structured response (dict)
        available_tools: List of available tool info dictionaries
        
    Returns:
        Action object with tool name and kwargs
    """
    # Extract tool names for validation
    tool_names = {tool["function"]["name"] for tool in available_tools}
    
    # Debug print
    print(f"DEBUG: tool_names = {tool_names}")
    print(f"DEBUG: response type = {type(response)}")
    print(f"DEBUG: response = {repr(response)}")
    
    # Handle dictionary input (e.g., OpenAI tool calls format)
    if isinstance(response, dict):
        action = _extract_dict_tool_call(response, tool_names)
        if action:
            return action
        # If dict doesn't contain tool calls, convert to string and continue
        response = json.dumps(response)
    
    # Handle string input
    if isinstance(response, str):
        # Try to extract direct JSON tool calls first (for simple JSON strings)
        action = _extract_direct_json(response, tool_names)
        if action:
            print(f"DEBUG: Found action via direct JSON: {action}")
            return action
        
        # Try to extract JSON tool calls from text/markdown
        action = _extract_json_tool_call(response, tool_names)
        if action:
            print(f"DEBUG: Found action via JSON extraction: {action}")
            return action
        
        # Try to extract ReAct-style tool calls
        action = _extract_react_tool_call(response, tool_names)
        if action:
            print(f"DEBUG: Found action via ReAct: {action}")
            return action
        
        # Try to extract function calls from code blocks
        action = _extract_function_call(response, tool_names, available_tools)
        if action:
            print(f"DEBUG: Found action via function call: {action}")
            return action
        
        # Check if it's just a tool name
        response_clean = response.strip()
        print(f"DEBUG: Checking direct tool name: '{response_clean}' in {tool_names}")
        if response_clean in tool_names:
            print(f"DEBUG: Found direct tool name: {response_clean}")
            return Action(name=response_clean, kwargs={})
    
    # Fall back to respond action with the full text
    response_text = response if isinstance(response, str) else json.dumps(response)
    print(f"DEBUG: Falling back to respond action")
    return Action(
        name=RESPOND_ACTION_NAME,
        kwargs={RESPOND_ACTION_FIELD_NAME: response_text.strip()}
    )


def _extract_direct_json(text: str, tool_names: set) -> Optional[Action]:
    """Extract direct JSON tool calls (for simple JSON strings)."""
    text = text.strip()
    
    print(f"DEBUG _extract_direct_json: text='{text}'")
    print(f"DEBUG _extract_direct_json: starts with {{: {text.startswith('{')}")
    print(f"DEBUG _extract_direct_json: ends with }}: {text.endswith('}')}")
    
    # Check if the entire text is a JSON object
    if text.startswith('{') and text.endswith('}'):
        try:
            parsed = json.loads(text)
            print(f"DEBUG _extract_direct_json: parsed JSON: {parsed}")
            
            # Handle different JSON structures
            if "name" in parsed and "arguments" in parsed:
                # Direct tool call format
                tool_name = parsed["name"]
                kwargs = parsed["arguments"]
                
                print(f"DEBUG _extract_direct_json: tool_name='{tool_name}', in tool_names: {tool_name in tool_names}")
                
                # Validate tool name
                if tool_name in tool_names:
                    return Action(name=tool_name, kwargs=kwargs)
                    
        except json.JSONDecodeError as e:
            print(f"DEBUG _extract_direct_json: JSON decode error: {e}")
            pass
    
    print(f"DEBUG _extract_direct_json: returning None")
    return None


def _extract_json_tool_call(text: str, tool_names: set) -> Optional[Action]:
    """Extract JSON-formatted tool calls from text."""
    # Look for JSON-like patterns
    json_patterns = [
        r'```json\s*(\{[^`]+\})\s*```',  # JSON in code blocks
        r'```\s*(\{[^`]+\})\s*```',      # JSON in code blocks without language
        r'(\{[^{}]*"name"\s*:[^{}]*"arguments"\s*:[^{}]*\})',  # Tool call structure
        r'(\{[^{}]*"function"\s*:[^{}]*\})',  # Function call structure
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            try:
                parsed = json.loads(match)
                
                # Handle different JSON structures
                if "name" in parsed and "arguments" in parsed:
                    # Direct tool call format
                    tool_name = parsed["name"]
                    kwargs = parsed["arguments"]
                elif "function" in parsed:
                    # Nested function format
                    func_info = parsed["function"]
                    tool_name = func_info.get("name")
                    kwargs = func_info.get("arguments", {})
                else:
                    continue
                
                # Validate tool name
                if tool_name in tool_names:
                    # Handle string arguments (need to parse again)
                    if isinstance(kwargs, str):
                        try:
                            kwargs = json.loads(kwargs)
                        except json.JSONDecodeError:
                            continue
                    
                    return Action(name=tool_name, kwargs=kwargs)
                    
            except json.JSONDecodeError:
                continue
    
    return None


def _extract_react_tool_call(text: str, tool_names: set) -> Optional[Action]:
    """Extract ReAct-style tool calls from text."""
    # Look for Action: patterns
    action_patterns = [
        r'Action:\s*(\{[^}]+\})',  # Action: {json}
        r'Action:\s*([^{}\n]+)',   # Action: tool_name
    ]
    
    for pattern in action_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            match = match.strip()
            
            # Try to parse as JSON
            if match.startswith('{'):
                try:
                    parsed = json.loads(match)
                    if "name" in parsed:
                        tool_name = parsed["name"]
                        kwargs = parsed.get("arguments", {})
                        
                        if tool_name in tool_names:
                            return Action(name=tool_name, kwargs=kwargs)
                except json.JSONDecodeError:
                    continue
            
            # Try to parse as simple tool name
            elif match in tool_names:
                return Action(name=match, kwargs={})
    
    return None


def _extract_dict_tool_call(response_dict: Dict[str, Any], tool_names: set) -> Optional[Action]:
    """Extract tool calls from dictionary format (e.g., OpenAI tool calls)."""
    # Handle OpenAI tool calls format
    if "tool_calls" in response_dict:
        tool_calls = response_dict["tool_calls"]
        if tool_calls and len(tool_calls) > 0:
            # Take the first tool call
            first_call = tool_calls[0]
            if "function" in first_call:
                func_info = first_call["function"]
                tool_name = func_info.get("name")
                arguments = func_info.get("arguments", {})
                
                # Parse arguments if they're a string
                if isinstance(arguments, str):
                    try:
                        arguments = json.loads(arguments)
                    except json.JSONDecodeError:
                        arguments = {}
                
                if tool_name and tool_name in tool_names:
                    return Action(name=tool_name, kwargs=arguments)
    
    # Handle direct function format
    if "function" in response_dict:
        func_info = response_dict["function"]
        tool_name = func_info.get("name")
        arguments = func_info.get("arguments", {})
        
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError:
                arguments = {}
        
        if tool_name and tool_name in tool_names:
            return Action(name=tool_name, kwargs=arguments)
    
    # Handle direct tool call format
    if "name" in response_dict and "arguments" in response_dict:
        tool_name = response_dict["name"]
        arguments = response_dict["arguments"]
        
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError:
                arguments = {}
        
        if tool_name and tool_name in tool_names:
            return Action(name=tool_name, kwargs=arguments)
    
    return None


def _extract_function_call(text: str, tool_names: set, available_tools: List[Dict[str, Any]]) -> Optional[Action]:
    """Extract function calls from code blocks."""
    # Look for function calls in code blocks - fix regex patterns
    code_patterns = [
        r'```python\s*(.*?)\s*```',  # Python code blocks
        r'```\s*(.*?)\s*```',        # Generic code blocks
    ]
    
    for pattern in code_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            # Look for function call pattern: function_name(arg1="value1", arg2="value2")
            func_call_pattern = r'(\w+)\s*\(\s*([^)]*)\s*\)'
            func_matches = re.findall(func_call_pattern, match)
            
            for func_name, args_str in func_matches:
                if func_name in tool_names:
                    # Parse arguments
                    kwargs = {}
                    if args_str.strip():
                        # Try different argument parsing strategies
                        
                        # Strategy 1: key="value" format
                        arg_pattern = r'(\w+)\s*=\s*["\']([^"\']*)["\']'
                        arg_matches = re.findall(arg_pattern, args_str)
                        if arg_matches:
                            kwargs = {key: value for key, value in arg_matches}
                        else:
                            # Strategy 2: positional arguments (would need tool schema to map)
                            # For now, just create a simple mapping
                            # This is a simplified approach - in real use, you'd want to match
                            # positional args to parameter names from the tool schema
                            arg_values = [arg.strip().strip('"\'') for arg in args_str.split(',')]
                            if len(arg_values) == 1 and arg_values[0]:
                                # Common case: single argument, try to guess the parameter name
                                # Look at the tool schema to find the first parameter
                                for tool in available_tools:
                                    if tool["function"]["name"] == func_name:
                                        params = tool["function"]["parameters"].get("properties", {})
                                        if params:
                                            first_param = next(iter(params.keys()))
                                            kwargs = {first_param: arg_values[0]}
                                            break
                    
                    return Action(name=func_name, kwargs=kwargs)
    
    return None


def format_tool_info_for_llm(tools_info: List[Dict[str, Any]]) -> str:
    """Format tool information for LLM context."""
    formatted_tools = []
    
    for tool in tools_info:
        tool_desc = {
            "name": tool["function"]["name"],
            "description": tool["function"]["description"],
            "parameters": tool["function"]["parameters"]
        }
        formatted_tools.append(json.dumps(tool_desc, indent=2))
    
    return "\n\n".join(formatted_tools) 