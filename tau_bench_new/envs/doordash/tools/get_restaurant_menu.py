"""Get restaurant menu tool for DoorDash domain."""

import json
from typing import Dict, Any


def get_restaurant_menu(restaurant_id: str, category: str = None) -> Dict[str, Any]:
    """
    Get the menu for a specific restaurant.
    
    Args:
        restaurant_id: The ID of the restaurant
        category: Optional filter by menu category
    
    Returns:
        Dict containing menu information
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
        
        # Get menu information
        menu = restaurant.get("full_menu", {})
        if not menu:
            # Fallback to basic menu items if full_menu not available
            menu_items = restaurant.get("menu_items", [])
            menu_categories = restaurant.get("menu_categories", [])
            
            return {
                "success": True,
                "restaurant_id": restaurant_id,
                "restaurant_name": restaurant["name"],
                "menu_items": menu_items,
                "menu_categories": menu_categories
            }
        
        # Filter by category if specified
        if category:
            filtered_categories = []
            for cat in menu.get("categories", []):
                if category.lower() in cat["name"].lower():
                    filtered_categories.append(cat)
            
            return {
                "success": True,
                "restaurant_id": restaurant_id,
                "restaurant_name": restaurant["name"],
                "categories": filtered_categories,
                "filtered_by": category
            }
        
        return {
            "success": True,
            "restaurant_id": restaurant_id,
            "restaurant_name": restaurant["name"],
            "menu": menu
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get restaurant menu: {str(e)}"
        } 