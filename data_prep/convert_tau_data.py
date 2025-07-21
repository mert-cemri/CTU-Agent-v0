# Copyright Sierra

import json
import pandas as pd
import argparse
import os
from typing import Dict, List, Any
from sklearn.model_selection import train_test_split

from .prompts import create_full_system_prompt, get_all_domains


def serialize_for_parquet(obj: Any) -> str:
    """Serialize complex objects to JSON strings for parquet compatibility."""
    if isinstance(obj, (dict, list)):
        return json.dumps(obj, ensure_ascii=False, default=str)
    return str(obj)


def load_tau_bench_data(path: str) -> List[Dict[str, Any]]:
    """Load data from a JSON file or a Python module."""
    print(f"Loading tau_bench data from: {path}")
    if path.endswith(".json"):
        with open(path, "r") as f:
            data = json.load(f)
    elif path.endswith(".py"):
        import importlib.util
        import sys
        
        module_name = "tau_bench.temp_tasks"
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None:
            raise ImportError(f"Could not load spec for module at {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        if not hasattr(module, "TASKS_TRAIN"):
            raise ValueError(f"Python module at {path} must define a 'TASKS_TRAIN' variable")
            
        # Convert Task objects to dictionaries and add domain
        tasks = getattr(module, "TASKS_TRAIN")
        data = []
        for task in tasks:
            task_dict = task.model_dump()
            if 'domain' not in task_dict or not task_dict['domain']:
                task_dict['domain'] = 'retail' # Add domain if missing
            data.append(task_dict)
    else:
        raise ValueError(f"Unsupported file type: {path}. Must be .json or .py")
        
    return data


def convert_task_to_skyrl_format(task: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a single tau_bench task to SkyRL training format."""
    try:
        # Extract required fields
        domain = task.get('domain')
        instruction = task.get('instruction')
        actions = task.get('actions', [])
        
        # Validate required fields
        if not domain:
            raise ValueError(f"Task missing domain: {task}")
        if not instruction:
            raise ValueError(f"Task missing instruction: {task}")
        if domain not in get_all_domains():
            raise ValueError(f"Unknown domain: {domain}")
        
        # Create system prompt for domain
        system_prompt = create_full_system_prompt(domain)
        
        # Create SkyRL-compatible format with serialized nested structures
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
                "annotator": task.get('annotator', 'unknown'),
                "user_id": task.get('user_id', 'unknown'),
                "complexity": task.get('complexity', 1),
                "generated_at": task.get('generated_at', 'unknown')
            })
        }
        
        return skyrl_task
    except Exception as e:
        print(f"Error converting task: {e}")
        return None


def filter_and_validate_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter and validate tau_bench tasks."""
    valid_tasks = []
    domain_counts = {}
    
    for i, task in enumerate(tasks):
        try:
            # Check if task has required fields
            if not task.get('domain') or not task.get('instruction'):
                print(f"Skipping task {i}: missing domain or instruction")
                continue
            
            # Check if domain is supported
            domain = task['domain']
            if domain not in get_all_domains():
                print(f"Skipping task {i}: unsupported domain '{domain}'")
                continue
            
            # Check if actions exist and are valid
            actions = task.get('actions', [])
            if not actions:
                print(f"Skipping task {i}: no actions provided")
                continue
            
            # Count tasks per domain
            domain_counts[domain] = domain_counts.get(domain, 0) + 1
            valid_tasks.append(task)
            
        except Exception as e:
            print(f"Error processing task {i}: {e}")
            continue
    
    print(f"Valid tasks: {len(valid_tasks)}")
    print("Tasks per domain:")
    for domain, count in domain_counts.items():
        print(f"  {domain}: {count}")
    
    return valid_tasks


def convert_tau_bench_data(
    tasks: List[Dict[str, Any]], 
    output_dir: str, 
    train_ratio: float = 0.9,
    max_tasks_per_domain: int = None,
    random_state: int = 42
) -> None:
    """
    Convert tau_bench training data to SkyRL format.
    
    Args:
        input_path: Path to tau_bench novel_sft_dataset.json or a Python file defining TASKS_TRAIN
        output_dir: Directory to save converted parquet files
        train_ratio: Ratio of data to use for training (rest for validation)
        max_tasks_per_domain: Maximum tasks per domain (for testing)
        random_state: Random seed for reproducibility
    """
    # Filter and validate tasks
    valid_tasks = filter_and_validate_tasks(tasks)
    
    if not valid_tasks:
        raise ValueError("No valid tasks found in data")
    
    # Limit tasks per domain if specified (for testing)
    if max_tasks_per_domain:
        domain_tasks = {}
        for task in valid_tasks:
            domain = task['domain']
            if domain not in domain_tasks:
                domain_tasks[domain] = []
            if len(domain_tasks[domain]) < max_tasks_per_domain:
                domain_tasks[domain].append(task)
        
        # Flatten back to list
        valid_tasks = []
        for domain_task_list in domain_tasks.values():
            valid_tasks.extend(domain_task_list)
        
        print(f"Limited to {len(valid_tasks)} tasks ({max_tasks_per_domain} per domain)")
    
    # Convert to SkyRL format
    print("Converting to SkyRL format...")
    converted_tasks = []
    for task in valid_tasks:
        try:
            skyrl_task = convert_task_to_skyrl_format(task)
            if skyrl_task:
                converted_tasks.append(skyrl_task)
        except Exception as e:
            print(f"Skipping task due to conversion error: {e}")
    
    if not converted_tasks:
        raise ValueError("No tasks successfully converted")
    
    print(f"Successfully converted {len(converted_tasks)} tasks")
    
    # Extract domains for stratification (deserialize the extra_info)
    domains = []
    for task in converted_tasks:
        extra_info = json.loads(task['extra_info'])
        domains.append(extra_info['domain'])
    
    # Split into train and validation
    train_tasks, val_tasks = train_test_split(
        converted_tasks, 
        train_size=train_ratio, 
        random_state=random_state,
        stratify=domains
    )
    
    print(f"Split: {len(train_tasks)} train, {len(val_tasks)} validation")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Save as parquet files
    train_df = pd.DataFrame(train_tasks)
    val_df = pd.DataFrame(val_tasks)
    
    train_path = os.path.join(output_dir, "train.parquet")
    val_path = os.path.join(output_dir, "validation.parquet")
    
    train_df.to_parquet(train_path, index=False)
    val_df.to_parquet(val_path, index=False)
    
    print(f"Saved training data to: {train_path}")
    print(f"Saved validation data to: {val_path}")
    
    # Print statistics
    print("\nDataset statistics:")
    print(f"Total tasks: {len(converted_tasks)}")
    print(f"Train tasks: {len(train_tasks)}")
    print(f"Validation tasks: {len(val_tasks)}")
    
    # Domain distribution
    train_domains = {}
    val_domains = {}
    
    for task in train_tasks:
        extra_info = json.loads(task['extra_info'])
        domain = extra_info['domain']
        train_domains[domain] = train_domains.get(domain, 0) + 1
    
    for task in val_tasks:
        extra_info = json.loads(task['extra_info'])
        domain = extra_info['domain']
        val_domains[domain] = val_domains.get(domain, 0) + 1
    
    print("\nTrain domain distribution:")
    for domain, count in train_domains.items():
        print(f"  {domain}: {count}")
    
    print("\nValidation domain distribution:")
    for domain, count in val_domains.items():
        print(f"  {domain}: {count}")


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Convert tau_bench data to SkyRL format")
    parser.add_argument("--input_path", required=True, help="Path to tau_bench data file (.json or .py)")
    parser.add_argument("--output_dir", required=True, help="Output directory for parquet files")
    parser.add_argument("--train_ratio", type=float, default=0.9, help="Training data ratio")
    parser.add_argument("--max_tasks_per_domain", type=int, help="Max tasks per domain (for testing)")
    parser.add_argument("--random_state", type=int, default=42, help="Random seed")
    
    args = parser.parse_args()
    
    # Load data based on file type
    tasks = load_tau_bench_data(args.input_path)
    if isinstance(tasks, dict) and 'tasks' in tasks:
        tasks = tasks['tasks'] # Handle original JSON structure
        
    convert_tau_bench_data(
        tasks=tasks,
        output_dir=args.output_dir,
        train_ratio=args.train_ratio,
        max_tasks_per_domain=args.max_tasks_per_domain,
        random_state=args.random_state
    )


if __name__ == "__main__":
    main()