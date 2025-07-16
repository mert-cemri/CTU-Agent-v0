# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class CheckFlightStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str = None) -> str:
        # Simplified implementation - in real scenario would check flight database
        return json.dumps({
            "flight_number": flight_number,
            "status": "On Time",
            "departure_time": "14:30",
            "arrival_time": "17:45",
            "gate": "A12"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_flight_status",
                "description": "Check the status of a specific flight",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number to check"
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight (optional)"
                        }
                    },
                    "required": ["flight_number"]
                }
            }
        } 