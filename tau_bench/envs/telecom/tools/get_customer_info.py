# Copyright Sierra

from envs.tool import Tool
import json


class GetCustomerInfo(Tool):
    @staticmethod
    def invoke(data, customer_id: str) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps(customer)
        return "Customer not found"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_customer_info",
                "description": "Get customer information by customer ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID (e.g., 'TC001')"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }