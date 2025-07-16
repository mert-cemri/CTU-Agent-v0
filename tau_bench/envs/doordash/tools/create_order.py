"""Create order tool for DoorDash domain."""

import json
from typing import Dict, Any, List
from datetime import datetime
import uuid


def create_order(
    user_id: str,
    restaurant_id: str,
    items: List[Dict[str, Any]],
    delivery_address: str = None,
    payment_method: str = None,
    special_instructions: str = None
) -> Dict[str, Any]:
    """
    Create a new order for a user.
    
    Args:
        user_id: The ID of the user placing the order
        restaurant_id: The ID of the restaurant
        items: List of items to order with quantities
        delivery_address: Optional delivery address
        payment_method: Optional payment method
        special_instructions: Optional special instructions
    
    Returns:
        Dict containing order creation result
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
        
        # Load restaurant data
        with open("envs/doordash/data/restaurants.json", "r") as f:
            restaurants = json.load(f)
        
        # Find the restaurant
        restaurant = None
        for r in restaurants:
            if r["restaurant_id"] == restaurant_id:
                restaurant = r
                break
        
        if not restaurant:
            return {
                "success": False,
                "error": f"Restaurant with ID {restaurant_id} not found"
            }
        
        # Check if restaurant is open
        if restaurant.get("status") != "open":
            return {
                "success": False,
                "error": f"Restaurant {restaurant['name']} is currently closed"
            }
        
        # Validate items and calculate total
        order_items = []
        subtotal = 0
        
        for item_request in items:
            item_id = item_request.get("item_id")
            quantity = item_request.get("quantity", 1)
            
            # Find item in restaurant menu
            item = None
            menu = restaurant.get("full_menu", {})
            if menu:
                for category in menu.get("categories", []):
                    for menu_item in category.get("items", []):
                        if menu_item["id"] == item_id:
                            item = menu_item
                            break
                    if item:
                        break
            
            if not item:
                return {
                    "success": False,
                    "error": f"Menu item with ID {item_id} not found"
                }
            
            if not item.get("available", True):
                return {
                    "success": False,
                    "error": f"Item {item['name']} is currently unavailable"
                }
            
            item_total = item["price"] * quantity
            subtotal += item_total
            
            order_items.append({
                "item_id": item_id,
                "name": item["name"],
                "quantity": quantity,
                "unit_price": item["price"],
                "total_price": item_total
            })
        
        # Check minimum order
        if subtotal < restaurant.get("minimum_order", 0):
            return {
                "success": False,
                "error": f"Order does not meet minimum order requirement of ${restaurant['minimum_order']}"
            }
        
        # Calculate fees and total
        delivery_fee = restaurant.get("delivery_fee", 0)
        tax = subtotal * 0.08  # 8% tax
        total = subtotal + delivery_fee + tax
        
        # Generate order ID
        order_id = f"O{str(uuid.uuid4())[:8].upper()}"
        
        # Create order
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "restaurant_id": restaurant_id,
            "restaurant_name": restaurant["name"],
            "items": order_items,
            "subtotal": round(subtotal, 2),
            "delivery_fee": delivery_fee,
            "tax": round(tax, 2),
            "total": round(total, 2),
            "status": "placed",
            "timestamp": datetime.now().isoformat(),
            "delivery_address": delivery_address or user.get("address", {}).get("street", ""),
            "payment_method": payment_method or "default",
            "special_instructions": special_instructions,
            "estimated_delivery_time": restaurant.get("estimated_delivery_time", "30-45 min")
        }
        
        return {
            "success": True,
            "message": f"Order {order_id} created successfully",
            "order": order
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to create order: {str(e)}"
        } 