# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class ProcessPayment(Tool):
    @staticmethod
    def invoke(data, customer_id: str, amount: float, payment_method: str) -> str:
        # Validate customer exists
        customers = data.get("customers", [])
        customer = next((c for c in customers if c.get("customer_id") == customer_id), None)
        if not customer:
            return "Customer not found"
        
        # Validate payment method
        valid_methods = ["credit_card", "debit_card", "bank_transfer", "autopay"]
        if payment_method not in valid_methods:
            return f"Invalid payment method. Valid methods: {', '.join(valid_methods)}"
        
        # Process payment (in real system, this would interface with payment processor)
        result = {
            "status": "success",
            "confirmation_number": f"PAY{customer_id[-3:]}{str(int(amount))[:4]}",
            "amount": amount,
            "payment_method": payment_method,
            "processing_time": "1-2 business days",
            "message": "Payment processed successfully"
        }
        
        return json.dumps(result)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "process_payment",
                "description": "Process payment for customer bill",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID"
                        },
                        "amount": {
                            "type": "number",
                            "description": "Payment amount"
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method (credit_card, debit_card, bank_transfer, autopay)"
                        }
                    },
                    "required": ["customer_id", "amount", "payment_method"]
                }
            }
        }