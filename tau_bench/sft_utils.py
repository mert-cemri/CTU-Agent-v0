# Copyright Sierra

import json
import hashlib
from typing import List, Dict, Any, Set
from tau_bench.sft_types import SFTConversation, SFTConversationTurn


class SFTMessageProcessor:
    @staticmethod
    def process_agent_message(message: Dict[str, Any]) -> List[SFTConversationTurn]:
        # Handle tool calls properly
        # Split assistant messages with tool calls into separate turns
        pass
    
    @staticmethod
    def process_tool_response(message: Dict[str, Any]) -> SFTConversationTurn:
        # Format tool responses
        pass
    
    @staticmethod
    def process_user_message(message: Dict[str, Any]) -> SFTConversationTurn:
        # Format user messages
        pass


def calculate_conversation_quality_score(conversation: SFTConversation) -> float:
    """Calculate a quality score for a conversation based on various metrics"""
    score = 0.0
    max_score = 100.0
    
    # Success bonus (30 points)
    if conversation.success:
        score += 30.0
    
    # Turn count score (20 points) - reward conversations with reasonable length
    if 5 <= conversation.num_turns <= 20:
        score += 20.0
    elif 3 <= conversation.num_turns <= 30:
        score += 15.0
    elif conversation.num_turns >= 3:
        score += 10.0
    
    # Tool usage score (25 points)
    if conversation.num_tool_calls > 0:
        score += 15.0
        if conversation.num_tool_calls >= 3:
            score += 10.0  # Bonus for multiple tool interactions
    
    # Content quality score (25 points)
    content_score = calculate_content_quality(conversation.turns)
    score += content_score * 25.0
    
    return min(score / max_score, 1.0)


def calculate_content_quality(turns: List[SFTConversationTurn]) -> float:
    """Calculate quality score based on conversation content"""
    if not turns:
        return 0.0
    
    quality_indicators = 0
    total_indicators = 6
    
    # Has meaningful user messages
    user_messages = [turn for turn in turns if turn.role == "user" and len(turn.content.strip()) > 10]
    if len(user_messages) >= 2:
        quality_indicators += 1
    
    # Has meaningful assistant responses
    assistant_messages = [turn for turn in turns if turn.role == "assistant" and len(turn.content.strip()) > 10]
    if len(assistant_messages) >= 2:
        quality_indicators += 1
    
    # Has tool interactions
    tool_calls = [turn for turn in turns if turn.tool_calls and len(turn.tool_calls) > 0]
    if len(tool_calls) > 0:
        quality_indicators += 1
    
    # Has tool responses
    tool_responses = [turn for turn in turns if turn.role == "tool"]
    if len(tool_responses) > 0:
        quality_indicators += 1
    
    # No extremely long messages (indicates potential errors)
    has_reasonable_length = all(len(turn.content) < 2000 for turn in turns)
    if has_reasonable_length:
        quality_indicators += 1
    
    # Conversation has good flow (alternating user/assistant)
    has_good_flow = check_conversation_flow(turns)
    if has_good_flow:
        quality_indicators += 1
    
    return quality_indicators / total_indicators


def check_conversation_flow(turns: List[SFTConversationTurn]) -> bool:
    """Check if conversation has reasonable flow between user and assistant"""
    if len(turns) < 3:
        return False
    
    # Look for alternating pattern (allowing for tool calls/responses)
    user_assistant_turns = [turn for turn in turns if turn.role in ["user", "assistant"]]
    
    if len(user_assistant_turns) < 2:
        return False
    
    # Check if it generally alternates
    consecutive_same_role = 0
    for i in range(1, len(user_assistant_turns)):
        if user_assistant_turns[i].role == user_assistant_turns[i-1].role:
            consecutive_same_role += 1
    
    # Allow some flexibility but not too many consecutive same-role messages
    return consecutive_same_role < len(user_assistant_turns) * 0.3


def deduplicate_by_content_similarity(conversations: List[SFTConversation], threshold: float = 0.8) -> List[SFTConversation]:
    """Remove conversations that are too similar based on content"""
    unique_conversations = []
    seen_signatures = set()
    
    for conv in conversations:
        signature = create_conversation_signature(conv)
        
        # Check similarity with existing conversations
        is_duplicate = False
        for existing_sig in seen_signatures:
            if calculate_signature_similarity(signature, existing_sig) > threshold:
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique_conversations.append(conv)
            seen_signatures.add(signature)
    
    return unique_conversations


def create_conversation_signature(conversation: SFTConversation) -> str:
    """Create a signature for conversation based on structure and key content"""
    signature_parts = []
    
    # Add conversation metadata
    signature_parts.append(f"domain:{conversation.domain}")
    signature_parts.append(f"agent:{conversation.agent_strategy}")
    signature_parts.append(f"user:{conversation.user_strategy}")
    
    # Add turn structure
    turn_pattern = []
    for turn in conversation.turns:
        if turn.role == "user":
            turn_pattern.append("U")
        elif turn.role == "assistant":
            turn_pattern.append("A")
        elif turn.role == "tool":
            turn_pattern.append("T")
        elif turn.role == "system":
            turn_pattern.append("S")
    
    signature_parts.append(f"pattern:{''.join(turn_pattern)}")
    
    # Add key content hashes (first and last few turns)
    content_turns = [turn for turn in conversation.turns if turn.role in ["user", "assistant"]]
    if content_turns:
        # First turn content
        first_turn_hash = hashlib.md5(content_turns[0].content.encode()).hexdigest()[:8]
        signature_parts.append(f"first:{first_turn_hash}")
        
        # Last turn content  
        last_turn_hash = hashlib.md5(content_turns[-1].content.encode()).hexdigest()[:8]
        signature_parts.append(f"last:{last_turn_hash}")
    
    return "|".join(signature_parts)


def calculate_signature_similarity(sig1: str, sig2: str) -> float:
    """Calculate similarity between two conversation signatures"""
    parts1 = set(sig1.split("|"))
    parts2 = set(sig2.split("|"))
    
    intersection = len(parts1.intersection(parts2))
    union = len(parts1.union(parts2))
    
    return intersection / union if union > 0 else 0.0


def analyze_dataset_diversity(conversations: List[SFTConversation]) -> Dict[str, Any]:
    """Analyze diversity metrics for a dataset"""
    if not conversations:
        return {}
    
    # Strategy diversity
    agent_strategies = set(conv.agent_strategy for conv in conversations)
    user_strategies = set(conv.user_strategy for conv in conversations)
    domains = set(conv.domain for conv in conversations)
    
    # Length diversity
    turn_counts = [conv.num_turns for conv in conversations]
    tool_call_counts = [conv.num_tool_calls for conv in conversations]
    
    # Content diversity (based on unique signatures)
    signatures = [create_conversation_signature(conv) for conv in conversations]
    unique_signatures = set(signatures)
    
    return {
        "strategy_diversity": {
            "agent_strategies": len(agent_strategies),
            "user_strategies": len(user_strategies),
            "domains": len(domains),
            "total_combinations": len(agent_strategies) * len(user_strategies) * len(domains)
        },
        "length_diversity": {
            "min_turns": min(turn_counts) if turn_counts else 0,
            "max_turns": max(turn_counts) if turn_counts else 0,
            "avg_turns": sum(turn_counts) / len(turn_counts) if turn_counts else 0,
            "min_tool_calls": min(tool_call_counts) if tool_call_counts else 0,
            "max_tool_calls": max(tool_call_counts) if tool_call_counts else 0,
            "avg_tool_calls": sum(tool_call_counts) / len(tool_call_counts) if tool_call_counts else 0
        },
        "content_diversity": {
            "total_conversations": len(conversations),
            "unique_signatures": len(unique_signatures),
            "diversity_ratio": len(unique_signatures) / len(conversations) if conversations else 0
        }
    }


def export_conversation_to_messages(conversation: SFTConversation) -> List[Dict[str, Any]]:
    """Convert SFT conversation to standard messages format"""
    messages = []
    
    for turn in conversation.turns:
        message = {
            "role": turn.role,
            "content": turn.content
        }
        
        if turn.tool_calls:
            message["tool_calls"] = turn.tool_calls
        
        if turn.tool_call_id:
            message["tool_call_id"] = turn.tool_call_id
            
        if turn.name:
            message["name"] = turn.name
            
        messages.append(message)
    
    return messages