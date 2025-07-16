import json
import os


def load_data():
    """Load telecom domain data from JSON files."""
    current_dir = os.path.dirname(__file__)
    
    # Load all data files
    data = {}
    
    # Load plans
    with open(os.path.join(current_dir, "plans.json"), "r") as f:
        data["plans"] = json.load(f)
    
    # Load devices
    with open(os.path.join(current_dir, "devices.json"), "r") as f:
        data["devices"] = json.load(f)
    
    # Load lines
    with open(os.path.join(current_dir, "lines.json"), "r") as f:
        data["lines"] = json.load(f)
    
    # Load customers
    with open(os.path.join(current_dir, "customers.json"), "r") as f:
        data["customers"] = json.load(f)
    
    # Load bills
    with open(os.path.join(current_dir, "bills.json"), "r") as f:
        data["bills"] = json.load(f)
    
    return data