# Copyright Sierra

import json
from typing import List
from tau_bench.types import Task, Action


def load_custom_dataset(dataset_path: str) -> List[Task]:
    """Load tasks from custom JSON dataset format"""
    with open(dataset_path, 'r') as f:
        data = json.load(f)
    
    tasks = []
    for task_data in data.get('tasks', []):
        # Convert actions from the new format to Action objects
        actions = []
        for action_data in task_data.get('actions', []):
            action = Action(
                name=action_data['name'],
                kwargs=action_data.get('kwargs', {})
            )
            actions.append(action)
        
        # Create Task object with the new format
        task = Task(
            user_id=task_data['user_id'],
            instruction=task_data['instruction'],
            actions=actions,
            domain=task_data.get('domain'),
            annotator=task_data.get('annotator'),
            complexity=task_data.get('complexity'),
            generated_at=task_data.get('generated_at'),
            outputs=task_data.get('outputs', [])
        )
        tasks.append(task)
    
    return tasks


def filter_tasks_by_domain(tasks: List[Task], domain: str) -> List[Task]:
    """Filter tasks by domain"""
    return [task for task in tasks if task.domain == domain] 