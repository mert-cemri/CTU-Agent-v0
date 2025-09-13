# Copyright Sierra

from .think import Think
from .search_patients import SearchPatients
from .book_appointment import BookAppointment
from .cancel_appointment import CancelAppointment
from .get_patient_info import GetPatientInfo
from .get_appointment_details import GetAppointmentDetails
from .get_doctor_availability import GetDoctorAvailability

ALL_TOOLS = [
    Think,
    SearchPatients,
    BookAppointment,
    CancelAppointment,
    GetPatientInfo,
    GetAppointmentDetails,
    GetDoctorAvailability,
]