#!/usr/bin/env python3
"""
Simple and clean testing script for evaluating models on tau_bench tasks using VLLM.
"""

import os
import sys
import json
import argparse
import importlib.util
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from vllm import LLM, SamplingParams
from tau_bench.envs import get_env
from tau_bench.agents import ToolCallingAgent
from tau_bench.tau_types import Task, EnvRunResult, Action, RunConfig


class ModelTester:
    """Simple tester for tau_bench tasks using VLLM."""
    
    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-8B",
        domain: str = "retail",
        user_model: str = "gpt-4o",
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ):
        """Initialize the tester."""
        self.model_name = model_name
        self.domain = domain
        self.user_model = user_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        print(f"Initializing VLLM with model: {model_name}")
        self.llm = LLM(
            model=model_name,
            tensor_parallel_size=1,
            gpu_memory_utilization=0.8,
            trust_remote_code=True,
            max_model_len=8192,
        )
        
        self.sampling_params = SamplingParams(
            temperature=temperature,
            max_tokens=max_tokens,
            stop=["</s>", "<|im_end|>", "<|endoftext|>"],
        )
    
    def load_tasks(self) -> List[Task]:
        """Load tasks for the specified domain."""
        module_path = Path(__file__).parent / "envs" / self.domain / "tasks_train.py"
        if not module_path.exists():
            raise FileNotFoundError(f"Tasks file not found: {module_path}")
        
        spec = importlib.util.spec_from_file_location("tasks_module", module_path)
        tasks_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tasks_module)
        
        return tasks_module.TASKS_TRAIN
    
    def evaluate_task(self, task_idx: int) -> Dict[str, Any]:
        """Evaluate a single task."""
        # Get environment
        env = get_env(
            env_name=self.domain,
            user_strategy="llm",
            user_model=self.user_model,
            task_split="train",
            user_provider="openai",
            task_index=task_idx,
        )
        
        # Create a simple agent wrapper for VLLM
        class VLLMAgent:
            def __init__(self, llm, sampling_params):
                self.llm = llm
                self.sampling_params = sampling_params

            def generate(self, prompt: str) -> str:
                """Generate response using VLLM."""
                outputs = self.llm.generate([prompt], self.sampling_params)
                return outputs[0].outputs[0].text.strip()

        agent = VLLMAgent(self.llm, self.sampling_params)

        # Reset environment (task_index already set in get_env)
        reset_response = env.reset()
        obs = reset_response.observation
        info = reset_response.info

        # Get the task from the environment info
        task = info.task
        
        # Run conversation
        conversation = []
        done = False
        turns = 0
        max_turns = 10
        
        # Initial observation
        conversation.append({"role": "user", "content": obs})
        
        while not done and turns < max_turns:
            # Format prompt for the model
            prompt = self._format_prompt(conversation, env.tools_info)
            
            # Generate response
            response = agent.generate(prompt)
            conversation.append({"role": "assistant", "content": response})
            
            # Parse and execute action
            try:
                # Simple action parsing - look for tool calls
                action = self._parse_action(response)
                
                if action:
                    # Convert dict to Action object if needed
                    if isinstance(action, dict):
                        action = Action(name=action["name"], kwargs=action.get("kwargs", {}))

                    # Execute action in environment
                    step_response = env.step(action)
                    obs = step_response.observation
                    reward = step_response.reward
                    done = step_response.done
                    info = step_response.info

                    if obs and not done:
                        conversation.append({"role": "tool", "content": obs})
                else:
                    # No action found, try to continue
                    respond_action = Action(name="respond", kwargs={"content": response})
                    step_response = env.step(respond_action)
                    obs = step_response.observation
                    reward = step_response.reward
                    done = step_response.done
                    info = step_response.info
            except Exception as e:
                print(f"Error in turn {turns}: {e}")
                done = True
                reward = 0
                info = {"error": str(e)}
            
            turns += 1
        
        # Get final reward
        final_reward = reward
        
        return {
            "task_id": task_idx,
            "domain": self.domain,
            "instruction": task.instruction,
            "ground_truth_actions": [action.model_dump() for action in task.actions],
            "conversation": conversation,
            "reward": final_reward,
            "success": final_reward > 0,
            "turns": turns,
            "timestamp": datetime.now().isoformat(),
        }
    
    def _format_prompt(self, conversation: List[Dict], tools_info: List[Dict]) -> str:
        """Format conversation into a prompt."""
        # Convert tools_info list to string format
        tools_str = ""
        if tools_info:
            tools_str = "Available tools:\n"
            for tool in tools_info:
                tools_str += f"- {tool.get('name', 'unknown')}: {tool.get('description', '')}\n"

        prompt = f"You are a helpful assistant. {tools_str}\n"
        
        for msg in conversation:
            role = msg["role"]
            content = msg["content"]
            
            if role == "user":
                prompt += f"User: {content}\n"
            elif role == "assistant":
                prompt += f"Assistant: {content}\n"
            elif role == "tool":
                prompt += f"Tool Output: {content}\n"
        
        prompt += "Assistant: "
        return prompt
    
    def _parse_action(self, response: str) -> Optional[Dict[str, Any]]:
        """Parse action from model response."""
        # Simple parsing - look for JSON-like structure
        # This should be improved based on your model's output format
        
        import re
        
        # Look for tool calls in various formats
        patterns = [
            r'```json\s*({.*?})\s*```',  # JSON code block
            r'<tool>(.*?)</tool>',        # XML tags
            r'Action:\s*({.*?})',          # Action prefix
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response, re.DOTALL)
            if match:
                try:
                    action_str = match.group(1)
                    action = json.loads(action_str)
                    return action
                except:
                    continue
        
        # Try to extract function calls
        func_pattern = r'(\w+)\((.*?)\)'
        match = re.search(func_pattern, response)
        if match:
            func_name = match.group(1)
            args_str = match.group(2)
            
            # Simple argument parsing
            kwargs = {}
            if args_str:
                # Split by comma and parse key=value pairs
                for arg in args_str.split(','):
                    if '=' in arg:
                        key, value = arg.split('=', 1)
                        key = key.strip().strip('"').strip("'")
                        value = value.strip().strip('"').strip("'")
                        kwargs[key] = value
            
            return {"name": func_name, "kwargs": kwargs}
        
        return None
    
    def run_evaluation(
        self,
        num_tasks: Optional[int] = None,
        start_idx: int = 0,
    ) -> List[Dict[str, Any]]:
        """Run evaluation on multiple tasks."""
        tasks = self.load_tasks()
        
        # Limit tasks if specified
        if num_tasks:
            task_indices = list(range(start_idx, min(start_idx + num_tasks, len(tasks))))
        else:
            task_indices = list(range(start_idx, len(tasks)))
        
        results = []
        for idx in task_indices:
            print(f"\n{'='*60}")
            print(f"Evaluating task {idx}/{len(tasks)}")
            print(f"{'='*60}")
            
            try:
                result = self.evaluate_task(idx)
                results.append(result)
                
                print(f"Result: Reward = {result['reward']:.2f}, Success = {result['success']}")
                print(f"Turns used: {result['turns']}")
            except Exception as e:
                print(f"Error evaluating task {idx}: {e}")
                import traceback
                traceback.print_exc()
        
        return results
    
    def save_results(self, results: List[Dict[str, Any]]) -> str:
        """Save results to JSONL file."""
        # Create results directory
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = results_dir / f"{self.domain}_{timestamp}.jsonl"
        
        # Save results
        with open(filename, "w") as f:
            for result in results:
                f.write(json.dumps(result) + "\n")
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"EVALUATION SUMMARY")
        print(f"{'='*60}")
        print(f"Results saved to: {filename}")
        
        if results:
            total = len(results)
            successful = sum(1 for r in results if r["success"])
            avg_reward = sum(r["reward"] for r in results) / total
            
            print(f"\nMetrics:")
            print(f"  Total tasks: {total}")
            print(f"  Successful: {successful} ({successful/total*100:.1f}%)")
            print(f"  Average reward: {avg_reward:.3f}")
            
            # Per-task breakdown
            print(f"\nPer-task results:")
            for r in results:
                status = "✓" if r["success"] else "✗"
                print(f"  Task {r['task_id']}: {status} (reward: {r['reward']:.2f})")
        
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
        help="Model to use (default: Qwen/Qwen3-8B)",
    )
    parser.add_argument(
        "--user-model",
        type=str,
        default="gpt-4o",
        help="User model for simulation (default: gpt-4o)",
    )
    parser.add_argument(
        "--num-tasks",
        type=int,
        default=5,
        help="Number of tasks to evaluate (default: 5)",
    )
    parser.add_argument(
        "--start-idx",
        type=int,
        default=0,
        help="Starting task index (default: 0)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Temperature for sampling (default: 0.7)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        help="Maximum tokens to generate (default: 2048)",
    )
    
    args = parser.parse_args()
    
    print(f"Testing Configuration:")
    print(f"  Domain: {args.domain}")
    print(f"  Model: {args.model}")
    print(f"  User Model: {args.user_model}")
    print(f"  Tasks: {args.num_tasks} starting from index {args.start_idx}")
    print(f"  Temperature: {args.temperature}")
    print()
    
    # Create tester
    tester = ModelTester(
        model_name=args.model,
        domain=args.domain,
        user_model=args.user_model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    
    # Run evaluation
    results = tester.run_evaluation(
        num_tasks=args.num_tasks,
        start_idx=args.start_idx,
    )
    
    # Save results
    if results:
        tester.save_results(results)


if __name__ == "__main__":
    main()