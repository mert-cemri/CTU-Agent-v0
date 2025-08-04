# Copyright Sierra

from envs.tool import Tool
import json


class GetPatientInfo(Tool):
    @staticmethod
    def invoke(data, patient_id: str) -> str:
        patients = data.get("patients", [])
        for patient in patients:
            if patient.get("patient_id") == patient_id:
                return json.dumps(patient)
        return "Patient not found"

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_patient_info",
                "description": "Get patient information by patient ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_id": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P001')"
                        }
                    },
                    "required": ["patient_id"]
                }
            }
        }