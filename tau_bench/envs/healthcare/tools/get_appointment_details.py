# Copyright Sierra

from envs.tool import Tool
import json


class GetAppointmentDetails(Tool):
    @staticmethod
    def invoke(data, appointment_id: str) -> str:
        appointments = data.get("appointments", [])
        appointment = next((apt for apt in appointments if apt.get("appointment_id") == appointment_id), None)
        
        if not appointment:
            return "Appointment not found"
        
        # Get related doctor info
        doctor_id = appointment.get("doctor_id")
        doctors = data.get("doctors", [])
        doctor = next((d for d in doctors if d.get("doctor_id") == doctor_id), None)
        
        # Get related patient info
        patient_id = appointment.get("patient_id")
        patients = data.get("patients", [])
        patient = next((p for p in patients if p.get("patient_id") == patient_id), None)
        
        result = {
            "appointment": appointment,
            "doctor": {
                "name": doctor.get("name") if doctor else "Unknown",
                "specialty": doctor.get("specialty") if doctor else "Unknown"
            },
            "patient": {
                "name": patient.get("name") if patient else "Unknown"
            }
        }
        
        return json.dumps(result)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_appointment_details",
                "description": "Get detailed information about an appointment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "appointment_id": {
                            "type": "string",
                            "description": "Appointment ID"
                        }
                    },
                    "required": ["appointment_id"]
                }
            }
        }