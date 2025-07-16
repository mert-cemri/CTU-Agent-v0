# Copyright Sierra

from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Union
from datetime import datetime

class SFTConversationTurn(BaseModel):
    role: str  # "system", "user", "assistant", "tool"
    content: str
    tool_calls: Optional[List[Dict[str, Any]]] = None
    tool_call_id: Optional[str] = None
    name: Optional[str] = None  # tool name for tool messages

class SFTConversation(BaseModel):
    conversation_id: str
    domain: str  # "airline" or "retail"
    task_id: int
    agent_strategy: str
    user_strategy: str
    success: bool  # reward == 1.0
    turns: List[SFTConversationTurn]
    metadata: Dict[str, Any]
    
    # Quality metrics
    num_turns: int = 0
    num_tool_calls: int = 0
    total_cost: Optional[float] = None
    generation_time: Optional[float] = None

class SFTDataset(BaseModel):
    conversations: List[SFTConversation]
    generation_config: Dict[str, Any]
    statistics: Dict[str, Any]
    
    def filter_successful(self) -> 'SFTDataset':
        """Keep only successful conversations (reward == 1.0)"""
        filtered_convs = [conv for conv in self.conversations if conv.success]
        return SFTDataset(
            conversations=filtered_convs,
            generation_config=self.generation_config,
            statistics=self._compute_statistics(filtered_convs)
        )
    
    def filter_by_length(self, min_turns: int = 3, max_turns: int = 50) -> 'SFTDataset':
        """Filter conversations by turn count"""
        filtered_convs = [
            conv for conv in self.conversations 
            if min_turns <= conv.num_turns <= max_turns
        ]
        return SFTDataset(
            conversations=filtered_convs,
            generation_config=self.generation_config,
            statistics=self._compute_statistics(filtered_convs)
        )
    
    def export_openai_format(self, output_path: str):
        """Export in OpenAI fine-tuning format"""
        import json
        with open(output_path, 'w') as f:
            for conv in self.conversations:
                messages = []
                for turn in conv.turns:
                    msg = {"role": turn.role, "content": turn.content}
                    if turn.tool_calls:
                        msg["tool_calls"] = turn.tool_calls
                    if turn.tool_call_id:
                        msg["tool_call_id"] = turn.tool_call_id
                    if turn.name:
                        msg["name"] = turn.name
                    messages.append(msg)
                
                entry = {
                    "messages": messages,
                    "metadata": {
                        "conversation_id": conv.conversation_id,
                        "domain": conv.domain,
                        "task_id": conv.task_id,
                        "agent_strategy": conv.agent_strategy,
                        "user_strategy": conv.user_strategy,
                        "success": conv.success,
                        "task_instruction": conv.metadata.get("task_instruction")
                    }
                }
                f.write(json.dumps(entry) + '\n')
    
    def export_alpaca_format(self, output_path: str):
        """Export in Alpaca format (instruction-response pairs)"""
        import json
        alpaca_data = []
        
        for conv in self.conversations:
            # Extract instruction from first user message
            instruction = ""
            response = ""
            
            for i, turn in enumerate(conv.turns):
                if turn.role == "user" and i == 1:  # Skip system, take first user
                    instruction = turn.content
                elif turn.role == "assistant":
                    response += turn.content + "\n"
            
            if instruction and response:
                alpaca_data.append({
                    "instruction": instruction.strip(),
                    "input": "",
                    "output": response.strip(),
                    "metadata": {
                        "conversation_id": conv.conversation_id,
                        "domain": conv.domain,
                        "success": conv.success,
                        "task_instruction": conv.metadata.get("task_instruction")
                    }
                })
        
        with open(output_path, 'w') as f:
            json.dump(alpaca_data, f, indent=2)
    
    def _compute_statistics(self, conversations: List[SFTConversation]) -> Dict[str, Any]:
        """Compute dataset statistics"""
        if not conversations:
            return {}
        
        total_convs = len(conversations)
        successful_convs = sum(1 for conv in conversations if conv.success)
        total_turns = sum(conv.num_turns for conv in conversations)
        total_tool_calls = sum(conv.num_tool_calls for conv in conversations)
        
        # Strategy distribution
        agent_strategies = {}
        user_strategies = {}
        domains = {}
        
        for conv in conversations:
            agent_strategies[conv.agent_strategy] = agent_strategies.get(conv.agent_strategy, 0) + 1
            user_strategies[conv.user_strategy] = user_strategies.get(conv.user_strategy, 0) + 1
            domains[conv.domain] = domains.get(conv.domain, 0) + 1
        
        return {
            "total_conversations": total_convs,
            "successful_conversations": successful_convs,
            "success_rate": successful_convs / total_convs if total_convs > 0 else 0,
            "avg_turns_per_conversation": total_turns / total_convs if total_convs > 0 else 0,
            "avg_tool_calls_per_conversation": total_tool_calls / total_convs if total_convs > 0 else 0,
            "agent_strategy_distribution": agent_strategies,
            "user_strategy_distribution": user_strategies,
            "domain_distribution": domains,
            "generation_timestamp": datetime.now().isoformat()
        }

class SFTConfig(BaseModel):
    # Strategy combinations
    agent_strategies: List[str] = ["tool-calling", "react", "act"]
    user_strategies: List[str] = ["llm", "react", "verify", "reflection"]
    num_conversations_per_combination: int = 50
    
    # Per-task conversation generation (NEW approach)
    conversations_per_task: int = 5
    
    # Domain and task selection
    domains: List[str] = ["airline", "retail"]
    task_splits: List[str] = ["train", "test"]
    task_id_ranges: Optional[Dict[str, List[int]]] = None  # Custom task ranges per domain
    
    # Quality control
    filter_successful_only: bool = True
    min_conversation_turns: int = 3
    max_conversation_turns: int = 50
    enable_deduplication: bool = True
    
    # Model configuration
    temperature_range: List[float] = [0.0, 0.3, 0.7]
    model_configs: List[Dict[str, str]] = [
        {"model": "gpt-4", "provider": "openai"},
        {"model": "claude-3-sonnet-20240229", "provider": "anthropic"}
    ]
    
    # Export settings
    output_formats: List[str] = ["openai"]  # "openai", "alpaca", "sharegpt"
    
    # Generation control
    max_parallel_generations: int = 4
    enable_cost_tracking: bool = True
    max_total_cost: Optional[float] = None
    
    # Reproducibility control
    seed: int = 42
    enable_shuffle: bool = True  # Task shuffling for diversity
    
    # Quality metrics
    enable_quality_scoring: bool = True
    quality_threshold: float = 0.7