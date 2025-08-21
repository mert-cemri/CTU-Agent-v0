"""
LLM Judge integration for tau_bench RL training.
Provides granular feedback during conversation to improve RL rewards.
"""

import os
import logging
from typing import Dict, List, Optional, Tuple
from llm_judge import MASTLLMJudge

logger = logging.getLogger(__name__)


class TauBenchLLMJudge:
    """Wrapper for MASTLLMJudge integrated with tau_bench environment."""
    
    def __init__(self, enabled: bool = False, api_key: Optional[str] = None, alpha: float = 1.0):
        """
        Initialize the LLM judge integration.
        
        Args:
            enabled: Whether to enable LLM judge evaluation
            api_key: OpenAI API key (optional, will use env var if not provided)
            alpha: Weighting factor for judge reward (default: 1.0)
        """
        self.enabled = enabled
        self.alpha = alpha
        self.judge = None
        
        if self.enabled:
            try:
                self.judge = MASTLLMJudge(api_key=api_key)
                logger.info("✓ LLM Judge initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize LLM Judge: {e}")
                logger.error("Disabling LLM Judge evaluation")
                self.enabled = False
    
    def format_trace_for_evaluation(self, messages: List[Dict]) -> str:
        """
        Convert tau_bench conversation messages to evaluable trace format.
        
        Args:
            messages: List of conversation messages from tau_bench
            
        Returns:
            Formatted trace string for LLM judge evaluation
        """
        trace_parts = []
        trace_parts.append("=== TAU-BENCH CONVERSATION TRACE ===\n")
        
        for i, msg in enumerate(messages):
            role = msg.get('role', 'unknown')
            content = msg.get('content', '')
            
            # Handle tool calls
            if 'tool_calls' in msg and msg['tool_calls']:
                try:
                    tool_call = msg['tool_calls'][0]
                    function_name = tool_call.get('function', {}).get('name', 'unknown_function')
                    arguments = tool_call.get('function', {}).get('arguments', '{}')
                    trace_parts.append(f"[Step {i+1}] AGENT: Tool call - {function_name}({arguments})")
                except (IndexError, KeyError, TypeError) as e:
                    trace_parts.append(f"[Step {i+1}] AGENT: Malformed tool call - {content[:100]}...")
            
            # Handle tool responses
            elif role == 'tool':
                tool_name = msg.get('name', 'unknown_tool')
                trace_parts.append(f"[Step {i+1}] SYSTEM ({tool_name}): {content}")
            
            # Handle regular messages
            elif role == 'assistant':
                trace_parts.append(f"[Step {i+1}] AGENT: {content}")
            elif role == 'user':
                trace_parts.append(f"[Step {i+1}] USER: {content}")
            elif role == 'system':
                trace_parts.append(f"[Step {i+1}] SYSTEM: {content}")
            else:
                trace_parts.append(f"[Step {i+1}] {role.upper()}: {content}")
        
        trace_parts.append("\n=== END TRACE ===")
        return "\n".join(trace_parts)
    
    def evaluate_conversation_step(self, messages: List[Dict]) -> Dict:
        """
        Evaluate current conversation state for failure modes.
        
        Args:
            messages: Current conversation messages
            
        Returns:
            Dictionary with evaluation results or None if disabled/failed
        """
        if not self.enabled or not self.judge:
            return {
                "enabled": False,
                "reward_bonus": 0.0,
                "evaluation": None
            }
        
        try:
            # Format messages for evaluation
            trace = self.format_trace_for_evaluation(messages)
            
            # Get LLM judge evaluation
            evaluation = self.judge.evaluate_trace(trace)
            
            # Calculate reward bonus: 1/total_failures (with safety checks)
            total_failures = evaluation.get('total_failures', 14)  # Default to max failures
            
            # Reward calculation: higher bonus for fewer failures, weighted by alpha
            if total_failures == 0:
                reward_bonus = self.alpha * 1.0  # Perfect score gets max bonus
            else:
                reward_bonus = self.alpha * (1.0 / total_failures)
            
            # Log evaluation for debugging
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"LLM Judge Evaluation:")
                logger.debug(f"  Total failures: {total_failures}")
                logger.debug(f"  Reward bonus: {reward_bonus:.3f}")
                logger.debug(f"  Summary: {evaluation.get('summary', 'No summary')}")
            
            return {
                "enabled": True,
                "reward_bonus": reward_bonus,
                "evaluation": evaluation,
                "trace_length": len(messages)
            }
            
        except Exception as e:
            logger.error(f"Error evaluating conversation: {e}")
            return {
                "enabled": True,
                "reward_bonus": 0.0,
                "evaluation": None,
                "error": str(e)
            }
    


def create_judge_from_config(config: Dict) -> TauBenchLLMJudge:
    """
    Create LLM judge from configuration.
    
    Args:
        config: Configuration dictionary or config object
        
    Returns:
        TauBenchLLMJudge instance
    """
    # Handle both dict and OmegaConf objects
    if hasattr(config, 'get'):
        # Dict-like access
        enabled = config.get('TAXONOMY_FEEDBACK', False)
        api_key = config.get('OPENAI_API_KEY', None)
        alpha = config.get('TAXONOMY_ALPHA', 1.0)
    else:
        # Attribute access (OmegaConf)
        enabled = getattr(config, 'TAXONOMY_FEEDBACK', False)
        api_key = getattr(config, 'OPENAI_API_KEY', None)
        alpha = getattr(config, 'TAXONOMY_ALPHA', 1.0)
    
    # Also check environment variables
    if enabled is False:
        enabled = os.environ.get('TAXONOMY_FEEDBACK', 'false').lower() == 'true'
    
    if api_key is None:
        api_key = os.environ.get('OPENAI_API_KEY', None)
    
    try:
        alpha = float(os.environ.get('TAXONOMY_ALPHA', alpha))
    except (ValueError, TypeError):
        alpha = 1.0
    
    return TauBenchLLMJudge(enabled=enabled, api_key=api_key, alpha=alpha)