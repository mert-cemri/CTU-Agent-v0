"""Get order status tool for DoorDash domain."""

import json
from typing import Dict, Any


def get_order_status(order_id: str) -> Dict[str, Any]:
    """
    Get the status and details of a specific order.
    
    Args:
        order_id: The ID of the order to check
    
    Returns:
        Dict containing order status and details
    """
    try:
        # Load order data
        with open("envs/doordash/data/orders.json", "r") as f:
            orders = json.load(f)
        
        # Find the order
        order = None
        for o in orders:
            if o["order_id"] == order_id:
                order = o
                break
        
        if not order:
            return {
                "success": False,
                "error": f"Order with ID {order_id} not found"
            }
        
        return {
            "success": True,
            "order": order
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get order status: {str(e)}"
        } 