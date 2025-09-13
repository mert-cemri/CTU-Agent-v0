"""Cancel order tool for DoorDash domain."""

import json
from typing import Dict, Any


def cancel_order(order_id: str, reason: str = None) -> Dict[str, Any]:
    """
    Cancel an existing order.
    
    Args:
        order_id: The ID of the order to cancel
        reason: Optional reason for cancellation
    
    Returns:
        Dict containing cancellation result
    """
    try:
        # Load order data
        with open("envs/doordash/data/orders.json", "r") as f:
            orders = json.load(f)
        
        # Find the order
        order = None
        order_index = None
        for i, o in enumerate(orders):
            if o["order_id"] == order_id:
                order = o
                order_index = i
                break
        
        if not order:
            return {
                "success": False,
                "error": f"Order with ID {order_id} not found"
            }
        
        # Check if order can be cancelled
        current_status = order.get("status", "")
        if current_status in ["delivered", "cancelled"]:
            return {
                "success": False,
                "error": f"Cannot cancel order {order_id} - order is already {current_status}"
            }
        
        if current_status == "out_for_delivery":
            return {
                "success": False,
                "error": f"Cannot cancel order {order_id} - order is out for delivery"
            }
        
        # Cancel the order
        order["status"] = "cancelled"
        order["cancellation_reason"] = reason or "Customer requested"
        
        # Calculate refund amount (usually full amount for early cancellation)
        refund_amount = order.get("total", 0)
        
        # Note: In a real implementation, you would save back to the file
        # For this demo, we'll just return the cancelled order
        
        return {
            "success": True,
            "message": f"Order {order_id} cancelled successfully",
            "order": order,
            "refund_amount": refund_amount,
            "cancellation_reason": reason or "Customer requested"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to cancel order: {str(e)}"
        } 