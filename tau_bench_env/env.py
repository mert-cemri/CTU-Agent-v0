# Copyright Sierra

import json
import os
from typing import Dict, Any, List, Tuple, Optional
from omegaconf import DictConfig

from skyrl_gym.envs.base_text_env import BaseTextEnv, BaseTextEnvStepOutput, ConversationType
from tau_bench.envs import get_env
from tau_bench.tau_types import Action, Task, RESPOND_ACTION_NAME, RESPOND_ACTION_FIELD_NAME
from tau_bench.envs.user import UserStrategy

from .parser import parse_llm_response, format_tool_info_for_llm
from .simple_parser import parse_tool_calling_response


class TauBenchEnv(BaseTextEnv):
    """
    SkyRL-Gym environment that bridges to tau_bench for multi-domain conversational AI training.
    Supports all 5 domains: airline, healthcare, telecom, doordash, retail.
    """

    def _convert_tools_to_openai_format(self) -> List[Dict[str, Any]]:
        """Convert tau_bench tools info to OpenAI tools format.
        
        Expected tau_bench format:
        {
            "function": {
                "name": "tool_name",
                "description": "...",
                "parameters": {...}
            }
        }
        
        Converts to OpenAI format:
        {
            "type": "function",
            "function": {
                "name": "tool_name",
                "description": "...", 
                "parameters": {...}
            }
        }
        """
        assert isinstance(self.tools_info, list), \
            f"tools_info must be a list, got {type(self.tools_info)}"
        assert len(self.tools_info) > 0, \
            "tools_info must not be empty"
        
        openai_tools = []
        for i, tool in enumerate(self.tools_info):
            assert isinstance(tool, dict), \
                f"Tool {i} must be dict, got {type(tool)}: {tool}"
            assert "function" in tool, \
                f"Tool {i} must have 'function' key, got keys: {list(tool.keys())}"
            assert isinstance(tool["function"], dict), \
                f"Tool {i} function must be dict, got {type(tool['function'])}"
            assert "name" in tool["function"], \
                f"Tool {i} function must have 'name', got keys: {list(tool['function'].keys())}"
            
            openai_tool = {
                "type": "function",
                "function": tool["function"]
            }
            openai_tools.append(openai_tool)
        
        return openai_tools
    
    def __init__(self, env_config: DictConfig, extras: Dict[str, Any] = {}):
        super().__init__()
        
        # Handle serialized fields in extras
        processed_extras = self._process_extras(extras)
        
        # Extract required fields from processed extras
        if "domain" not in processed_extras:
            raise ValueError("domain field is required in extras")
        if "instruction" not in processed_extras:
            raise ValueError("instruction field is required in extras")
        if "reward_spec" not in processed_extras:
            raise ValueError("reward_spec field is required in extras")
        
        # Handle both serialized and direct reward_spec formats
        reward_spec = processed_extras["reward_spec"]
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
        self.domain = processed_extras["domain"]
        self.instruction = processed_extras["instruction"]
        self.ground_truth_actions = reward_spec["ground_truth"]
        
        # User simulation configuration
        self.user_strategy = env_config.get("user_strategy", "llm")
        self.user_model = env_config.get("user_model", "gpt-4o")
        self.user_provider = env_config.get("user_provider", "openai")
        
        # Tool calling configuration
        self.use_native_tool_calling = env_config.get("use_native_tool_calling", False)
        
        # Check if we have API keys for LLM user simulation
        if self.user_strategy == "llm" and self.user_provider == "openai":
            if not os.environ.get("OPENAI_API_KEY"):
                print("Warning: OPENAI_API_KEY not set in this environment")
                print("This might be expected in Ray worker processes - tau_bench will handle authentication")
        
        # Conversation tracking
        self.agent_actions = []  # Actions taken by the agent
        self.conversation_history = []  # Full conversation history
        self.turns = 0
        self.max_turns = env_config.get("max_turns", 20)
        
        # Initialize tau_bench environment
        self.tau_env = self._create_tau_env()
        assert self.tau_env is not None, "Failed to create tau_bench environment"
        self.tools_info = self.tau_env.tools_info
        assert len(self.tools_info) > 0, f"No tools available for domain {self.domain}"
        
        # Environment state
        self.task_initialized = False
        self.conversation_done = False
    
    def _process_extras(self, extras: Dict[str, Any]) -> Dict[str, Any]:
        """Process extras dictionary, deserializing JSON strings as needed."""
        processed = {}
        
        for key, value in extras.items():
            if isinstance(value, str) and key in ['extra_info', 'reward_spec']:
                # Try to deserialize JSON strings
                try:
                    import json
                    deserialized = json.loads(value)
                    if key == 'extra_info':
                        # Merge extra_info contents into the main dictionary
                        processed.update(deserialized)
                    else:
                        processed[key] = deserialized
                except (json.JSONDecodeError, TypeError):
                    # If it's not valid JSON, keep as string
                    processed[key] = value
            else:
                processed[key] = value
        
        return processed
        
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
        # print("=" * 50)
        # print("DEBUG: init() called with prompt:")
        # print("Type:", type(prompt))
        # print("Content:", prompt)
        # print("Repr:", repr(prompt))
        # print("=" * 50)
        
        # Reset environment state
        self.turns = 0
        self.agent_actions = []
        self.conversation_history = []
        self.conversation_done = False
        
        # Reset tau_bench environment
        env_reset_response = self.tau_env.reset(task_index=0)
        assert hasattr(env_reset_response, 'observation'), \
            f"Invalid reset response: {env_reset_response}"
        
        # Store initial user message
        initial_user_message = env_reset_response.observation
        assert isinstance(initial_user_message, str) and len(initial_user_message) > 0, \
            "Empty or invalid initial user message"
        
        # Create enhanced prompt with domain context and tool information
        enhanced_prompt = self._create_enhanced_prompt(prompt, initial_user_message)
        
        # Store in conversation history
        assert len(enhanced_prompt) >= 2, "Enhanced prompt must have system and user messages"
        assert enhanced_prompt[0]["role"] == "system", "First message must be system"
        assert enhanced_prompt[1]["role"] == "user", "Second message must be user"
        self.conversation_history.extend(enhanced_prompt)
        
        self.task_initialized = True
        
        metadata = {
            "domain": self.domain,
            "instruction": self.instruction,
            "tools_available": len(self.tools_info),
            "initial_user_message": initial_user_message
        }
        
        # Add tools in OpenAI format if native tool calling is enabled
        if self.use_native_tool_calling:
            metadata["tools"] = self._convert_tools_to_openai_format()
        
        return enhanced_prompt, metadata
    
    def _create_enhanced_prompt(self, original_prompt: ConversationType, user_message: str) -> ConversationType:
        """Create enhanced prompt with domain-specific context and tool information."""
        
        # Debug: Print the type and content of original_prompt
        # print("=" * 50)
        # print("DEBUG: original_prompt type:", type(original_prompt))
        # print("DEBUG: original_prompt content:", original_prompt)
        # print("=" * 50)
        
        # Handle the case where original_prompt is a string instead of a list
        if isinstance(original_prompt, str):
            # print("INFO: original_prompt is a string, parsing as JSON...")
            try:
                import json
                original_prompt = json.loads(original_prompt)
                # print("SUCCESS: Parsed original_prompt as JSON")
            except json.JSONDecodeError as e:
                print(f"ERROR: Could not parse original_prompt as JSON: {e}")
                # Create a default prompt structure
                original_prompt = [{"role": "user", "content": original_prompt}]
        
        # Extract system message if it exists
        system_content = ""
        user_content = ""
        
        # Now process the messages (should be a proper list now)
        for i, message in enumerate(original_prompt):
            # print(f"DEBUG: Processing message {i}: {type(message)} = {message}")
            try:
                if isinstance(message, dict) and "role" in message and "content" in message:
                    if message["role"] == "system":
                        system_content = message["content"]
                    elif message["role"] == "user":
                        user_content = message["content"]
                else:
                    print(f"WARNING: Message {i} is not a proper dict: {message}")
            except Exception as e:
                print(f"ERROR: Exception processing message {i}: {e}")
        
        # Create comprehensive system prompt with OpenAI-style tool calling examples
        domain_context = f"""
You are a helpful assistant for {self.domain} customer service. You have access to various tools to help customers.

Available tools:
{format_tool_info_for_llm(self.tools_info)}

CRITICAL INSTRUCTIONS FOR TOOL USAGE:
You MUST respond in one of these two ways:

1. For regular conversation (no tool needed):
   Simply respond with helpful text.

2. For tool usage:
   Output ONLY a valid JSON object with this EXACT structure:
   {{"tool_calls": [{{"function": {{"name": "tool_name", "arguments": "{{\\"param\\": \\"value\\"}}"}}}}]}}

IMPORTANT: 
- The "arguments" field must be a JSON string (not a JSON object)
- Do NOT add any text before or after the JSON when using tools
- Do NOT use markdown code blocks
- Do NOT include <|im_end|> or any other tokens

EXAMPLES OF CORRECT USAGE:

Example 1 - Finding a user by name and zip:
User: My name is Yusuf Rossi and my zip is 19122. I need help with my order.
Assistant: {{"tool_calls": [{{"function": {{"name": "find_user_id_by_name_zip", "arguments": "{{\\"first_name\\": \\"Yusuf\\", \\"last_name\\": \\"Rossi\\", \\"zip\\": \\"19122\\"}}"}}}}]}}

Example 2 - Getting user details:
User: [Previous tool returned user_id: yusuf_rossi_9620]
Assistant: {{"tool_calls": [{{"function": {{"name": "get_user_details", "arguments": "{{\\"user_id\\": \\"yusuf_rossi_9620\\"}}"}}}}]}}

Example 3 - Getting order details:
User: [User has order #W4776164]
Assistant: {{"tool_calls": [{{"function": {{"name": "get_order_details", "arguments": "{{\\"order_id\\": \\"#W4776164\\"}}"}}}}]}}

Example 4 - Regular conversation (no tool):
User: Thank you for your help!
Assistant: You're welcome! Is there anything else I can help you with today?

Example 5 - Canceling an order:
User: I want to cancel order #W2989580
Assistant: {{"tool_calls": [{{"function": {{"name": "cancel_pending_order", "arguments": "{{\\"order_id\\": \\"#W2989580\\"}}"}}}}]}}

Remember: When you need to use a tool, output ONLY the JSON object, nothing else!
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
        
        # print("DEBUG: Created enhanced_prompt:", enhanced_prompt)
        return enhanced_prompt
    
    def step(self, action: str) -> BaseTextEnvStepOutput:
        """Execute one step in the environment."""
        if not self.task_initialized:
            raise RuntimeError("Environment not initialized. Call init() first.")
        
        self.turns += 1
        
        # Validate input
        assert isinstance(action, str), \
            f"action must be string, got {type(action)}: {repr(action)[:100]}"
        
        # Debug logging for native tool calling
        if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"\n🎯 ENV STEP DEBUG:")
            print(f"   use_native_tool_calling: {self.use_native_tool_calling}")
            print(f"   action type: {type(action)}")
            print(f"   action length: {len(action)}")
            # Check if action looks like JSON
            if action.strip().startswith('{'):
                print(f"   action appears to be JSON")
            else:
                print(f"   action appears to be plain text")
        
        # Parse agent's LLM response to tau_bench Action
        if self.use_native_tool_calling:
            # Use simple parser for structured tool calling responses
            parsed_action = parse_tool_calling_response(action, source="agent")
        else:
            # Use complex parser for text-based responses
            parsed_action = parse_llm_response(action, self.tools_info, source="agent")
        
        assert hasattr(parsed_action, 'name') and hasattr(parsed_action, 'kwargs'), \
            f"Invalid parsed_action: {parsed_action}"
        
        # Store agent action (except for respond actions)
        if parsed_action.name != RESPOND_ACTION_NAME:
            self.agent_actions.append(parsed_action)
        
        # Execute action in tau_bench environment
        tau_result = self.tau_env.step(parsed_action)
        assert hasattr(tau_result, 'observation') and hasattr(tau_result, 'done'), \
            f"Invalid tau_result structure: {tau_result}"
        
        # Update conversation history with agent's response
        agent_message = {"role": "assistant", "content": action}
        assert isinstance(action, str) and len(action) > 0, "Agent action must be non-empty string"
        self.conversation_history.append(agent_message)
        
        # Check if conversation is done
        done = tau_result.done or self.turns >= self.max_turns
        
        # Prepare observations for next turn
        observations = []
        if not done:
            # Handle the response from tau_bench environment
            if parsed_action.name != RESPOND_ACTION_NAME:
                # Tool was used, tau_result.observation contains tool result
                tool_result = self._clean_tool_result(tau_result.observation)
                observations.append({
                    "role": "tool", 
                    "content": tool_result
                })
            else:
                # Agent made a conversational response, tau_result.observation contains user's next message
                user_response = self._clean_user_response(tau_result.observation)
                observations.append({
                    "role": "user",
                    "content": user_response
                })
            
            # Assert observation structure
            assert len(observations) == 1, f"Expected 1 observation, got {len(observations)}"
            assert observations[0]["role"] in ["tool", "user"], f"Invalid role: {observations[0]['role']}"
            assert "content" in observations[0], "Observation missing content field"
            # Note: Empty content is valid (e.g., think tool can return empty string)
            
            # Update conversation history with the new observation
            assert all("role" in obs and "content" in obs for obs in observations), \
                "All observations must have role and content"
            self.conversation_history.extend(observations)
            
            # Assert conversation consistency
            assert len(self.conversation_history) >= 2, "Conversation must have at least system+user messages"
            assert self.conversation_history[0]["role"] == "system", "First message must be system"
            assert self.conversation_history[-1]["role"] in ["user", "tool"], \
                f"Last message role must be user or tool, got: {self.conversation_history[-1]['role']}"
        
        # Log complete conversation rollouts for observability (AFTER conversation history is updated)
        # if os.environ.get("DEBUG_PARSER", "0") == "1" and self.turns % 5 == 0:  # Log every 5 turns
            # self._log_conversation_rollout(parsed_action, tau_result)
            
        # Calculate reward if conversation is done
        reward = tau_result.reward if done else 0.0
        
        # Mark as done
        if done:
            self.conversation_done = True
            
            # Log conversation rollout for debugging (limit to 4 per epoch)
            if os.environ.get("DEBUG_PARSER", "0") == "1":
                # Track how many conversations we've logged
                if not hasattr(self.__class__, '_conversations_logged'):
                    self.__class__._conversations_logged = 0
                    self.__class__._last_log_time = 0
                
                # Reset counter every ~30 minutes (roughly an epoch)
                import time
                current_time = time.time()
                if current_time - self.__class__._last_log_time > 1800:  # 30 minutes
                    self.__class__._conversations_logged = 0
                    self.__class__._last_log_time = current_time
                
                # Only log first 4 conversations per epoch
                if self.__class__._conversations_logged < 4:
                    self._log_conversation_rollout(parsed_action, tau_result)
                    self.__class__._conversations_logged += 1

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
        
    def _log_conversation_rollout(self, parsed_action, tau_result):
        """Log complete conversation rollout for observability"""
        print(f"\n{'='*80}")
        print(f"CONVERSATION ROLLOUT (Turn {self.turns}/{self.max_turns})")
        print(f"Domain: {self.domain} | Task: {self.instruction[:100]}...")
        print(f"{'='*80}")
        
        # Show last few conversation turns (up to 6 messages)
        recent_history = self.conversation_history[-6:] if len(self.conversation_history) >= 6 else self.conversation_history
        
        for i, msg in enumerate(recent_history):
            role = msg["role"].upper()
            content = msg["content"]
            
            if role == "USER":
                print(f"\n🧑 USER:")
                print(f"   {content}")
            elif role == "ASSISTANT":
                print(f"\n🤖 ASSISTANT:")
                # Try to parse if it's a tool call
                try:
                    if content.strip().startswith('{') and 'tool_calls' in content:
                        parsed = json.loads(content.strip())
                        if 'tool_calls' in parsed:
                            tool_call = parsed['tool_calls'][0]
                            func_name = tool_call['function']['name']
                            func_args = tool_call['function']['arguments']
                            print(f"   🔧 TOOL CALL: {func_name}")
                            print(f"   📋 ARGUMENTS: {func_args}")
                        else:
                            print(f"   💬 RESPONSE: {content[:200]}{'...' if len(content) > 200 else ''}")
                    else:
                        print(f"   💬 RESPONSE: {content[:200]}{'...' if len(content) > 200 else ''}")
                except:
                    print(f"   💬 RESPONSE: {content[:200]}{'...' if len(content) > 200 else ''}")
            elif role == "TOOL":
                print(f"\n⚙️  TOOL RESULT:")
                print(f"   {content[:300]}{'...' if len(content) > 300 else ''}")
        
        # Show current action details
        print(f"\n🎯 CURRENT ACTION:")
        print(f"   Tool: {parsed_action.name}")
        print(f"   Args: {parsed_action.kwargs}")
        
        # Show environment result
        print(f"\n📊 ENV RESULT:")
        print(f"   Done: {tau_result.done}")
        print(f"   Reward: {getattr(tau_result, 'reward', 'N/A')}")
        print(f"   Next obs length: {len(str(tau_result.observation))}")
        print(f"{'='*80}\n")
    
    def _clean_user_response(self, user_response: str) -> str:
        """Clean user response from GPT-4o by removing model-specific tokens."""
        if not isinstance(user_response, str):
            return str(user_response)
        
        # Remove common model-specific tokens that might interfere
        tokens_to_strip = [
            '<|im_end|>', '<|endoftext|>', '<|im_start|>', 
            '<eos>', '<bos>', '\x07', '\x00'
        ]
        
        cleaned = user_response
        for token in tokens_to_strip:
            cleaned = cleaned.replace(token, '')
        
        # Clean up extra whitespace
        cleaned = cleaned.strip()
        
        # Debug logging for user response cleaning
        if os.environ.get("DEBUG_PARSER", "0") == "1" and cleaned != user_response:
            print(f"\n🧹 CLEANED USER RESPONSE:")
            print(f"   Original: {repr(user_response[:200])}")
            print(f"   Cleaned:  {repr(cleaned[:200])}")
        
        return cleaned
    
    def _clean_tool_result(self, tool_result: str) -> str:
        """Clean tool result by ensuring it's properly formatted."""
        if not isinstance(tool_result, str):
            return str(tool_result)
        
        # Tool results should generally be clean, but ensure no token contamination
        cleaned = tool_result.strip()
        
        # Debug logging for tool results
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"\n🔧 TOOL RESULT: {repr(cleaned[:200])}{'...' if len(cleaned) > 200 else ''}")
        
        return cleaned