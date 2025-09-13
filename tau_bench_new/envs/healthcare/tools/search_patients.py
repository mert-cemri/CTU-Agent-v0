# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class SearchPatients(Tool):
    @staticmethod
    def invoke(data, name: str = None, phone: str = None) -> str:
        patients = data.get("patients", [])
        results = []
        
        for patient in patients:
            match = False
            if name and name.lower() in patient.get("name", "").lower():
                match = True
            if phone and phone in patient.get("phone", ""):
                match = True
            
            if match:
                results.append(patient)
        
        return json.dumps(results)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "search_patients",
                "description": "Search for patients by name or phone number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Patient name to search for"
                        },
                        "phone": {
                            "type": "string", 
                            "description": "Patient phone number to search for"
                        }
                    },
                    "required": []
                }
            }
        }