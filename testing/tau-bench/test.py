#!/usr/bin/env python3
"""Unified tau-bench testing script - replaces run.py, run_vllm.py, and test_qwen.py"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Import tau_bench modules
from tau_bench.envs import get_env
from tau_bench.types import EnvRunResult, RunConfig
from tau_bench.agents.vllm_agent import VLLMAgent
from tau_bench.agents.qwen_vllm_agent import QwenVLLMAgent
from tau_bench.run import agent_factory


class TauBenchTester:
    """Unified tester for tau-bench evaluation"""
    
    def __init__(self, args):
        self.args = args
        self.results = []
        self.setup_output_dir()
        
    def setup_output_dir(self):
        """Create output directory structure"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create organized output structure
        if self.args.output_dir:
            self.output_dir = Path(self.args.output_dir)
        else:
            self.output_dir = Path("results") / f"{self.args.env}_{timestamp}"
            
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        (self.output_dir / "conversations").mkdir(exist_ok=True)
        (self.output_dir / "summary").mkdir(exist_ok=True)
        
    def get_agent(self, env):
        """Get appropriate agent based on mode"""
        if self.args.mode == "vllm":
            # Use VLLM agent with OpenAI-compatible API
            if "qwen" in self.args.model.lower():
                return QwenVLLMAgent(
                    tools_info=env.tools_info,
                    wiki=env.wiki,
                    model=self.args.model,
                    base_url=self.args.base_url,
                    temperature=self.args.temperature
                )
            else:
                return VLLMAgent(
                    tools_info=env.tools_info,
                    wiki=env.wiki,
                    model=self.args.model,
                    base_url=self.args.base_url,
                    temperature=self.args.temperature
                )
        else:
            # Use standard tau-bench agent factory
            config = RunConfig(
                agent_strategy=self.args.agent_strategy,
                model=self.args.model,
                model_provider=self.args.model_provider,
                temperature=self.args.temperature,
                env=self.args.env,
                user_strategy=self.args.user_strategy,
                user_model=self.args.user_model,
                user_model_provider=self.args.user_provider
            )
            return agent_factory(
                tools_info=env.tools_info,
                wiki=env.wiki,
                config=config
            )
    
    def run_single_task(self, task_id: int) -> Dict:
        """Run a single task and return results in the specified format"""
        print(f"\n{'='*50}")
        print(f"Testing Task {task_id} ({self.args.env})")
        print('='*50)
        
        # Ensure API keys are available in worker threads  
        import os
        import litellm
        
        # Set API key explicitly for litellm in worker threads
        if os.environ.get("OPENAI_API_KEY"):
            litellm.api_key = os.environ.get("OPENAI_API_KEY")
        
        # Create environment for this task
        env = get_env(
            self.args.env,
            user_strategy=self.args.user_strategy,
            user_model=self.args.user_model,
            user_provider=self.args.user_provider,
            task_split="test",
            task_index=task_id
        )
        
        # Get agent
        agent = self.get_agent(env)
        
        try:
            # Run the task
            result = agent.solve(env=env, task_index=task_id)
            
            # Format result according to specification
            formatted_result = {
                "task_id": task_id,
                "reward": result.reward,
                "info": {
                    "task": env.tasks[task_id] if task_id < len(env.tasks) else {},
                    "source": "user",
                    "user_cost": getattr(result, 'cost', 0.0),
                    "reward_info": {
                        "reward": result.reward,
                        "info": getattr(result, 'info', {}),
                        "actions": getattr(result, 'actions', [])
                    }
                },
                "traj": result.messages,  # Full conversation trajectory
                "trial": self.args.trial
            }
            
            # Print summary
            success = "✅" if result.reward > 0.9 else "❌"
            print(f"{success} Task {task_id}: Reward = {result.reward:.2f}")
            
            # Count turns
            turns = len([m for m in result.messages if m.get('role') in ['user', 'assistant']])
            print(f"   Turns: {turns}")
            
            # Show tool usage
            tool_calls = [m for m in result.messages if 'tool_calls' in m]
            if tool_calls:
                print(f"   Tools used: {len(tool_calls)}")
                for tc in tool_calls[:3]:  # Show first 3
                    if tc.get('tool_calls'):
                        tool_name = tc['tool_calls'][0]['function']['name']
                        print(f"     - {tool_name}")
            
            return formatted_result
            
        except Exception as e:
            print(f"❌ Task {task_id} failed with error: {e}")
            return {
                "task_id": task_id,
                "reward": 0.0,
                "info": {
                    "error": str(e),
                    "source": "error"
                },
                "traj": [],
                "trial": self.args.trial
            }
    
    def run_parallel(self, task_ids: List[int]) -> List[Dict]:
        """Run multiple tasks in parallel"""
        results = []
        
        with ThreadPoolExecutor(max_workers=self.args.max_concurrency) as executor:
            # Submit all tasks
            future_to_task = {
                executor.submit(self.run_single_task, task_id): task_id 
                for task_id in task_ids
            }
            
            # Process completed tasks with progress bar
            with tqdm(total=len(task_ids), desc=f"Running {self.args.env} tasks") as pbar:
                for future in as_completed(future_to_task):
                    task_id = future_to_task[future]
                    try:
                        result = future.result()
                        results.append(result)
                        pbar.update(1)
                    except Exception as e:
                        print(f"Task {task_id} exception: {e}")
                        results.append({
                            "task_id": task_id,
                            "reward": 0.0,
                            "info": {"error": str(e)},
                            "traj": [],
                            "trial": self.args.trial
                        })
                        pbar.update(1)
        
        # Sort results by task_id
        results.sort(key=lambda x: x['task_id'])
        return results
    
    def save_results(self, results: List[Dict]):
        """Save results to JSON files"""
        # Save full results with conversations
        full_results_file = self.output_dir / f"{self.args.env}_full_results.json"
        with open(full_results_file, 'w') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n📁 Full results saved to: {full_results_file}")
        
        # Save individual conversations for easier inspection
        for result in results:
            task_file = self.output_dir / "conversations" / f"task_{result['task_id']:03d}.json"
            with open(task_file, 'w') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
        
        # Create summary report
        summary = {
            "timestamp": datetime.now().isoformat(),
            "environment": self.args.env,
            "model": self.args.model,
            "mode": self.args.mode,
            "total_tasks": len(results),
            "successful_tasks": sum(1 for r in results if r['reward'] > 0.9),
            "success_rate": sum(1 for r in results if r['reward'] > 0.9) / len(results) if results else 0,
            "average_reward": sum(r['reward'] for r in results) / len(results) if results else 0,
            "task_rewards": {r['task_id']: r['reward'] for r in results}
        }
        
        summary_file = self.output_dir / "summary" / "evaluation_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Print summary
        print("\n" + "="*60)
        print("EVALUATION SUMMARY")
        print("="*60)
        print(f"Environment: {self.args.env}")
        print(f"Model: {self.args.model}")
        print(f"Total Tasks: {summary['total_tasks']}")
        print(f"Successful Tasks: {summary['successful_tasks']}")
        print(f"Success Rate: {summary['success_rate']:.2%}")
        print(f"Average Reward: {summary['average_reward']:.3f}")
        print("="*60)
    
    def run(self):
        """Main execution method"""
        # Determine task IDs to run
        if self.args.task_ids:
            task_ids = self.args.task_ids
        elif self.args.mode == "quick":
            # Quick mode: run first 5 tasks
            task_ids = list(range(5))
        else:
            # Full evaluation based on environment
            if self.args.env == "retail":
                task_ids = list(range(115))  # 115 retail tasks
            else:  # airline
                task_ids = list(range(50))   # 50 airline tasks
        
        print(f"\n🚀 Starting evaluation of {len(task_ids)} tasks in {self.args.env} domain")
        print(f"   Model: {self.args.model}")
        print(f"   Mode: {self.args.mode}")
        if self.args.mode == "vllm":
            print(f"   Base URL: {self.args.base_url}")
        print()
        
        # Run tasks
        if self.args.max_concurrency > 1:
            results = self.run_parallel(task_ids)
        else:
            results = [self.run_single_task(tid) for tid in task_ids]
        
        # Save results
        self.save_results(results)
        
        return results


def main():
    parser = argparse.ArgumentParser(
        description="Unified tau-bench testing script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Quick test with VLLM
  python test.py --mode vllm --model Qwen/Qwen2.5-3B-Instruct --env retail --base-url http://localhost:8000/v1
  
  # Full evaluation with standard agent
  python test.py --mode standard --model gpt-4o --model-provider openai --env airline
  
  # Test specific tasks
  python test.py --mode vllm --model my-model --env retail --task-ids 0 1 2 3 4
        """
    )
    
    # Mode selection
    parser.add_argument(
        "--mode",
        type=str,
        choices=["standard", "vllm", "quick"],
        default="vllm",
        help="Testing mode: standard (tau-bench agents), vllm (VLLM server), quick (first 5 tasks)"
    )
    
    # Model configuration
    parser.add_argument("--model", type=str, required=True, help="Model name or path")
    parser.add_argument("--model-provider", type=str, help="Model provider (for standard mode)")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1", 
                       help="VLLM server URL (for vllm mode)")
    
    # Environment configuration
    parser.add_argument("--env", type=str, choices=["retail", "airline"], default="retail",
                       help="Environment to test")
    parser.add_argument("--task-ids", type=int, nargs="+", help="Specific task IDs to run")
    
    # Agent configuration
    parser.add_argument("--agent-strategy", type=str, default="tool-calling",
                       choices=["tool-calling", "act", "react", "few-shot"],
                       help="Agent strategy (for standard mode)")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature")
    
    # User simulator configuration
    parser.add_argument("--user-strategy", type=str, default="llm",
                       choices=["llm", "react", "verify", "reflection"],
                       help="User simulator strategy")
    parser.add_argument("--user-model", type=str, default="gpt-4o",
                       help="User simulator model")
    parser.add_argument("--user-provider", type=str, default="openai",
                       help="User simulator provider")
    
    # Execution configuration
    parser.add_argument("--max-concurrency", type=int, default=4,
                       help="Maximum concurrent tasks")
    parser.add_argument("--trial", type=int, default=0,
                       help="Trial number for multiple runs")
    parser.add_argument("--output-dir", type=str, help="Output directory for results")
    
    args = parser.parse_args()
    
    # Validation
    if args.mode == "standard" and not args.model_provider:
        parser.error("--model-provider is required for standard mode")
    
    # Check API keys
    if args.user_provider == "openai" and not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not set for user simulator")
    
    # Run tester
    tester = TauBenchTester(args)
    tester.run()


if __name__ == "__main__":
    main()