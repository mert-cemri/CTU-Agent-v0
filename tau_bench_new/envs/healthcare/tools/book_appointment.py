# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class BookAppointment(Tool):
    @staticmethod
    def invoke(data, patient_id: str, doctor_id: str, date: str, time: str, reason: str) -> str:
        appointments = data.get("appointments", [])
        
        # Create new appointment
        new_appointment = {
            "id": f"A{len(appointments) + 1:03d}",
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time,
            "status": "scheduled",
            "reason": reason
        }
        
        appointments.append(new_appointment)
        return json.dumps(new_appointment)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "book_appointment",
                "description": "Book a new appointment for a patient",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_id": {
                            "type": "string",
                            "description": "Patient ID"
                        },
                        "doctor_id": {
                            "type": "string",
                            "description": "Doctor ID"
                        },
                        "date": {
                            "type": "string",
                            "description": "Appointment date (YYYY-MM-DD)"
                        },
                        "time": {
                            "type": "string",
                            "description": "Appointment time (HH:MM)"
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for appointment"
                        }
                    },
                    "required": ["patient_id", "doctor_id", "date", "time", "reason"]
                }
            }
        }