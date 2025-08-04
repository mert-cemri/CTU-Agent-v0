"""DoorDash domain environment."""

import json
import os
from typing import Dict, Any, List, Optional, Union

from tau_bench.envs.base import Env
from tau_bench.envs.doordash.data import load_data
from tau_bench.envs.doordash.rules import RULES
from tau_bench.envs.doordash.tools import ALL_TOOLS
from tau_bench.envs.doordash.wiki import WIKI
from tau_bench.envs.user import UserStrategy
from tau_bench.tau_types import Task


class MockDoordashDomainEnv(Env):
    """DoorDash environment following the same pattern as Airline / Healthcare."""

    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
        custom_tasks: Optional[List[Task]] = None,
    ):
        # Use custom tasks if provided, otherwise use placeholder
        if custom_tasks is not None:
            tasks = custom_tasks
        else:
            # Currently no curated DoorDash tasks – supply one placeholder so the
            # base Env initialisation logic that picks a random task does not
            # fail.  Replace with real tasks when available.
            from tau_bench.tau_types import Task, Action

            tasks = [
                Task(
                    user_id="placeholder_user",
                    instruction="Placeholder DoorDash task – replace with real dataset.",
                    actions=[Action(name="think", kwargs={"thought": "placeholder"})],
                    outputs=[],
                )
            ]

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
        # Tools that terminate the conversation automatically (same as others)
        self.terminate_tools = ["transfer_to_human_agents"]
 