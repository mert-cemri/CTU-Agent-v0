# Copyright Sierra

import json
import os


def load_data():
    """Load healthcare domain data from JSON files."""
    current_dir = os.path.dirname(__file__)
    
    # Load all data files
    data = {}
    
    # Load patients
    with open(os.path.join(current_dir, "patients.json"), "r") as f:
        data["patients"] = json.load(f)
    
    # Load doctors
    with open(os.path.join(current_dir, "doctors.json"), "r") as f:
        data["doctors"] = json.load(f)
    
    # Load appointments
    with open(os.path.join(current_dir, "appointments.json"), "r") as f:
        data["appointments"] = json.load(f)
    
    return data