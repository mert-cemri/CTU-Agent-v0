# Copyright Sierra

import random
from hashlib import sha256
from tau_bench.envs.tool import Tool
from typing import Any, Callable, Dict, List, Type, Optional, Set, Union, Tuple

from tau_bench.envs.user import load_user, UserStrategy
from tau_bench.tau_types import (
    Action,
    Task,
    EnvInfo,
    EnvResetResponse,
    EnvResponse,
    RewardResult,
    RewardOutputInfo,
    RewardActionInfo,
    RESPOND_ACTION_NAME,
)

ToHashable = Union[
    str, int, float, Dict[str, "ToHashable"], List["ToHashable"], Set["ToHashable"]
]
Hashable = Union[str, int, float, Tuple["Hashable"], Tuple[Tuple[str, "Hashable"]]]


def to_hashable(item: ToHashable) -> Hashable:
    if isinstance(item, dict):
        return tuple((key, to_hashable(value)) for key, value in sorted(item.items()))
    elif isinstance(item, list):
        return tuple(to_hashable(element) for element in item)
    elif isinstance(item, set):
        return tuple(sorted(to_hashable(element) for element in item))
    else:
        return item


def consistent_hash(
    value: Hashable,
) -> str:
    return sha256(str(value).encode("utf-8")).hexdigest()


class Env(object):
    def __init__(
        self,
        data_load_func: Callable[[], Dict[str, Any]],
        tools: List[Type[Tool]],
        tasks: List[Task],
        wiki: str,
        rules: List[str],
        user_strategy: Union[str, UserStrategy],
        user_model: str,
        user_provider: Optional[str] = None,
        task_index: Optional[int] = None,
    ) -> None:
        super().__init__()
        self.data_load_func = data_load_func
        self.data = data_load_func()
        self.tools_map: Dict[str, Type[Tool]] = {
            tool.get_info()["function"]["name"]: tool for tool in tools
        }
        self.tools_info = [tool.get_info() for tool in tools]
        self.terminate_tools = []
        self.tasks = tasks
        if task_index is not None:
            self.task_index = task_index
        else:
            self.task_index = random.randint(0, len(tasks) - 1) if tasks else 0
        self.task = tasks[self.task_index] if tasks else None
        self.wiki = wiki
        self.rules = rules
        self.user = load_user(
            user_strategy=user_strategy, model=user_model, provider=user_provider
        )
        self.actions: List[Action] = []

    def reset(self, task_index: Optional[int] = None) -> EnvResetResponse:
        if task_index is None:
            task_index = random.randint(0, len(self.tasks) - 1) if self.tasks else 0
        self.task_index = task_index
        self.data = self.data_load_func()
        self.task = self.tasks[task_index] if self.tasks else None
        self.actions = []
        initial_observation = self.user.reset(instruction=self.task.instruction if self.task else "Test instruction")
        return EnvResetResponse(
            observation=initial_observation, 
            info=EnvInfo(
                task=self.task if self.task else Task(
                    user_id="test",
                    instruction="Test instruction",
                    actions=[],
                    outputs=[]
                ), 
                source="user"
            )
        )

    def step(self, action: Action) -> EnvResponse:
        self.actions.append(action)

        info = EnvInfo(
            task=self.task if self.task else Task(
                user_id="test",
                instruction="Test instruction",
                actions=[],
                outputs=[]
            )
        )
        reward = 0
        done = False
        if action.name == RESPOND_ACTION_NAME:
            observation = self.user.step(action.kwargs["content"])
            info.source = "user"
            done = "###STOP###" in observation
        elif action.name in self.tools_map:
            try:
                observation = self.tools_map[action.name].invoke(
                    data=self.data, **action.kwargs
                )
            except Exception as e:
                observation = f"Error: {e}"
            info.source = action.name
            if action.name in self.terminate_tools:
                done = True
        else:
            observation = f"Unknown action {action.name}"
            info.source = action.name

        if done:
            reward_res = self.calculate_reward()
            reward = reward_res.reward
            info.reward_info = reward_res
            info.user_cost = self.user.get_total_cost()
        return EnvResponse(observation=observation, reward=reward, done=done, info=info)

    def get_data_hash(self) -> str:
        return consistent_hash(to_hashable(self.data))

    def calculate_reward(self) -> RewardResult:
        from copy import deepcopy
        import os
        
        # CRITICAL FIX: Save current state before corruption
        original_data = deepcopy(self.data)
        data_hash = self.get_data_hash()
        reward = 1.0
        actions = [
            action for action in self.task.actions if action.name != RESPOND_ACTION_NAME
        ]

        # Check if the database changes are correct. If they are not correct, then we set the reward to 0.
        # TODO: cache gt_data_hash in tasks.py (low priority)
        
        # Step-by-step hash comparison for debugging
        debug_hashes = os.environ.get("DEBUG_HASH_COMPARISON", "0") == "1"
        
        if debug_hashes:
            print("\n" + "="*80)
            print("STEP-BY-STEP HASH COMPARISON")
            print("="*80)
            print(f"Initial agent hash after all actions: {data_hash[:32]}...")
            
            # Track agent's actions that modified state
            print("\nAgent's executed actions (non-respond only):")
            agent_tool_actions = [a for a in self.actions if a.name != RESPOND_ACTION_NAME]
            for i, action in enumerate(agent_tool_actions):
                print(f"  {i+1}. {action.name}")
                if hasattr(action, 'kwargs'):
                    print(f"     kwargs: {action.kwargs}")
            
            print("\n" + "-"*40)
            print("Replaying ground truth actions...")
            print("-"*40)
        
        # Use fresh environment for ground truth simulation
        self.data = self.data_load_func()
        
        if debug_hashes:
            fresh_hash = self.get_data_hash()
            print(f"Fresh data hash: {fresh_hash[:32]}...")
        
        # OLD CODE COMMENTED OUT:
        # for action in self.task.actions:
        #     if action.name not in self.terminate_tools:
        #         self.step(action)
        
        # CRITICAL BUG FIX: Save original actions list to avoid pollution
        original_actions = self.actions.copy()
        
        # NEW CODE: Track hash after each ground truth action
        for i, action in enumerate(self.task.actions):
            if action.name not in self.terminate_tools:
                if debug_hashes:
                    print(f"\n{i+1}. Executing GT action: {action.name}")
                    if hasattr(action, 'arguments'):
                        print(f"   arguments: {action.arguments}")
                    elif hasattr(action, 'kwargs'):
                        print(f"   kwargs: {action.kwargs}")
                
                # Execute the action
                self.step(action)
                
                if debug_hashes:
                    current_hash = self.get_data_hash()
                    print(f"   Hash after action: {current_hash[:32]}...")
                    
                    # Check if this action changed the hash
                    if i == 0:
                        prev_hash = fresh_hash
                    else:
                        prev_hash = prev_gt_hashes[-1] if 'prev_gt_hashes' in locals() else fresh_hash
                    
                    if current_hash != prev_hash:
                        print(f"   ✓ Hash changed (state modified)")
                    else:
                        print(f"   - Hash unchanged (read-only or no-op)")
                    
                    # Track hashes for comparison
                    if 'prev_gt_hashes' not in locals():
                        prev_gt_hashes = []
                    prev_gt_hashes.append(current_hash)
        
        gt_data_hash = self.get_data_hash()
        
        if debug_hashes:
            print("\n" + "="*80)
            print("FINAL COMPARISON:")
            print(f"Agent final hash:  {data_hash[:32]}...")
            print(f"GT final hash:     {gt_data_hash[:32]}...")
            print(f"Hashes match:      {data_hash == gt_data_hash}")
            print("="*80 + "\n")
        
        # CRITICAL BUG FIX: Restore original actions list after ground truth replay
        self.actions = original_actions
        
        # CRITICAL FIX: Restore original state to prevent corruption
        self.data = original_data
        info = RewardActionInfo(
            r_actions=data_hash == gt_data_hash, gt_data_hash=gt_data_hash
        )
        if not info.r_actions:
            reward = 0.0

        if len(self.task.outputs) > 0:
            # check outputs
            r_outputs = 1.0
            outputs = {}
            for output in self.task.outputs:
                found = False
                for action in self.actions:
                    if (
                        action.name == RESPOND_ACTION_NAME
                        and output.lower()
                        in action.kwargs["content"].lower().replace(",", "")
                    ):
                        found = True
                        break
                outputs[output] = found
                if not found:
                    r_outputs = 0.0
                    reward = 0.0
            info = RewardOutputInfo(r_outputs=r_outputs, outputs=outputs)
            
        return RewardResult(reward=reward, info=info, actions=actions)
