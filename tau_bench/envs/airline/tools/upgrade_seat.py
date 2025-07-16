# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class UpgradeSeat(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str, seat_class: str, **kwargs) -> str:
        # Simplified implementation - upgrade seat class
        return json.dumps({
            "success": True,
            "reservation_id": reservation_id,
            "new_seat_class": seat_class,
            "upgrade_fee": "$150",
            "message": f"Seat upgraded to {seat_class} class successfully"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upgrade_seat",
                "description": "Upgrade seat class for a reservation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The reservation ID"
                        },
                        "seat_class": {
                            "type": "string",
                            "description": "The new seat class (e.g., business, first)"
                        }
                    },
                    "required": ["reservation_id", "seat_class"]
                }
            }
        } 