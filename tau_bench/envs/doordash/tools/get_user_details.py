"""Get user details tool for DoorDash domain."""

import json
from typing import Dict, Any


def get_user_details(user_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific user.
    
    Args:
        user_id: The ID of the user to get details for
    
    Returns:
        Dict containing user details
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
        
        return {
            "success": True,
            "user": user
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get user details: {str(e)}"
        } 