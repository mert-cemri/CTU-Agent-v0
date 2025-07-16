"""Get user order history tool for DoorDash domain."""

import json
from typing import Dict, Any


def get_user_order_history(user_id: str, limit: int = 10) -> Dict[str, Any]:
    """
    Get the order history for a specific user.
    
    Args:
        user_id: The ID of the user
        limit: Maximum number of orders to return
    
    Returns:
        Dict containing order history
    """
    try:
        # Load user data
        with open("envs/doordash/data/users.json", "r") as f:
            users = json.load(f)
        
        # Find the user
        user = None
        for u in users:
            if u["user_id"] == user_id:
                user = u
                break
        
        if not user:
            return {
                "success": False,
                "error": f"User with ID {user_id} not found"
            }
        
        # Get order history from user data
        order_history = user.get("order_history", [])
        
        # Limit results
        limited_history = order_history[:limit]
        
        return {
            "success": True,
            "user_id": user_id,
            "order_history": limited_history,
            "total_orders": len(order_history),
            "returned_count": len(limited_history)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get user order history: {str(e)}"
        } 