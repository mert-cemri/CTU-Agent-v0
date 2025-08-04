"""Get item details tool for DoorDash domain."""

import json
from typing import Dict, Any


def get_item_details(restaurant_id: str, item_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific menu item.
    
    Args:
        restaurant_id: The ID of the restaurant
        item_id: The ID of the menu item
    
    Returns:
        Dict containing item details
    """
    try:
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
        
        return {
            "success": True,
            "restaurant_id": restaurant_id,
            "restaurant_name": restaurant["name"],
            "item": item
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get item details: {str(e)}"
        } 