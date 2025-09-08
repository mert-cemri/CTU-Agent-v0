#!/usr/bin/env python3
"""Live conversation tester for Qwen models with detailed logging"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from tau_bench.envs import get_env
from tau_bench.agents.qwen_vllm_agent import QwenVLLMAgent
from tau_bench.types import EnvRunResult


class LiveConversationTester:
    def __init__(self, args):
        self.args = args
        self.setup_output_dir()
    
    def setup_output_dir(self):
        """Create clean output directory structure"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        model_name = self.args.model.split('/')[-1].replace('/', '_')
        
        self.output_dir = Path(self.args.output_dir) / f"{model_name}_{self.args.env}_{timestamp}"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Output directory: {self.output_dir}")
    
    def print_conversation_header(self, task_id: int, task_info: Dict):
        """Print formatted conversation header"""
        print(f"\n{'='*80}")
        print(f"🎯 TASK {task_id:03d} - {self.args.env.upper()} DOMAIN")
        print(f"{'='*80}")
        if 'instruction' in task_info:
            instruction = task_info['instruction'][:150] + "..." if len(task_info['instruction']) > 150 else task_info['instruction']
            print(f"📋 Goal: {instruction}")
        print(f"🎭 User Model: {self.args.user_model}")
        print(f"🤖 Agent Model: {self.args.model}")
        print(f"{'='*80}")
    
    def print_live_message(self, role: str, content: str, turn_num: int):
        """Print a conversation message with nice formatting"""
        if role == "user":
            icon = "👤"
            color = "\033[94m"  # Blue
            label = "USER"
        elif role == "assistant":
            icon = "🤖" 
            color = "\033[92m"  # Green
            label = "AGENT"
        else:
            icon = "ℹ️"
            color = "\033[93m"  # Yellow
            label = role.upper()
        
        reset_color = "\033[0m"
        
        print(f"\n{color}[Turn {turn_num:02d}] {icon} {label}:{reset_color}")
        
        # Handle long messages
        if len(content) > 500:
            print(f"{content[:500]}...")
            print(f"{color}[Message truncated for display - full content in logs]{reset_color}")
        else:
            print(content)
    
    def print_tool_call(self, tool_call: Dict, turn_num: int):
        """Print tool call with formatting"""
        color = "\033[95m"  # Magenta
        reset_color = "\033[0m"
        
        print(f"\n{color}[Turn {turn_num:02d}] 🔧 TOOL CALL:{reset_color}")
        print(f"Function: {tool_call['function']['name']}")
        
        # Pretty print arguments
        try:
            args = json.loads(tool_call['function']['arguments'])
            if len(str(args)) > 200:
                print("Arguments: [Large payload - see logs]")
            else:
                print(f"Arguments: {json.dumps(args, indent=2)}")
        except:
            print(f"Arguments: {tool_call['function']['arguments']}")
    
    def print_tool_result(self, tool_result: str, turn_num: int):
        """Print tool result with formatting"""
        color = "\033[96m"  # Cyan
        reset_color = "\033[0m"
        
        print(f"\n{color}[Turn {turn_num:02d}] ⚙️ TOOL RESULT:{reset_color}")
        if len(tool_result) > 300:
            print(f"{tool_result[:300]}...")
            print(f"{color}[Result truncated for display - full content in logs]{reset_color}")
        else:
            print(tool_result)
    
    def test_single_task(self, agent, task_id: int) -> Dict:
        """Test a single task with live conversation display"""
        
        # Create environment
        env = get_env(
            self.args.env,
            user_strategy="llm",
            user_model=self.args.user_model,
            user_provider="openai",
            task_split="test",
            task_index=task_id
        )
        
        # Get task info
        task_info = env.tasks[task_id] if task_id < len(env.tasks) else {}
        self.print_conversation_header(task_id, task_info)
        
        # Set up live tracking
        turn_counter = 0
        messages_seen = []
        
        try:
            # Run the task
            result = agent.solve(env=env, task_index=task_id)
            
            # Display conversation live
            for msg in result.messages:
                if msg not in messages_seen:  # Only show new messages
                    messages_seen.append(msg)
                    turn_counter += 1
                    
                    if msg.get('role') == 'user':
                        self.print_live_message('user', msg['content'], turn_counter)
                    
                    elif msg.get('role') == 'assistant':
                        if msg.get('tool_calls'):
                            # Show tool calls
                            for tool_call in msg['tool_calls']:
                                self.print_tool_call(tool_call, turn_counter)
                        else:
                            # Regular assistant message
                            content = msg.get('content', '')
                            if content:  # Only print if there's actual content
                                self.print_live_message('assistant', content, turn_counter)
                    
                    elif msg.get('role') == 'tool':
                        self.print_tool_result(msg['content'], turn_counter)
            
            # Print final result
            self.print_task_result(task_id, result)
            
            # Format result in the required structure
            # Convert task_info to serializable format
            serializable_task = {}
            if task_info:
                if hasattr(task_info, 'model_dump'):
                    serializable_task = task_info.model_dump()
                elif hasattr(task_info, '__dict__'):
                    serializable_task = {k: v for k, v in task_info.__dict__.items() if not k.startswith('_')}
                else:
                    serializable_task = str(task_info)
            
            formatted_result = {
                "task_id": task_id,
                "reward": result.reward,
                "info": {
                    "task": serializable_task,
                    "source": "user",
                    "user_cost": getattr(env.user, 'get_total_cost', lambda: 0.0)(),
                    "reward_info": {
                        "reward": result.reward,
                        "info": getattr(result, 'info', {}),
                        "actions": getattr(result, 'actions', [])
                    }
                },
                "traj": result.messages,
                "trial": 0
            }
            
            # Save individual task log
            self.save_task_log(task_id, formatted_result)
            
            return formatted_result
            
        except Exception as e:
            print(f"\n❌ Task {task_id} failed with error: {str(e)}")
            
            # Convert task_info to serializable format for error case
            serializable_task = {}
            if task_info:
                if hasattr(task_info, 'model_dump'):
                    serializable_task = task_info.model_dump()
                elif hasattr(task_info, '__dict__'):
                    serializable_task = {k: v for k, v in task_info.__dict__.items() if not k.startswith('_')}
                else:
                    serializable_task = str(task_info)
            
            error_result = {
                "task_id": task_id,
                "reward": 0.0,
                "info": {
                    "task": serializable_task,
                    "source": "error",
                    "user_cost": 0.0,
                    "error": str(e),
                    "reward_info": {
                        "reward": 0.0,
                        "info": {},
                        "actions": []
                    }
                },
                "traj": [],
                "trial": 0
            }
            
            self.save_task_log(task_id, error_result)
            return error_result
    
    def print_task_result(self, task_id: int, result):
        """Print final task result"""
        color = "\033[92m" if result.reward > 0.9 else "\033[93m" if result.reward > 0 else "\033[91m"
        reset_color = "\033[0m"
        
        print(f"\n{color}{'='*80}")
        print(f"📊 TASK {task_id:03d} COMPLETE")
        print(f"{'='*80}{reset_color}")
        
        success_icon = "✅" if result.reward > 0.9 else "⚠️" if result.reward > 0 else "❌"
        print(f"{success_icon} Reward: {result.reward:.3f}")
        
        # Count conversation turns
        turns = len([m for m in result.messages if m.get('role') in ['user', 'assistant']])
        tool_calls = len([m for m in result.messages if m.get('tool_calls')])
        
        print(f"💬 Turns: {turns}")
        print(f"🔧 Tool Calls: {tool_calls}")
        
        if result.reward < 0.1:
            print(f"{color}📝 Analysis: Task failed - likely tool calling or reasoning issue{reset_color}")
        elif result.reward < 0.9:
            print(f"{color}📝 Analysis: Partial success - goal partially achieved{reset_color}")
        else:
            print(f"{color}📝 Analysis: Full success - goal achieved{reset_color}")
    
    def save_task_log(self, task_id: int, result_data: Dict):
        """Save individual task log in the required format"""
        log_file = self.output_dir / f"task_{task_id:03d}.json"
        
        with open(log_file, 'w') as f:
            json.dump(result_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Task {task_id:03d} logged to: {log_file.name}")
    
    def run_tests(self):
        """Main test execution"""
        # Load environment to get task info
        env = get_env(
            self.args.env, 
            user_strategy="llm", 
            user_model=self.args.user_model, 
            user_provider="openai",
            task_split="test"
        )
        
        # Determine tasks to run
        if self.args.tasks is None:
            num_tasks = len(env.tasks)
            tasks_to_run = list(range(num_tasks))
        else:
            tasks_to_run = self.args.tasks
        
        print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        🧪 LIVE CONVERSATION TESTER                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

📋 Configuration:
   Model: {self.args.model}
   VLLM URL: {self.args.base_url}
   Environment: {self.args.env}
   Tasks: {"ALL (" + str(len(tasks_to_run)) + " tasks)" if self.args.tasks is None else tasks_to_run}
   Temperature: {self.args.temperature}
   User Model: {self.args.user_model}
   Output: {self.output_dir}

🚀 Starting live testing...
""")
        
        # Create agent
        agent = QwenVLLMAgent(
            tools_info=env.tools_info,
            wiki=env.wiki,
            model=self.args.model,
            base_url=self.args.base_url,
            temperature=self.args.temperature
        )
        
        # Run tests
        results = []
        for i, task_id in enumerate(tasks_to_run):
            print(f"\n🎯 Starting task {i+1}/{len(tasks_to_run)} (ID: {task_id})")
            result = self.test_single_task(agent, task_id)
            results.append(result)
            
            # Brief pause between tasks for readability
            if i < len(tasks_to_run) - 1:
                print(f"\n{'─'*80}")
                print(f"⏭️  Moving to next task...")
                import time
                time.sleep(1)
        
        # Save aggregated results
        self.save_aggregated_results(results)
        self.print_final_summary(results)
    
    def save_aggregated_results(self, results: List[Dict]):
        """Save all results in a single file matching the required format"""
        # Save as array of results (matching the user's format)
        results_file = self.output_dir / f"{self.args.env}_results.json"
        
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 All results saved to: {results_file}")
    
    def print_final_summary(self, results: List[Dict]):
        """Print final test summary"""
        successful = sum(1 for r in results if r["reward"] > 0.9)
        failed = sum(1 for r in results if r["reward"] < 0.1)
        partial = len(results) - successful - failed
        avg_reward = sum(r["reward"] for r in results) / len(results)
        
        print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              📊 FINAL RESULTS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

🎯 Task Summary:
   ✅ Successful: {successful}/{len(results)} ({successful/len(results)*100:.1f}%)
   ⚠️  Partial:    {partial}/{len(results)} ({partial/len(results)*100:.1f}%)
   ❌ Failed:     {failed}/{len(results)} ({failed/len(results)*100:.1f}%)

📈 Performance:
   Average Reward: {avg_reward:.3f}
   Success Rate: {successful/len(results)*100:.1f}%

📁 Outputs:
   Individual Tasks: {self.output_dir}/task_*.json
   Aggregated: {self.output_dir}/{self.args.env}_results.json

💡 Analysis:""")
        
        if avg_reward < 0.3:
            print("   ⚠️  Model shows low task completion - consider fine-tuning")
        elif avg_reward < 0.6:
            print("   📊 Moderate performance - shows capability but room for improvement")
        else:
            print("   🎯 Strong performance - model handles tasks well")
        
        print(f"\n{'═'*80}")


def main():
    parser = argparse.ArgumentParser(description="Live conversation tester for Qwen models")
    parser.add_argument("--model", type=str, default="Qwen/Qwen2.5-3B-Instruct",
                       help="Model name or path")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1",
                       help="VLLM server URL")
    parser.add_argument("--env", type=str, choices=["retail", "airline"], default="retail",
                       help="Environment to test")
    parser.add_argument("--tasks", type=int, nargs="+", default=None,
                       help="Specific task IDs to test (default: all)")
    parser.add_argument("--temperature", type=float, default=0.0,
                       help="Sampling temperature")
    parser.add_argument("--user-model", type=str, default="gpt-4o",
                       help="User simulator model")
    parser.add_argument("--output-dir", type=str, default="live_results",
                       help="Output directory for results")
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not set - user simulator may fail")
    
    tester = LiveConversationTester(args)
    tester.run_tests()


if __name__ == "__main__":
    main()