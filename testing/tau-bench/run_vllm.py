#!/usr/bin/env python3
"""Run tau-bench evaluation with VLLM models"""

import argparse
import json
import os
from datetime import datetime
from tau_bench.envs import get_env
from tau_bench.agents.vllm_agent import VLLMAgent
from tau_bench.types import EnvRunResult
from concurrent.futures import ThreadPoolExecutor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Model name/path")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    parser.add_argument("--env", type=str, choices=["retail", "airline"], default="retail")
    parser.add_argument("--task-ids", type=int, nargs="+", help="Specific task IDs")
    parser.add_argument("--max-concurrency", type=int, default=4)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--user-model", type=str, default="gpt-4o")
    parser.add_argument("--user-provider", type=str, default="openai")
    parser.add_argument("--output-dir", type=str, default="vllm_results")
    args = parser.parse_args()
    
    # Setup environment
    env = get_env(
        args.env,
        user_strategy="llm",
        user_model=args.user_model,
        user_provider=args.user_provider,
        task_split="test"
    )
    
    # Create agent
    agent = VLLMAgent(
        tools_info=env.tools_info,
        wiki=env.wiki,
        model=args.model,
        base_url=args.base_url,
        temperature=args.temperature
    )
    
    # Task selection
    task_ids = args.task_ids if args.task_ids else list(range(min(10, len(env.tasks))))
    
    # Output setup
    os.makedirs(args.output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{args.output_dir}/{args.model.replace('/', '_')}_{args.env}_{timestamp}.json"
    
    results = []
    
    def run_task(task_id):
        print(f"Running task {task_id}")
        task_env = get_env(
            args.env,
            user_strategy="llm",
            user_model=args.user_model,
            user_provider=args.user_provider,
            task_split="test",
            task_index=task_id
        )
        
        try:
            res = agent.solve(env=task_env, task_index=task_id)
            result = EnvRunResult(
                task_id=task_id,
                reward=res.reward,
                info=res.info,
                traj=res.messages,
                trial=0
            )
            print(f"{'✓' if res.reward > 0.5 else '✗'} Task {task_id}: reward={res.reward:.2f}")
        except Exception as e:
            result = EnvRunResult(
                task_id=task_id,
                reward=0.0,
                info={"error": str(e)},
                traj=[],
                trial=0
            )
            print(f"✗ Task {task_id}: {e}")
        
        return result
    
    # Run tasks
    with ThreadPoolExecutor(max_workers=args.max_concurrency) as executor:
        results = list(executor.map(run_task, task_ids))
    
    # Save results
    with open(output_file, "w") as f:
        json.dump([r.model_dump() for r in results], f, indent=2)
    
    # Display summary
    avg_reward = sum(r.reward for r in results) / len(results)
    print(f"\n{'='*50}")
    print(f"Average reward: {avg_reward:.3f}")
    print(f"Success rate: {sum(1 for r in results if r.reward > 0.5) / len(results):.1%}")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()