# Copyright Sierra

from envs.base import Env
from envs.healthcare.data import load_data
from envs.healthcare.rules import RULES
from envs.healthcare.tools import ALL_TOOLS
from envs.healthcare.wiki import WIKI
from typing import Optional, Union, List
from envs.user import UserStrategy
from tau_types import Task


class MockHealthcareDomainEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
        custom_tasks: Optional[List[Task]] = None,
    ):
        # Use custom tasks if provided, otherwise use empty tasks
        if custom_tasks is not None:
            tasks = custom_tasks
        else:
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