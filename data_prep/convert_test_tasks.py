#!/usr/bin/env python3
"""
Convert tau_bench test tasks to parquet format for evaluation during training.
This handles retail and airline test sets using the same format as convert_tau_data.py.
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Any

import pandas as pd
from tau_bench.envs.retail.tasks_test import TASKS_TEST as retail_test_tasks
from tau_bench.envs.airline.tasks_test import TASKS as airline_test_tasks

from prompts import create_full_system_prompt, get_all_domains


def serialize_for_parquet(obj: Any) -> str:
    """Serialize complex objects to JSON strings for parquet compatibility."""
    if isinstance(obj, (dict, list)):
        return json.dumps(obj, ensure_ascii=False, default=str)
    return str(obj)


def convert_task_to_skyrl_format(task: Any, domain: str) -> Dict[str, Any]:
    """Convert a single tau_bench task to SkyRL training format (same as convert_tau_data.py)."""
    try:
        # Extract required fields from tau_bench task object
        instruction = task.instruction
        actions = []
        
        # Convert tau_bench Action objects to dictionaries
        for action in task.actions:
            action_dict = {
                "name": action.name,
                "kwargs": action.kwargs
            }
            actions.append(action_dict)
        
        # Validate required fields
        if not domain:
            raise ValueError(f"Task missing domain: {task}")
        if not instruction:
            raise ValueError(f"Task missing instruction: {task}")
        if domain not in get_all_domains():
            raise ValueError(f"Unknown domain: {domain}")
        
        # Create system prompt for domain
        system_prompt = create_full_system_prompt(domain)
        
        # Create SkyRL-compatible format with serialized nested structures (same as train data)
        skyrl_task = {
            "data_source": "tau_bench",
            "prompt": serialize_for_parquet([
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": instruction}
            ]),
            "env_class": "tau_bench",
            "reward_spec": serialize_for_parquet({
                "method": "tau_bench_reward",
                "ground_truth": actions
            }),
            "extra_info": serialize_for_parquet({
                "domain": domain,
                "instruction": instruction,
                "actions": actions,
                "annotator": getattr(task, 'annotator', 'unknown'),
                "user_id": getattr(task, 'user_id', 'unknown'),
                "complexity": getattr(task, 'complexity', 1),
                "generated_at": "test_data",
                "task_type": "test"  # Mark as test task
            })
        }
        
        return skyrl_task
    except Exception as e:
        print(f"Error converting task: {e}")
        return None


def convert_test_tasks(output_dir: str):
    """Convert test tasks to parquet files using the same format as training data."""
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Convert retail test tasks
    print(f"Converting {len(retail_test_tasks)} retail test tasks...")
    retail_data = []
    for task in retail_test_tasks:
        skyrl_task = convert_task_to_skyrl_format(task, "retail")
        if skyrl_task:
            retail_data.append(skyrl_task)
    
    if retail_data:
        retail_df = pd.DataFrame(retail_data)
        retail_output = output_path / "retail_test.parquet"
        retail_df.to_parquet(retail_output, index=False)
        print(f"Saved retail test set to {retail_output}")
    
    # Convert airline test tasks
    print(f"Converting {len(airline_test_tasks)} airline test tasks...")
    airline_data = []
    for task in airline_test_tasks:
        skyrl_task = convert_task_to_skyrl_format(task, "airline")
        if skyrl_task:
            airline_data.append(skyrl_task)
    
    if airline_data:
        airline_df = pd.DataFrame(airline_data)
        airline_output = output_path / "airline_test.parquet"
        airline_df.to_parquet(airline_output, index=False)
        print(f"Saved airline test set to {airline_output}")
    
    # Create combined test set
    print("Creating combined test set...")
    combined_data = retail_data + airline_data
    if combined_data:
        combined_df = pd.DataFrame(combined_data)
        combined_output = output_path / "combined_test.parquet"
        combined_df.to_parquet(combined_output, index=False)
        print(f"Saved combined test set to {combined_output}")
    
    # Print statistics
    print("\nTest Set Statistics:")
    print(f"  Retail: {len(retail_data)} tasks")
    print(f"  Airline: {len(airline_data)} tasks")
    print(f"  Combined: {len(combined_data)} tasks")
    
    # Print file sizes
    for file in [retail_output, airline_output, combined_output]:
        if file.exists():
            size_kb = file.stat().st_size / 1024
            print(f"  {file.name}: {size_kb:.1f} KB")


def main():
    parser = argparse.ArgumentParser(description="Convert tau_bench test tasks to parquet format")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="training/data/tau_bench_test",
        help="Output directory for parquet files"
    )
    
    args = parser.parse_args()
    convert_test_tasks(args.output_dir)


if __name__ == "__main__":
    main()