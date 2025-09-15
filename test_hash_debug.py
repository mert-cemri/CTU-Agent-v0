#!/usr/bin/env python3
"""
Test script to debug hash comparison in tau_bench reward calculation.
Set DEBUG_HASH_COMPARISON=1 to see step-by-step hash tracking.
"""

import os
import sys

# Enable hash debugging
os.environ["DEBUG_HASH_COMPARISON"] = "1"

# Set OpenAI API key if available
if "OPENAI_API_KEY" in os.environ:
    import litellm
    litellm.api_key = os.environ.get("OPENAI_API_KEY")

# Add the project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tau_bench.envs import get_env
from tau_bench.tau_types import Action

def test_retail_exchange():
    """Test a retail exchange scenario to debug hash comparison."""
    
    # Create retail environment with proper parameters
    env = get_env(
        "retail", 
        user_strategy="llm", 
        user_model="gpt-4o",
        user_provider="openai",  # Add the provider
        task_split="test",
        task_index=0  # Use first task
    )
    
    # Use the first task (exchange task)
    task = env.tasks[0]
    env.task = task
    
    # Reset environment
    env.reset(task_index=0)
    
    # Simulate agent actions (similar to the problematic conversation)
    # These are the actions the agent actually took
    agent_actions = [
        Action(name="find_user_id_by_name_zip", 
               kwargs={"first_name": "Yusuf", "last_name": "Rossi", "zip": "19122"}),
        Action(name="get_user_details", 
               kwargs={"user_id": "yusuf_rossi_9620"}),
        Action(name="get_order_details", 
               kwargs={"order_id": "#W2378156"}),
        Action(name="get_product_details", 
               kwargs={"product_id": "1656367028"}),
        Action(name="get_product_details", 
               kwargs={"product_id": "4896585277"}),
        Action(name="exchange_delivered_order_items",
               kwargs={
                   "order_id": "#W2378156",
                   "item_ids": ["1151293680", "4983901480"],
                   "new_item_ids": ["7706410293", "7747408585"],
                   "payment_method_id": "credit_card_9513926"
               })
    ]
    
    print("Testing agent actions vs ground truth...")
    print(f"Ground truth has {len([a for a in task.actions if a.name != 'respond'])} tool actions")
    print(f"Agent executed {len(agent_actions)} tool actions")
    
    # Execute agent actions
    for action in agent_actions:
        result = env.step(action)
        print(f"Executed: {action.name} -> {result.observation[:50]}...")
    
    # Calculate reward (this will trigger our debug output)
    reward_result = env.calculate_reward()
    
    print(f"\n{'='*60}")
    print(f"REWARD RESULT: {reward_result.reward}")
    print(f"Actions match: {reward_result.info.r_actions}")
    print(f"{'='*60}")

if __name__ == "__main__":
    test_retail_exchange()