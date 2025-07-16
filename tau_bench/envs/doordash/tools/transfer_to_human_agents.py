"""Transfer to human agents utility tool for DoorDash domain."""

from typing import Dict, Any


def transfer_to_human_agents(reason: str, context: str = None) -> Dict[str, Any]:
    """
    Transfer the conversation to human agents.
    
    Args:
        reason: Reason for transferring to human agents
        context: Additional context for the transfer
    
    Returns:
        Dict containing transfer result
    """
    return {
        "success": True,
        "action": "transfer_to_human_agents",
        "reason": reason,
        "context": context or "",
        "message": "Transferring to human customer service agents..."
    } 