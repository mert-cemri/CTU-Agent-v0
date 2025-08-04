"""Search restaurants tool for DoorDash domain."""

import json
from typing import Dict, List, Any


def search_restaurants(
    cuisine: str = None,
    location: str = None,
    price_range: str = None,
    rating_min: float = None,
    dietary_options: List[str] = None,
    delivery_time_max: int = None
) -> Dict[str, Any]:
    """
    Search for restaurants based on various criteria.
    
    Args:
        cuisine: Filter by cuisine type (e.g., "Italian", "Chinese", "Mexican")
        location: Filter by location/address
        price_range: Filter by price range ("$", "$$", "$$$")
        rating_min: Minimum rating threshold
        dietary_options: Filter by dietary options (e.g., ["vegetarian", "vegan"])
        delivery_time_max: Maximum delivery time in minutes
    
    Returns:
        Dict containing search results
    """
    try:
        # Load restaurant data
        with open("envs/doordash/data/restaurants.json", "r") as f:
            restaurants = json.load(f)
        
        results = []
        
        for restaurant in restaurants:
            # Apply filters
            if cuisine and cuisine.lower() not in restaurant.get("cuisine", "").lower():
                continue
                
            if location and location.lower() not in restaurant.get("address", "").lower():
                continue
                
            if price_range and restaurant.get("price_range") != price_range:
                continue
                
            if rating_min and restaurant.get("rating", 0) < rating_min:
                continue
                
            if dietary_options:
                restaurant_dietary = restaurant.get("dietary_options", [])
                if not any(option in restaurant_dietary for option in dietary_options):
                    continue
                    
            if delivery_time_max:
                # Parse delivery time (e.g., "30-45 min" -> 45)
                delivery_time = restaurant.get("estimated_delivery_time", "")
                if "-" in delivery_time:
                    max_time = int(delivery_time.split("-")[1].split(" ")[0])
                    if max_time > delivery_time_max:
                        continue
            
            # Add to results
            results.append({
                "restaurant_id": restaurant["restaurant_id"],
                "name": restaurant["name"],
                "cuisine": restaurant["cuisine"],
                "rating": restaurant["rating"],
                "review_count": restaurant["review_count"],
                "price_range": restaurant["price_range"],
                "delivery_fee": restaurant["delivery_fee"],
                "estimated_delivery_time": restaurant["estimated_delivery_time"],
                "status": restaurant["status"],
                "address": restaurant["address"],
                "dietary_options": restaurant.get("dietary_options", [])
            })
        
        return {
            "success": True,
            "results": results,
            "total_count": len(results)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to search restaurants: {str(e)}"
        } 