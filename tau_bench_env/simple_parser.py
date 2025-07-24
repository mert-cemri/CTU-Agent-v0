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
    # Handle dictionary response (structured tool calling)
    if isinstance(response, dict):
        # Check for tool_calls in OpenAI format
        if "tool_calls" in response and response["tool_calls"] is not None:
            tool_calls = response["tool_calls"]
            if len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call:
                    func_info = tool_call["function"]
                    tool_name = func_info.get("name")
                    arguments = func_info.get("arguments", {})
                    
                    # Parse arguments if they're a JSON string
                    if isinstance(arguments, str):
                        try:
                            arguments = json.loads(arguments)
                        except json.JSONDecodeError:
                            arguments = {}
                    
                    if tool_name:
                        return Action(name=tool_name, kwargs=arguments)
        
        # Check for direct content response
        if "content" in response and response["content"]:
            return Action(
                name=RESPOND_ACTION_NAME,
                kwargs={RESPOND_ACTION_FIELD_NAME: response["content"]}
            )
    
    # Handle string response (fallback to text parsing)
    if isinstance(response, str):
        return Action(
            name=RESPOND_ACTION_NAME,
            kwargs={RESPOND_ACTION_FIELD_NAME: response.strip()}
        )
    
    # Final fallback
    response_text = str(response) if response else ""
    return Action(
        name=RESPOND_ACTION_NAME,
        kwargs={RESPOND_ACTION_FIELD_NAME: response_text}
    )