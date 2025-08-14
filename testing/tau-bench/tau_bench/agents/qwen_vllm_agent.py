import json
import re
from typing import List, Optional, Dict, Any
from tau_bench.agents.base import Agent
from tau_bench.envs.base import Env
from tau_bench.types import SolveResult, Action, RESPOND_ACTION_NAME


class QwenVLLMAgent(Agent):
    """VLLM Agent optimized for Qwen models with special token handling"""
    
    def __init__(
        self,
        tools_info: List[Dict[str, Any]],
        wiki: str,
        model: str,
        base_url: str = "http://localhost:8000/v1",
        temperature: float = 0.0,
    ):
        from openai import OpenAI
        self.tools_info = tools_info
        self.wiki = wiki
        self.model = model
        self.temperature = temperature
        self.client = OpenAI(base_url=base_url, api_key="EMPTY")
        
        # Qwen special tokens to clean
        self.special_tokens = [
            '<|im_end|>', '<|endoftext|>', '<|im_start|>', 
            '<eos>', '<bos>', '<|assistant|>', '<|user|>',
            '<|system|>', '\\n<|im_start|>', '\\n<|im_end|>'
        ]

    def solve(self, env: Env, task_index: Optional[int] = None, max_num_steps: int = 30) -> SolveResult:
        env_reset_res = env.reset(task_index=task_index)
        obs = env_reset_res.observation
        info = env_reset_res.info.model_dump()
        reward = 0.0
        messages = [
            {"role": "system", "content": self.wiki},
            {"role": "user", "content": obs},
        ]
        
        for _ in range(max_num_steps):
            try:
                res = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=self.tools_info,
                    temperature=self.temperature,
                    stop=["<|im_end|>", "<|endoftext|>"],  # Qwen stop tokens
                )
                
                msg = res.choices[0].message.model_dump()
                
                # Clean Qwen special tokens from content
                if msg.get("content"):
                    msg["content"] = self._clean_response(msg["content"])
                
                action = self._parse_action(msg)
                env_response = env.step(action)
                reward = env_response.reward
                info = {**info, **env_response.info.model_dump()}
                
                # Update conversation
                if action.name != RESPOND_ACTION_NAME and "tool_calls" in msg:
                    msg["tool_calls"] = msg["tool_calls"][:1]
                    messages.extend([
                        msg,
                        {
                            "role": "tool",
                            "tool_call_id": msg["tool_calls"][0]["id"],
                            "name": msg["tool_calls"][0]["function"]["name"],
                            "content": env_response.observation,
                        }
                    ])
                else:
                    # Clean response before adding
                    if msg.get("content"):
                        msg["content"] = self._clean_response(msg["content"])
                    messages.extend([msg, {"role": "user", "content": env_response.observation}])
                
                if env_response.done:
                    break
                    
            except Exception as e:
                print(f"Error in step: {e}")
                # Fallback to text response
                fallback_action = Action(
                    name=RESPOND_ACTION_NAME,
                    kwargs={"content": "I encountered an error. Could you please rephrase your request?"}
                )
                env_response = env.step(fallback_action)
                if env_response.done:
                    break
                    
        return SolveResult(reward=reward, info=info, messages=messages, total_cost=0.0)
    
    def _clean_response(self, text: str) -> str:
        """Remove Qwen special tokens from response"""
        for token in self.special_tokens:
            text = text.replace(token, '')
        return text.strip()
    
    def _parse_action(self, msg: Dict[str, Any]) -> Action:
        """Parse action with Qwen-specific handling"""
        
        # Try native tool calling first
        if "tool_calls" in msg and msg["tool_calls"]:
            tc = msg["tool_calls"][0]
            try:
                args = json.loads(tc["function"]["arguments"]) if isinstance(tc["function"]["arguments"], str) else tc["function"]["arguments"]
                return Action(name=tc["function"]["name"], kwargs=args)
            except:
                pass
        
        # Fallback to text parsing for Qwen's text-based tool calls
        content = msg.get("content", "")
        if content:
            # Clean special tokens first
            content = self._clean_response(content)
            
            # Look for tool call patterns
            # Pattern 1: function_name(arg1=value1, arg2=value2)
            tool_pattern = r'(\w+)\((.*?)\)'
            match = re.search(tool_pattern, content)
            if match:
                tool_name = match.group(1)
                args_str = match.group(2)
                
                # Check if tool exists
                if any(tool["function"]["name"] == tool_name for tool in self.tools_info):
                    try:
                        # Parse arguments
                        kwargs = {}
                        if args_str:
                            # Simple arg parsing
                            for arg in args_str.split(','):
                                if '=' in arg:
                                    key, val = arg.split('=', 1)
                                    key = key.strip()
                                    val = val.strip().strip('"\'')
                                    kwargs[key] = val
                        return Action(name=tool_name, kwargs=kwargs)
                    except:
                        pass
            
            # Pattern 2: JSON-like structure
            try:
                # Look for JSON in content
                json_match = re.search(r'\{.*?\}', content, re.DOTALL)
                if json_match:
                    data = json.loads(json_match.group())
                    if "function" in data and "name" in data["function"]:
                        return Action(
                            name=data["function"]["name"],
                            kwargs=data["function"].get("arguments", {})
                        )
            except:
                pass
        
        # Default to respond action
        return Action(name=RESPOND_ACTION_NAME, kwargs={"content": content})