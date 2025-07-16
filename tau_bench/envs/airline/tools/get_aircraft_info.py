# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class GetAircraftInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_code: str) -> str:
        # Simplified implementation
        return json.dumps({
            "aircraft_code": aircraft_code,
            "model": "Boeing 737",
            "capacity": 150,
            "range": "3000 miles"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_aircraft_info",
                "description": "Get information about a specific aircraft",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_code": {
                            "type": "string",
                            "description": "The aircraft code"
                        }
                    },
                    "required": ["aircraft_code"]
                }
            }
        } 