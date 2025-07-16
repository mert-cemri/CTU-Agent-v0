# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class SuspendLine(Tool):
    @staticmethod
    def invoke(data, line_id: str, reason: str) -> str:
        lines = data.get("lines", [])
        for line in lines:
            if line.get("id") == line_id:
                if line.get("status") == "suspended":
                    return "Line is already suspended"
                line["status"] = "suspended"
                line["suspension_reason"] = reason
                return json.dumps(line)
        return "Line not found"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "suspend_line",
                "description": "Suspend a phone line",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "line_id": {
                            "type": "string",
                            "description": "Line ID to suspend"
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for suspension"
                        }
                    },
                    "required": ["line_id", "reason"]
                }
            }
        }