#!/usr/bin/env python3
"""Test Qwen2.5-3B-Instruct on tau-bench"""

import argparse
import json
import os
from datetime import datetime
from tau_bench.envs import get_env
from tau_bench.agents.qwen_vllm_agent import QwenVLLMAgent
from tau_bench.types import EnvRunResult


def test_single_task(agent, env_name, task_id, user_model="gpt-4o"):
    """Test a single task"""
    print(f"\n{'='*50}")
    print(f"Testing Task {task_id}")
    print('='*50)
    
    env = get_env(
        env_name,
        user_strategy="llm",
        user_model=user_model,
        user_provider="openai",
        task_split="test",
        task_index=task_id
    )
    
    try:
        result = agent.solve(env=env, task_index=task_id)
        success = "✅" if result.reward > 0.9 else "❌"
        print(f"{success} Task {task_id}: Reward = {result.reward:.2f}")
        
        # Show conversation summary
        print(f"   Turns: {len([m for m in result.messages if m['role'] in ['user', 'assistant']])}")
        
        # Show tool calls made
        tool_calls = [m for m in result.messages if 'tool_calls' in m]
        if tool_calls:
            print(f"   Tools used: {len(tool_calls)}")
            for tc in tool_calls[:3]:  # Show first 3
                if tc.get('tool_calls'):
                    print(f"     - {tc['tool_calls'][0]['function']['name']}")
        
        return result
        
    except Exception as e:
        print(f"❌ Task {task_id} failed: {e}")
        return EnvRunResult(
            task_id=task_id,
            reward=0.0,
            info={"error": str(e)},
            traj=[],
            trial=0
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="Qwen/Qwen2.5-3B-Instruct")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    parser.add_argument("--env", type=str, choices=["retail", "airline"], default="retail")
    parser.add_argument("--tasks", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--user-model", type=str, default="gpt-4o")
    parser.add_argument("--output-dir", type=str, default="qwen_results")
    args = parser.parse_args()
    
    print(f"""
╔════════════════════════════════════════════════╗
║         Qwen2.5-3B-Instruct Testing           ║
╚════════════════════════════════════════════════╝

Configuration:
- Model: {args.model}
- VLLM URL: {args.base_url}
- Environment: {args.env}
- Tasks: {args.tasks}
- Temperature: {args.temperature}
- User Model: {args.user_model}
""")
    
    # Load environment for tools
    env = get_env(args.env, user_strategy="llm", user_model=args.user_model, user_provider="openai")
    
    # Create Qwen-optimized agent
    agent = QwenVLLMAgent(
        tools_info=env.tools_info,
        wiki=env.wiki,
        model=args.model,
        base_url=args.base_url,
        temperature=args.temperature
    )
    
    print(f"Available tools ({len(env.tools_info)}):")
    for tool in env.tools_info[:5]:
        print(f"  - {tool['function']['name']}")
    if len(env.tools_info) > 5:
        print(f"  ... and {len(env.tools_info) - 5} more")
    
    # Test each task
    results = []
    for task_id in args.tasks:
        result = test_single_task(agent, args.env, task_id, args.user_model)
        results.append(result)
    
    # Save results
    os.makedirs(args.output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{args.output_dir}/qwen25_3b_{args.env}_{timestamp}.json"
    
    with open(output_file, "w") as f:
        json.dump([r.model_dump() if hasattr(r, 'model_dump') else r.__dict__ for r in results], f, indent=2)
    
    # Summary
    successful = sum(1 for r in results if r.reward > 0.9)
    total = len(results)
    avg_reward = sum(r.reward for r in results) / total if total > 0 else 0
    
    print(f"""
╔════════════════════════════════════════════════╗
║                  RESULTS                       ║
╚════════════════════════════════════════════════╝

Tasks Completed: {successful}/{total} ({successful/total*100:.1f}%)
Average Reward: {avg_reward:.3f}
Results saved to: {output_file}

Performance Analysis:
""")
    
    if avg_reward < 0.3:
        print("⚠️  Low performance - Model may need fine-tuning on tool-calling tasks")
    elif avg_reward < 0.6:
        print("📊 Moderate performance - Shows capability but room for improvement")
    else:
        print("🎯 Good performance - Model handles tool-calling well")
    
    # Task-specific feedback
    print("\nTask Analysis:")
    for r in results:
        status = "✅ Success" if r.reward > 0.9 else "⚠️  Partial" if r.reward > 0 else "❌ Failed"
        print(f"  Task {r.task_id}: {status} (reward: {r.reward:.2f})")


if __name__ == "__main__":
    main()