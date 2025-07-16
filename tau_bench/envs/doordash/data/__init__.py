import json
import os


def load_data():
    """Load doordash domain data from JSON files."""
    current_dir = os.path.dirname(__file__)
    
    # Load all data files
    data = {}
    
    # Load restaurants
    with open(os.path.join(current_dir, "restaurants.json"), "r") as f:
        data["restaurants"] = json.load(f)
    
    # Load users
    with open(os.path.join(current_dir, "users.json"), "r") as f:
        data["users"] = json.load(f)
    
    # Load orders
    with open(os.path.join(current_dir, "orders.json"), "r") as f:
        data["orders"] = json.load(f)
    
    return data 