# Copyright Sierra

from envs.tool import Tool
import json


class CancelAppointment(Tool):
    @staticmethod
    def invoke(data, appointment_id: str, reason: str = None) -> str:
        appointments = data.get("appointments", [])
        appointment = next((apt for apt in appointments if apt.get("appointment_id") == appointment_id), None)
        
        if not appointment:
            return "Appointment not found"
        
        current_status = appointment.get("status", "")
        if current_status == "cancelled":
            return "Appointment is already cancelled"
        
        if current_status == "completed":
            return "Cannot cancel completed appointment"
        
        # In a real system, this would update the database
        result = {
            "appointment_id": appointment_id,
            "previous_status": current_status,
            "new_status": "cancelled",
            "cancellation_reason": reason or "Patient request",
            "message": "Appointment cancelled successfully"
        }
        
        return json.dumps(result)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "cancel_appointment",
                "description": "Cancel an existing appointment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "appointment_id": {
                            "type": "string",
                            "description": "Appointment ID to cancel"
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for cancellation (optional)"
                        }
                    },
                    "required": ["appointment_id"]
                }
            }
        }