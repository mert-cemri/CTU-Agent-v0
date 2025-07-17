# Copyright Sierra

import json
from typing import Dict, Any, List, Tuple, Optional
from omegaconf import DictConfig

from skyrl_gym.envs.base_text_env import BaseTextEnv, BaseTextEnvStepOutput, ConversationType
from tau_bench.envs import get_env
from tau_bench.types import Action, Task, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME
from tau_bench.envs.user import UserStrategy

from .parser import parse_llm_response, format_tool_info_for_llm


class TauBenchEnv(BaseTextEnv):
    """
    SkyRL-Gym environment that bridges to tau_bench for multi-domain conversational AI training.
    Supports all 5 domains: airline, healthcare, telecom, doordash, retail.
    """

    def __init__(self, env_config: DictConfig, extras: Dict[str, Any] = {}):
        super().__init__()
        
        # Extract required fields from extras
        if "domain" not in extras:
            raise ValueError("domain field is required in extras")
        if "instruction" not in extras:
            raise ValueError("instruction field is required in extras")
        if "reward_spec" not in extras:
            raise ValueError("reward_spec field is required in extras")
        
        # Handle both serialized and direct reward_spec formats
        reward_spec = extras["reward_spec"]
        if isinstance(reward_spec, str):
            # Parse JSON string
            try:
                import json
                reward_spec = json.loads(reward_spec)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format in reward_spec")
        
        if "ground_truth" not in reward_spec:
            raise ValueError("ground_truth field is required in reward_spec")
        
        # Core environment parameters
        self.domain = extras["domain"]
        self.instruction = extras["instruction"]
        self.ground_truth_actions = reward_spec["ground_truth"]
        
        # User simulation configuration
        self.user_strategy = env_config.get("user_strategy", "llm")
        self.user_model = env_config.get("user_model", "gpt-4o")
        self.user_provider = env_config.get("user_provider", "openai")
        
        # Conversation tracking
        self.agent_actions = []  # Actions taken by the agent
        self.conversation_history = []  # Full conversation history
        self.turns = 0
        self.max_turns = env_config.get("max_turns", 20)
        
        # Initialize tau_bench environment
        self.tau_env = self._create_tau_env()
        self.tools_info = self.tau_env.tools_info
        
        # Environment state
        self.task_initialized = False
        self.conversation_done = False
        
    def _create_tau_env(self) -> Any:
        """Create tau_bench environment for the specified domain."""
        # Create a custom task for this specific instruction
        task = Task(
            user_id=f"user_{self.domain}",
            instruction=self.instruction,
            actions=self.ground_truth_actions,
            outputs=[],  # Will be populated if needed
            domain=self.domain
        )
        
        # Initialize tau_bench environment
        tau_env = get_env(
            env_name=self.domain,
            user_strategy=self.user_strategy,
            user_model=self.user_model,
            user_provider=self.user_provider,
            task_split="train",  # Default split
            custom_tasks=[task]  # Use our custom task
        )
        
        return tau_env
    
    def init(self, prompt: ConversationType) -> Tuple[ConversationType, Dict[str, Any]]:
        """Initialize the environment and return the initial prompt."""
        # Reset environment state
        self.turns = 0
        self.agent_actions = []
        self.conversation_history = []
        self.conversation_done = False
        
        # Reset tau_bench environment
        env_reset_response = self.tau_env.reset(task_index=0)
        
        # Store initial user message
        initial_user_message = env_reset_response.observation
        
        # Create enhanced prompt with domain context and tool information
        enhanced_prompt = self._create_enhanced_prompt(prompt, initial_user_message)
        
        # Store in conversation history
        self.conversation_history.extend(enhanced_prompt)
        
        self.task_initialized = True
        
        return enhanced_prompt, {
            "domain": self.domain,
            "instruction": self.instruction,
            "tools_available": len(self.tools_info),
            "initial_user_message": initial_user_message
        }
    
    def _create_enhanced_prompt(self, original_prompt: ConversationType, user_message: str) -> ConversationType:
        """Create enhanced prompt with domain-specific context and tool information."""
        # Extract system message if it exists
        system_content = ""
        user_content = ""
        
        for message in original_prompt:
            if message["role"] == "system":
                system_content = message["content"]
            elif message["role"] == "user":
                user_content = message["content"]
        
        # Create comprehensive system prompt
        domain_context = f"""
You are a helpful assistant for {self.domain} customer service. You have access to various tools to help customers.

Available tools:
{format_tool_info_for_llm(self.tools_info)}

Instructions:
- Use the available tools to help the customer with their request
- When using tools, format your response as JSON: {{"name": "tool_name", "arguments": {{"param": "value"}}}}
- Always be helpful and professional
- If you can't complete a task, explain why and suggest alternatives
"""
        
        # Combine with original system content
        if system_content:
            full_system_content = f"{system_content}\n\n{domain_context}"
        else:
            full_system_content = domain_context
        
        # Create enhanced prompt
        enhanced_prompt = [
            {"role": "system", "content": full_system_content},
            {"role": "user", "content": user_message}  # Use the actual user message from tau_bench
        ]
        
        return enhanced_prompt
    
    def step(self, action: str) -> BaseTextEnvStepOutput:
        """Execute one step in the environment."""
        if not self.task_initialized:
            raise RuntimeError("Environment not initialized. Call init() first.")
        
        self.turns += 1
        
        # Parse LLM response to tau_bench Action
        parsed_action = parse_llm_response(action, self.tools_info)
        
        # Store agent action (except for respond actions)
        if parsed_action.name != RESPOND_ACTION_NAME:
            self.agent_actions.append(parsed_action)
        
        # Execute action in tau_bench environment
        tau_result = self.tau_env.step(parsed_action)
        
        # Update conversation history
        self.conversation_history.append({"role": "assistant", "content": action})
        
        # Check if conversation is done
        done = tau_result.done or self.turns >= self.max_turns
        
        # Prepare observations for next turn
        observations = []
        if not done:
            # Add tool result or user response to observations
            if parsed_action.name != RESPOND_ACTION_NAME:
                # Tool was used, add tool result
                observations.append({
                    "role": "user", 
                    "content": f"Tool result: {tau_result.observation}"
                })
            else:
                # Regular response, add user's next message
                observations.append({
                    "role": "user",
                    "content": tau_result.observation
                })
            
            # Update conversation history
            self.conversation_history.extend(observations)
        
        # Calculate reward if conversation is done
        reward = tau_result.reward if done else 0.0
        
        # Mark as done
        if done:
            self.conversation_done = True
        
        return BaseTextEnvStepOutput(
            observations=observations,
            reward=reward,
            done=done,
            metadata={
                "domain": self.domain,
                "turns": self.turns,
                "agent_actions": [action.model_dump() for action in self.agent_actions],
                "ground_truth_actions": self.ground_truth_actions,
                "tau_result": tau_result.model_dump(),
                "conversation_history": self.conversation_history,
                "parsed_action": parsed_action.model_dump()
            }
        )
    
    def close(self):
        """Clean up environment resources."""
        # Clean up tau_bench environment if needed
        if hasattr(self.tau_env, 'close'):
            self.tau_env.close()
        
        # Reset internal state
        self.task_initialized = False
        self.conversation_done = False
        self.agent_actions = []
        self.conversation_history = [] 