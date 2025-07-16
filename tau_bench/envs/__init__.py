# Copyright Sierra

from typing import Optional, Union, List
from tau_bench.envs.base import Env
from tau_bench.envs.user import UserStrategy
from tau_bench.types import Task


def get_env(
    env_name: str,
    user_strategy: Union[str, UserStrategy],
    user_model: str,
    task_split: str,
    user_provider: Optional[str] = None,
    task_index: Optional[int] = None,
    custom_tasks: Optional[List[Task]] = None,
) -> Env:
    """Get environment for specified domain with optional custom tasks"""
    
    if env_name == "retail":
        from tau_bench.envs.retail import MockRetailDomainEnv
        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            custom_tasks=custom_tasks,
        )
    elif env_name == "airline":
        from tau_bench.envs.airline import MockAirlineDomainEnv
        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            custom_tasks=custom_tasks,
        )
    elif env_name == "telecom":
        from tau_bench.envs.telecom import MockTelecomDomainEnv
        return MockTelecomDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            custom_tasks=custom_tasks,
        )
    elif env_name == "doordash":
        from tau_bench.envs.doordash import MockDoordashDomainEnv
        return MockDoordashDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            custom_tasks=custom_tasks,
        )
    elif env_name == "healthcare":
        from tau_bench.envs.healthcare import MockHealthcareDomainEnv
        return MockHealthcareDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            custom_tasks=custom_tasks,
        )
    else:
        raise ValueError(f"Unknown environment: {env_name}. Supported: retail, airline, telecom, doordash, healthcare")
