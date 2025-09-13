"""Get restaurant details tool for DoorDash domain."""

import json
from typing import Dict, Any


def get_restaurant_details(restaurant_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific restaurant.
    
    Args:
        restaurant_id: The ID of the restaurant to get details for
    
    Returns:
        Dict containing restaurant details
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
        
        return {
            "success": True,
            "restaurant": restaurant
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to get restaurant details: {str(e)}"
        } 