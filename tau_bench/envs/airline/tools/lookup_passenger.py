# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class LookupPassenger(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], confirmation_number: str = None, email: str = None, **kwargs) -> str:
        # Simplified implementation - lookup passenger by confirmation or email
        return json.dumps({
            "passenger_id": "P123456",
            "name": "John Doe",
            "email": email or "john.doe@example.com",
            "confirmation_number": confirmation_number or "ABC123"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lookup_passenger",
                "description": "Look up passenger information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_number": {
                            "type": "string",
                            "description": "The confirmation number"
                        },
                        "email": {
                            "type": "string",
                            "description": "The passenger email"
                        }
                    },
                    "required": []
                }
            }
        } 