# Copyright Sierra

from envs.base import Env
from envs.telecom.data import load_data
from envs.telecom.rules import RULES
from envs.telecom.tools import ALL_TOOLS
from envs.telecom.wiki import WIKI
from typing import Optional, Union
from envs.user import UserStrategy


class MockTelecomDomainEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
    ):
        # For now, use empty tasks since we don't have telecom tasks yet
        tasks = []
        
        super().__init__(
            data_load_func=load_data,
            tools=ALL_TOOLS,
            tasks=tasks,
            wiki=WIKI,
            rules=RULES,
            user_strategy=user_strategy,
            user_model=user_model,
            user_provider=user_provider,
            task_index=task_index,
        )
        self.terminate_tools = ["transfer_to_human_agents"]