# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class GetBillDetails(Tool):
    @staticmethod
    def invoke(data, customer_id: str, bill_date: str = None) -> str:
        bills = data.get("bills", [])
        customer_bills = [bill for bill in bills if bill.get("customer_id") == customer_id]
        
        if bill_date:
            # Filter bills by specific date or month
            filtered_bills = []
            for bill in customer_bills:
                billing_period = bill.get("billing_period", {})
                start_date = billing_period.get("start_date", "")
                end_date = billing_period.get("end_date", "")
                
                # Check if the date falls within the billing period
                if bill_date >= start_date and bill_date <= end_date:
                    filtered_bills.append(bill)
                # Or if just year-month is provided, check if it matches
                elif len(bill_date) == 7 and start_date.startswith(bill_date):
                    filtered_bills.append(bill)
            
            customer_bills = filtered_bills
        
        if not customer_bills:
            return "No bills found for customer"
        
        # Return most recent bill if no specific date requested
        if not bill_date:
            customer_bills = sorted(customer_bills, key=lambda x: x.get("bill_date", ""), reverse=True)
            return json.dumps(customer_bills[0])
        
        return json.dumps(customer_bills)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_bill_details",
                "description": "Get billing information for a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID"
                        },
                        "bill_date": {
                            "type": "string",
                            "description": "Bill date or month (YYYY-MM-DD or YYYY-MM format) - optional"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }