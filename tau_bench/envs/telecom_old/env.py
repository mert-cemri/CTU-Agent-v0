# Copyright Sierra

from tau_bench.envs.base import Env
from tau_bench.envs.telecom.data import load_data
from tau_bench.envs.telecom.rules import RULES
from tau_bench.envs.telecom.tools import ALL_TOOLS
from tau_bench.envs.telecom.wiki import WIKI
from typing import Optional, Union, List
from tau_bench.envs.user import UserStrategy
from tau_bench.tau_types import Task


class MockTelecomDomainEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
        custom_tasks: Optional[List[Task]] = None,
    ):
        # Use custom tasks if provided, otherwise use empty list
        tasks = custom_tasks if custom_tasks is not None else []
        
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