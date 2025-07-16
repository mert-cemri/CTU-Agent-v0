# Copyright Sierra

import json
import re
from typing import List, Dict, Any, Optional
from tau_bench.types import Action, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME


def parse_llm_response(text: str, available_tools: List[Dict[str, Any]]) -> Action:
    """
    Parse raw LLM text response to extract tool calls and convert to tau_bench Action objects.
    
    Args:
        text: Raw LLM response text
        available_tools: List of available tool info dictionaries
        
    Returns:
        Action object with tool name and kwargs
    """
    # Extract tool names for validation
    tool_names = {tool["function"]["name"] for tool in available_tools}
    
    # Try to extract JSON tool calls from text (similar to tau_bench tool_calling_agent)
    action = _extract_json_tool_call(text, tool_names)
    if action:
        return action
    
    # Try to extract ReAct-style tool calls
    action = _extract_react_tool_call(text, tool_names)
    if action:
        return action
    
    # Fall back to respond action with the full text
    return Action(
        name=RESPOND_ACTION_NAME,
        kwargs={RESPOND_ACTION_FIELD_NAME: text.strip()}
    )


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