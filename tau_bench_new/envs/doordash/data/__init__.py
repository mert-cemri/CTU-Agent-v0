import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)


def load_data() -> Dict[str, Any]:
    """Load DoorDash domain data (restaurants, users, orders)."""
    with open(os.path.join(FOLDER_PATH, "restaurants.json")) as f:
        restaurants = json.load(f)
    with open(os.path.join(FOLDER_PATH, "users.json")) as f:
        users = json.load(f)
    with open(os.path.join(FOLDER_PATH, "orders.json")) as f:
        orders = json.load(f)
    return {
        "restaurants": restaurants,
        "users": users,
        "orders": orders,
    } 