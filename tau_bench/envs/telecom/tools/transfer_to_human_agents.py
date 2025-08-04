# Copyright Sierra

from envs.tool import Tool


class TransferToHumanAgents(Tool):
    @staticmethod
    def invoke(data, summary: str) -> str:
        return "Transfer successful"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to human agents when the issue cannot be resolved automatically",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "Summary of the conversation and issue for human agents"
                        }
                    },
                    "required": ["summary"]
                }
            }
        }