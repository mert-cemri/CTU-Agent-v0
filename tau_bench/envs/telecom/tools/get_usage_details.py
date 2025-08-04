# Copyright Sierra

from envs.tool import Tool
import json


class GetUsageDetails(Tool):
    @staticmethod
    def invoke(data, customer_id: str, line_id: str = None) -> str:
        lines = data.get("lines", [])
        customer_lines = [line for line in lines if line.get("customer_id") == customer_id]
        
        if not customer_lines:
            return "No lines found for customer"
        
        if line_id:
            specific_line = next((line for line in customer_lines if line.get("line_id") == line_id), None)
            if not specific_line:
                return "Line not found"
            
            usage = specific_line.get("usage_current_month", {})
            result = {
                "line_id": line_id,
                "phone_number": specific_line.get("phone_number"),
                "usage": usage
            }
            return json.dumps(result)
        
        # Return usage for all lines
        usage_summary = []
        for line in customer_lines:
            usage = line.get("usage_current_month", {})
            usage_summary.append({
                "line_id": line.get("line_id"),
                "phone_number": line.get("phone_number"),
                "usage": usage
            })
        
        return json.dumps(usage_summary)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_usage_details",
                "description": "Get usage details for customer's phone lines",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID"
                        },
                        "line_id": {
                            "type": "string",
                            "description": "Specific line ID (optional)"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }