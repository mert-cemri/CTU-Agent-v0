#!/usr/bin/env python3
"""
Clean testing script for evaluating models on tau_bench tasks using VLLM.
"""

import os
import sys
import json
import argparse
import importlib.util
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict

# Add tau_bench to path
sys.path.append(str(Path(__file__).parent.parent))

from vllm import LLM, SamplingParams
from tau_bench_new.tau_types import Task, Action
from tau_bench_new.envs.base import Env


@dataclass
class TaskResult:
    """Result for a single task evaluation."""
    task_id: int
    domain: str
    instruction: str
    ground_truth_actions: List[Dict[str, Any]]
    conversation: List[Dict[str, Any]]
    reward: float
    success: bool
    timestamp: str


class TauBenchTester:
    """Clean tester for tau_bench tasks using VLLM."""
    
    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-8B",
        user_model: str = "gpt-4o",
        temperature: float = 0.7,
        max_turns: int = 10,
    ):
        """Initialize the tester with VLLM model."""
        print(f"Loading model: {model_name}")
        self.model_name = model_name
        self.user_model = user_model
        self.temperature = temperature
        self.max_turns = max_turns
        
        # Initialize VLLM
        self.llm = LLM(
            model=model_name,
            tensor_parallel_size=1,
            gpu_memory_utilization=0.8,
            trust_remote_code=True,
        )
        self.sampling_params = SamplingParams(
            temperature=temperature,
            max_tokens=2048,
        )
        
    def load_tasks(self, domain: str) -> List[Task]:
        """Load tasks from a specific domain."""
        # Import the tasks module dynamically
        module_path = Path(__file__).parent / "envs" / domain / "tasks_train.py"
        if not module_path.exists():
            raise FileNotFoundError(f"Tasks file not found: {module_path}")
        
        spec = importlib.util.spec_from_file_location("tasks_module", module_path)
        tasks_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tasks_module)
        
        tasks = tasks_module.TASKS_TRAIN
        print(f"Loaded {len(tasks)} tasks from {domain}")
        return tasks
    
    def create_environment(self, domain: str) -> Env:
        """Create environment for a specific domain."""
        # Import the environment module dynamically
        module_path = Path(__file__).parent / "envs" / domain / "__init__.py"
        spec = importlib.util.spec_from_file_location("env_module", module_path)
        env_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(env_module)
        
        # Get the environment class (usually named after the domain)
        env_class_name = f"{domain.capitalize()}BashEnv"
        if hasattr(env_module, env_class_name):
            env_class = getattr(env_module, env_class_name)
        else:
            # Try alternative naming
            for attr_name in dir(env_module):
                if "env" in attr_name.lower() and not attr_name.startswith("_"):
                    env_class = getattr(env_module, attr_name)
                    break
            else:
                raise ValueError(f"Could not find environment class in {domain}")
        
        return env_class(user_model=self.user_model, user_strategy="llm")
    
    def format_prompt(self, instruction: str, conversation: List[Dict], tools: List[Dict]) -> str:
        """Format prompt for VLLM model."""
        # Build conversation history
        messages = [
            {"role": "system", "content": "You are a helpful assistant that can use tools to help users."},
            {"role": "user", "content": instruction}
        ]
        
        # Add conversation history
        for msg in conversation:
            messages.append(msg)
        
        # For now, use a simple format. You may need to adjust based on model
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            prompt += f"{role.upper()}: {content}\n"
        
        # Add available tools information
        if tools:
            prompt += "\nAvailable tools:\n"
            for tool in tools:
                prompt += f"- {tool['name']}: {tool.get('description', '')}\n"
        
        prompt += "\nASSISTANT: "
        return prompt
    
    def evaluate_task(self, task: Task, env: Env, task_id: int, domain: str) -> TaskResult:
        """Evaluate a single task."""
        print(f"\nEvaluating task {task_id}: {task.instruction[:100]}...")
        
        # Reset environment with task
        obs, info = env.reset(task=task)
        
        conversation = []
        done = False
        turn = 0
        
        while not done and turn < self.max_turns:
            # Format prompt for model
            prompt = self.format_prompt(
                task.instruction,
                conversation,
                env.tools if hasattr(env, 'tools') else []
            )
            
            # Generate response
            outputs = self.llm.generate([prompt], self.sampling_params)
            response = outputs[0].outputs[0].text.strip()
            
            # Add to conversation
            conversation.append({"role": "assistant", "content": response})
            
            # Step environment (simplified - you'll need proper action parsing)
            # This is a placeholder - you need to parse the response into actions
            try:
                # Simple parsing - look for tool calls in response
                # This needs to be improved based on your model's output format
                obs, reward, done, info = env.step(response)
                
                if obs:
                    conversation.append({"role": "tool", "content": obs})
            except Exception as e:
                print(f"Error stepping environment: {e}")
                done = True
                reward = 0
            
            turn += 1
        
        # Get final reward
        final_reward = info.get("reward", 0) if info else 0
        
        return TaskResult(
            task_id=task_id,
            domain=domain,
            instruction=task.instruction,
            ground_truth_actions=[action.dict() for action in task.actions],
            conversation=conversation,
            reward=final_reward,
            success=final_reward > 0,
            timestamp=datetime.now().isoformat(),
        )
    
    def run_evaluation(
        self,
        domain: str,
        num_tasks: Optional[int] = None,
        start_idx: int = 0,
    ) -> List[TaskResult]:
        """Run evaluation on tasks from a domain."""
        # Load tasks
        tasks = self.load_tasks(domain)
        
        # Limit number of tasks if specified
        if num_tasks:
            tasks = tasks[start_idx:start_idx + num_tasks]
        else:
            tasks = tasks[start_idx:]
        
        # Create environment
        env = self.create_environment(domain)
        
        # Evaluate each task
        results = []
        for idx, task in enumerate(tasks, start=start_idx):
            try:
                result = self.evaluate_task(task, env, idx, domain)
                results.append(result)
                print(f"Task {idx}: Reward = {result.reward}, Success = {result.success}")
            except Exception as e:
                print(f"Error evaluating task {idx}: {e}")
                continue
        
        return results
    
    def save_results(self, results: List[TaskResult], domain: str) -> str:
        """Save results to JSONL file."""
        # Create results directory
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = results_dir / f"{domain}_{timestamp}.jsonl"
        
        # Save results
        with open(filename, "w") as f:
            for result in results:
                f.write(json.dumps(asdict(result)) + "\n")
        
        print(f"\nResults saved to: {filename}")
        
        # Print summary
        total = len(results)
        successful = sum(1 for r in results if r.success)
        avg_reward = sum(r.reward for r in results) / total if total > 0 else 0
        
        print(f"\nSummary:")
        print(f"  Total tasks: {total}")
        print(f"  Successful: {successful} ({successful/total*100:.1f}%)")
        print(f"  Average reward: {avg_reward:.3f}")
        
        return str(filename)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Test VLLM models on tau_bench tasks")
    parser.add_argument(
        "--domain",
        type=str,
        required=True,
        choices=["airline", "retail", "doordash", "healthcare", "telecom"],
        help="Domain to test on",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-8B",
        help="Model to use for evaluation",
    )
    parser.add_argument(
        "--user-model",
        type=str,
        default="gpt-4o",
        help="User model for simulation",
    )
    parser.add_argument(
        "--num-tasks",
        type=int,
        default=None,
        help="Number of tasks to evaluate (default: all)",
    )
    parser.add_argument(
        "--start-idx",
        type=int,
        default=0,
        help="Starting task index",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Temperature for sampling",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=10,
        help="Maximum turns per task",
    )
    
    args = parser.parse_args()
    
    # Create tester
    tester = TauBenchTester(
        model_name=args.model,
        user_model=args.user_model,
        temperature=args.temperature,
        max_turns=args.max_turns,
    )
    
    # Run evaluation
    results = tester.run_evaluation(
        domain=args.domain,
        num_tasks=args.num_tasks,
        start_idx=args.start_idx,
    )
    
    # Save results
    if results:
        tester.save_results(results, args.domain)


if __name__ == "__main__":
    main()