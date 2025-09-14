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
        max_model_len: int = 32768,
        tensor_parallel_size: int = 1,
        gpu_memory_utilization: float = 0.8,
        enable_thinking: bool = True,
    ):
        """Initialize the tester."""
        self.model_name = model_name
        self.domain = domain
        self.user_model = user_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_model_len = max_model_len
        self.tensor_parallel_size = tensor_parallel_size
        self.gpu_memory_utilization = gpu_memory_utilization
        self.enable_thinking = enable_thinking

        print(f"Initializing VLLM with model: {model_name}")
        print(f"  Max model length: {max_model_len}")
        print(f"  Tensor parallel size: {tensor_parallel_size}")
        print(f"  GPU memory utilization: {gpu_memory_utilization}")
        print(f"  Thinking mode: {'enabled' if enable_thinking else 'disabled'}")

        self.llm = LLM(
            model=model_name,
            tensor_parallel_size=tensor_parallel_size,
            gpu_memory_utilization=gpu_memory_utilization,
            trust_remote_code=True,
            max_model_len=max_model_len,
        )
        
        # Configure stop tokens based on thinking mode setting
        stop_tokens = ["</s>", "<|im_end|>", "<|endoftext|>"]

        # Add thinking stop tokens for Qwen models if thinking is disabled
        if "qwen" in model_name.lower() and not enable_thinking:
            stop_tokens.extend(["<|thinking|>", "</thinking>"])

        self.sampling_params = SamplingParams(
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop_tokens,
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
        
        # Initialize conversation with system message and user observation
        conversation = [
            {"role": "system", "content": env.wiki if hasattr(env, 'wiki') and env.wiki else "You are a helpful assistant."},
            {"role": "user", "content": obs}
        ]

        done = False
        turns = 0
        max_turns = 10
        
        while not done and turns < max_turns:
            # Format prompt for the model
            prompt = self._format_prompt(conversation, env.tools_info)

            # Generate response
            response = agent.generate(prompt)

            # Parse and execute action
            try:
                action = self._parse_action_from_response(response, env.tools_info)
                print(f"Turn {turns}: Parsed action = {action}")
                print(f"Turn {turns}: Model response = {response[:200]}...")

                # Add assistant message to conversation
                if action.name != "respond":
                    # This is a tool call - format as tool calling message
                    assistant_msg = {
                        "role": "assistant",
                        "content": None,
                        "tool_calls": [{
                            "id": f"call_{turns}",
                            "function": {
                                "name": action.name,
                                "arguments": json.dumps(action.kwargs)
                            },
                            "type": "function"
                        }]
                    }
                else:
                    # This is a regular response
                    assistant_msg = {"role": "assistant", "content": response}

                conversation.append(assistant_msg)

                # Execute action in environment
                step_response = env.step(action)
                obs = step_response.observation
                reward = step_response.reward
                done = step_response.done
                info = step_response.info

                # Add appropriate response to conversation
                if action.name != "respond":
                    # Add tool response
                    if obs:
                        conversation.append({
                            "role": "tool",
                            "tool_call_id": f"call_{turns}",
                            "name": action.name,
                            "content": obs
                        })
                else:
                    # Add user response for regular chat
                    if obs and not done:
                        conversation.append({"role": "user", "content": obs})

            except Exception as e:
                print(f"Error in turn {turns}: {e}")
                print(f"Action type: {type(action) if 'action' in locals() else 'action not defined'}")
                print(f"Action value: {action if 'action' in locals() else 'action not defined'}")
                import traceback
                traceback.print_exc()

                # Try to create a fallback action if parsing failed
                if 'action' not in locals():
                    try:
                        action = Action(name="respond", kwargs={"content": response})
                        print(f"Created fallback action: {action}")
                    except:
                        print("Failed to create fallback action, ending conversation")
                        done = True
                        reward = 0
                        info = None
                        break

                done = True
                reward = 0
                info = step_response.info if 'step_response' in locals() else None

            turns += 1

            # Break if environment indicates completion
            if done:
                break
        
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
        """Format conversation into a prompt with proper tool instructions."""
        prompt = ""

        # Add tools information if available
        if tools_info:
            prompt += "You have access to the following tools. Use them when appropriate:\n\n"
            for tool in tools_info:
                # Handle different tool info structures
                name = tool.get('name') or tool.get('function', {}).get('name') or 'unknown'
                desc = tool.get('description') or tool.get('function', {}).get('description', '')
                params = tool.get('parameters') or tool.get('function', {}).get('parameters', {})

                prompt += f"Tool: {name}\n"
                prompt += f"Description: {desc}\n"
                if params and 'properties' in params:
                    prompt += "Parameters:\n"
                    for param_name, param_info in params['properties'].items():
                        param_desc = param_info.get('description', '')
                        param_type = param_info.get('type', 'string')
                        prompt += f"  - {param_name} ({param_type}): {param_desc}\n"
                prompt += f"\nTo use this tool, call: {name}(param1=\"value1\", param2=\"value2\")\n\n"

            prompt += "When you want to use a tool, write the function call clearly. When you want to respond normally, just write your response.\n\n"

        # Add conversation history
        for msg in conversation:
            role = msg["role"]
            content = msg.get("content", "")

            if role == "system":
                prompt += f"System: {content}\n\n"
            elif role == "user":
                prompt += f"User: {content}\n\n"
            elif role == "assistant":
                if msg.get("tool_calls"):
                    # Format tool call
                    for tool_call in msg["tool_calls"]:
                        func_name = tool_call["function"]["name"]
                        func_args = tool_call["function"]["arguments"]
                        prompt += f"Assistant: {func_name}({func_args})\n\n"
                else:
                    prompt += f"Assistant: {content}\n\n"
            elif role == "tool":
                tool_name = msg.get("name", "tool")
                prompt += f"Tool ({tool_name}): {content}\n\n"

        prompt += "Assistant: "
        return prompt
    
    def _parse_action_from_response(self, response: str, tools_info: List[Dict]) -> Action:
        """Parse action from model response with better tool detection."""
        import re

        # Get available tool names - first check the structure
        print(f"Tools info structure: {tools_info}")
        if tools_info and len(tools_info) > 0:
            print(f"First tool structure: {tools_info[0]}")
            print(f"First tool keys: {list(tools_info[0].keys()) if isinstance(tools_info[0], dict) else 'not a dict'}")

        # Handle different possible structures
        available_tools = []
        if tools_info:
            for tool in tools_info:
                if isinstance(tool, dict):
                    # Try different possible key names
                    name = tool.get("name") or tool.get("function", {}).get("name") or tool.get("tool_name")
                    if name:
                        available_tools.append(name)
                else:
                    print(f"Unexpected tool type: {type(tool)}")

        print(f"Available tools: {available_tools}")
        print(f"Response to parse: {response[:200]}...")

        # Look for various tool call patterns
        patterns = [
            # JSON format: {"name": "tool_name", "arguments": {...}}
            r'```json\s*\{\s*"name"\s*:\s*"([^"]+)"\s*,\s*"arguments"\s*:\s*(\{.*?\})\s*\}\s*```',
            # Function call format: tool_name({"arg": "value"})
            r'(\w+)\(\s*(\{[^}]*\})\s*\)',
            # Function call with direct args: tool_name(arg1="value1", arg2="value2")
            r'(\w+)\(([^)]+)\)',
            # Tool tags: <tool name="tool_name">{"arg": "value"}</tool>
            r'<tool\s+name="([^"]+)"\s*>([^<]*)</tool>',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, response, re.DOTALL | re.IGNORECASE)
            for match in matches:
                if len(match) == 2:
                    tool_name, args_str = match

                    # Check if this is an available tool
                    if tool_name in available_tools:
                        try:
                            # Try to parse arguments as JSON
                            if args_str.strip().startswith('{'):
                                kwargs = json.loads(args_str)
                            else:
                                # Parse key=value pairs
                                kwargs = {}
                                for arg in args_str.split(','):
                                    if '=' in arg:
                                        key, value = arg.split('=', 1)
                                        key = key.strip().strip('"').strip("'")
                                        value = value.strip().strip('"').strip("'")
                                        kwargs[key] = value

                            tool_action = Action(name=tool_name, kwargs=kwargs)
                            print(f"Found tool call: {tool_action}")
                            return tool_action
                        except:
                            continue

        # Check if response mentions any available tools
        for tool in available_tools:
            if tool.lower() in response.lower():
                # Found tool mention, try to extract arguments
                tool_pattern = rf'{re.escape(tool)}\s*\(([^)]*)\)'
                match = re.search(tool_pattern, response, re.IGNORECASE)
                if match:
                    args_str = match.group(1)
                    kwargs = {}
                    if args_str:
                        for arg in args_str.split(','):
                            if '=' in arg:
                                key, value = arg.split('=', 1)
                                kwargs[key.strip().strip('"').strip("'")] = value.strip().strip('"').strip("'")
                    tool_action = Action(name=tool, kwargs=kwargs)
                    print(f"Found tool mention: {tool_action}")
                    return tool_action

        # Default to respond action
        try:
            default_action = Action(name="respond", kwargs={"content": response})
            print(f"Successfully created Action: {default_action}")
            print(f"Action type: {type(default_action)}")
            print(f"Action name: {default_action.name}")
            return default_action
        except Exception as e:
            print(f"Error creating Action: {e}")
            # Return a simple dictionary as fallback
            return {"name": "respond", "kwargs": {"content": response}}
    
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
    parser.add_argument(
        "--max-model-len",
        type=int,
        default=32768,
        help="Maximum model context length (default: 32768)",
    )
    parser.add_argument(
        "--tensor-parallel-size",
        type=int,
        default=1,
        help="Tensor parallel size for VLLM (default: 1)",
    )
    parser.add_argument(
        "--gpu-memory-utilization",
        type=float,
        default=0.8,
        help="GPU memory utilization for VLLM (default: 0.8)",
    )
    parser.add_argument(
        "--enable-thinking",
        action="store_true",
        default=True,
        help="Enable thinking mode for Qwen models (default: True)",
    )
    parser.add_argument(
        "--disable-thinking",
        action="store_true",
        help="Disable thinking mode for Qwen models",
    )

    args = parser.parse_args()

    # Handle thinking mode logic
    if args.disable_thinking:
        args.enable_thinking = False
    
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
        max_model_len=args.max_model_len,
        tensor_parallel_size=args.tensor_parallel_size,
        gpu_memory_utilization=args.gpu_memory_utilization,
        enable_thinking=args.enable_thinking,
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