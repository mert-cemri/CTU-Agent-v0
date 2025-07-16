# Copyright Sierra

from tau_bench.envs.tool import Tool
from typing import Dict, Any, List, Optional
import json

# Import the existing functions
from .search_restaurants import search_restaurants
from .get_restaurant_details import get_restaurant_details
from .get_restaurant_menu import get_restaurant_menu
from .get_item_details import get_item_details
from .add_item_to_cart import add_item_to_cart
from .create_order import create_order
from .get_order_status import get_order_status
from .update_order import update_order
from .cancel_order import cancel_order
from .get_user_details import get_user_details
from .get_user_order_history import get_user_order_history
from .calculate import calculate
from .think import think
from .transfer_to_human_agents import transfer_to_human_agents


class SearchRestaurants(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        result = search_restaurants(**kwargs)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_restaurants",
                "description": "Search for restaurants based on various criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {"type": "string", "description": "Filter by cuisine type"},
                        "location": {"type": "string", "description": "Filter by location/address"},
                        "price_range": {"type": "string", "description": "Filter by price range ($, $$, $$$)"},
                        "rating_min": {"type": "number", "description": "Minimum rating threshold"},
                        "dietary_options": {"type": "array", "items": {"type": "string"}, "description": "Filter by dietary options"},
                        "delivery_time_max": {"type": "integer", "description": "Maximum delivery time in minutes"}
                    },
                    "required": []
                }
            }
        }


class GetRestaurantDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], restaurant_id: str) -> str:
        result = get_restaurant_details(restaurant_id)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_restaurant_details",
                "description": "Get detailed information about a specific restaurant",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restaurant_id": {"type": "string", "description": "The restaurant ID"}
                    },
                    "required": ["restaurant_id"]
                }
            }
        }


class GetRestaurantMenu(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], restaurant_id: str, category: str = None) -> str:
        result = get_restaurant_menu(restaurant_id, category)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_restaurant_menu",
                "description": "Get the menu for a specific restaurant",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restaurant_id": {"type": "string", "description": "The restaurant ID"},
                        "category": {"type": "string", "description": "Filter by menu category (optional)"}
                    },
                    "required": ["restaurant_id"]
                }
            }
        }


class GetItemDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], restaurant_id: str, item_id: str) -> str:
        result = get_item_details(restaurant_id, item_id)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_item_details",
                "description": "Get details about a specific menu item",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restaurant_id": {"type": "string", "description": "The restaurant ID"},
                        "item_id": {"type": "string", "description": "The item ID"}
                    },
                    "required": ["restaurant_id", "item_id"]
                }
            }
        }


class AddItemToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        result = add_item_to_cart(**kwargs)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_cart",
                "description": "Add an item to the shopping cart",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restaurant_id": {"type": "string", "description": "The restaurant ID"},
                        "item_id": {"type": "string", "description": "The item ID"},
                        "quantity": {"type": "integer", "description": "Quantity to add", "default": 1},
                        "customizations": {"type": "object", "description": "Item customizations"}
                    },
                    "required": ["restaurant_id", "item_id"]
                }
            }
        }


class CreateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        result = create_order(**kwargs)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create a new order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID"},
                        "restaurant_id": {"type": "string", "description": "The restaurant ID"},
                        "items": {"type": "array", "description": "List of items to order"},
                        "delivery_address": {"type": "string", "description": "Delivery address"}
                    },
                    "required": ["user_id", "restaurant_id", "items"]
                }
            }
        }


class GetOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        result = get_order_status(order_id)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_status",
                "description": "Get the status of an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"}
                    },
                    "required": ["order_id"]
                }
            }
        }


class UpdateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        result = update_order(**kwargs)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order",
                "description": "Update an existing order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "updates": {"type": "object", "description": "Order updates"}
                    },
                    "required": ["order_id"]
                }
            }
        }


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, reason: str = None) -> str:
        result = cancel_order(order_id, reason)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order",
                "description": "Cancel an existing order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "reason": {"type": "string", "description": "Cancellation reason"}
                    },
                    "required": ["order_id"]
                }
            }
        }


class GetUserDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        result = get_user_details(user_id)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get user profile information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID"}
                    },
                    "required": ["user_id"]
                }
            }
        }


class GetUserOrderHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, limit: int = 10) -> str:
        result = get_user_order_history(user_id, limit)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_order_history",
                "description": "Get user's order history",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID"},
                        "limit": {"type": "integer", "description": "Number of orders to return", "default": 10}
                    },
                    "required": ["user_id"]
                }
            }
        }


class Calculate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], expression: str) -> str:
        result = calculate(expression)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Perform mathematical calculations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {"type": "string", "description": "Mathematical expression to calculate"}
                    },
                    "required": ["expression"]
                }
            }
        }


class Think(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thought: str) -> str:
        result = think(thought)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "Think about the problem or situation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {"type": "string", "description": "The thought or reasoning"}
                    },
                    "required": ["thought"]
                }
            }
        }


class TransferToHumanAgents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reason: str, context: str = None) -> str:
        result = transfer_to_human_agents(reason, context)
        return json.dumps(result)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to human agents",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reason": {"type": "string", "description": "Reason for transfer"},
                        "context": {"type": "string", "description": "Additional context"}
                    },
                    "required": ["reason"]
                }
            }
        }


ALL_TOOLS = [
    SearchRestaurants,
    GetRestaurantDetails,
    GetRestaurantMenu,
    GetItemDetails,
    AddItemToCart,
    CreateOrder,
    GetOrderStatus,
    UpdateOrder,
    CancelOrder,
    GetUserDetails,
    GetUserOrderHistory,
    Calculate,
    Think,
    TransferToHumanAgents,
] 