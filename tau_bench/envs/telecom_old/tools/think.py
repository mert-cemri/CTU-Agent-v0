# Copyright Sierra

from tau_bench.envs.tool import Tool


class Think(Tool):
    @staticmethod
    def invoke(data, thought: str) -> str:
        return ""

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "Think about the current situation and plan next steps. This tool does not change any data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {
                            "type": "string",
                            "description": "Your thoughts about the current situation"
                        }
                    },
                    "required": ["thought"]
                }
            }
        }