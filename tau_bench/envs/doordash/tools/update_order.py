"""Update order tool for DoorDash domain."""

import json
from typing import Dict, Any


def update_order(
    order_id: str,
    status: str = None,
    delivery_address: str = None,
    special_instructions: str = None
) -> Dict[str, Any]:
    """
    Update an existing order.
    
    Args:
        order_id: The ID of the order to update
        status: New status for the order
        delivery_address: New delivery address
        special_instructions: New special instructions
    
    Returns:
        Dict containing update result
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
        
        # Check if order can be updated
        if order.get("status") in ["delivered", "cancelled"]:
            return {
                "success": False,
                "error": f"Cannot update order {order_id} - order is {order['status']}"
            }
        
        # Update fields
        updated_fields = []
        if status:
            order["status"] = status
            updated_fields.append("status")
        
        if delivery_address:
            order["delivery_address"] = delivery_address
            updated_fields.append("delivery_address")
        
        if special_instructions:
            order["special_instructions"] = special_instructions
            updated_fields.append("special_instructions")
        
        if not updated_fields:
            return {
                "success": False,
                "error": "No fields provided to update"
            }
        
        # Note: In a real implementation, you would save back to the file
        # For this demo, we'll just return the updated order
        
        return {
            "success": True,
            "message": f"Order {order_id} updated successfully",
            "updated_fields": updated_fields,
            "order": order
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to update order: {str(e)}"
        } 