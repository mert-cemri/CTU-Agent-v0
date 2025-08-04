# Copyright Sierra

import json
import os
import re
from typing import List, Dict, Any, Optional, Union
from tau_bench.tau_types import Action, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME


def _validate_and_sanitize_kwargs(kwargs: Any, tool_name: str, debug_context: str = "") -> Dict[str, Any]:
    """
    Validate and sanitize kwargs to ensure they're a dictionary for Action creation.
    
    Args:
        kwargs: The kwargs value to validate (could be any type)
        tool_name: Name of the tool for logging context
        debug_context: Additional context for debugging
    
    Returns:
        A valid dictionary for Action.kwargs
    """
    import os
    
    if isinstance(kwargs, dict):
        return kwargs
    
    # Handle JSON string arguments (common in OpenAI format)
    if isinstance(kwargs, str):
        try:
            # Try to parse as JSON
            parsed = json.loads(kwargs)
            if isinstance(parsed, dict):
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"   ✅ Successfully parsed JSON arguments for {tool_name}")
                return parsed
        except json.JSONDecodeError:
            pass
    
    # Log the problematic case for debugging
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n⚠️  KWARGS VALIDATION WARNING:")
        print(f"   Tool: {tool_name}")
        print(f"   Context: {debug_context}")
        print(f"   Expected: dict, Got: {type(kwargs).__name__}")
        print(f"   Value: {repr(kwargs)}")
        print(f"   Falling back to empty dict")
    
    # Fallback: return empty dict to prevent ValidationError
    return {}


def parse_llm_response(response: Union[str, Dict[str, Any]], tools_info: List[Dict[str, Any]], source: str = "unknown") -> Action:
    """
    Parse the LLM response and return a tau_bench Action.
    
    Args:
        response: The response to parse (from agent or user)
        tools_info: Available tools information
        source: Source of response ("agent", "user", or "unknown")
    """
    assert isinstance(tools_info, list) and len(tools_info) > 0, "tools_info must be non-empty list"
    assert all("function" in tool and "name" in tool["function"] for tool in tools_info), \
        "Invalid tools_info structure"
    
    # Pre-process a dict response to handle nested tool_name
    if isinstance(response, dict):
        if "tool_name" in response and isinstance(response["tool_name"], dict):
            if "name" in response["tool_name"]:
                response["tool_name"] = response["tool_name"]["name"]

    tool_names = [tool["function"]["name"] for tool in tools_info]
    
    # Enhanced debug logging with source awareness
    import os
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n=== PARSER DEBUG ({source.upper()}) ===")
        print(f"Available tools: {tool_names}")
        print(f"Response type: {type(response)}")
        if isinstance(response, str):
            print(f"Response (first 500 chars): {repr(response[:500])}")
        else:
            print(f"Response: {repr(response)}")
        print("=" * (20 + len(source)))
    
    # If this is a user response, skip tool call parsing entirely
    # User responses should be treated as conversational content, not tool calls
    if source == "user":
        response_text = response if isinstance(response, str) else json.dumps(response)
        
        # Clean user response from model tokens
        tokens_to_strip = ['<|im_end|>', '<|endoftext|>', '<|im_start|>', '<eos>', '<bos>']
        for token in tokens_to_strip:
            response_text = response_text.replace(token, '')
        response_text = response_text.strip()
        
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"🧑 USER RESPONSE - Skipping tool call parsing, treating as conversational content")
        return Action(
            name=RESPOND_ACTION_NAME,
            kwargs={RESPOND_ACTION_FIELD_NAME: response_text}
        )
    
    # Handle dictionary input (e.g., OpenAI tool calls format)
    if isinstance(response, dict):
        action = _extract_dict_tool_call(response, tool_names)
        if action:
            return action
        # If dict doesn't contain tool calls, convert to string and continue
        response = json.dumps(response)
    
    # Handle string input
    if isinstance(response, str):
        # Try to parse as OpenAI tool_calls format first (highest priority)
        action = _extract_openai_tool_calls(response, tool_names)
        if action:
            if os.environ.get("DEBUG_PARSER", "0") == "1":
                print(f"DEBUG: Successfully parsed OpenAI tool_calls format")
            return action
        
        # Try to extract direct JSON tool calls (for simple JSON strings)
        action = _extract_direct_json(response, tool_names)
        if action:
            if os.environ.get("DEBUG_PARSER", "0") == "1":
                print(f"DEBUG: Successfully parsed direct JSON format")
            return action
        
        # Try to extract JSON tool calls from text/markdown
        action = _extract_json_tool_call(response, tool_names)
        if action:
            if os.environ.get("DEBUG_PARSER", "0") == "1":
                print(f"DEBUG: Successfully parsed embedded JSON format")
            return action
        
        # Try to extract ReAct-style tool calls
        action = _extract_react_tool_call(response, tool_names)
        if action:
            # print(f"DEBUG: Found action via ReAct: {action}")
            return action
        
        # Try to extract function calls from code blocks
        action = _extract_function_call(response, tool_names, tools_info)
        if action:
            # print(f"DEBUG: Found action via function call: {action}")
            return action
        
        # Check if it's just a tool name
        response_clean = response.strip()
        if response_clean in tool_names:
            try:
                return Action(name=response_clean, kwargs={})
            except Exception as e:
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"\n❌ DIRECT TOOL NAME ACTION CREATION FAILED:")
                    print(f"   Tool: {response_clean}")
                    print(f"   Error: {e}")
    
    # Fall back to respond action with the full text
    response_text = response if isinstance(response, str) else json.dumps(response)
    
    # Log parsing failure details with source context
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n=== PARSER FALLBACK ({source.upper()}) ===")
        print(f"Failed to parse tool call, falling back to respond action")
        print(f"Original response: {repr(response_text[:200])}")
        if source == "agent":
            print("⚠️  Agent response didn't match any tool call pattern")
        print("=" * (25 + len(source)))
    
    fallback_action = Action(
        name=RESPOND_ACTION_NAME,
        kwargs={RESPOND_ACTION_FIELD_NAME: response_text.strip()}
    )
    
    # Assert the action is valid before returning
    assert hasattr(fallback_action, 'name') and hasattr(fallback_action, 'kwargs'), \
        f"Invalid Action created: {fallback_action}"
    assert fallback_action.name == RESPOND_ACTION_NAME, "Fallback action must be respond action"
    
    return fallback_action


def _extract_openai_tool_calls(text: str, tool_names: set) -> Optional[Action]:
    """Extract OpenAI-style tool_calls format from text."""
    text = text.strip()
    
    # Remove common model-specific tokens
    tokens_to_strip = ['<|im_end|>', '<|endoftext|>', '<|im_start|>', '<eos>', '<bos>']
    for token in tokens_to_strip:
        text = text.replace(token, '').strip()
    
    # Check if it looks like a tool_calls JSON object
    if text.startswith('{') and 'tool_calls' in text:
        # Skip obviously malformed JSON
        if text.count('{') != text.count('}') or text.count('"') % 2 != 0:
            return None
            
        try:
            parsed = json.loads(text)
            
            # Handle OpenAI tool_calls format: {"tool_calls": [{"function": {"name": "...", "arguments": "..."}}]}
            if "tool_calls" in parsed and isinstance(parsed["tool_calls"], list) and len(parsed["tool_calls"]) > 0:
                first_call = parsed["tool_calls"][0]
                
                if "function" in first_call:
                    func_info = first_call["function"]
                    tool_name = func_info.get("name")
                    arguments_str = func_info.get("arguments", "{}")
                    
                    # Validate tool name
                    if tool_name and tool_name in tool_names:
                        # Parse arguments (they should be a JSON string)
                        try:
                            if isinstance(arguments_str, str):
                                kwargs = json.loads(arguments_str)
                            else:
                                kwargs = arguments_str  # Already parsed
                        except json.JSONDecodeError:
                            # If arguments can't be parsed, try as-is
                            kwargs = arguments_str if isinstance(arguments_str, dict) else {}
                        
                        # Validate and sanitize kwargs before creating Action
                        sanitized_kwargs = _validate_and_sanitize_kwargs(
                            kwargs, tool_name, "OpenAI tool_calls format"
                        )
                        
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"DEBUG: Parsed OpenAI tool call - tool: {tool_name}, args: {sanitized_kwargs}")
                        
                        try:
                            return Action(name=tool_name, kwargs=sanitized_kwargs)
                        except Exception as e:
                            # Log Action creation failure for debugging
                            if os.environ.get("DEBUG_PARSER", "0") == "1":
                                print(f"\n❌ OPENAI ACTION CREATION FAILED:")
                                print(f"   Tool: {tool_name}")
                                print(f"   Sanitized kwargs: {sanitized_kwargs}")
                                print(f"   Error: {e}")
                            # Return None to continue with other parsing attempts
                            return None
                        
        except json.JSONDecodeError as e:
            if os.environ.get("DEBUG_PARSER", "0") == "1":
                print(f"DEBUG: Failed to parse tool_calls JSON: {e}")
            pass
    
    return None


def _extract_direct_json(text: str, tool_names: set) -> Optional[Action]:
    """Extract direct JSON tool calls (for simple JSON strings)."""
    text = text.strip()
    
    # Strip common model-specific tokens that might interfere with JSON parsing
    tokens_to_strip = [
        '<|im_end|>',
        '<|endoftext|>',
        '<|im_start|>',
        '',
        '',
        '<eos>',
        '<bos>',
        '```',
    ]
    
    for token in tokens_to_strip:
        text = text.replace(token, '').strip()
    
    # print(f"DEBUG _extract_direct_json: cleaned text='{text}'")
    # print(f"DEBUG _extract_direct_json: starts with {{: {text.startswith('{')}")
    # print(f"DEBUG _extract_direct_json: ends with }}: {text.endswith('}')}")
    
    # Check if the entire text is a JSON object
    if text.startswith('{') and text.endswith('}'):
        # Skip obviously malformed JSON
        if text.count('{') != text.count('}') or text.count('"') % 2 != 0:
            return None
            
        try:
            parsed = json.loads(text)
            # print(f"DEBUG _extract_direct_json: parsed JSON: {parsed}")
            
            # Handle different JSON structures
            if "name" in parsed and "arguments" in parsed:
                # Direct tool call format
                tool_name = parsed["name"]
                kwargs = parsed["arguments"]
                
                # print(f"DEBUG _extract_direct_json: tool_name='{tool_name}', in tool_names: {tool_name in tool_names}")
                
                # Validate tool name
                if isinstance(tool_name, str) and tool_name in tool_names:
                    # Validate and sanitize kwargs before creating Action
                    sanitized_kwargs = _validate_and_sanitize_kwargs(
                        kwargs, tool_name, "Direct JSON format"
                    )
                    
                    try:
                        return Action(name=tool_name, kwargs=sanitized_kwargs)
                    except Exception as e:
                        # Log Action creation failure for debugging
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"\n❌ DIRECT JSON ACTION CREATION FAILED:")
                            print(f"   Tool: {tool_name}")
                            print(f"   Sanitized kwargs: {sanitized_kwargs}")
                            print(f"   Error: {e}")
                else:
                    # print(f"DEBUG _extract_direct_json: tool_name '{tool_name}' not in available tools")
                    pass
                    
        except json.JSONDecodeError as e:
            # print(f"DEBUG _extract_direct_json: JSON decode error: {e}")
            pass
    
    # print(f"DEBUG _extract_direct_json: returning None")
    return None


def _extract_json_tool_call(text: str, tool_names: set) -> Optional[Action]:
    """Extract JSON-formatted tool calls from text."""
    # Look for JSON objects by finding balanced braces
    import re
    
    # Find all potential JSON objects (balanced braces)
    brace_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.findall(brace_pattern, text, re.DOTALL)
    
    # Also try code block patterns
    code_patterns = [
        r'```json\s*(\{.*?\})\s*```',  # JSON in code blocks
        r'```\s*(\{.*?\})\s*```',      # JSON in code blocks without language
    ]
    
    for pattern in code_patterns:
        code_matches = re.findall(pattern, text, re.DOTALL)
        matches.extend(code_matches)
    
    # Process all matches
    for match in matches:
            # Skip obviously malformed JSON patterns
            if len(match) < 10 or match.count('{') != match.count('}') or match.count('"') % 2 != 0:
                continue
                
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
                    if isinstance(func_info, dict):
                        tool_name = func_info.get("name")
                        kwargs = func_info.get("arguments", {})
                    else:
                        # func_info is not a dict, skip this pattern
                        continue
                else:
                    continue
                
                # Validate tool name
                if tool_name in tool_names:
                    # Validate and sanitize kwargs before creating Action
                    sanitized_kwargs = _validate_and_sanitize_kwargs(
                        kwargs, tool_name, f"JSON tool call extraction from {match[:100]}..."
                    )
                    
                    try:
                        return Action(name=tool_name, kwargs=sanitized_kwargs)
                    except Exception as e:
                        # Log Action creation failure for debugging
                        import os
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"\n❌ ACTION CREATION FAILED:")
                            print(f"   Tool: {tool_name}")
                            print(f"   Sanitized kwargs: {sanitized_kwargs}")
                            print(f"   Error: {e}")
                        continue
                    
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
                            sanitized_kwargs = _validate_and_sanitize_kwargs(
                                kwargs, tool_name, "ReAct JSON format"
                            )
                            try:
                                return Action(name=tool_name, kwargs=sanitized_kwargs)
                            except Exception as e:
                                if os.environ.get("DEBUG_PARSER", "0") == "1":
                                    print(f"\n❌ REACT JSON ACTION CREATION FAILED:")
                                    print(f"   Tool: {tool_name}")
                                    print(f"   Sanitized kwargs: {sanitized_kwargs}")
                                    print(f"   Error: {e}")
                                continue
                except json.JSONDecodeError:
                    continue
            
            # Try to parse as simple tool name
            elif match in tool_names:
                try:
                    return Action(name=match, kwargs={})
                except Exception as e:
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"\n❌ REACT SIMPLE ACTION CREATION FAILED:")
                        print(f"   Tool: {match}")
                        print(f"   Error: {e}")
                    continue
    
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
                    except json.JSONDecodeError as e:
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"\n⚠️  MALFORMED JSON ARGUMENTS:")
                            print(f"   Tool: {tool_name}")
                            print(f"   Raw arguments: {repr(arguments[:200])}")
                            print(f"   JSON error: {e}")
                        # Try to fix common JSON issues
                        try:
                            # Remove trailing garbage characters
                            fixed_args = arguments.split(' fix all issues')[0]
                            if not fixed_args.endswith('}'):
                                fixed_args += '}'
                            arguments = json.loads(fixed_args)
                            if os.environ.get("DEBUG_PARSER", "0") == "1":
                                print(f"   ✓ Fixed arguments: {arguments}")
                        except:
                            # If still can't parse, use empty dict
                            arguments = {}
                            if os.environ.get("DEBUG_PARSER", "0") == "1":
                                print(f"   Using empty arguments as fallback")
                
                if tool_name and tool_name in tool_names:
                    sanitized_kwargs = _validate_and_sanitize_kwargs(
                        arguments, tool_name, "Dict tool_calls format"
                    )
                    try:
                        return Action(name=tool_name, kwargs=sanitized_kwargs)
                    except Exception as e:
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"\n❌ DICT TOOL_CALLS ACTION CREATION FAILED:")
                            print(f"   Tool: {tool_name}")
                            print(f"   Sanitized kwargs: {sanitized_kwargs}")
                            print(f"   Error: {e}")
    
    # Handle direct function format
    if "function" in response_dict:
        func_info = response_dict["function"]
        tool_name = func_info.get("name")
        arguments = func_info.get("arguments", {})
        
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError as e:
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"\n⚠️  MALFORMED JSON ARGUMENTS (Dict function format):")
                    print(f"   Tool: {tool_name}")
                    print(f"   Raw arguments: {repr(arguments[:200])}")
                    print(f"   JSON error: {e}")
                # Try to fix common JSON issues
                try:
                    # Remove trailing garbage characters
                    fixed_args = arguments.split(' fix all issues')[0]
                    if not fixed_args.endswith('}'):
                        fixed_args += '}'
                    arguments = json.loads(fixed_args)
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ✓ Fixed arguments: {arguments}")
                except:
                    # If still can't parse, use empty dict
                    arguments = {}
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   Using empty arguments as fallback")
        
        if tool_name and tool_name in tool_names:
            sanitized_kwargs = _validate_and_sanitize_kwargs(
                arguments, tool_name, "Dict function format"
            )
            try:
                return Action(name=tool_name, kwargs=sanitized_kwargs)
            except Exception as e:
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"\n❌ DICT FUNCTION ACTION CREATION FAILED:")
                    print(f"   Tool: {tool_name}")
                    print(f"   Sanitized kwargs: {sanitized_kwargs}")
                    print(f"   Error: {e}")
    
    # Handle direct tool call format
    if "name" in response_dict and "arguments" in response_dict:
        tool_name = response_dict["name"]
        arguments = response_dict["arguments"]
        
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError as e:
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"\n⚠️  MALFORMED JSON ARGUMENTS (Dict direct format):")
                    print(f"   Tool: {tool_name}")
                    print(f"   Raw arguments: {repr(arguments[:200])}")
                    print(f"   JSON error: {e}")
                # Try to fix common JSON issues
                try:
                    # Remove trailing garbage characters
                    fixed_args = arguments.split(' fix all issues')[0]
                    if not fixed_args.endswith('}'):
                        fixed_args += '}'
                    arguments = json.loads(fixed_args)
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   ✓ Fixed arguments: {arguments}")
                except:
                    # If still can't parse, use empty dict
                    arguments = {}
                    if os.environ.get("DEBUG_PARSER", "0") == "1":
                        print(f"   Using empty arguments as fallback")
        
        if tool_name and tool_name in tool_names:
            sanitized_kwargs = _validate_and_sanitize_kwargs(
                arguments, tool_name, "Dict direct format"
            )
            try:
                return Action(name=tool_name, kwargs=sanitized_kwargs)
            except Exception as e:
                if os.environ.get("DEBUG_PARSER", "0") == "1":
                    print(f"\n❌ DICT DIRECT ACTION CREATION FAILED:")
                    print(f"   Tool: {tool_name}")
                    print(f"   Sanitized kwargs: {sanitized_kwargs}")
                    print(f"   Error: {e}")
    
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
                    
                    sanitized_kwargs = _validate_and_sanitize_kwargs(
                        kwargs, func_name, "Function call format"
                    )
                    try:
                        return Action(name=func_name, kwargs=sanitized_kwargs)
                    except Exception as e:
                        if os.environ.get("DEBUG_PARSER", "0") == "1":
                            print(f"\n❌ FUNCTION CALL ACTION CREATION FAILED:")
                            print(f"   Tool: {func_name}")
                            print(f"   Sanitized kwargs: {sanitized_kwargs}")
                            print(f"   Error: {e}")
                        continue
    
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