"""Add item to cart tool for DoorDash domain."""

import json
from typing import Dict, Any


def add_item_to_cart(
    user_id: str, 
    restaurant_id: str, 
    item_id: str, 
    quantity: int = 1,
    customizations: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Add an item to the user's cart.
    
    Args:
        user_id: The ID of the user
        restaurant_id: The ID of the restaurant
        item_id: The ID of the menu item
        quantity: Number of items to add
        customizations: Optional customizations for the item
    
    Returns:
        Dict containing cart update result
    """
    try:
        # Load restaurant data to validate item
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
        
        # Find the menu item
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
                "error": f"Menu item with ID {item_id} not found in restaurant {restaurant_id}"
            }
        
        # Check if item is available
        if not item.get("available", True):
            return {
                "success": False,
                "error": f"Item {item['name']} is currently unavailable"
            }
        
        # Calculate total price
        base_price = item["price"]
        total_price = base_price * quantity
        
        # Create cart item
        cart_item = {
            "item_id": item_id,
            "item_name": item["name"],
            "restaurant_id": restaurant_id,
            "restaurant_name": restaurant["name"],
            "quantity": quantity,
            "unit_price": base_price,
            "total_price": total_price,
            "customizations": customizations or {}
        }
        
        return {
            "success": True,
            "message": f"Added {quantity} {item['name']} to cart",
            "cart_item": cart_item,
            "total_price": total_price
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to add item to cart: {str(e)}"
        } 