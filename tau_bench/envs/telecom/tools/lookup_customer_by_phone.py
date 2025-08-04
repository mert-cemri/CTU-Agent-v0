# Copyright Sierra

from envs.tool import Tool
import json


class LookupCustomerByPhone(Tool):
    @staticmethod
    def invoke(data, phone_number: str) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("phone") == phone_number:
                return json.dumps(customer)
        return "Customer not found"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "lookup_customer_by_phone",
                "description": "Look up customer information by phone number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "phone_number": {
                            "type": "string",
                            "description": "Phone number to look up (e.g., '+1-555-0001')"
                        }
                    },
                    "required": ["phone_number"]
                }
            }
        }