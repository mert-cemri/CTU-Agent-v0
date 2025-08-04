# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class GetCustomerLines(Tool):
    @staticmethod
    def invoke(data, customer_id: str) -> str:
        lines = data.get("lines", [])
        customer_lines = [line for line in lines if line.get("customer_id") == customer_id]
        return json.dumps(customer_lines)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_customer_lines",
                "description": "Get all lines associated with a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }