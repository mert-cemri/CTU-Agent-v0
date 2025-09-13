# Copyright Sierra

from tau_bench.envs.tool import Tool
import json


class GetDoctorAvailability(Tool):
    @staticmethod
    def invoke(data, doctor_id: str, date: str = None) -> str:
        doctors = data.get("doctors", [])
        doctor = next((d for d in doctors if d.get("doctor_id") == doctor_id), None)
        
        if not doctor:
            return "Doctor not found"
        
        # Get doctor's general schedule
        schedule = doctor.get("schedule", {})
        
        # Check existing appointments for the date
        appointments = data.get("appointments", [])
        doctor_appointments = [apt for apt in appointments if apt.get("doctor_id") == doctor_id]
        
        if date:
            # Filter appointments for specific date
            date_appointments = [apt for apt in doctor_appointments if apt.get("date") == date]
            booked_times = [apt.get("time") for apt in date_appointments if apt.get("status") != "cancelled"]
            
            result = {
                "doctor_id": doctor_id,
                "doctor_name": doctor.get("name"),
                "date": date,
                "schedule": schedule,
                "booked_times": booked_times,
                "available": len(booked_times) < 8  # Assume 8 slots per day
            }
        else:
            result = {
                "doctor_id": doctor_id,
                "doctor_name": doctor.get("name"),
                "general_schedule": schedule,
                "total_appointments": len(doctor_appointments)
            }
        
        return json.dumps(result)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_doctor_availability",
                "description": "Check doctor availability for appointments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doctor_id": {
                            "type": "string",
                            "description": "Doctor ID"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date to check availability (YYYY-MM-DD format) - optional"
                        }
                    },
                    "required": ["doctor_id"]
                }
            }
        }