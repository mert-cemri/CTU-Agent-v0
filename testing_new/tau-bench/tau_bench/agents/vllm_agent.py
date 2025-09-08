import json
from typing import List, Optional, Dict, Any
from tau_bench.agents.base import Agent
from tau_bench.envs.base import Env
from tau_bench.types import SolveResult, Action, RESPOND_ACTION_NAME


class VLLMAgent(Agent):
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
            res = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools_info,
                temperature=self.temperature,
            )
            
            msg = res.choices[0].message.model_dump()
            action = self._parse_action(msg)
            env_response = env.step(action)
            reward = env_response.reward
            info = {**info, **env_response.info.model_dump()}
            
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
                messages.extend([msg, {"role": "user", "content": env_response.observation}])
            
            if env_response.done:
                break
                
        return SolveResult(reward=reward, info=info, messages=messages, total_cost=0.0)
    
    def _parse_action(self, msg: Dict[str, Any]) -> Action:
        if "tool_calls" in msg and msg["tool_calls"]:
            tc = msg["tool_calls"][0]
            return Action(
                name=tc["function"]["name"],
                kwargs=json.loads(tc["function"]["arguments"])
            )
        return Action(name=RESPOND_ACTION_NAME, kwargs={"content": msg.get("content", "")})