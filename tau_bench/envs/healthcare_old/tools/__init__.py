# Copyright Sierra

from .think import Think
from .search_patients import SearchPatients
from .book_appointment import BookAppointment
from .get_appointment_details import GetAppointmentDetails
from .get_doctor_availability import GetDoctorAvailability
from .get_patient_info import GetPatientInfo
from .cancel_appointment import CancelAppointment

ALL_TOOLS = [
    Think,
    SearchPatients,
    BookAppointment,
    GetAppointmentDetails,
    GetDoctorAvailability,
    GetPatientInfo,
    CancelAppointment,
]