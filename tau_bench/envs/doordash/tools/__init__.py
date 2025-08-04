# Copyright Sierra

"""DoorDash domain tools – class-based wrappers around the function
implementations so that they follow the same design pattern used in the
Airline and Healthcare domains (Tool subclasses with invoke / get_info and
an aggregated ALL_TOOLS list).  Nothing from the original functional style
is removed – the wrappers simply delegate to the original functions so no
logic is duplicated.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List
from envs.tool import Tool

# ---------------------------------------------------------------------------
# Bring in the original function-based implementations so we can delegate.
# ---------------------------------------------------------------------------
from .search_restaurants import search_restaurants  # noqa: E402
from .get_restaurant_details import get_restaurant_details  # noqa: E402
from .get_restaurant_menu import get_restaurant_menu  # noqa: E402
from .get_user_details import get_user_details  # noqa: E402
from .get_user_order_history import get_user_order_history  # noqa: E402
from .create_order import create_order  # noqa: E402
from .get_order_status import get_order_status  # noqa: E402
from .update_order import update_order  # noqa: E402
from .cancel_order import cancel_order  # noqa: E402
from .add_item_to_cart import add_item_to_cart  # noqa: E402
from .get_item_details import get_item_details  # noqa: E402
from .calculate import calculate  # noqa: E402
from .think import think  # noqa: E402
from .transfer_to_human_agents import transfer_to_human_agents  # noqa: E402

# ---------------------------------------------------------------------------
# Helper to wrap a simple function into a Tool subclass quickly.
# ---------------------------------------------------------------------------

def _generate_get_info(name: str, description: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Return an OpenAI-style function schema."""
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": params,
                # Require all parameters that do not have defaults (simple rule)
                "required": [k for k, v in params.items() if v.get("required", False)],
            },
        },
    }

# ---------------------------------------------------------------------------
# Individual wrapper classes
# ---------------------------------------------------------------------------

class SearchRestaurants(Tool):
    """Search for restaurants by criteria"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:  # noqa: D401
        return json.dumps(search_restaurants(**kwargs))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "search_restaurants",
            "Search for restaurants based on cuisine, location and other filters.",
            {
                "cuisine": {"type": "string", "description": "Cuisine type"},
                "location": {"type": "string", "description": "User location"},
                "price_range": {"type": "string", "description": "Price range ($, $$, $$$)"},
                "rating_min": {"type": "number", "description": "Minimum rating"},
                "dietary_options": {"type": "array", "items": {"type": "string"}},
                "delivery_time_max": {"type": "integer", "description": "Maximum delivery time in minutes"},
            },
        )


class GetRestaurantDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], restaurant_id: str | None = None, **kwargs) -> str:
        if restaurant_id is None:
            restaurant_id = kwargs.get("name")  # backwards compatibility
        return json.dumps(get_restaurant_details(restaurant_id=restaurant_id))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "get_restaurant_details",
            "Get detailed information about a single restaurant.",
            {
                "restaurant_id": {"type": "string", "description": "Restaurant identifier", "required": True},
            },
        )


class GetRestaurantMenu(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], restaurant_id: str, category: str | None = None) -> str:
        return json.dumps(get_restaurant_menu(restaurant_id, category))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "get_restaurant_menu",
            "Retrieve a restaurant's menu optionally filtered by category.",
            {
                "restaurant_id": {"type": "string", "description": "Restaurant identifier", "required": True},
                "category": {"type": "string", "description": "Menu category filter"},
            },
        )


class GetUserDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        return json.dumps(get_user_details(user_id))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "get_user_details",
            "Retrieve user profile information.",
            {"user_id": {"type": "string", "required": True}},
        )


class GetUserOrderHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, limit: int = 10) -> str:
        return json.dumps(get_user_order_history(user_id, limit))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "get_user_order_history",
            "Get recent orders placed by a user.",
            {
                "user_id": {"type": "string", "required": True},
                "limit": {"type": "integer", "description": "Maximum number of orders to return"},
            },
        )


class CreateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps(create_order(**kwargs))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "create_order",
            "Create a new DoorDash order for a user.",
            {
                "user_id": {"type": "string", "required": True},
                "restaurant_id": {"type": "string", "required": True},
                "items": {"type": "array", "items": {"type": "object"}, "description": "List of items with quantity and modifiers", "required": True},
                "delivery_address": {"type": "string"},
                "payment_method": {"type": "string"},
                "special_instructions": {"type": "string"},
            },
        )


class GetOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        return json.dumps(get_order_status(order_id))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "get_order_status",
            "Check the current status of an order.",
            {"order_id": {"type": "string", "required": True}},
        )


class UpdateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps(update_order(**kwargs))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "update_order",
            "Modify an existing order (status, address, instructions).",
            {
                "order_id": {"type": "string", "required": True},
                "status": {"type": "string"},
                "delivery_address": {"type": "string"},
                "special_instructions": {"type": "string"},
            },
        )


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, reason: str | None = None) -> str:
        return json.dumps(cancel_order(order_id, reason))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "cancel_order",
            "Cancel an order providing an optional reason.",
            {
                "order_id": {"type": "string", "required": True},
                "reason": {"type": "string"},
            },
        )


class AddItemToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps(add_item_to_cart(**kwargs))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "add_item_to_cart",
            "Add a menu item to the user’s cart.",
            {
                "user_id": {"type": "string", "required": True},
                "restaurant_id": {"type": "string", "required": True},
                "item_id": {"type": "string", "required": True},
                "quantity": {"type": "integer"},
                "customizations": {"type": "object"},
            },
        )


class GetItemDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], restaurant_id: str, item_id: str) -> str:
        return json.dumps(get_item_details(restaurant_id, item_id))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "get_item_details",
            "Retrieve details for a specific menu item.",
            {
                "restaurant_id": {"type": "string", "required": True},
                "item_id": {"type": "string", "required": True},
            },
        )


class Calculate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], expression: str) -> str:
        return json.dumps(calculate(expression))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "calculate",
            "Evaluate a mathematical expression.",
            {"expression": {"type": "string", "required": True}},
        )


class Think(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thought: str) -> str:
        return json.dumps(think(thought))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "think",
            "Internal deliberate reasoning step (chain-of-thought).",
            {"thought": {"type": "string", "required": True}},
        )


class TransferToHumanAgents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reason: str, context: str | None = None) -> str:
        return json.dumps(transfer_to_human_agents(reason, context))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return _generate_get_info(
            "transfer_to_human_agents",
            "Escalate the conversation to a human support agent.",
            {
                "reason": {"type": "string", "required": True},
                "context": {"type": "string"},
            },
        )

# ---------------------------------------------------------------------------
# Public export list
# ---------------------------------------------------------------------------

ALL_TOOLS = [
    SearchRestaurants,
    GetRestaurantDetails,
    GetRestaurantMenu,
    GetUserDetails,
    GetUserOrderHistory,
    CreateOrder,
    GetOrderStatus,
    UpdateOrder,
    CancelOrder,
    AddItemToCart,
    GetItemDetails,
    Calculate,
    Think,
    TransferToHumanAgents,
]

__all__ = [tool.__name__ for tool in ALL_TOOLS] 