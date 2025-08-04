# Copyright Sierra

from envs.tool import Tool
import json


class GetLineDetails(Tool):
    @staticmethod
    def invoke(data, line_id: str) -> str:
        lines = data.get("lines", [])
        for line in lines:
            if line.get("id") == line_id:
                return json.dumps(line)
        return "Line not found"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_line_details",
                "description": "Get detailed information about a specific line",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "line_id": {
                            "type": "string",
                            "description": "Line ID"
                        }
                    },
                    "required": ["line_id"]
                }
            }
        }