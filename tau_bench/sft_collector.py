# Copyright Sierra

import json
import uuid
import time
from typing import List, Dict, Any, Optional
from tau_bench.sft_types import SFTConversation, SFTConversationTurn, SFTDataset, SFTConfig
from tau_bench.types import SolveResult, EnvRunResult


class SFTDataCollector:
    def __init__(self, config: Optional[SFTConfig] = None):
        self.conversations: List[SFTConversation] = []
        self.config = config or SFTConfig()
        self.total_cost = 0.0
        self.failed_conversions = 0
        self.conversion_errors = []
    
    def collect_from_env_result(
        self, 
        result: EnvRunResult,
        domain: str,
        agent_strategy: str,
        user_strategy: str,
        agent_model: str = "",
        user_model: str = ""
    ) -> Optional[SFTConversation]:
        """Convert an EnvRunResult to SFT conversation format"""
        try:
            if not result.traj:
                return None
                
            conversation_id = f"{domain}_{result.task_id}_{agent_strategy}_{user_strategy}_{uuid.uuid4().hex[:8]}"
            turns = []
            tool_call_count = 0
            
            # Convert trajectory messages to SFT format
            for i, msg in enumerate(result.traj):
                if msg is None:
                    continue
                    
                turn = self._convert_message_to_turn(msg, i)
                if turn:
                    turns.append(turn)
                    if turn.tool_calls:
                        tool_call_count += len(turn.tool_calls)
            
            # Extract cost from result info if available
            conversation_cost = self._extract_cost_from_result(result)
            
            # Extract task instruction for metadata
            task_instruction = self._extract_task_instruction(result)
            
            # Create conversation
            conversation = SFTConversation(
                conversation_id=conversation_id,
                domain=domain,
                task_id=result.task_id,
                agent_strategy=agent_strategy,
                user_strategy=user_strategy,
                success=(result.reward >= 0.99),  # Consider reward >= 0.99 as success
                turns=turns,
                num_turns=len(turns),
                num_tool_calls=tool_call_count,
                total_cost=conversation_cost,
                metadata={
                    "trial": result.trial,
                    "agent_model": agent_model,
                    "user_model": user_model,
                    "original_reward": result.reward,
                    "task_instruction": task_instruction,
                    "task_id_mapping_preserved": True,  # New integrity guarantee
                    "instruction_source": "tau_bench_original",
                    "generation_info": result.info,
                    "conversion_timestamp": time.time()
                }
            )
            
            return conversation
            
        except Exception as e:
            self.failed_conversions += 1
            error_details = {
                "task_id": result.task_id,
                "domain": domain,
                "agent_strategy": agent_strategy,
                "user_strategy": user_strategy,
                "error": str(e),
                "error_type": type(e).__name__,
                "timestamp": time.time()
            }
            
            # Add more debugging info
            try:
                error_details["result_info_type"] = str(type(result.info))
                error_details["result_traj_length"] = len(result.traj) if result.traj else 0
                if result.traj and len(result.traj) > 0:
                    error_details["first_msg_type"] = str(type(result.traj[0]))
            except:
                pass
                
            self.conversion_errors.append(error_details)
            print(f"⚠️ Failed to convert conversation for task {result.task_id}: {str(e)}")
            print(f"    Error type: {type(e).__name__}")
            import traceback
            print(f"    Traceback: {traceback.format_exc()}")
            return None
    
    def _extract_cost_from_result(self, result: EnvRunResult) -> Optional[float]:
        """Extract cost information from the result"""
        try:
            # Look for cost information in various places
            if hasattr(result, 'info') and result.info is not None:
                # Check for user_cost in info
                if hasattr(result.info, 'user_cost') and result.info.user_cost is not None:
                    return float(result.info.user_cost)
                
                # Check for cost in other info fields
                if isinstance(result.info, dict):
                    for key in ['total_cost', 'cost', 'user_cost', 'generation_cost']:
                        if key in result.info and result.info[key] is not None:
                            return float(result.info[key])
                elif hasattr(result.info, '__dict__'):
                    # Handle object with attributes
                    for key in ['total_cost', 'cost', 'user_cost', 'generation_cost']:
                        if hasattr(result.info, key):
                            value = getattr(result.info, key)
                            if value is not None:
                                return float(value)
            
            # Look in trajectory for cost information
            if result.traj:
                total_cost = 0.0
                for msg in result.traj:
                    if isinstance(msg, dict) and 'cost' in msg and msg['cost'] is not None:
                        total_cost += float(msg['cost'])
                if total_cost > 0:
                    return total_cost
                    
            return None
            
        except (ValueError, TypeError, AttributeError) as e:
            # Log the specific error for debugging
            print(f"    Warning: Cost extraction failed: {str(e)}")
            return None
    
    def _convert_message_to_turn(self, msg: Dict[str, Any], index: int) -> Optional[SFTConversationTurn]:
        """Convert a single message from tau-bench format to SFT turn format"""
        
        try:
            # Handle None messages
            if msg is None:
                return None
                
            # Handle different message formats from tau-bench
            if isinstance(msg, dict):
                role = msg.get("role", "")
                content = msg.get("content", "")
                
                # Handle tool calls in assistant messages
                tool_calls = None
                if "tool_calls" in msg and msg["tool_calls"]:
                    tool_calls = self._normalize_tool_calls(msg["tool_calls"])
                elif role == "assistant" and "function_call" in msg:
                    # Convert legacy function_call to tool_calls format
                    func_call = msg["function_call"]
                    if func_call is not None:
                        tool_calls = [{
                            "id": f"call_{uuid.uuid4().hex[:8]}",
                            "type": "function",
                            "function": {
                                "name": func_call.get("name", "") if func_call else "",
                                "arguments": func_call.get("arguments", "{}") if func_call else "{}"
                            }
                        }]
                elif role == "assistant" and self._looks_like_tool_call(content):
                    # Handle cases where tool calls are embedded in content
                    tool_calls = self._extract_tool_calls_from_content(content)
                
                # Handle tool response messages
                tool_call_id = msg.get("tool_call_id")
                name = msg.get("name")  # Function/tool name for tool messages
                
                # Clean up content
                content = self._clean_message_content(content, role)
                
                # Skip empty messages unless they have tool calls
                if not content and not tool_calls:
                    return None
                    
                turn = SFTConversationTurn(
                    role=role,
                    content=content,
                    tool_calls=tool_calls,
                    tool_call_id=tool_call_id,
                    name=name
                )
                return turn
            else:
                return None
        
        except Exception as e:
            print(f"      Error converting message {index}: {str(e)}")
            return None
    
    def _normalize_tool_calls(self, tool_calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize tool calls to ensure consistent format"""
        normalized = []
        
        for tc in tool_calls:
            if isinstance(tc, dict):
                # Ensure required fields exist
                normalized_tc = {
                    "id": tc.get("id", f"call_{uuid.uuid4().hex[:8]}"),
                    "type": tc.get("type", "function"),
                    "function": {
                        "name": tc.get("function", {}).get("name", "unknown"),
                        "arguments": tc.get("function", {}).get("arguments", "{}")
                    }
                }
                
                # Ensure arguments is a string
                if isinstance(normalized_tc["function"]["arguments"], dict):
                    normalized_tc["function"]["arguments"] = json.dumps(normalized_tc["function"]["arguments"])
                
                normalized.append(normalized_tc)
        
        return normalized if normalized else None
    
    def _looks_like_tool_call(self, content: str) -> bool:
        """Check if content looks like it contains tool call information"""
        if not content:
            return False
        
        # Look for common patterns that indicate tool usage
        tool_indicators = [
            "function_call",
            "tool_call",
            '{"name":',
            '{"function":',
            "action:",
            "invoke"
        ]
        
        content_lower = content.lower()
        return any(indicator in content_lower for indicator in tool_indicators)
    
    def _extract_tool_calls_from_content(self, content: str) -> Optional[List[Dict[str, Any]]]:
        """Extract tool calls from content that has embedded tool call information"""
        try:
            # This is a heuristic approach - in practice, you'd want more sophisticated parsing
            # Look for JSON-like structures in the content
            import re
            
            # Try to find JSON objects that look like function calls
            json_pattern = r'\{[^{}]*"name"[^{}]*\}'
            matches = re.findall(json_pattern, content)
            
            tool_calls = []
            for match in matches:
                try:
                    parsed = json.loads(match)
                    if "name" in parsed:
                        tool_call = {
                            "id": f"call_{uuid.uuid4().hex[:8]}",
                            "type": "function",
                            "function": {
                                "name": parsed["name"],
                                "arguments": json.dumps(parsed.get("arguments", {}))
                            }
                        }
                        tool_calls.append(tool_call)
                except json.JSONDecodeError:
                    continue
            
            return tool_calls if tool_calls else None
            
        except Exception:
            return None
    
    def _clean_message_content(self, content: str, role: str) -> str:
        """Clean and normalize message content"""
        if not content:
            return ""
        
        # Remove excessive whitespace
        content = " ".join(content.split())
        
        # Remove common system artifacts
        artifacts_to_remove = [
            "assistant:",
            "user:",
            "system:",
            "tool:",
            "[INST]",
            "[/INST]"
        ]
        
        for artifact in artifacts_to_remove:
            if content.lower().startswith(artifact.lower()):
                content = content[len(artifact):].strip()
        
        # Handle role-specific cleaning
        if role == "tool":
            # For tool messages, ensure we have clean output
            if content.startswith("Error:"):
                # Keep error messages as-is
                pass
            else:
                # Clean up common tool output artifacts
                content = content.replace("Tool output:", "").strip()
        
        return content
    
    def add_conversation(self, conversation: SFTConversation):
        """Add a conversation to the collection"""
        self.conversations.append(conversation)
        if conversation.total_cost:
            self.total_cost += conversation.total_cost
    
    def filter_successful_only(self) -> 'SFTDataCollector':
        """Return a new collector with only successful conversations"""
        filtered_collector = SFTDataCollector(self.config)
        filtered_collector.conversations = [conv for conv in self.conversations if conv.success]
        filtered_collector.total_cost = sum(
            conv.total_cost or 0 for conv in filtered_collector.conversations
        )
        filtered_collector.failed_conversions = self.failed_conversions
        filtered_collector.conversion_errors = self.conversion_errors
        return filtered_collector
    
    def filter_by_quality(self, min_turns: int = 3, max_turns: int = 50) -> 'SFTDataCollector':
        """Filter conversations by quality metrics"""
        filtered_collector = SFTDataCollector(self.config)
        filtered_collector.conversations = [
            conv for conv in self.conversations 
            if (min_turns <= conv.num_turns <= max_turns and 
                conv.num_tool_calls > 0)  # Require at least some tool usage
        ]
        filtered_collector.total_cost = sum(
            conv.total_cost or 0 for conv in filtered_collector.conversations
        )
        filtered_collector.failed_conversions = self.failed_conversions
        filtered_collector.conversion_errors = self.conversion_errors
        return filtered_collector
    
    def deduplicate_conversations(self) -> 'SFTDataCollector':
        """Remove duplicate conversations based on content similarity"""
        # Simple deduplication based on turn content hashes
        seen_hashes = set()
        filtered_collector = SFTDataCollector(self.config)
        
        for conv in self.conversations:
            # Create a hash based on the conversation content
            content_str = "".join([turn.content for turn in conv.turns])
            content_hash = hash(content_str)
            
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                filtered_collector.conversations.append(conv)
        
        filtered_collector.total_cost = sum(
            conv.total_cost or 0 for conv in filtered_collector.conversations
        )
        filtered_collector.failed_conversions = self.failed_conversions
        filtered_collector.conversion_errors = self.conversion_errors
        return filtered_collector
    
    def to_dataset(self) -> SFTDataset:
        """Convert the collected conversations to an SFTDataset"""
        return SFTDataset(
            conversations=self.conversations,
            generation_config=self.config.model_dump() if self.config else {},
            statistics=self._compute_statistics()
        )
    
    def _compute_statistics(self) -> Dict[str, Any]:
        """Compute statistics for the collected conversations"""
        if not self.conversations:
            return {
                "total_conversations": 0,
                "failed_conversions": self.failed_conversions,
                "conversion_errors": len(self.conversion_errors)
            }
        
        total_convs = len(self.conversations)
        successful_convs = sum(1 for conv in self.conversations if conv.success)
        total_turns = sum(conv.num_turns for conv in self.conversations)
        total_tool_calls = sum(conv.num_tool_calls for conv in self.conversations)
        
        # Strategy distribution
        agent_strategies = {}
        user_strategies = {}
        domains = {}
        
        for conv in self.conversations:
            agent_strategies[conv.agent_strategy] = agent_strategies.get(conv.agent_strategy, 0) + 1
            user_strategies[conv.user_strategy] = user_strategies.get(conv.user_strategy, 0) + 1
            domains[conv.domain] = domains.get(conv.domain, 0) + 1
        
        return {
            "total_conversations": total_convs,
            "successful_conversations": successful_convs,
            "success_rate": successful_convs / total_convs if total_convs > 0 else 0,
            "avg_turns_per_conversation": total_turns / total_convs if total_convs > 0 else 0,
            "avg_tool_calls_per_conversation": total_tool_calls / total_convs if total_convs > 0 else 0,
            "total_generation_cost": self.total_cost,
            "agent_strategy_distribution": agent_strategies,
            "user_strategy_distribution": user_strategies,
            "domain_distribution": domains,
            "failed_conversions": self.failed_conversions,
            "conversion_errors": len(self.conversion_errors),
            "conversion_success_rate": total_convs / (total_convs + self.failed_conversions) if (total_convs + self.failed_conversions) > 0 else 0
        }
    
    def export_to_jsonl(self, path: str, format: str = "openai"):
        """Export conversations in JSONL format"""
        dataset = self.to_dataset()
        
        if format == "openai":
            dataset.export_openai_format(path)
        elif format == "alpaca":
            dataset.export_alpaca_format(path)
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def save_raw_dataset(self, path: str):
        """Save the raw dataset with all metadata"""
        dataset = self.to_dataset()
        with open(path, 'w') as f:
            f.write(dataset.model_dump_json(indent=2))
    
    def save_error_report(self, path: str):
        """Save a report of conversion errors"""
        error_report = {
            "total_errors": len(self.conversion_errors),
            "failed_conversions": self.failed_conversions,
            "errors": self.conversion_errors,
            "timestamp": time.time()
        }
        
        with open(path, 'w') as f:
            json.dump(error_report, f, indent=2)
    
    def get_conversion_statistics(self) -> Dict[str, Any]:
        """Get detailed conversion statistics"""
        total_attempts = len(self.conversations) + self.failed_conversions
        
        return {
            "successful_conversions": len(self.conversations),
            "failed_conversions": self.failed_conversions,
            "total_attempts": total_attempts,
            "conversion_success_rate": len(self.conversations) / total_attempts if total_attempts > 0 else 0,
            "error_count": len(self.conversion_errors),
            "avg_cost_per_conversation": self.total_cost / len(self.conversations) if self.conversations else 0
        }

    def _extract_task_instruction(self, result: EnvRunResult) -> Optional[str]:
        """Extract task instruction from result.info.task.instruction"""
        try:
            if hasattr(result, 'info') and result.info is not None:
                # Handle different possible structures
                if hasattr(result.info, 'task') and result.info.task is not None:
                    # Object with attributes
                    if hasattr(result.info.task, 'instruction') and result.info.task.instruction is not None:
                        return result.info.task.instruction
                elif isinstance(result.info, dict) and 'task' in result.info and result.info['task'] is not None:
                    # Dictionary structure
                    task = result.info['task']
                    if isinstance(task, dict) and 'instruction' in task:
                        return task['instruction']
                    elif hasattr(task, 'instruction'):
                        return task.instruction
            return None
        except Exception as e:
            print(f"    Warning: Task instruction extraction failed: {str(e)}")
            return None