# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class GetAirportInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], airport_code: str) -> str:
        # Use airports data if available, otherwise simplified response
        airports = data.get("airports", {})
        if airport_code in airports:
            return json.dumps(airports[airport_code])
        return json.dumps({
            "airport_code": airport_code,
            "name": f"{airport_code} Airport",
            "city": "Unknown",
            "country": "Unknown"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_airport_info",
                "description": "Get information about a specific airport",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_code": {
                            "type": "string",
                            "description": "The airport code (e.g., LAX, JFK)"
                        }
                    },
                    "required": ["airport_code"]
                }
            }
        } 