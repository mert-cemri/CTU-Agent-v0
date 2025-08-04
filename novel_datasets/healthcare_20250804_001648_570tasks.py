"""
Generated tasks for healthcare domain.
Generated at: 2025-08-04T00:16:48.865935
Total tasks: 570
"""

from tau_types import Task, Action

TASKS_TRAIN = [
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are patient, flexible. First, search for Maria Johnson's patient record using her email (maria.johnson759@email.com) to verify her identity. Once her identity is confirmed, verify Maria Johnson's insurance details to ensure coverage for a general consultation with Dr. Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are organized, logical, flexible. Search for available doctors who specialize in cardiology for patient Robert Johnson.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson", "specialty": "cardiology"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, independent. think with context \"Emily Davis needs to schedule a routine check-up with Dr. Smith\"",
        actions=[
            Action(
                name="think",
                kwargs={"context": "Emily Davis needs to schedule a routine check-up with Dr. Smith"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_id": "P032", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are optimistic, flexible. First, use the think tool to verify David Miller's insurance coverage for a routine check-up. Once coverage is confirmed, use the think tool to identify available doctors for a routine check-up. Finally, use the book_appointment tool to schedule a routine check-up with Dr. Smith for David Miller, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="think",
                kwargs={"task": "verify insurance coverage for a routine check-up", "patient_name": "David Miller", "user_id": "P028"}
            ),
            Action(
                name="think",
                kwargs={"task": "identify available doctors for a routine check-up", "patient_name": "David Miller", "user_id": "P028"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_name": "Dr. Smith", "patient_name": "David Miller", "appointment_type": "routine check-up", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are independent, patient, organized. Search_patients for John Johnson using email john.johnson627@email.com to retrieve patient ID and insurance details. Then, think to verify if John Johnson's insurance covers routine check-ups and determine the next steps. This process is crucial to ensure that John Johnson can proceed with scheduling his routine check-up without any financial surprises, and it aligns with our commitment to providing seamless healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve John Johnson's patient ID and insurance details to verify insurance coverage for routine check-ups."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are polite, patient, cautious, logical. First, search for patient information for user Maria Smith with email maria.smith554@email.com to verify authorization for access. Once authorization is confirmed, proceed to verify insurance details for Maria Smith to ensure coverage for the upcoming appointment with Dr. John Doe. This process is crucial to ensure that Maria Smith can seamlessly receive the necessary healthcare services without any administrative hurdles.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "name": "Maria Smith", "email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization for Maria Smith's access to patient information."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once authorization is confirmed, proceed to verify insurance details for Maria Smith."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are patient, optimistic, logical. Use search_patients with email maria.johnson759@email.com to retrieve Maria Johnson's patient ID and current healthcare details. Then, use book_appointment with Maria's patient ID, the doctor's ID, and a selected time slot to schedule a routine appointment, ensuring it falls within the doctor's available hours. This will help Maria Johnson maintain her regular health check-ups and ensure her healthcare needs are met in a timely manner.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor_id": "D456", "time_slot": "2023-11-15T10:00:00", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are polite, logical, confident. First, search_patients with email sarah.davis118@email.com to retrieve the patient ID and insurance information. Once you have the patient ID, check for any existing appointments or medical records. This will ensure that Sarah Davis's records are up-to-date and that there are no scheduling conflicts before proceeding. If everything is in order, you can then proceed to book_appointment for the patient ID with the selected doctor during available hours. This process ensures that Sarah receives timely medical attention and that all necessary information is accurately recorded in the healthcare system.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance information for Sarah Davis from the search_patients response."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check for any existing appointments or medical records using the retrieved patient ID to ensure no scheduling conflicts."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P047", "doctor_id": "D123", "appointment_time": "2023-11-15T10:00:00", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are patient, direct. First, search_patients with criteria: email \"emily.jones379@email.com\" to verify patient details and authorization status. Once confirmed, think to verify insurance coverage for Emily with her insurance provider before booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are confident, flexible, polite, optimistic. First, search for the patient record using the email sarah.brown753@email.com to confirm authorization and retrieve necessary healthcare details. Once the patient record is confirmed, verify the insurance details for the patient to ensure coverage for upcoming appointments. After verifying insurance, book an appointment for the patient with Dr. John Smith on October 25th, 2023, at 10:00 AM, ensuring that insurance verification is completed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirming patient record and retrieving healthcare details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verifying insurance details for the patient to ensure coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "doctor": "Dr. John Smith", "date": "2023-10-25", "time": "10:00", "patient_email": "sarah.brown753@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are flexible, optimistic, independent, polite. search_patients with email robert.johnson197@email.com to retrieve patient ID and authorization status",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, logical, patient. Search_patients with the name \"Emily Garcia\" and email \"emily.garcia400@email.com\" to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Garcia", "email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are confident, polite. First, search for the user ID associated with Sarah Brown using her email sarah.brown753@email.com. Once you have confirmed her user ID, proceed to check her healthcare details to verify her insurance coverage. This will ensure that her upcoming appointments are covered and any necessary pre-approvals are in place.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"note": "Confirm the user ID for Sarah Brown from the search results."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "action": "check_healthcare_details", "target_user_id": "S001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are optimistic, flexible, confident. \"search_patients\" with the parameter user_email as \"maria.smith554@email.com\" to retrieve patient ID and authorization status",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.smith554@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are organized, patient, confident, logical. Search for the patient profile of Michael Miller using the email michael.miller534@email.com to retrieve his patient ID and insurance details. Verify the insurance details for the patient ID retrieved from Michael Miller's profile to ensure coverage for his upcoming appointments. Once insurance coverage is confirmed, search for available appointment slots for general consultations and book an appointment for Michael Miller using his patient ID with the selected available slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure coverage for upcoming appointments."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once insurance is confirmed, search for available appointment slots for general consultations."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P048", "appointment_slot": "selected_available_slot", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are flexible, patient, organized, cautious. Use `search_patients` with email \"sarah.brown426@email.com\" to retrieve Sarah's patient ID and verify her authorization. Once verified, use `think` to determine if Sarah requires an emergency appointment or a routine visit based on her symptoms. If it is determined that a routine visit is appropriate, proceed to book an appointment using `book_appointment` with Sarah's ID, the physician's ID, and her preferred time slot, ensuring it is within available hours. This will ensure that Sarah receives the necessary medical attention in a timely and efficient manner.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"symptoms": "Sarah's symptoms here"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "physician_id": "Physician's ID", "time_slot": "Sarah's preferred time slot", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are logical, cautious, patient, organized. First, search_patients for Sarah Brown using the email sarah.brown753@email.com to retrieve her patient ID. Once you have the patient ID, verify her insurance details to ensure coverage for upcoming appointments. After confirming her insurance, proceed to book_appointment for Sarah Brown with Dr. John Smith (doctor ID D001) on the next available date and time. Ensure that all steps are completed accurately to facilitate a smooth appointment process for Sarah Brown.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID for Sarah Brown from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Brown's insurance details to ensure coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P025", "doctor_id": "D001", "date": "next_available_date", "time": "next_available_time", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are confident, independent, organized. Use the \"think\" tool to determine if Emily Davis's appointment request is an emergency or routine. Once you have confirmed that it is a routine appointment, use the \"book_appointment\" tool to schedule a routine appointment with Dr. Smith for Emily Davis, ensuring it falls within available hours.",
        actions=[
            Action(
                name="think",
                kwargs={"appointment_request": "Emily Davis's appointment request"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Emily Davis", "doctor_name": "Dr. Smith", "appointment_type": "routine", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are cautious, patient, confident. Use the search_patients tool to find patient information for user Michael Miller using email michael.miller534@email.com. Once you have located his information, use the think tool to verify authorization for accessing Michael Miller's healthcare details to ensure compliance with privacy regulations. After confirming authorization, use the book_appointment tool to schedule an appointment for Michael Miller with Dr. Smith on Tuesday at 3 PM, ensuring it is within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify authorization to access healthcare details for Michael Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "patient_email": "michael.miller534@email.com", "doctor_name": "Dr. Smith", "appointment_time": "Tuesday 3 PM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are logical, flexible, optimistic. First, search_patients with email robert.brown551@email.com to verify authorization and retrieve patient ID. Next, think to determine the preferred doctor for Robert Brown based on past appointments. Finally, search_patients for available appointment slots for the preferred doctor in the upcoming week. These steps are essential to ensure that Robert Brown receives timely and appropriate healthcare services, aligning with his preferences and medical needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D001", "week": "upcoming", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are organized, polite, cautious. First, use search_patients to find patient records associated with Michael Brown using email michael.brown235@email.com to review his medical history and ensure all information is up-to-date. Once you have verified the details, use book_appointment to schedule a routine check-up for Michael Brown with Dr. Smith, ensuring it fits within available hours. This will help maintain continuity of care and address any ongoing health concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com", "user_id": "P016"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "michael.brown235@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are logical, patient, confident. First, search_patients: Find patient details for Sarah Davis using her email sarah.davis118@email.com to confirm identity and retrieve any existing medical records. Once you have confirmed her identity and retrieved her records, think: Consider Sarah Davis's healthcare needs and check her current insurance status for eligibility verification. This will ensure that any necessary medical procedures or consultations are covered and that she receives the appropriate care without financial obstacles.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are independent, patient, logical. Search_patients with email \"david.brown214@email.com\" to retrieve patient ID and healthcare details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are confident, cautious, polite, independent. Search for patient records for user Emily Davis with email emily.davis525@email.com to verify authorization.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "name": "Emily Davis", "email": "emily.davis525@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, organized, confident, patient. Use search_patients to verify Robert Brown's insurance status with insurance ID 12345. Once the insurance verification is complete, use book_appointment to schedule a routine check-up for Robert Brown with Dr. Smith on the next available date. After scheduling the appointment, use search_patients to retrieve Robert Brown's medical history for Dr. Smith's review prior to the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "insurance_id": "12345"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "request": "medical history"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are polite, optimistic. First, search for patients using the email emily.garcia400@email.com to retrieve Emily Garcia's patient ID and insurance information. Once you have her patient ID, verify her insurance status and coverage details to ensure there are no issues. After confirming her insurance, proceed to book an appointment for Emily Garcia with doctor ID D5678 at the next available slot during office hours. Make sure to consider any prerequisite tests or documents Emily might need to complete before her appointment to ensure a smooth visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Emily Garcia's patient ID and insurance information from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Garcia's insurance status and coverage details using her patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor_id": "D5678", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are direct, polite. \"Search for patient information for Robert Jones using search_patients tool with email robert.jones332@email.com\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are logical, organized, optimistic, polite. Search for patient details using the email robert.brown551@email.com to retrieve patient ID and insurance information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, organized, flexible, independent. First, search_patients with email \"maria.smith554@email.com\" to retrieve Maria Smith's patient ID and healthcare details. Next, search_patients for any recent medical history or notes that Dr. John Doe should review before the appointment. Finally, book_appointment for the retrieved patient ID with Dr. John Doe on the next available slot, ensuring it is within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013", "include_medical_history": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_name": "Dr. John Doe", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are confident, cautious, optimistic, patient. Search for patient records of John Johnson using email john.johnson627@email.com to verify identity and retrieve medical history, then check insurance details for John Johnson to ensure coverage for upcoming appointments. This is crucial to confirm that all necessary documentation is in place before scheduling any medical procedures, ensuring a smooth and efficient process for both the healthcare provider and the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, patient, independent. Search for patient records using the email john.johnson941@email.com to verify John Johnson's identity and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, flexible. Book an appointment for Sarah Brown with Dr. Emily Smith for a dermatology consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "doctor_name": "Dr. Emily Smith", "specialty": "dermatology", "appointment_type": "consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are logical, polite. think: Confirm if Emily's insurance covers the type of appointment she intends to book.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "patient_name": "Emily"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are optimistic, polite. First, search for patient Emily Brown's insurance details using the search_patients tool with user ID emily.brown290@email.com to ensure she is covered for a general check-up. Next, think about available doctors who accept Emily Brown's insurance for a general check-up. Once you have verified that Dr. John Smith accepts her insurance, proceed to book an appointment for Emily Brown with Dr. John Smith using the book_appointment tool, ensuring that insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Dr. John Smith accepts Emily Brown's insurance for a general check-up."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "patient_email": "emily.brown290@email.com", "doctor_name": "Dr. John Smith", "appointment_type": "general check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, patient. Search_patients with email robert.garcia592@email.com to retrieve patient ID and insurance details, then think if Robert Garcia has valid insurance for booking an appointment. This process is crucial to ensure that patients are eligible for the healthcare services they need. If Robert Garcia's insurance is verified, you can proceed to the next step of coordinating his care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Robert Garcia has valid insurance for booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, optimistic, independent, polite. Search for Robert Brown in the healthcare database using email robert.brown551@email.com to verify his patient ID and insurance details. Once you have confirmed his insurance coverage is valid, book an appointment for Robert Brown with Dr. Smith for a routine check-up, ensuring that the insurance verification is complete. Finally, think about confirming the appointment details with Robert Brown via email to ensure he is aware of the date and time of his appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance details to ensure coverage is valid."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P003", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true, "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm the appointment details with Robert Brown via email to ensure he is aware of the date and time of his appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are cautious, logical, organized, independent. Book_appointment for Sarah Brown with Dr. Smith (Doctor ID: D456) after confirming insurance coverage and available slots.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Brown's insurance coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Dr. Smith's available appointment slots."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "doctor_id": "D456", "appointment_time": "2023-11-15T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are independent, flexible, patient. First, search for patients with the name \"Maria Johnson\" to retrieve her patient ID and insurance details. Once you have obtained her patient ID, use it to check for any existing medical conditions that need attention. After reviewing her medical conditions, book an appointment for Maria Johnson using her patient ID for a routine check-up with Dr. Smith, ensuring it falls within the available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Maria Johnson", "user_id": "P023"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Maria Johnson's patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use Maria Johnson's patient ID to check for any existing medical conditions that need attention."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure Maria Johnson's insurance is verified before booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are confident, organized, optimistic. Check healthcare details for patient Maria Smith (maria.smith554@email.com) to verify insurance status, then book an appointment for Maria Smith with Dr. Green during available hours for a routine check-up, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "email": "maria.smith554@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "patient_email": "maria.smith554@email.com", "doctor_name": "Dr. Green", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, independent. \"Think tool: Determine if Robert Brown requires an emergency or routine appointment based on symptoms provided\"",
        actions=[
            Action(
                name="think",
                kwargs={"task": "Determine if Robert Brown requires an emergency or routine appointment based on symptoms provided"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are logical, flexible, cautious. First, search for patient records using user email maria.miller855@email.com to find any existing patient ID. Once you have located her records, proceed to search for Maria Miller's insurance details to verify her coverage. After confirming her insurance, book an appointment for Maria Miller with Dr. Smith on the earliest available slot next week. Ensure that all steps are completed accurately to facilitate a seamless appointment scheduling process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P042", "doctor": "Dr. Smith", "date": "next_week_earliest_slot", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are logical, independent, polite, cautious. Search_patients for available primary care physicians for Emily Davis, considering her insurance provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "insurance_provider": "Primary Insurance Provider"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, organized. First, search_patients with email 'maria.johnson759@email.com' to verify patient ID and insurance status. Once you have confirmed that Maria Johnson's insurance is verified and valid for booking, proceed to book_appointment for her patient ID with the appropriate doctor ID during available hours for a general check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor_id": "D123", "appointment_type": "general check-up", "appointment_time": "2023-10-15T10:00:00", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are logical, optimistic. First, verify insurance details for Robert Brown using insurance ID I45678 to confirm coverage for upcoming appointments. Once confirmed, proceed to book an appointment for Robert Brown with Dr. Smith using appointment ID A1122 for a routine check-up on 2023-10-21 at 10:00 AM.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"insurance_id": "I45678", "user_id": "P017"}
            ),
            Action(
                name="book_appointment",
                kwargs={"appointment_id": "A1122", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "date": "2023-10-21", "time": "10:00 AM", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are confident, direct, organized. First, search for patient information using email john.johnson627@email.com to verify identity and access permissions. Once verified, proceed to book an appointment with Dr. Smith for John Johnson on the next available Wednesday at 10:00 AM, ensuring insurance is verified. This sequence is essential to streamline the appointment scheduling process and confirm that John Johnson has the necessary coverage for his visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson627@email.com", "doctor_name": "Dr. Smith", "appointment_time": "next Wednesday 10:00 AM", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are polite, optimistic, flexible, confident. First, search_patients for the user ID associated with the email lisa.williams792@email.com to retrieve patient information. Once you have the user ID, proceed to search_patients for the insurance details of the retrieved user ID for Lisa Williams to ensure her coverage is valid. This will help in confirming her eligibility for booking an appointment with Dr. Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, direct, patient. Search_patients with ID P001 to verify patient Sarah Williams' information and authorization status. Then, think to verify if Sarah Williams' insurance covers the desired healthcare service. This will ensure that Sarah can proceed with her scheduled treatment without any unexpected issues regarding her coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are logical, independent, flexible, direct. First, search_patients with parameters: user_email=lisa.jones889@email.com, authorization_status=verified to ensure you are accessing the correct patient records. Next, think with parameters: action=determine if user has any upcoming appointments, user_email=lisa.jones889@email.com to check Lisa's current appointment schedule and avoid any conflicts. Finally, if no appointments are found, proceed to book_appointment with parameters: user_email=lisa.jones889@email.com, appointment_type=routine, doctor_id=D123, appointment_time=next available to ensure Lisa receives timely healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "lisa.jones889@email.com", "authorization_status": "verified"}
            ),
            Action(
                name="think",
                kwargs={"action": "determine if user has any upcoming appointments", "user_email": "lisa.jones889@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_email": "lisa.jones889@email.com", "appointment_type": "routine", "doctor_id": "D123", "appointment_time": "next available"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are direct, logical, flexible, cautious. Search for patient Robert Johnson using email robert.johnson197@email.com to verify existing records.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are patient, flexible, polite, direct. Search for patient Robert Brown using email robert.brown551@email.com to verify identity and retrieve patient ID. Once you have the patient ID, check healthcare details for the patient ID retrieved to confirm insurance status and coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the patient ID to check healthcare details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are flexible, optimistic, logical. First, search for patient John Johnson using user ID U941 to verify existing records and retrieve patient information. Once the records are verified, check healthcare details for John Johnson to confirm insurance eligibility for booking an appointment. After confirming insurance eligibility, proceed to book an appointment for John Johnson with Dr. Smith (Doctor ID D123) at an available slot on October 20, 2023. Ensure all insurance verification is complete before finalizing the booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "U941", "patient_name": "John Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify patient records and retrieve healthcare details for insurance eligibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check insurance eligibility for John Johnson to confirm appointment booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_id": "D123", "appointment_date": "2023-10-20", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are direct, cautious, patient. Search_patients with email emily.brown290@email.com to retrieve patient ID and insurance details. Then, think to check if the retrieved insurance details are valid for booking appointments. Once you confirm the insurance is valid, proceed to book_appointment for the user ID from the previous task with doctor ID at the next available slot, ensuring all insurance details are verified for a seamless booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if the retrieved insurance details are valid for booking appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "doctor_id": "D123", "slot": "next_available", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are optimistic, flexible, polite, independent. Use the search_patients tool to check if Robert Brown has any upcoming appointments. If no appointments are found, use the book_appointment tool to schedule a routine appointment for Robert Brown during available hours, ensuring no conflicts with emergency appointments. This is important to maintain efficient scheduling and patient care in our healthcare facility.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Robert Brown", "user_id": "P003"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Robert Brown", "appointment_type": "routine", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are confident, cautious. Search_patients with criteria: email \"john.johnson699@email.com\" to retrieve patient ID and insurance details. Once you have the patient ID, proceed to Search_patients with the retrieved patient ID to check for any existing appointments or upcoming healthcare needs. This will ensure that you have a comprehensive understanding of the patient's current healthcare status and can make informed decisions about their care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, confident, patient. \"Search for patient Maria Smith using email maria.smith256@email.com to retrieve patient ID and details.\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are flexible, independent, organized, polite. First, search for patient Sarah Brown using email sarah.brown426@email.com to retrieve patient ID and insurance details. Next, check Sarah Brown's insurance status to verify coverage before scheduling an appointment. Finally, book an appointment for Sarah Brown with Dr. John Smith (Doctor ID: D123) on the next available date and time slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details to check insurance status."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Brown's insurance coverage before proceeding to book an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_id": "D123", "date": "2023-11-01", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are logical, flexible. Use search_patients to retrieve available doctors and their schedules for Maria Johnson's preferred specialty.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P023", "specialty": "Maria Johnson's preferred specialty"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are patient, independent. Search_patients to retrieve Maria Smith's insurance details for verification, and then think to check if Maria Smith's insurance covers Dr. John Doe for primary care. This is crucial to ensure that her upcoming medical needs are covered. Once you have confirmed the insurance coverage, proceed to book_appointment for Maria Smith with Dr. John Doe on March 15, 2024, at 10:00 AM, ensuring insurance is verified to avoid any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Maria Smith's insurance covers Dr. John Doe for primary care."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith", "doctor_name": "Dr. John Doe", "date": "2024-03-15", "time": "10:00 AM", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are confident, polite. \"search_patients using email michael.brown235@email.com to retrieve patient ID and authorization status\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are logical, patient, optimistic. Search_patients for patient ID using email sarah.williams853@email.com to verify user identity and access permissions. Once verified, book_appointment for Sarah Williams with Dr. Smith on the available date and time, ensuring insurance verification is completed. This process is crucial to ensure that Sarah Williams receives the necessary healthcare services without any administrative delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor": "Dr. Smith", "date": "2023-11-15", "time": "10:00", "insurance_verified": true, "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are cautious, patient. Search_patients with criteria \"Robert Garcia\", email \"robert.garcia592@email.com\" to retrieve patient ID and insurance information. Then, check healthcare details for the retrieved patient ID to verify insurance status. This process is essential to ensure that Robert Garcia's insurance is active and covers the necessary services before proceeding with any further healthcare actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"criteria": "Robert Garcia", "email": "robert.garcia592@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are cautious, patient. First, search for patient information for Robert Garcia using email robert.garcia592@email.com to verify authorization status. Once authorization is confirmed, verify insurance coverage for Robert Garcia before proceeding with appointment booking. This ensures that all necessary information is accurate and up-to-date, allowing for a smooth and efficient appointment scheduling process within the healthcare system.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are cautious, logical, direct. Search for user information using email lisa.williams792@email.com to verify identity and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are optimistic, independent, flexible. First, search_patients to retrieve patient details for user ID robert.brown624@email.com to understand his medical history and specific needs. Next, think to determine the best available doctor based on Robert Brown's needs and availability, ensuring the doctor specializes in his required area of care. Finally, search_patients to find available appointment slots for the doctor identified in the previous step, so Robert Brown can receive timely and appropriate medical attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "doctor_specialty": "cardiology", "availability": "next_week"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, optimistic. Search_patients for Robert Brown using email robert.brown624@email.com to retrieve patient ID and medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, organized, direct. First, use the search_patients tool to retrieve Sarah Williams' patient ID and medical history for context in booking an appointment. Next, use the search_patients tool to find available doctors within Sarah Williams' preferred specialties and location to ensure she receives the best care tailored to her needs. Finally, use the book_appointment tool to schedule an appointment for Sarah Williams with Dr. Emily Johnson on the next available date, ensuring it aligns with her schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "specialty": "preferred_specialty", "location": "preferred_location"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "patient_id": "P018", "doctor_name": "Dr. Emily Johnson", "date": "next_available_date"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are patient, independent, confident. First, search for the patient with email david.brown214@email.com using the search_patients tool to verify authorization. Once authorization is confirmed, proceed to check healthcare details to verify David Brown's insurance status. This sequence ensures that all necessary information is validated before any further actions are taken.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are cautious, patient, confident, logical. Search_patients with email sarah.williams602@email.com to retrieve patient ID and authorization status. Once you have the patient ID, check healthcare details for the retrieved patient ID to verify insurance status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, organized. Search_patients using user ID sarah.smith521@email.com to retrieve patient details and authorization status. Think about the retrieved patient details to identify if Sarah Smith has insurance verified. Book_appointment for Sarah Smith with doctor D123 at an identified suitable time slot, ensuring insurance verification is confirmed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Sarah Smith has insurance verified from the retrieved patient details."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_id": "P033", "doctor_id": "D123", "time_slot": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are organized, polite, optimistic, cautious. Book_appointment for John Johnson with Dr. Smith for a routine check-up during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are polite, organized, logical, optimistic. First, search_patients with email sarah.williams853@email.com to retrieve the patient ID and insurance details. Next, search_patients to find available doctors for a routine check-up within the patient's insurance network. Once you have identified an available doctor, book_appointment for the patient ID with the available doctor ID for a routine check-up on the earliest available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"insurance_details": "retrieved_insurance_details", "appointment_type": "routine check-up"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor_id": "available_doctor_id", "appointment_type": "routine check-up", "date": "earliest_available_date", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are optimistic, cautious, direct. First, search for patient information for Robert Garcia using email robert.garcia592@email.com with proper authorization to ensure all personal and medical details are up-to-date. Once you have verified his information, proceed to verify his insurance details to ensure coverage for his upcoming appointments. Finally, book an appointment for Robert Garcia with Dr. Smith on the next available date and time, ensuring that his insurance coverage aligns with this appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005", "action": "verify_insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.garcia592@email.com", "doctor_name": "Dr. Smith", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are independent, cautious, optimistic, patient. First, search for patients using the criteria of the email \"david.brown214@email.com\" to retrieve the patient ID and details. Once you have obtained the patient ID, check the healthcare details to verify the patient's insurance coverage. After confirming the insurance coverage, proceed to book an appointment for the patient with their preferred time slot and doctor ID, ensuring that all insurance details are in order.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the patient's insurance coverage using the retrieved patient ID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After confirming insurance coverage, proceed to book an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor_id": "D123", "time_slot": "2023-11-15T10:00:00", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are patient, organized. Search_patients with name \"Lisa Williams\" and email \"lisa.williams792@email.com\" to retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "email": "lisa.williams792@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are logical, independent. Verify Sarah Miller’s insurance details before proceeding with appointment booking. Once verified, schedule a routine check-up for Sarah Miller with Dr. John Smith on the nearest available date. Ensure that all insurance requirements are met to facilitate a smooth appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Miller's insurance details to ensure they meet the requirements for booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_name": "Dr. John Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, organized. First, search_patients for David Brown's insurance details to verify coverage for upcoming appointments. Once coverage is confirmed, proceed to book_appointment for David Brown with Dr. Smith (doctor ID D001) for a routine check-up on 2023-11-15 at 10:00 AM. This ensures that his insurance will cover the necessary medical services during the visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P020", "patient_name": "David Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P020", "patient_name": "David Brown", "doctor_id": "D001", "appointment_date": "2023-11-15", "appointment_time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are organized, optimistic. First, search_patients for patient ID associated with email emily.davis525@email.com to retrieve patient details. Once you have her information, check healthcare details for user Emily Davis to verify her insurance coverage status. After confirming her insurance, book_appointment for Emily Davis with Dr. Smith at the next available slot, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient details for Emily Davis to check her insurance coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Davis's insurance coverage status before booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor": "Dr. Smith", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are cautious, logical, direct, flexible. \"search_patients for user Lisa Williams using email lisa.williams792@email.com to retrieve patient ID and details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P045", "email": "lisa.williams792@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are flexible, optimistic, logical, confident. Search_patients for Maria Smith using email maria.smith256@email.com to retrieve patient ID and current health records. Think to verify insurance details for the patient ID retrieved and ensure coverage for upcoming appointments. This is crucial to prevent any unexpected costs for the patient and to maintain seamless healthcare service.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and current health records for Maria Smith using the email provided."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure coverage for upcoming appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, polite, flexible, logical. First, search_patients with email \"lisa.williams792@email.com\" to retrieve patient ID and insurance details. Once you have verified the patient ID and insurance, proceed to book_appointment for Lisa Williams with Dr. John Smith at 10:00 AM on 2023-11-15.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P045", "doctor": "Dr. John Smith", "time": "10:00 AM", "date": "2023-11-15", "insurance_details": "retrieved_insurance_details", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are cautious, independent, direct, polite. Check the availability of Dr. Smith for an emergency appointment on the current date. Once the availability is confirmed, book an emergency appointment for Robert Johnson with Dr. Smith for the earliest available time today. After securing the appointment, send a confirmation email to robert.johnson741@email.com to inform him of the appointment details.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "I need to check Dr. Smith's availability for an emergency appointment today."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P024", "doctor_name": "Dr. Smith", "patient_name": "Robert Johnson", "appointment_type": "emergency", "date": "current_date", "time": "earliest_available"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Now that the appointment is booked, I need to send a confirmation email to Robert Johnson."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are independent, direct, cautious, organized. First, search for patient information for John Johnson (john.johnson699@email.com) in the system using search_patients with proper authorization to ensure you have the correct and up-to-date records. Once you have confirmed his details, verify insurance details for John Johnson to ensure coverage for upcoming appointments using think with user ID. This will help avoid any billing issues and confirm that his insurance plan covers the necessary treatments and consultations.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "authorized_by": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are flexible, optimistic, independent. Verify insurance information for John Johnson to ensure coverage before booking an appointment. Once coverage is confirmed, book an appointment with Dr. Smith (Doctor ID: D123) for John Johnson on the earliest available date. This ensures that John can receive the necessary medical care without any delays due to insurance issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P029", "patient_name": "John Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance information for John Johnson to ensure coverage."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "doctor_id": "D123", "patient_name": "John Johnson", "date": "earliest_available"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are optimistic, patient, logical. First, search_patients for Sarah Smith to verify insurance details and authorization to ensure she is covered for her upcoming medical needs. Once the insurance details are confirmed, book_appointment for Sarah Smith with Dr. John Doe during available slot ID A123. This ensures that Sarah can receive timely care with her insurance benefits in place.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Smith", "user_id": "P033"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Smith", "doctor_name": "Dr. John Doe", "slot_id": "A123", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are flexible, patient, logical. First, search_patients with email robert.brown551@email.com to verify patient exists. If the patient is found, think to check insurance status for patient ID [PatientID] and verify coverage. If insurance coverage is confirmed, book_appointment for patient ID [PatientID] with doctor ID [DoctorID] at available time slot. If any issues arise, such as the patient not being found or insurance not being verified, ensure to document the issue and notify the relevant department for further assistance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if the patient with email robert.brown551@email.com exists in the system."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If the patient is found, verify their insurance coverage using their PatientID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If insurance coverage is confirmed, proceed to book an appointment with the doctor using the available time slot."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If any issues arise, such as the patient not being found or insurance not being verified, document the issue and notify the relevant department for further assistance."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are cautious, flexible, polite. search_patients for Sarah Williams using email sarah.williams602@email.com to retrieve patient ID and authorization status",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are confident, logical. Search for patient with email lisa.williams792@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are flexible, optimistic. Use search_patients to retrieve Michael Brown's insurance details for eligibility, and then use think to verify insurance coverage for a general consultation with Doctor ID D567.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "patient_name": "Michael Brown"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P016", "insurance_details": "retrieved_insurance_details", "doctor_id": "D567", "service": "general consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are independent, direct. First, search for patient information with email david.brown214@email.com for authorization verification. Once verified, proceed to search_patients with the user ID associated with David Brown to retrieve his insurance details. This sequence ensures that all necessary information is gathered before any further actions, such as booking appointments, are taken, maintaining the integrity and efficiency of the healthcare process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are optimistic, direct, organized. search_patients with name \"Sarah Miller\" and email \"sarah.miller381@email.com\" to retrieve patient ID",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Miller", "email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are independent, flexible, confident, patient. First, search for patient information for Robert Johnson using email robert.johnson197@email.com to verify authorization. Once authorization is confirmed, search_patients for Robert Johnson's insurance details to confirm validity and coverage. After ensuring that the insurance is valid, proceed to book_appointment for Robert Johnson with Dr. Smith during available hours, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "detail": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Robert Johnson", "doctor_name": "Dr. Smith", "insurance_verified": true, "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are logical, patient. search_patients with name \"John Johnson\" and email \"john.johnson941@email.com\" to retrieve patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Johnson", "email": "john.johnson941@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are flexible, patient, polite. Book_appointment for user \"Robert Jones\" with Dr. Smith (Doctor ID: D567) on available date and time.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones", "doctor_id": "D567", "appointment_date": "2023-11-15", "appointment_time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are polite, logical, optimistic. Please start by searching for patients using the user email lisa.jones889@email.com to retrieve the patient ID and details. Once you have the patient ID, proceed to check the healthcare details to verify insurance requirements and ensure everything is in order for the patient. After verifying the insurance details, book an appointment for the retrieved patient ID with Dr. Smith on the next available date within working hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P050", "doctor": "Dr. Smith", "date": "next_available_date", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are optimistic, independent. Search_patients with email sarah.brown753@email.com to retrieve patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are logical, confident. Search_patients for user Sarah Williams (sarah.williams602@email.com) to retrieve her patient ID and insurance details, then verify her insurance provider and plan details for coverage. Ensure all information is accurate and up-to-date to facilitate a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "name": "Sarah Williams", "email": "sarah.williams602@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, independent, direct. First, use \"search_patients\" to find the patient profile for Sarah Smith using her email sarah.smith521@email.com to verify her authorization. Next, use \"think\" to check Sarah Smith's insurance status and confirm her eligibility for appointment booking. Finally, use \"book_appointment\" to schedule an appointment for Sarah Smith with Dr. Johnson on October 18, 2023, at 10:00 AM, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"task": "Check Sarah Smith's insurance status to confirm eligibility for appointment booking.", "user_id": "P033"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.smith521@email.com", "doctor_name": "Dr. Johnson", "appointment_date": "2023-10-18", "appointment_time": "10:00 AM", "insurance_verified": true, "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are polite, optimistic. Book an emergency appointment for Michael Miller with Dr. Smith using user ID U001 and doctor ID D123.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "patient_id": "P048", "doctor_id": "D123", "appointment_type": "emergency"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, patient. First, search for Sarah Smith's patient profile using her email (sarah.smith521@email.com) to verify her identity. Once her identity is confirmed, retrieve Sarah Smith's insurance details from her patient profile to verify coverage for her upcoming healthcare needs. After confirming her insurance coverage, proceed to book a routine check-up appointment for Sarah Smith with Dr. Johnson at an available time slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"thoughts": "Verify Sarah Smith's identity and retrieve her insurance details from the patient profile."}
            ),
            Action(
                name="think",
                kwargs={"thoughts": "Ensure Sarah Smith's insurance coverage is confirmed for her upcoming healthcare needs."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.smith521@email.com", "doctor_name": "Dr. Johnson", "appointment_type": "routine check-up", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are cautious, confident, logical, flexible. Search for patient details with email sarah.brown426@email.com to verify identity and access level for booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are flexible, logical, direct, cautious. First, search_patients for Michael Brown to retrieve patient ID and healthcare details. Next, book_appointment for Michael Brown with Dr. Smith on Thursday at 2 PM, ensuring availability. Finally, think to confirm all appointment details with Michael Brown via email, providing him with the appointment time, location, and any necessary preparation instructions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Michael Brown", "user_id": "P016"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P016", "doctor": "Dr. Smith", "date": "Thursday", "time": "2 PM", "user_id": "P016"}
            ),
            Action(
                name="think",
                kwargs={"message": "Confirm all appointment details with Michael Brown via email, providing him with the appointment time, location, and any necessary preparation instructions.", "user": "Robert Johnson", "email": "robert.johnson197@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are logical, organized, flexible, independent. Search_patients with email \"maria.miller855@email.com\" to retrieve Maria's patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are cautious, optimistic, flexible. First, use search_patients to verify Maria Smith's insurance details for coverage confirmation. Once the insurance verification is complete, proceed to use book_appointment to schedule a routine check-up for Maria Smith with Dr. Johnson on 2023-11-15 at 10:00 AM. Finally, use search_patients to find any recent test results for Maria Smith to ensure that Dr. Johnson has all necessary information for the upcoming appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith", "details": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith", "doctor_name": "Dr. Johnson", "date": "2023-11-15", "time": "10:00 AM", "appointment_type": "routine check-up"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith", "details": "recent test results"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are patient, cautious, organized. Search_patients with email \"maria.johnson759@email.com\" to retrieve patient ID and details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are independent, organized, cautious, optimistic. First, think to assess doctor's availability for appointments based on Sarah Miller’s preferred schedule, ensuring her needs align with Dr. Smith's (ID: D002) calendar. Next, search_patients to find available timeslots for Dr. Smith (ID: D002) within the next week that match Sarah's preferences. Finally, book_appointment for Sarah Miller with Dr. Smith (ID: D002) on the available date and time, ensuring insurance verification is completed to confirm the appointment.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D002", "user_id": "P046", "preferred_schedule": "next_week"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Miller", "doctor_id": "D002", "user_id": "P046", "appointment_time": "2023-10-25T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are direct, independent. First, search for Emily Jones in the patient database using email emily.jones379@email.com to verify her details. Once her details are confirmed, proceed to verify Emily Jones's insurance coverage before confirming the appointment with Dr. Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Jones's insurance coverage before confirming her appointment with Dr. Smith."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are optimistic, patient, confident. Search for patient Emily Jones using her email emily.jones379@email.com to retrieve her patient ID and healthcare plan details. Verify insurance coverage for Emily Jones to ensure eligibility for booking appointments. Book an appointment for Emily Jones with Dr. Smith (doctor ID D101) on the next available date and time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Emily Jones' patient ID and healthcare plan details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Jones' insurance coverage to ensure eligibility for booking appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "D101", "date": "next_available_date", "time": "next_available_time", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are logical, cautious. First, verify insurance details for Emily Jones using policy number 123456789 to ensure her coverage is active. Once the insurance is confirmed, proceed to book an appointment for Emily Jones with Dr. Smith on 2023-11-15 at 10:00 AM. Finally, send a confirmation email to emily.jones379@email.com with the appointment details, ensuring she is aware of the time and location, and that her insurance has been verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"policy_number": "123456789", "user_id": "P007"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Emily Jones", "doctor_name": "Dr. Smith", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are confident, polite. Search_patients for user Robert Johnson (robert.johnson197@email.com) to retrieve personal healthcare records and verify authorization for access. Then, think to determine the most appropriate specialist for Robert Johnson based on his current healthcare records and needs. Ensure that the selected specialist aligns with his medical requirements and insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P027", "email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are polite, optimistic. Search for patient records of Sarah Miller using the email sarah.miller381@email.com with authorization check.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are polite, flexible, organized. First, search_patients for Michael Brown's insurance status to verify coverage. Once coverage is confirmed, book_appointment for Michael Brown with Dr. Smith (ID: D456) on the next available slot, ensuring it's during working hours. This will ensure that Michael Brown's visit is covered and scheduled efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "patient_name": "Michael Brown", "information": "insurance_status"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P016", "patient_name": "Michael Brown", "doctor_id": "D456", "appointment_type": "routine", "time_slot": "next_available"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are organized, confident, independent. Use think to determine if Emily Garcia needs a routine check-up or has an urgent healthcare concern. Once you have confirmed that Emily requires a routine check-up, use book_appointment to schedule a routine appointment with Dr. Smith for Emily Garcia on the available date and time.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, confident, logical, optimistic. Search_patients with email michael.miller534@email.com to verify patient authorization and retrieve patient ID. Once the patient ID is confirmed, book_appointment for patient ID with the selected specialist at an available time, ensuring insurance verification is complete. This process is crucial to ensure that Michael Miller receives timely and efficient healthcare services, with all necessary authorizations and insurance details accurately verified before the appointment is scheduled.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "patient_id": "P048", "specialist": "selected_specialist", "time": "available_time", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are polite, confident, independent. \"Search_patients for Michael Brown to retrieve patient ID and medical history\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "patient_name": "Michael Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are patient, flexible, optimistic. Search for patient John Johnson using email john.johnson699@email.com to retrieve patient ID and authorization status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are confident, patient. Search_patients with email \"maria.smith554@email.com\" to retrieve patient ID and insurance details. Then, think to verify insurance coverage for the retrieved patient ID to ensure that the patient is covered for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for the retrieved patient ID to ensure that the patient is covered for a routine check-up."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, logical, direct. First, search_patients for Maria Smith's insurance details to verify coverage before scheduling an appointment. Once you have confirmed that her insurance covers the healthcare service, proceed to book_appointment for Maria Smith with doctor ID D001 on the next available date and time slot. This ensures that Maria's appointment is scheduled efficiently and without unexpected costs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith", "doctor_id": "D001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are independent, flexible, cautious. First, search_patients with user_email \"maria.miller855@email.com\" to retrieve patient ID and insurance information. Next, think to verify insurance details for the patient ID retrieved from search_patients to ensure eligibility for appointments. Once insurance verification is complete, book_appointment for the patient ID with Dr. John Smith (Doctor ID D001) on the earliest available date and time, ensuring the patient is eligible for the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the patient ID retrieved from search_patients to ensure eligibility for appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P042", "doctor_id": "D001", "date": "earliest_available_date", "time": "earliest_available_time", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are optimistic, organized, polite. search_patients with parameters: email=\"maria.smith256@email.com\", retrieve medical history and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "retrieve": ["medical history", "insurance details"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are confident, logical, cautious. think: Assess Robert Johnson's healthcare needs and determine if an appointment is necessary based on his medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are patient, cautious, flexible, polite. Search for John Johnson's patient record using email john.johnson941@email.com to verify insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are polite, organized. Search_patients with name \"Emily Davis\" and email \"emily.davis525@email.com\" to retrieve patient ID, then think to determine a suitable healthcare specialty for Emily Davis based on her medical history. Emily recently experienced recurring chest pains and shortness of breath, indicating a potential heart issue. After reviewing her medical history, you decide that a cardiologist is the appropriate specialist for her condition.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Davis", "email": "emily.davis525@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Based on Emily Davis's symptoms of recurring chest pains and shortness of breath, which indicate a potential heart issue, a cardiologist is the appropriate specialist for her condition."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are optimistic, direct, logical, confident. Use search_patients with patient_id 290 to retrieve Emily Brown's medical history for consultation preparation. Then, use think to prioritize Emily Brown's appointment based on urgency and doctor availability, ensuring that her needs are met promptly. Finally, use book_appointment to schedule a consultation for Emily Brown with Dr. Smith, ensuring it falls within available hours, and notify Emily Brown via email about the confirmed appointment details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P021"}
            ),
            Action(
                name="think",
                kwargs={"task": "Prioritize Emily Brown's appointment based on urgency and doctor availability"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P021", "doctor_id": "D001", "appointment_time": "2023-10-15T10:00:00", "user_id": "P021", "insurance_verified": true, "notify_email": "emily.brown@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are confident, polite. Search for patient profile using email john.johnson941@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are flexible, organized. First, think to determine if Emily Jones requires a routine or emergency appointment. Once you have established that Emily Jones needs a routine appointment, search_patients with doctor_id='D123' to retrieve available appointment slots.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are flexible, patient. First, search for patient Emily Garcia using email emily.garcia400@email.com to retrieve her patient ID. Once you have the patient ID, verify the insurance details to ensure her coverage is up-to-date. This will help in scheduling her upcoming appointments without any issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results to verify insurance details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are independent, confident, organized, patient. First, use the \"search_patients\" tool with parameters: user_email=sarah.williams602@email.com, search_criteria=\"patient medical history\" to gather necessary medical history for an upcoming appointment. Next, use the \"think\" tool with parameters: context=\"appointment type\" to prioritize if the appointment is routine or emergency based on the patient's medical history. Finally, use the \"search_patients\" tool with parameters: user_email=sarah.williams602@email.com, search_criteria=\"doctor availability\" to confirm Dr. Smith's available hours, ensuring the appointment can be scheduled at a suitable time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.williams602@email.com", "search_criteria": "patient medical history"}
            ),
            Action(
                name="think",
                kwargs={"context": "appointment type"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.williams602@email.com", "search_criteria": "doctor availability"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, optimistic, flexible, logical. Search for patient information using email maria.smith256@email.com to verify identity and authorization.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are direct, organized, cautious, flexible. think: Consider Lisa Williams' medical history and insurance information to determine eligibility for appointment scheduling.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, organized, independent. Use the tool `search_patients` to find patient details for Lisa Jones using email lisa.jones889@email.com, and then use the tool `think` to verify insurance status for patient Lisa Jones to ensure eligibility for scheduling an appointment. This process is crucial to confirm her insurance details are up-to-date before proceeding with any further actions, ensuring a smooth experience for both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
            Action(
                name="think",
                kwargs={"patient_email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, flexible, cautious. First, identify available doctors for Sarah Williams' required treatment to ensure she receives the best care possible. Once a suitable doctor is found, retrieve available appointment slots for Dr. John Smith within the next week. Finally, schedule an appointment for Sarah Williams with Dr. John Smith on 12/10/2023 at 10:00 AM, ensuring insurance verification is complete to avoid any issues on the day of the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Identify available doctors for Sarah Williams' required treatment."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Dr. John Smith is identified as a suitable doctor for Sarah Williams."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve available appointment slots for Dr. John Smith within the next week."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance for Sarah Williams to ensure no issues on the day of the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams", "doctor_name": "Dr. John Smith", "appointment_date": "12/10/2023", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are flexible, confident. Think to determine what type of healthcare service Robert Johnson needs based on recent interactions and preferences. Then, book_appointment for Robert Johnson with Dr. Smith (doctor ID: D123) for a cardiology check-up, ensuring insurance verification is complete. This sequence ensures that Robert receives the necessary care promptly while confirming his insurance coverage for the cardiology service, aligning with his recent health focus and preferences.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Robert Johnson has shown a recent focus on cardiology services, indicating a need for a cardiology check-up. He prefers Dr. Smith for this service."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P027", "email": "robert.johnson197@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P027", "doctor_id": "D123", "service": "cardiology check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are organized, confident, optimistic. Verify insurance coverage for user Sarah Brown (sarah.brown426@email.com) before proceeding with appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "email": "sarah.brown426@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are independent, patient, organized. Search for patient Maria Johnson using email maria.johnson759@email.com to retrieve her patient ID, and then use this ID to check Maria Johnson's healthcare details and insurance status. This process is essential to ensure that Maria Johnson's insurance coverage is verified for her appointment eligibility, allowing for a smooth and efficient scheduling process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search_patients response and use it to check Maria Johnson's healthcare details and insurance status."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are organized, direct, confident, patient. Begin by searching for patients with the user email sarah.williams853@email.com to retrieve the patient ID and authorization status. Once you have obtained the authorization status, think to verify whether you are permitted to access the patient's information. This process is crucial to ensure compliance with healthcare privacy regulations before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization status to ensure compliance with healthcare privacy regulations."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are direct, independent, polite. Use tool \"search_patients\" to verify the identity and authorization of user John Johnson (john.johnson699@email.com). Once verified, use tool \"search_patients\" to retrieve available appointment slots for Dr. Smith, ensuring they align with John Johnson's insurance coverage. This process is essential to confirm that John Johnson can schedule an appointment with Dr. Smith without any issues related to insurance acceptance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P029", "email": "john.johnson699@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P029", "doctor_name": "Dr. Smith", "insurance_email": "john.johnson699@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, organized, flexible, independent. \"search_patients for user Emily Brown using email emily.brown290@email.com to retrieve patient ID and insurance details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user": "Emily Brown", "email": "emily.brown290@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are cautious, logical. Search for patient information for Robert Johnson using email robert.johnson741@email.com to verify authorization and retrieve healthcare details. Then, think to assess if Robert Johnson qualifies for an emergency appointment based on the retrieved healthcare details, ensuring that the decision is made with consideration of the urgency of his medical needs and the availability of resources.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess if Robert Johnson qualifies for an emergency appointment based on the retrieved healthcare details, considering the urgency of his medical needs and the availability of resources."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are cautious, polite, confident. Search_patients with email \"sarah.williams853@email.com\" to retrieve patient ID and authorization status",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are flexible, confident, independent, organized. Search for Emily Garcia's patient ID using her email (emily.garcia400@email.com) for appointment booking, and then book an appointment for her with Dr. John Smith (ID: D567) for a cardiology consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor_id": "D567", "specialty": "cardiology", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are independent, organized, patient, polite. First, search for patient information for David Brown using email david.brown214@email.com to verify authorization. Once authorization is confirmed, verify David Brown's insurance details to ensure coverage for an appointment with Dr. Smith. This process is essential to ensure that David Brown can receive the necessary care without any financial or administrative issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are independent, patient, cautious. Search for patient information for Sarah Brown using email sarah.brown753@email.com to verify authorization. Once verified, proceed to book an appointment for Sarah Brown with Dr. Smith on the next available date, ensuring the time is within Dr. Smith’s working hours. After securing the appointment, confirm the appointment details with Sarah Brown via email sarah.brown753@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown753@email.com", "doctor_name": "Dr. Smith", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are logical, polite, patient, organized. Search_patients with criteria: name \"Lisa Williams\" and email \"lisa.williams792@email.com\" to retrieve patient ID and medical records.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are flexible, logical, optimistic, organized. First, search_patients with the name \"Robert Brown\" to retrieve patient ID and insurance details for verification. Next, use this information to verify Robert Brown's insurance status and coverage for the upcoming appointment. Finally, book_appointment for Robert Brown with Dr. Smith on the next available slot, ensuring it aligns with Robert's insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Brown", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Robert Brown to verify insurance status."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance status and coverage for the upcoming appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P003", "doctor": "Dr. Smith", "date": "next_available", "insurance_verified": true, "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, flexible, patient. First, search for patient David Brown using email david.brown214@email.com to retrieve his patient ID and healthcare details. Once you have confirmed his information, verify David Brown's insurance eligibility for a general consultation appointment to ensure coverage. After confirming eligibility, book an appointment for David Brown with Dr. Smith on the earliest available date to facilitate timely healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor": "Dr. Smith", "date": "2023-11-01", "time": "10:00 AM", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are optimistic, cautious, organized. Use the tool `search_patients` with the parameter `email` set to \"maria.smith256@email.com\" to verify Maria Smith's patient ID and authorized access.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are cautious, optimistic, polite. First, search for patient information using user email sarah.williams602@email.com to verify authorization, ensuring you have the correct patient details for further actions. Once authorization is confirmed, proceed to search_patients to check Sarah Williams's insurance status and coverage details, as this is crucial for determining her healthcare options. After confirming her insurance coverage, think to determine available doctors for Sarah Williams based on her insurance network, ensuring that the options provided are within her plan. Finally, book_appointment for Sarah Williams with Dr. John Smith on the earliest available date, making sure it aligns with his working hours to provide a seamless scheduling experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.williams602@email.com", "doctor_name": "Dr. John Smith", "date": "2023-10-15", "time": "10:00 AM", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are organized, cautious. First, search for patient details of Sarah Miller using the search_patients tool with the email sarah.miller381@email.com. Once you have retrieved her details, verify Sarah Miller's insurance information for validity and coverage using available records. After confirming her insurance, book a routine check-up appointment with Dr. Smith for Sarah Miller on November 16th at 10:00 AM, ensuring that the insurance is verified beforehand.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Miller's insurance information for validity and coverage using available records."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.miller381@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-16", "appointment_time": "10:00", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are cautious, optimistic. First, use `search_patients` to find patient information for David Miller using email david.miller979@email.com. Once you have located his information, use `think` to check David Miller's insurance details for verification. After confirming his insurance details, proceed to use `book_appointment` to schedule a routine check-up for David Miller with Dr. Smith during available hours. Ensure that the insurance verification is completed before finalizing the appointment to maintain a seamless experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com", "user_id": "P028"}
            ),
            Action(
                name="think",
                kwargs={"action": "verify_insurance", "patient_email": "david.miller979@email.com", "user_id": "P028"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.miller979@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are polite, independent. Search for emergency appointment availability for John Johnson with Dr. Smith using book_appointment tool.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"doctor_name": "Dr. Smith", "patient_name": "John Johnson", "appointment_type": "emergency", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are flexible, polite. First, search for Maria Smith's patient record using her email maria.smith554@email.com to confirm her identity and retrieve her patient ID. Once you have the patient ID, verify Maria Smith's insurance details to ensure she has coverage for her upcoming healthcare services. This will help us provide a seamless experience for Maria Smith and ensure that her routine check-up with Dr. Johnson is fully covered.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are independent, logical, confident. First, check healthcare details for user John Johnson (john.johnson941@email.com) to retrieve current primary care physician information. Then, search_patients for John Johnson's insurance information to verify coverage details, ensuring that his insurance plan will cover an appointment with his primary care physician.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "email": "john.johnson941@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are polite, optimistic, patient. Search for insurance details for Maria Johnson using her insurance ID I98765 to verify coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P023", "insurance_id": "I98765"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are flexible, direct, cautious, patient. First, identify available doctors for Emily Davis based on her medical history and preferences to ensure she receives the most suitable care. Once you have identified the appropriate specialists, find available appointment slots for Dr. John Smith, who specializes in Emily Davis's health concerns, to provide her with timely and expert medical attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Identify specialists based on Emily Davis's medical history and preferences."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Dr. John Smith is identified as a suitable specialist for Emily Davis's health concerns."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "doctor_name": "Dr. John Smith", "patient_name": "Emily Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are optimistic, cautious, independent, flexible. First, search for patient information using email michael.brown235@email.com to verify authorization for accessing healthcare details. Once authorization is confirmed, think to confirm insurance information is available for Michael Brown prior to booking an appointment. This ensures that all necessary information is in place for a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are confident, optimistic, direct. Search_patients with email robert.johnson741@email.com to retrieve user ID and authorization status, then think to verify insurance details for user Robert Johnson using the retrieved user ID. This process is essential to ensure that Robert's insurance covers his upcoming healthcare needs, providing him with peace of mind and seamless access to medical services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve user ID and authorization status for Robert Johnson to verify insurance details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are organized, optimistic. First, search_patients with parameters: email=emily.jones379@email.com, context=retrieve patient profile details to gather necessary information about Emily Jones. Once you have the details, think with parameters: context=determine suitable doctor based on Emily's healthcare needs to ensure she is matched with the most appropriate healthcare provider for her upcoming appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "context": "retrieve patient profile details"}
            ),
            Action(
                name="think",
                kwargs={"context": "determine suitable doctor based on Emily's healthcare needs"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are patient, polite, logical, direct. Use search_patients to find patient records for Sarah Smith's healthcare provider to ensure you have the correct patient information. Then, use think to check Sarah Smith's insurance details for coverage verification, ensuring that the consultation with Dr. John Doe is covered by her insurance plan. Finally, use book_appointment to schedule a consultation for Sarah Smith with Dr. John Doe during available hours, ensuring that all necessary information is in place for a smooth appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P033", "task": "Verify insurance coverage for Sarah Smith's consultation with Dr. John Doe"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith", "doctor_name": "Dr. John Doe", "appointment_time": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are direct, flexible, patient, optimistic. Use `search_patients` to find Emily Garcia's patient record using email emily.garcia400@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are confident, polite, independent, optimistic. Search for patient details for Sarah Brown using email sarah.brown753@email.com with proper authorization to ensure you have the correct information on file. Once verified, proceed to book an appointment for Sarah Brown with Dr. Smith on the earliest available date to address her healthcare needs promptly. After securing the appointment, confirm the booking details and send a confirmation email to sarah.brown753@email.com to keep her informed and prepared for her visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown753@email.com", "doctor_name": "Dr. Smith", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are flexible, independent, direct. Search for patient information for Robert Brown using the search_patients tool with email robert.brown624@email.com to verify identity and retrieve patient ID. Then, verify insurance details for Robert Brown using the think tool to ensure eligibility for booking an appointment. This process is crucial to ensure that Robert Brown's healthcare needs are met efficiently and that he is eligible for the services he requires.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance details for patient ID retrieved for Robert Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are cautious, independent, logical. Book an appointment with Dr. Smith (Doctor ID: D567) for a consultation on preventative healthcare for John Johnson.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "doctor_id": "D567", "patient_name": "John Johnson", "appointment_type": "consultation", "topic": "preventative healthcare"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, optimistic, confident. Use the search_patients tool with email emily.jones379@email.com to verify Emily Jones' patient ID and basic details. Then, use the think tool to identify available doctors for Emily Jones' required specialty, ensuring they meet her healthcare needs. Finally, use the search_patients tool to find available appointment slots for the identified doctor that match Emily Jones' schedule preferences, ensuring a seamless booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Identify available doctors for Emily Jones' required specialty"}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D123", "schedule_preferences": "morning"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are logical, optimistic, flexible, patient. First, search_patients with the name \"Lisa Jones\" to verify her patient ID and insurance information. Once her insurance information is confirmed, proceed to book_appointment for Lisa Jones with Dr. Smith for a general check-up, ensuring all insurance details are accurately recorded.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones", "user_id": "P050"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P050", "doctor": "Dr. Smith", "appointment_type": "general check-up", "insurance_info": "verified", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are organized, flexible. First, check healthcare details for patient 'David Brown' to verify insurance eligibility. After confirming insurance, think to determine available doctors for appointment scheduling based on David Brown's healthcare needs. Finally, book_appointment for David Brown with Dr. Smith (doctorID 'DR123') on available slot '2023-10-15T10:00'.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "David Brown", "user_id": "P020"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance eligibility for David Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine available doctors for appointment scheduling based on David Brown's healthcare needs"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor_id": "DR123", "appointment_time": "2023-10-15T10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are patient, cautious. Search_patients using Sarah Brown's email (sarah.brown426@email.com) to retrieve her patient ID and medical history. Then, think to determine if Sarah Brown's medical condition requires an emergency appointment based on her medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are cautious, optimistic, polite, direct. Search for patient Maria Johnson using email maria.johnson759@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are patient, direct, optimistic, polite. First, search_patients for Robert Johnson using email robert.johnson197@email.com to retrieve patient ID and insurance details. Next, think to verify if Robert Johnson has valid insurance coverage for booking appointments. Once verified, search_patients for available doctors specializing in cardiology to find suitable matches for Robert Johnson, ensuring that the selected doctor accepts his insurance for a seamless booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Robert Johnson has valid insurance coverage for booking appointments."}
            ),
            Action(
                name="search_patients",
                kwargs={"specialization": "cardiology", "insurance": "Robert Johnson's insurance details"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are flexible, independent. Search_patients with email john.johnson941@email.com to retrieve patient ID and insurance details. Then, verify insurance details for patient ID to ensure coverage for upcoming appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search_patients response."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are cautious, optimistic, polite. First, search for patient Michael Brown using email michael.brown235@email.com to verify authorization status. Once his authorization is confirmed, use the think tool to confirm Michael Brown's insurance details for appointment eligibility. This ensures that when booking an appointment, all necessary prerequisites are met, facilitating a smooth and efficient process for Michael's healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com", "user_id": "P016"}
            ),
            Action(
                name="think",
                kwargs={"task": "Confirm Michael Brown's insurance details for appointment eligibility", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are logical, direct, patient. Use `search_patients` to find patient information with email maria.miller855@email.com for verification purposes. Once you have retrieved Maria Miller's information, use `think` to verify her insurance status to ensure she is covered for a routine check-up. After confirming her insurance details, use `think` to identify available doctors for a routine check-up. Finally, use `book_appointment` to schedule an appointment for Maria Miller with Dr. Smith on October 20, 2023, at 2:00 PM, ensuring that her insurance has been verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify insurance status for Maria Miller"}
            ),
            Action(
                name="think",
                kwargs={"task": "Identify available doctors for a routine check-up"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.miller855@email.com", "doctor_name": "Dr. Smith", "date": "2023-10-20", "time": "14:00", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, cautious, flexible, optimistic. First, Search_patients with parameters: user_email=sarah.brown753@email.com, authorization_code=AUTH1234 to retrieve patient ID and insurance details. Then, Think: Evaluate if Sarah Brown has any existing appointments in the system. If she does not have any, proceed to Think: Determine the next available appointment slot for Dr. Smith for a routine check-up. Once the slot is identified, Book_appointment with parameters: patient_id=PID5678, doctor_id=DOC4321, appointment_type=routine, date=2023-10-15, time=10:00, insurance_verified=true to schedule a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.brown753@email.com", "authorization_code": "AUTH1234"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P025", "doctor_id": "DOC4321", "appointment_type": "routine", "date": "2023-10-15", "time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are cautious, organized, direct. Search for patient details using email sarah.smith521@email.com to verify identity and authorization for accessing medical records.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are optimistic, flexible, direct. Book an appointment using patient ID P001 with doctor D123 on 2023-11-15 at 10:00 AM.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are optimistic, logical. Search_patient for user Robert Brown with email robert.brown731@email.com to retrieve patient ID and insurance details. Think to verify if user Robert Brown has insurance coverage for routine visits. Book_appointment for user Robert Brown with Dr. Smith for a routine check-up next Tuesday at 10:00 AM, ensuring insurance coverage is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P014", "name": "Robert Brown", "email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Robert Brown has insurance coverage for routine visits."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_id": "P014", "doctor": "Dr. Smith", "time": "2023-10-31T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are logical, independent. First, search for patient records using the user email lisa.jones889@email.com to retrieve the patient ID. Once you have obtained the patient ID, proceed to verify the insurance details for this patient. This sequence ensures that the patient's insurance information is up-to-date before any further healthcare services are scheduled.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the patient ID to verify insurance details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are organized, patient, polite, logical. First, search for patient records for David Williams using email david.williams693@email.com to verify insurance details. Once you have retrieved the insurance information, verify the insurance status for David Williams and obtain the policy number and coverage details. After confirming his insurance coverage, proceed to book an appointment for David Williams with Dr. Smith on the available date and time slot that suits his schedule. Finally, send a confirmation email to David Williams at david.williams693@email.com with the appointment details, ensuring all information is clear and accurate.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com", "user_id": "P006"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve insurance details for David Williams to verify coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status and obtain policy number and coverage details for David Williams."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.williams693@email.com", "doctor_name": "Dr. Smith", "user_id": "P006"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Send a confirmation email to David Williams with the appointment details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are flexible, logical. Book an appointment for John Johnson with Dr. John Smith on the first available slot.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "doctor_name": "Dr. John Smith", "patient_name": "John Johnson", "email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are independent, organized. Search_patients for Maria Smith using email maria.smith256@email.com to retrieve patient ID and medical history, then check insurance details for user Maria Smith to verify coverage for upcoming appointments. Ensure that her medical history aligns with her insurance coverage for any necessary treatments or procedures.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are optimistic, independent, polite. First, search_patients to check Robert Brown's insurance status and verify coverage details to ensure that his medical expenses are covered. Once the insurance verification is complete, proceed to book_appointment for Robert Brown with the selected doctor using the best available appointment slot, ensuring that all insurance requirements are met.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "doctor_id": "D001", "appointment_time": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are independent, polite, patient. Use search_patients to locate patient Sarah Brown using email sarah.brown753@email.com. Once you have retrieved Sarah Brown's information, verify her insurance eligibility to ensure she can proceed with scheduling an appointment. After confirming her insurance details, book an appointment for Sarah Brown with Dr. Smith at the next available slot, ensuring it fits within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After retrieving Sarah Brown's information, I will verify her insurance eligibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Sarah Brown's insurance is verified. Now, I will proceed to book an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown753@email.com", "doctor_name": "Dr. Smith", "appointment_time": "next_available", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are optimistic, direct, patient. Use `search_patients` to find patient records for Robert Garcia, ensuring proper authorization is granted. Then, use `think` to verify Robert Garcia's insurance details and check eligibility for an appointment. Finally, use `book_appointment` to schedule a routine appointment for Robert Garcia with Dr. Smith, ensuring it falls within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P005", "task": "Verify insurance details and check eligibility for Robert Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are independent, confident, direct, logical. Search_patients with email \"lisa.jones889@email.com\" to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are cautious, confident. First, use `search_patients` to find patient Robert Jones with email robert.jones332@email.com for verification. Once you have confirmed his identity, proceed to use `search_patients` to verify Robert Jones's insurance details for eligibility. This ensures that his insurance is valid and covers the necessary services before any further steps are taken.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026", "verify_insurance": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are flexible, cautious, patient, optimistic. First, search_patients for Maria Johnson using email maria.johnson759@email.com to retrieve her patient ID and details. Next, use the patient ID retrieved to check for any existing appointments or medical history to ensure there are no conflicts or necessary preparations. Finally, search_patients using the same patient ID to retrieve a list of available appointment slots with her preferred doctor, Dr. Smith, so you can proceed with booking an appointment that suits her schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023", "doctor": "Dr. Smith"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are optimistic, flexible. Search for patient details using user ID 'john.johnson627@email.com' to verify patient authorization. Once verified, think to determine the appropriate department for John Johnson's healthcare needs based on retrieved patient details. If cardiology is determined to be the appropriate department, search_patients for available doctors specializing in cardiology for patient 'John Johnson' to check availability.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "specialty": "cardiology", "patient_name": "John Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are logical, direct, cautious, confident. Search for Robert Johnson's medical records using his email robert.johnson741@email.com to ensure you have the most up-to-date information. Next, check healthcare details for Robert Johnson's insurance coverage and policy details to confirm that his insurance is valid and will cover his upcoming appointment. Finally, book an appointment for Robert Johnson with Dr. Sarah Lee on October 21st at 10:00 AM, ensuring that insurance verification is completed and send a confirmation email to Robert to notify him of the appointment details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="think",
                kwargs={"text": "Verify Robert Johnson's insurance coverage and policy details to ensure it is valid for the upcoming appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson741@email.com", "doctor_name": "Dr. Sarah Lee", "appointment_date": "2023-10-21", "appointment_time": "10:00", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are logical, independent, optimistic. Search_patients for Robert Brown using email robert.brown624@email.com to verify patient record. Then, search_patients for Robert Brown's medical history to prepare for the upcoming appointment with Dr. Smith. Finally, book_appointment for Robert Brown with Dr. Smith for a routine check-up, ensuring the appointment fits within Dr. Smith's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com", "user_id": "P017"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Robert Brown", "user_id": "P017"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, confident. First, book an appointment for Emily Davis with Dr. Brown for an emergency visit at 10 AM on 2023-11-14, prioritizing it over routine visits. Next, think to decide if Emily Davis needs to cancel her routine appointment due to the emergency visit. Finally, book an appointment for a follow-up visit with Dr. Green at 2 PM on 2023-11-20 for Emily Davis, ensuring insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "doctor_name": "Dr. Brown", "appointment_type": "emergency", "date": "2023-11-14", "time": "10:00"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Consider if Emily Davis needs to cancel her routine appointment due to the emergency visit."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "doctor_name": "Dr. Green", "appointment_type": "follow-up", "date": "2023-11-20", "time": "14:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are confident, logical. Search for patient information for user Sarah Brown (sarah.brown426@email.com) in the healthcare database using the search_patients tool. Once you have confirmed her details, book an appointment for Sarah Brown with Dr. Smith at the earliest available slot using the book_appointment tool.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown426@email.com", "doctor_name": "Dr. Smith", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are polite, flexible, optimistic. First, search for patient information using the search_patients tool with parameters: patient name \"Sarah Miller\" and email \"sarah.miller381@email.com\" to verify user identity and access permissions. Once verified, proceed to verify Sarah Miller's insurance details to ensure coverage is available for her upcoming appointments. After confirming her insurance, search for available appointment slots with Dr. Smith using the book_appointment tool with parameters: provider ID \"D123\" and patient ID \"P456\". This will help in efficiently scheduling Sarah's medical consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Sarah Miller", "email": "sarah.miller381@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"provider_id": "D123", "patient_id": "P046", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are organized, confident, logical. Use `search_patients` tool to find patient record for Robert Johnson (robert.johnson197@email.com) to verify insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are cautious, flexible. Use `book_appointment` to schedule a routine check-up appointment for John Johnson with Dr. Smith during available hours next Tuesday at 10 AM.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "date": "next Tuesday", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are flexible, patient, optimistic, independent. First, search for patient information using the search_patients tool with parameters: patient_email=emily.jones379@email.com, authorization_code=AUTH123, to verify the patient's identity and gather necessary contact details. Once you have confirmed the patient's identity and ensured all information is accurate, proceed to book an appointment using the book_appointment tool with parameters: patient_id=PAT001, doctor_id=DOC101, appointment_date=2023-11-15, appointment_time=10:00 AM, insurance_verified=True. This sequence ensures that the patient's details are up-to-date and that the appointment is scheduled efficiently and correctly, maintaining a high standard of patient care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "emily.jones379@email.com", "authorization_code": "AUTH123"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "DOC101", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are flexible, independent, organized, polite. First, search for patient information using search_patients with patient_email \"emily.davis525@email.com\" to verify identity and authorization. Once verified, check healthcare details for the retrieved patient ID to confirm insurance status and coverage details, ensuring that the patient is eligible for the services they require.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "emily.davis525@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are logical, flexible, patient. Think to assess Robert Garcia's healthcare needs and determine if an appointment is necessary. Then, think to determine if Robert Garcia's condition requires an emergency or routine appointment. Consider his recent symptoms, medical history, and any advice from previous consultations to make an informed decision. Ensure that your assessment aligns with the clinic's protocol for prioritizing patient care, and communicate your findings clearly to the scheduling team to facilitate the appropriate next steps for Robert's healthcare management.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005", "name": "Robert Garcia"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess Robert Garcia's recent symptoms, medical history, and previous consultations to determine if an appointment is necessary and whether it should be an emergency or routine."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "appointment_type": "emergency", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, independent. First, use the search_patients tool to find the patient record for user Robert Jones (robert.jones332@email.com) to verify his insurance details. Once you have confirmed his insurance eligibility, use the book_appointment tool to schedule a routine check-up for Robert Jones with Dr. Smith at 10:00 AM on the next available date. Finally, use the search_patients tool to retrieve Robert Jones's medical history for Dr. Smith's review prior to the appointment, ensuring all necessary information is prepared for optimal patient care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.jones332@email.com", "doctor_name": "Dr. Smith", "appointment_time": "10:00 AM", "user_id": "P026"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are optimistic, patient, cautious, organized. Search for patient information using user ID sarah.miller381@email.com to verify authorization for appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are optimistic, independent, confident, polite. Use search_patients with parameters: user_email=david.brown214@email.com to retrieve patient ID and insurance status. Then, use think to analyze retrieved patient details to verify insurance coverage. If the patient is covered, proceed to book_appointment with parameters: patient_id=<patient_id>, doctor_id=<doctor_id>, appointment_type=\"routine\", date=<available_date>, time=<available_time> to schedule a routine check-up. This ensures that David Brown receives timely healthcare services while confirming his insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_details": "<retrieved_patient_details>"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor_id": "<doctor_id>", "appointment_type": "routine", "date": "<available_date>", "time": "<available_time>"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, polite, confident. Search_patients for user ID robert.johnson197@email.com to verify insurance details and ensure proper authorization.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P027", "email": "robert.johnson197@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are logical, optimistic, confident. Retrieve Maria Miller's patient records using her email maria.miller855@email.com to verify identity and obtain patient ID. Evaluate the retrieved patient information to identify any scheduled appointments or recent healthcare interactions. Determine the need for a routine check-up or follow-up appointment based on Maria Miller's recent healthcare history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are polite, cautious. Use think to determine if Emily needs a routine check-up or an emergency appointment. If it is determined that Emily needs a routine check-up, use search_patients to check available time slots for Dr. Smith (provider ID: D102) for a routine appointment.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"provider_id": "D102", "appointment_type": "routine", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are direct, polite. Search for patient John Johnson using email john.johnson699@email.com to verify identity and retrieve patient ID. Think to determine if John Johnson requires an emergency appointment or a routine visit. Book_appointment for John Johnson with Dr. Smith on the earliest available date for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if John Johnson requires an emergency appointment or a routine visit based on his medical records or symptoms."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P029", "doctor_name": "Dr. Smith", "appointment_type": "routine", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, independent, cautious. Book_appointment for patient ID with preferred doctor during available hours, ensuring no conflicts with emergency appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P048"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "doctor_id": "D123", "appointment_time": "2023-11-15T10:00:00", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are independent, patient. Search_patients for Robert Brown using email robert.brown731@email.com to retrieve patient ID and records. Then, think to determine the next available appointment slot for Robert Brown with the prioritized doctor. This will ensure that Robert receives timely medical attention and maintains continuity of care with his preferred healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are independent, organized, polite, optimistic. First, search_patients with email \"maria.smith256@email.com\" to retrieve patient ID and check insurance details. Next, think to verify that Maria Smith's insurance is valid and appointment can be booked. Finally, book_appointment for the patient ID with doctor ID and selected time slot, ensuring it aligns with insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "doctor_id": "doctor_id_retrieved", "time_slot": "time_slot_retrieved", "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are flexible, logical, organized. Check healthcare details for patient Maria Johnson (maria.johnson759@email.com) to verify insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P023", "email": "maria.johnson759@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are cautious, polite, organized, confident. First, use search_patients to find patient information for Robert Brown using his email robert.brown551@email.com, ensuring proper authorization is obtained. Once you have accessed his information, verify Robert Brown's insurance details to ensure coverage is valid for upcoming appointments. This verification is crucial before proceeding with any scheduling tasks.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are patient, polite, organized. Use `search_patients` to find patient ID for Emily Brown using email emily.brown290@email.com",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com", "user_id": "P021"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are confident, polite, flexible. First, search_patients(email=\"david.williams693@email.com\") to retrieve David Williams' insurance details, ensuring that his coverage is active and valid. Next, think about the insurance verification process for David Williams to confirm that all necessary steps have been completed accurately. Once the insurance is verified, proceed to book_appointment(patient_email=\"david.williams693@email.com\", doctor_id=\"D456\", time_slot=\"2023-10-15T10:00\", reason=\"routine check-up\") to secure his visit with the doctor.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify David Williams' insurance details to ensure coverage is active and valid."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.williams693@email.com", "doctor_id": "D456", "time_slot": "2023-10-15T10:00", "reason": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are patient, independent, optimistic, confident. Search for patient Michael Miller in the database using email michael.miller534@email.com to retrieve his patient ID and healthcare details. Then, verify insurance details for the patient ID retrieved for Michael Miller to ensure coverage for upcoming appointments. This process is crucial for maintaining accurate records and ensuring that Michael's healthcare needs are met without any administrative issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are independent, cautious. First, use the \"search_patients\" tool to find patient Sarah Williams with email sarah.williams602@email.com for her healthcare details. Once you have located her information, use the \"think\" tool to verify Sarah Williams' insurance details to ensure she is eligible for booking a consultation. This step is crucial to confirm her coverage before proceeding with any appointment scheduling.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance details for Sarah Williams to confirm eligibility for consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, independent, confident, cautious. Search_patients for user with email david.williams693@email.com to retrieve patient ID and healthcare details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com", "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are direct, independent. Search_patients with email john.johnson627@email.com to retrieve patient ID and insurance details. Then, book_appointment for the retrieved patient ID with doctor ID D67890 at an available time slot during office hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P031", "doctor_id": "D67890", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are direct, logical, independent, confident. First, search for patient details for user ID sarah.brown753@email.com using the search_patients tool to ensure you have the correct patient information. Next, verify insurance details for user ID sarah.brown753@email.com before proceeding with appointment booking to confirm coverage and avoid any issues. Finally, book a routine appointment for user ID sarah.brown753@email.com with Dr. Smith on the available date, ensuring all details are accurate and complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "doctor": "Dr. Smith", "date": "2023-11-15", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are polite, cautious, flexible. Please begin by using the \"search_patients\" task with parameters: {email: \"maria.johnson759@email.com\"} to retrieve the patient ID and insurance information for Maria Johnson. Once you have confirmed her insurance details, proceed with the \"search_patients\" task using parameters: {patient_id: \"P123\"} to check her current doctor assignments and available appointment slots. After verifying that her insurance covers the appointment, book a routine appointment for Maria with Dr. Smith using the \"book_appointment\" task with parameters: {patient_id: \"P123\", doctor_id: \"D456\", appointment_time: \"2023-10-25 10:00\", appointment_type: \"routine\"}. Ensure all steps are completed accurately to facilitate a smooth scheduling process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor_id": "D456", "appointment_time": "2023-10-25 10:00", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are cautious, independent, direct. First, search_patients with email sarah.brown753@email.com to verify authorization for accessing healthcare details. Once authorization is confirmed, proceed to search_patients with user ID U123 to access Sarah Brown's insurance verification status to ensure coverage for upcoming appointments. Finally, search_patients with user ID U123 to retrieve Sarah Brown's preferred doctor and their availability, so you can coordinate her care effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "U123"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "U123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are patient, cautious. Search patients with email michael.brown235@email.com to retrieve patient ID and insurance details, then think to verify insurance details for the patient ID retrieved in the previous step. Ensure that the insurance covers routine check-ups, as this will be necessary for the next steps in scheduling the patient's healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if the insurance covers routine check-ups for the retrieved patient ID."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are flexible, cautious, organized, direct. Search for patient Sarah Smith using email sarah.smith521@email.com to retrieve her patient ID and insurance details. Verify Sarah Smith's insurance coverage for a general check-up appointment using her insurance details. Book an appointment for Sarah Smith with Dr. Johnson for a general check-up at an available time slot, ensuring insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Smith's patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Smith's insurance coverage for a general check-up appointment using her insurance details."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P033", "doctor": "Dr. Johnson", "appointment_type": "general check-up", "insurance_verified": true, "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are patient, logical, cautious, direct. First, think to check Robert Brown's insurance details for appointment eligibility to ensure that the upcoming medical consultation is covered. Once you have confirmed the insurance details, proceed to book an appointment for Robert Brown with Dr. Smith on 2023-11-15 at 10:00 AM, ensuring all necessary information is accurately recorded to facilitate a smooth visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance details to ensure appointment eligibility."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are direct, patient. First, search for patient Emily Davis by email emily.davis525@email.com to verify her insurance information, ensuring that all details are up-to-date for her upcoming appointments. Once the insurance information is confirmed, book an appointment for Emily Davis with Dr. Smith (doctor ID D102) for a routine check-up during available hours, ensuring that the appointment aligns with her insurance coverage requirements.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.davis525@email.com", "doctor_id": "D102", "appointment_type": "routine check-up", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are direct, optimistic. Search_patients with name \"David Brown\" and email \"david.brown214@email.com\" to retrieve patient ID and insurance details. Think to verify if David Brown's insurance is valid for coverage before proceeding with appointment booking. Book_appointment for David Brown with Dr. Smith (ID: D456) for a routine check-up on a weekday during available hours after verifying insurance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "David Brown", "email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if David Brown's insurance is valid for coverage."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor_id": "D456", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are polite, direct, confident. First, search_patients for patient_id using michael.brown235@email.com to verify authorization for accessing patient information. Once authorization is confirmed, proceed to search_patients for insurance details using patient_id to verify insurance coverage. After confirming the insurance coverage, book_appointment for patient_id with doctor_id during available hours for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P016", "info_type": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P016", "doctor_id": "doctor_id", "appointment_type": "routine check-up", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are organized, confident, logical, flexible. Search_patients for user Sarah Williams using email sarah.williams853@email.com to retrieve patient ID and details. Once you have the patient ID, check healthcare details for the retrieved patient ID to confirm insurance status and coverage. After confirming the insurance coverage, book_appointment for the patient ID with doctor ID on the next available date ensuring it aligns with insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and details for Sarah Williams to verify insurance status."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details for the retrieved patient ID to confirm insurance status and coverage."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor_id": "D001", "date": "next_available_date", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are independent, confident. First, analyze Emily Jones' healthcare needs based on her medical history and upcoming requirements to ensure she receives appropriate care. Next, determine if Emily Jones requires a routine check-up or has any immediate health concerns based on her profile to prioritize her healthcare needs effectively. Finally, check insurance coverage details for Emily Jones to ensure the appointment with Dr. Smith is covered, facilitating a smooth and hassle-free healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Analyze Emily Jones' healthcare needs based on her medical history and upcoming requirements."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if Emily Jones requires a routine check-up or has any immediate health concerns."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check insurance coverage details for Emily Jones to ensure the appointment with Dr. Smith is covered."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are cautious, organized, polite, optimistic. Search_patients for Emily Brown to retrieve her patient ID and medical history. Then, verify Emily Brown's insurance with the retrieved patient ID to ensure coverage for upcoming appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "name": "Emily Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, polite, organized. First, search for patient John Johnson using email john.johnson627@email.com to verify authorization status for accessing healthcare records. Once authorization is confirmed, proceed to search_patients to confirm that John Johnson's insurance details are up to date. After verifying the insurance details, ensure that John Johnson's insurance coverage is confirmed before booking an emergency appointment, prioritizing available slots to accommodate his urgent healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "check_insurance": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson627@email.com", "appointment_type": "emergency", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are direct, organized, flexible. First, search_patients with parameters: user_email=sarah.brown426@email.com, condition=doctor availability to find available slots. Once you have identified suitable options, think with parameters: user_context=Sarah Brown, task_context=appointment scheduling, action=select available appointment slot. This will ensure that Sarah Brown can efficiently schedule her routine appointment with the doctor.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.brown426@email.com", "condition": "doctor availability"}
            ),
            Action(
                name="think",
                kwargs={"user_context": "Sarah Brown", "task_context": "appointment scheduling", "action": "select available appointment slot"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are optimistic, direct. First, search for the patient using the email david.williams693@email.com to retrieve the patient ID and insurance details. Then, verify the insurance status using the patient ID obtained from the previous task. Ensure that the insurance is active and valid, as this will be crucial for any subsequent appointments or treatments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com", "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are direct, organized, cautious. First, search_patients with user_email \"robert.jones332@email.com\" to verify patient authorization, ensuring compliance with privacy regulations. Once authorization is confirmed, proceed to search_patients with user_email \"robert.jones332@email.com\" to retrieve insurance details, which are necessary for billing and administrative purposes. Finally, book_appointment for user_email \"robert.jones332@email.com\" with Dr. Smith during available hours for a general consultation, ensuring that all necessary information is prepared for the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.jones332@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.jones332@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_email": "robert.jones332@email.com", "doctor": "Dr. Smith", "appointment_type": "general consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are confident, logical. Search for patient Robert Jones with email robert.jones332@email.com to retrieve patient ID and insurance information. Then, check healthcare details to verify insurance for the retrieved patient ID. This process is crucial to ensure that Robert Jones has active insurance coverage before proceeding with any medical appointments, thereby avoiding any potential billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P026", "name": "Robert Jones", "email": "robert.jones332@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance information from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the retrieved patient ID to verify insurance details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are cautious, flexible, direct, organized. First, search_patients with email robert.garcia592@email.com to verify patient existence and retrieve ID. Once you have confirmed your patient ID, proceed to book_appointment for Robert Garcia with Dr. Smith on 10/15/2023 at 10:00 AM, ensuring doctor's availability and insurance verification. This sequence ensures that your patient information is up-to-date and that the appointment is successfully scheduled with all necessary verifications in place.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor_name": "Dr. Smith", "appointment_date": "10/15/2023", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are logical, optimistic, patient, direct. First, search for patient John Johnson's healthcare information using email john.johnson627@email.com to verify insurance details. Once you have confirmed his insurance verification status, think about John's eligibility for appointment booking. If eligible, proceed to book an appointment for John Johnson with Dr. Smith on the chosen date and time, ensuring that all insurance verification is complete beforehand.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "user_id": "P031"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if John Johnson's insurance is verified and if he is eligible for booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson627@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are logical, organized, confident, direct. First, search_patients with user_email emily.davis525@email.com to retrieve patient ID and insurance details. Next, check healthcare details for the retrieved patient ID to verify insurance coverage. Finally, book_appointment for the verified patient ID with Dr. Smith at a selected time slot, ensuring that all insurance details are confirmed and in order.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "emily.davis525@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details for the retrieved patient ID to verify insurance coverage."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_id": "P032", "doctor": "Dr. Smith", "time_slot": "selected_time_slot", "insurance_confirmed": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are polite, independent, logical. First, search for patient records of Lisa Williams (lisa.williams792@email.com) to verify her insurance information. Once verified, proceed to book an emergency appointment for Lisa Williams with Dr. John Smith (Doctor ID: D001) at the next available slot. Ensure that the insurance coverage is adequate for Dr. John Smith's services during the booking process to facilitate a smooth appointment experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "lisa.williams792@email.com", "doctor_id": "D001", "appointment_type": "emergency", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are logical, cautious, confident. Search for patient records with the email sarah.williams853@email.com to verify patient identity and obtain authorization. Once identity is confirmed, search for insurance details for patient Sarah Williams to verify coverage before booking an appointment. Ensure these steps are completed accurately to maintain compliance with healthcare regulations and facilitate a seamless patient experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are direct, independent, flexible, polite. Use search_patients to retrieve patient details for Michael Brown using the email michael.brown235@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are optimistic, flexible. search_patients: Identify any existing appointments for Maria Miller within the next month",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Maria Miller", "time_frame": "next_month", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are logical, optimistic. Use search_patients to find the patient ID for Sarah Smith using her email sarah.smith521@email.com. Once you have located her patient ID, use think to verify Sarah Smith's insurance coverage status for her upcoming appointments. This will ensure that her insurance is active and applicable for the services she needs, allowing us to proceed with scheduling her appointments confidently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P033", "task": "verify_insurance_status"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are polite, logical, independent. Search for patient details for Lisa Jones (lisa.jones889@email.com) to verify insurance information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "email": "lisa.jones889@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are organized, cautious. First, search_patients with parameters: { \"email\": \"emily.davis525@email.com\", \"authorization\": \"valid\" } to retrieve the necessary patient information. Once the patient information is retrieved, think with parameters: { \"patient_info\": \"retrieved\", \"insurance_status\": \"check required\" } to ensure that the patient's insurance status is verified and up-to-date. This sequence is crucial to ensure that Emily Davis's details are accurate and her insurance can cover the upcoming medical services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "authorization": "valid"}
            ),
            Action(
                name="think",
                kwargs={"patient_info": "retrieved", "insurance_status": "check required"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are logical, polite, cautious. First, search_patients for user Robert Brown to retrieve patient ID and insurance information. Then, book_appointment for Robert Brown with Dr. Emily Carter on the earliest available date, ensuring it is within the doctor's available hours. This process is crucial to verify Robert's insurance coverage before scheduling his appointment, thereby ensuring a smooth and efficient experience for both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "patient_id": "P017", "doctor_name": "Dr. Emily Carter", "date": "2023-11-01"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are direct, optimistic, organized. Search for patient John Johnson using email john.johnson941@email.com to verify identity and retrieve patient ID. Once you have the patient ID, check healthcare details to confirm insurance information and eligibility. This will ensure that the patient can be scheduled for an appointment with Dr. Smith at the earliest available slot covered by their insurance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "user_id": "P037"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once the patient ID is retrieved, the next step is to check healthcare details to confirm insurance information and eligibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After confirming insurance eligibility, proceed to book an appointment with Dr. Smith at the earliest available slot covered by the insurance."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are optimistic, polite. First, search for patient Michael Brown using email michael.brown235@email.com to verify authorization. Once authorization is confirmed, verify insurance details for Michael Brown to ensure eligibility for appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com", "user_id": "P016"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization for patient Michael Brown using the provided email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once authorization is confirmed, proceed to verify insurance details for eligibility."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are cautious, patient, independent. Search for patient records using user ID John Johnson (john.johnson627@email.com) to verify insurance details. Once you have confirmed that the insurance covers the requested appointment, proceed to book an appointment for John Johnson with Dr. Smith for an emergency consultation using the patient's verified insurance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "email": "john.johnson627@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P031", "patient_email": "john.johnson627@email.com", "doctor_name": "Dr. Smith", "appointment_type": "emergency", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are direct, independent, polite, flexible. First, verify insurance details for John Johnson using the think tool to ensure coverage for his upcoming appointments. Once you have confirmed his insurance coverage, proceed to book an appointment for John Johnson with Dr. Smith for a routine check-up using the book_appointment tool. Ensure that all details are accurate to facilitate a smooth healthcare experience for the patient.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "task": "verify insurance details"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are optimistic, organized, confident. Search for patients with the criteria (email: \"john.johnson627@email.com\") to retrieve their patient ID and insurance details. Once you have the patient ID, book an appointment for them with Dr. Smith, ensuring to select a preferred time slot if it's a routine check-up, or prioritize the booking if it's an emergency.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P031", "doctor": "Dr. Smith", "appointment_type": "routine", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, polite, optimistic, patient. Search_patients with name \"Robert Johnson\" and email \"robert.johnson741@email.com\" to retrieve patient ID and insurance details. Think to verify insurance status for patient ID retrieved from the previous search to ensure that Robert Johnson's insurance is active and can cover the upcoming medical services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status for the retrieved patient ID to ensure it is active."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are cautious, independent. \"search_patients with email robert.garcia592@email.com to retrieve patient ID and insurance information\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, cautious, confident, optimistic. Use `search_patients` to find patient information for Lisa Williams using email (lisa.williams792@email.com) with proper authorization.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are logical, optimistic. First, search_patients with email sarah.williams602@email.com to retrieve the patient ID and verify the authorization status for accessing patient information. Once you confirm the authorization, proceed to book_appointment for Sarah Williams with doctor ID D456 for a routine check-up during available hours next week. Finally, search_patients to retrieve Sarah Williams' medical history to ensure the doctor is well-prepared for the upcoming appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P018", "doctor_id": "D456", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P018"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "retrieve": "medical_history"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are polite, cautious. First, search for patient ID for Maria Miller (maria.miller855@email.com) to verify account details. Once verified, think to determine the best time slot for an appointment based on Dr. Smith's available hours and Maria's preferences, ensuring the chosen time is convenient for both parties.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Miller's account details and check Dr. Smith's available hours and Maria's preferences for a suitable appointment time."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, direct. First, search_patients for user Sarah Brown with email sarah.brown426@email.com to retrieve patient ID and verify authorization. Once authorization is confirmed, book_appointment for Sarah Brown with doctor ID D123 for an emergency consultation, ensuring insurance verification is complete. This sequence is crucial to ensure that Sarah receives timely medical attention while maintaining compliance with healthcare protocols.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Brown", "email": "sarah.brown426@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_id": "D123", "appointment_type": "emergency", "insurance_verified": true, "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are optimistic, logical. Search_patients tool to retrieve patient ID for Emily Jones using email emily.jones379@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, polite, logical, optimistic. Search_patients with name \"Sarah Miller\" and email \"sarah.miller381@email.com\" to retrieve patient ID and insurance details. Once you have the patient ID, check healthcare details to verify insurance coverage. After confirming the insurance, search_patients for available doctors specializing in general medicine for the retrieved patient ID to ensure Sarah Miller can receive the appropriate care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Miller", "email": "sarah.miller381@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P046", "insurance_details": true}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P046", "specialization": "general medicine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are optimistic, polite, logical, flexible. search_patients with patient ID to find preferred doctor and their available hours",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are flexible, confident, polite, organized. \"Use think to determine if Robert Jones needs a routine check-up or a specialist visit based on recent health changes.\"",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P026", "task": "determine if Robert Jones needs a routine check-up or a specialist visit based on recent health changes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are optimistic, logical. Search_patient with email \"robert.brown551@email.com\" to retrieve patient ID and relevant healthcare details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are independent, direct. Search_patients for user Sarah Brown (sarah.brown426@email.com) to verify patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "email": "sarah.brown426@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are direct, patient. Think to determine if John Johnson has any upcoming appointments that need to be rescheduled due to a scheduling conflict with his work commitments. Once identified, think to identify the next available appointment slot for John's preferred doctor, Dr. Smith, ensuring it aligns with John's availability.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P031"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P031", "doctor": "Dr. Smith", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are polite, independent. \"search_patients with name 'Lisa Williams' to verify patient ID and insurance details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, cautious, optimistic. Use think to decide on the type of doctor's appointment needed based on Lisa Williams' medical history and current symptoms.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P045", "name": "Maria Smith", "email": "maria.smith554@email.com", "traits": ["independent", "cautious", "optimistic"], "task": "decide on the type of doctor's appointment needed based on Lisa Williams' medical history and current symptoms"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are confident, optimistic, cautious. \"search_patients to check Sarah Williams' insurance status and eligibility for booking\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Sarah Williams", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, direct. First, search for patient ID associated with email robert.brown551@email.com using the search_patients tool. Once you have confirmed the patient ID, retrieve Robert Brown's insurance details using the think tool to verify coverage. This ensures that his insurance is valid and covers the necessary services before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P003", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are optimistic, polite, logical, patient. First, search_patients with criteria (name: \"Lisa Jones\", email: \"lisa.jones889@email.com\") to retrieve the patient ID. Once you have the patient ID, proceed to check healthcare details for the retrieved patient ID to ensure that her insurance is verified. This will allow us to confirm her coverage before any appointments are scheduled, ensuring a smooth process for her routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones", "email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results to proceed with checking healthcare details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, independent, direct, optimistic. First, think to check if the appointment for Emily Davis is a routine visit or an emergency. If it is determined to be an emergency, book the appointment for Emily Davis as an emergency appointment with priority if applicable. Finally, think to ensure all healthcare appointments for Emily Davis are confirmed, providing her with peace of mind and ensuring she receives timely care.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to check if Emily Davis's appointment is a routine visit or an emergency."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="think",
                kwargs={"thought": "If the appointment is an emergency, I will book it as an emergency appointment with priority."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "appointment_type": "emergency", "priority": "high"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Finally, I need to ensure all healthcare appointments for Emily Davis are confirmed."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are organized, patient, independent. First, search for the patient profile using the email robert.brown551@email.com to verify identity and access level. Once verified, check healthcare details for Robert Brown to confirm his insurance status and policy coverage. After confirming that his insurance covers cardiology appointments, proceed to book an appointment for Robert Brown with Dr. Smith (Doctor ID: D101) on the next available afternoon slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify identity and access level of Robert Brown to ensure proper authorization."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details to confirm insurance status and policy coverage for cardiology."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P003", "doctor_id": "D101", "patient_email": "robert.brown551@email.com", "appointment_time": "next available afternoon slot"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are polite, confident. Search for patient Sarah Brown using email sarah.brown426@email.com to verify her account and obtain her patient ID. Once you have confirmed her identity, think to check Sarah Brown's insurance information to verify coverage for upcoming appointments. This will ensure that her upcoming visit with Dr. John Smith is covered and scheduled appropriately within his available working hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Sarah Brown's patient ID is obtained, verify her insurance information to ensure coverage for her upcoming appointment with Dr. John Smith."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are confident, independent, polite, flexible. First, check Sarah Miller's insurance details for coverage verification using user ID U12345 to ensure her upcoming medical procedures are covered. Next, search_patients with user ID U12345 to retrieve Sarah Miller's patient records for appointment history, which will help in assessing her past treatments and current needs. Finally, think to determine the best specialist for Sarah Miller's condition based on the retrieved patient records, ensuring she receives the most appropriate care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "U12345"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are optimistic, cautious, organized. First, search for patient details using the email robert.brown624@email.com to verify identity and authorization. Once verified, proceed to book an appointment with Dr. Smith (doctor ID: D101) for Robert Brown for a routine check-up. Ensure that the booking aligns with Dr. Smith's availability and Robert Brown's preferences.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "doctor_id": "D101", "patient_email": "robert.brown624@email.com", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, independent, patient, flexible. Search for patient information for user Emily Davis (emily.davis525@email.com) to verify insurance details, and then check healthcare details to ensure her insurance is valid for upcoming appointments. This will help confirm that her coverage aligns with the services she requires, ensuring a smooth experience during her visits.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "email": "emily.davis525@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are optimistic, direct. Search for patient Emily Garcia's healthcare records using her email emily.garcia400@email.com to verify insurance details, and then verify Emily Garcia's insurance coverage for the selected doctor and appointment type. This ensures that her appointment can be scheduled without any issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are logical, optimistic. \"search_patients to find Robert Jones' patient ID using email robert.jones332@email.com\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are flexible, direct. First, search for patient Michael Miller's healthcare profile using email michael.miller534@email.com to verify his insurance status. Once confirmed, book an appointment for Michael Miller with Dr. Smith, ID D123, on the available slot on 2023-11-05 at 10:00 AM. After booking, send an appointment confirmation to Michael Miller's email michael.miller534@email.com with all the details of the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "michael.miller534@email.com", "doctor_id": "D123", "appointment_date": "2023-11-05", "appointment_time": "10:00 AM", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are organized, polite, confident. Search_patients for Emily Jones using email emily.jones379@email.com to verify patient record and authorization status",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are organized, patient, direct, independent. First, search_patients to find Emily Davis's patient ID and verify her authorization status for accessing healthcare services. Once her authorization status is confirmed, proceed to verify insurance details for Emily Davis with her insurance provider to ensure coverage for the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Davis", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are confident, cautious. Use search_patients to find patient details for Robert Brown (robert.brown551@email.com) to verify insurance coverage, and then use think to analyze Robert Brown's insurance details to confirm coverage for a routine check-up. Once confirmed, ensure that the patient is eligible for the appointment to proceed smoothly.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"task": "Analyze Robert Brown's insurance details to confirm coverage for a routine check-up.", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are cautious, direct. Search for patient records using user email robert.brown731@email.com to retrieve patient ID and insurance details. Then, verify insurance details for patient ID retrieved from Robert Brown's records to ensure coverage. This process is crucial to confirm the patient's eligibility for upcoming medical procedures and to prevent any billing discrepancies.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, organized. \"Check healthcare details for user Maria Smith (maria.smith256@email.com) to verify insurance coverage\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "email": "maria.smith256@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are logical, confident, flexible, direct. Search_patients with name \"Robert Garcia\" to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Garcia", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are flexible, cautious, organized, confident. First, search_patients for Maria Smith using email maria.smith554@email.com to retrieve patient ID and records. Once you have the patient ID, think to verify insurance details for the patient ID retrieved from search_patients to ensure coverage for upcoming services. After confirming the insurance details, proceed to book_appointment for patient ID with doctor ID during available hours for a routine check-up, ensuring that all necessary information is accurate and communicated effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from search_patients response to verify insurance details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure coverage for upcoming services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_id": "D001", "appointment_type": "routine check-up", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, flexible, patient, polite. Search for patient John Johnson using email john.johnson941@email.com to retrieve medical history and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are independent, flexible, patient. First, search for patient information using user email lisa.williams792@email.com to verify authorization status. Once authorization is confirmed, proceed to search_patients for insurance details for user ID U001 to confirm coverage. This sequence ensures that Lisa Williams' insurance details are verified before any appointments are scheduled, maintaining compliance with healthcare regulations.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "U001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are polite, optimistic, confident. Search_patients with name \"John Johnson\" and email \"john.johnson699@email.com\" to retrieve patient ID and insurance information. Check healthcare details for patient ID [retrieved_patient_id] to confirm insurance status and coverage details. Book_appointment for patient ID [retrieved_patient_id] with doctor ID [retrieved_doctor_id] on [available_date] and time with verified insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Johnson", "email": "john.johnson699@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P029", "doctor_id": "[retrieved_doctor_id]", "date": "[available_date]", "time": "[available_time]", "insurance_verified": true, "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, organized. First, search for the patient profile using the email michael.miller534@email.com to retrieve the user ID and healthcare details. Then, use the user ID to search for available medical records and history for Michael Miller. This process is crucial for ensuring that Michael receives the appropriate care, whether it be a routine visit or an emergency appointment, based on his medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are patient, flexible. First, search_patients to retrieve Sarah Smith's insurance information for verification. Once her insurance is verified and it is confirmed that she is due for a routine visit, proceed to book_appointment for Sarah Smith with Dr. John Doe during available hours. This ensures that her healthcare needs are addressed in a timely manner.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith", "doctor_name": "Dr. John Doe", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are logical, cautious, polite. Use think to confirm user Emily Garcia's authorization to access patient information. Once authorization is confirmed, use think to verify Emily Garcia's insurance information for eligibility. After ensuring that the insurance verification is complete and valid, use book_appointment to schedule a routine appointment for Emily Garcia with Dr. Smith during available hours. Ensure all patient data and appointments are recorded securely and confidentially in line with healthcare guidelines.",
        actions=[
            Action(
                name="think",
                kwargs={"action": "confirm_authorization", "user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="think",
                kwargs={"action": "verify_insurance", "user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Emily Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, polite, cautious. First, check healthcare details for patient David Brown (david.brown214@email.com) to verify insurance status. Once you have confirmed the insurance status, search patients to verify insurance provider details for David Brown to ensure all information is accurate and up-to-date. After verifying the insurance details, proceed to book an appointment for David Brown with Dr. Smith on 2023-10-18 at 10:00 AM, pending the successful confirmation of his insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com", "user_id": "P020"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.brown214@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-10-18", "appointment_time": "10:00 AM", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are organized, flexible. First, search_patients for user Robert Jones with email robert.jones332@email.com for healthcare details to gather necessary information. Next, think to verify insurance information for patient Robert Jones to ensure coverage for upcoming medical services. Finally, think to determine the best available doctor based on Robert Jones's healthcare requirements, and book_appointment for Robert Jones with doctor D456 on 2023-11-15 at 10:00 AM to ensure he receives the appropriate care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Jones", "email": "robert.jones332@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones", "doctor_id": "D456", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are cautious, direct, flexible, optimistic. Book an appointment with Dr. Smith (Doctor ID: D101) for David Brown on 2023-10-15 at 10:00 AM, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P020", "patient_name": "David Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if David Brown has valid insurance before booking the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P020", "doctor_id": "D101", "patient_name": "David Brown", "appointment_date": "2023-10-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, logical, polite, flexible. First, use search_patients to confirm insurance coverage for Sarah Williams before booking an appointment. Next, use think to determine Sarah Williams’ preferred available doctor for a routine check-up. Finally, use book_appointment to reserve a slot with Dr. Smith for Sarah Williams on 11/15/2023 at 10:00 AM, ensuring all necessary details are in place for a smooth and efficient visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams", "email": "sarah.williams853@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Determine preferred available doctor for Sarah Williams for a routine check-up"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams", "doctor_name": "Dr. Smith", "date": "11/15/2023", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, organized, direct, patient. Book_appointment for Lisa Jones with Dr. Smith on the available date and time, ensuring insurance is verified and noted.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones", "doctor_name": "Dr. Smith", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are polite, direct. First, search for patient Robert Garcia using email robert.garcia592@email.com to retrieve his patient ID and medical history. Once you have the patient ID, verify the insurance details to ensure coverage for his upcoming appointments. After confirming the insurance coverage, proceed to book an appointment for Robert Garcia with Dr. Emily Johnson at an available slot on Wednesday at 10:00 AM.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and medical history from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Robert Garcia using the retrieved patient ID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance coverage is confirmed for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor": "Dr. Emily Johnson", "time": "Wednesday 10:00 AM", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are flexible, polite, logical. Search for user Sarah Williams in the patient database using search_patients tool to confirm patient ID and insurance status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Williams", "email": "sarah.williams853@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are polite, cautious, direct. First, search_patients with email robert.garcia592@email.com to verify identity and access permissions. Once verified, proceed to search_patients for Robert Garcia's medical history to confirm the appropriate appointment type. Finally, book_appointment for Robert Garcia with doctor ID D123 for the confirmed appointment type at 10:00 AM on 2023-10-25, ensuring it's within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.garcia592@email.com", "doctor_id": "D123", "appointment_type": "confirmed_appointment_type", "time": "10:00 AM", "date": "2023-10-25", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are independent, organized. Search for patient record using email robert.garcia592@email.com to retrieve user ID and healthcare details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are logical, patient, direct. Search for patient Sarah Williams using email sarah.williams602@email.com to retrieve her patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are confident, flexible, optimistic, patient. search_patients with email robert.johnson197@email.com to verify patient information and retrieve patient ID",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, confident, logical, patient. Search for patients using the tool 'search_patients' with the query \"Sarah Miller\" and obtain patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"query": "Sarah Miller", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are optimistic, patient. First, think to verify if Michael Brown's insurance details are current and valid for appointment booking. Once you have confirmed the insurance validity, proceed to book an appointment for Michael Brown with his preferred doctor during available hours, ensuring all insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "patient_name": "Michael Brown"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P016", "patient_name": "Michael Brown", "doctor_name": "Dr. Smith", "appointment_time": "2023-11-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are independent, organized, polite, confident. Use think to confirm Emily's insurance is verified for appointment booking. Once verified, use think to determine if the appointment time aligns with Emily's schedule based on her preferences. Emily is due for her annual routine check-up, and she prefers morning appointments. Ensure her insurance covers routine check-ups before proceeding to check her availability.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Verify Emily's insurance coverage for routine check-ups."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Emily's preferred appointment time aligns with her schedule, focusing on morning availability."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are flexible, confident, cautious. search_patients for user Sarah Williams (sarah.williams602@email.com) to retrieve her medical history and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "name": "Sarah Williams", "email": "sarah.williams602@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are polite, independent. \"search_patients with name 'Emily Garcia' to verify patient ID and insurance status\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Garcia", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are cautious, logical. First, search_patients for Robert Garcia's insurance information to verify coverage. Once you have confirmed the insurance details, proceed to book_appointment for Robert Garcia with doctor ID D5678 on date 2023-11-15 at 10:00 AM, ensuring that the insurance verification is complete for seamless appointment scheduling.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "doctor_id": "D5678", "date": "2023-11-15", "time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are cautious, confident, polite. search_patients with email=\"robert.brown624@email.com\" to retrieve patient ID and authorization status",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are patient, independent, cautious. First, think to determine the need for Robert Brown's upcoming healthcare appointment by considering his recent medical history and any symptoms he may have reported. Next, search_patients with the parameter email \"robert.brown551@email.com\" to retrieve patient ID and insurance details, ensuring that you have accurate information to proceed. Finally, think to check if Robert Brown needs an emergency or routine appointment based on the retrieved data, such as his medical conditions and insurance coverage, to ensure he receives the appropriate level of care in a timely manner.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are patient, polite. Search_patients to find available doctors for a general check-up for Robert Brown.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown", "purpose": "general check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are patient, polite, cautious. First, search_patients: Verify Sarah Miller's insurance details and coverage for dermatology services to ensure she is eligible for the consultation. Next, think: Determine if Sarah Miller's insurance covers dermatology consultations with provider ID P987, as this will confirm whether she can proceed with the appointment. Finally, book_appointment: Schedule an appointment for Sarah Miller with Dr. Emily Carter (doctor ID D567) on 2023-11-15 at 10:00 AM, ensuring insurance verification is complete to avoid any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "service": "dermatology"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "insurance_coverage": "dermatology", "provider_id": "P987"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_id": "D567", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are polite, patient, logical. Search_patients for Sarah Davis's medical history to determine the appropriate specialist required.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P047", "patient_name": "Sarah Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are logical, independent, direct, confident. Search_patients for Lisa Jones using email lisa.jones889@email.com to retrieve her patient ID and insurance details. Then, think to verify if Lisa Jones has the necessary insurance coverage for a general consultation. Ensure that the insurance verification is complete before proceeding to any further steps.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Lisa Jones has the necessary insurance coverage for a general consultation."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are optimistic, logical, confident, independent. Search_patient with user email robert.brown551@email.com to retrieve patient ID and authorization status. Then, think to verify if Robert Brown has a valid insurance on file to proceed with appointment booking. This ensures that we can efficiently manage Robert's healthcare needs by confirming his eligibility and preparing for his routine visit without any delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Robert Brown has a valid insurance on file to proceed with appointment booking."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are patient, flexible, polite, optimistic. First, search_patients with email robert.johnson741@email.com to retrieve patient ID and healthcare details. Once you have confirmed the patient ID, use it to verify if Robert Johnson's insurance information is up-to-date. This ensures that his records are accurate and ready for any upcoming appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and healthcare details for Robert Johnson."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the retrieved patient ID to verify if Robert Johnson's insurance information is up-to-date."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, independent, direct. First, use search_patients with the parameter \"name\" set to \"John Doe\" to retrieve patient details for a routine check-up. Once you have the details, use think to verify if John Doe's insurance is active and covers routine check-ups. This ensures that the patient can proceed with the appointment without any financial concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Doe"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if John Doe's insurance is active and covers routine check-ups."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, patient, logical, polite. \"Book_appointment for Maria Miller with Dr. Smith on November 3rd at 10:00 AM, pending insurance verification\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P042", "patient_name": "Maria Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P042", "patient_name": "Maria Miller", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-03", "appointment_time": "10:00", "status": "pending insurance verification"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are flexible, independent, patient, logical. Search_patients with name \"Sarah Williams\" to retrieve patient ID and insurance details. Then, verify insurance details for the patient ID obtained from the search to ensure coverage for appointments. This process is crucial to confirm that Sarah Williams is eligible for her healthcare benefits, which will allow you to proceed with scheduling her medical services confidently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Williams", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are flexible, independent, confident. Use the `search_patients` tool to search for patient profile using email \"sarah.smith521@email.com\" to verify authorization and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are direct, cautious. First, search_patients with email emily.garcia400@email.com to retrieve patient ID and authorization status. Once you have confirmed Emily Garcia's authorization, proceed to verify her insurance details and coverage for cardiology appointments to ensure there are no issues with billing.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm Emily Garcia's authorization status before proceeding with insurance verification."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once authorization is confirmed, verify insurance details and coverage for cardiology appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are polite, flexible, cautious. First, search_patients for patient Sarah Miller's insurance details to verify coverage eligibility. Once you have confirmed her insurance coverage, book_appointment for patient Sarah Miller with Dr. Smith during available hours. This ensures that Sarah's appointment is scheduled efficiently and without any coverage issues, allowing her to receive the necessary care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_name": "Dr. Smith", "appointment_time": "available_hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are patient, direct. First, search_patients to retrieve Sarah Smith's patient ID using her email sarah.smith521@email.com. Next, think to analyze Sarah Smith's previous appointment history to determine her preferred doctors and times. Finally, search_patients to identify available appointment slots for Dr. Jonathan Lee, her preferred doctor, within the next two weeks.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"analysis": "Analyze Sarah Smith's previous appointment history to determine her preferred doctors and times."}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_name": "Dr. Jonathan Lee", "time_frame": "next two weeks", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are cautious, independent, polite. Book an appointment for Sarah Miller with Dr. James Smith during available hours, ensuring insurance verification is completed beforehand. Once the appointment is confirmed, think to confirm the appointment details and send a confirmation email to sarah.miller381@email.com, providing her with the date, time, and location of the appointment, as well as any necessary preparation instructions.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to verify Sarah Miller's insurance before booking an appointment."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "email": "sarah.miller381@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After verifying insurance, I will book an appointment with Dr. James Smith during his available hours."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_email": "sarah.miller381@email.com", "doctor_name": "Dr. James Smith", "appointment_type": "routine", "insurance_verified": true}
            ),
            Action(
                name="think",
                kwargs={"thought": "Now that the appointment is booked, I will confirm the details and send a confirmation email to Sarah Miller."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are patient, independent. First, use `search_patients` to find the patient ID for Maria Smith using her email maria.smith256@email.com. Once you have retrieved the patient ID, use `book_appointment` to schedule a routine check-up for Maria Smith with the appropriate doctor ID at the next available time slot. Ensure that the appointment is convenient for both the patient and the doctor, considering the clinic's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "user_id": "P019"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "doctor_id": "appropriate_doctor_id", "appointment_type": "routine check-up", "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are cautious, flexible. Search_patients with email maria.johnson759@email.com to retrieve patient ID and medical history. Then, think to determine if Maria Johnson requires a routine or emergency appointment based on her medical history. Use this information to ensure her healthcare needs are addressed promptly and appropriately.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are flexible, polite. Search_patients with email robert.johnson197@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are flexible, patient. Search for patient details using user ID \"robert.brown624@email.com\" to verify his medical history and current health status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "email": "robert.brown624@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are flexible, direct, patient. Search_patients for Maria Miller's insurance coverage details using email maria.miller855@email.com, then think to verify Maria Miller's insurance coverage is valid for booking an appointment. Once verified, book_appointment for Maria Miller with doctor ID D123 on date 2023-11-15 at 10:00 AM, verify insurance and ensure it's within doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Miller's insurance coverage is valid for booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.miller855@email.com", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are confident, flexible, logical. Think about Lisa Jones's current healthcare needs and potential upcoming appointments, then search_patients for Lisa Jones in the healthcare system to verify existing patient records. This will ensure that her medical history is up-to-date and accurate, allowing you to make informed decisions about her care and schedule any necessary follow-up appointments efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are logical, optimistic, independent. Search_patients with email \"john.johnson699@email.com\" to retrieve patient ID and insurance details. Then, think to verify insurance coverage for the retrieved patient ID. This process ensures that you have all necessary information to proceed with any future healthcare services for the patient, such as booking appointments or confirming treatment plans.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search results."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are logical, direct, independent, confident. Search_patients for Emily Brown using email emily.brown290@email.com to retrieve patient ID and insurance details. Then, think to verify insurance status for Emily Brown based on retrieved insurance details. This will ensure that her insurance is active and covers cardiology appointments, which is crucial before proceeding with any medical consultations.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status for Emily Brown to ensure it is active and covers cardiology appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are direct, patient, cautious. Search for patient Maria Miller using email maria.miller855@email.com to retrieve her patient ID and medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are polite, flexible, confident. search_patients for user Emily Brown (emily.brown290@email.com) to verify insurance status and personal details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "email": "emily.brown290@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are independent, flexible. First, check Sarah Smith's insurance details to ensure coverage for healthcare services. Once you have verified her insurance, proceed to book an appointment for Sarah Smith with Dr. John Doe on 2023-10-15 at 10:00 AM, ensuring that the insurance verification is completed beforehand to avoid any issues during the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith", "doctor_name": "Dr. John Doe", "appointment_date": "2023-10-15", "appointment_time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are flexible, confident, independent, logical. Search for patient information for Sarah Williams using email sarah.williams602@email.com to verify identity and access permissions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are cautious, optimistic. First, search_patients for patient ID matching Robert Jones with email robert.jones332@email.com. Once you have identified the patient ID, proceed to search_patients to check for any existing appointments for the identified patient ID. This will ensure that Robert Jones does not have any overlapping or conflicting appointments, allowing for efficient scheduling within the healthcare system.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Jones", "email": "robert.jones332@email.com", "user_id": "P026"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P026", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are patient, organized, direct, independent. Search for patients with email \"maria.johnson759@email.com\" to verify Maria Johnson's patient ID and authorization status. Once verified, book an appointment for Maria Johnson with the available doctor during their working hours, ensuring that her insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor_id": "D456", "appointment_time": "2023-10-15T10:00:00", "insurance_verified": true, "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are optimistic, logical. Search_patients with email \"robert.brown731@email.com\" to retrieve patient ID and healthcare information. Think to determine the most suitable physician for a routine check-up based on patient preferences and physician specialties, ensuring the selected physician aligns with the patient's needs for a general wellness visit. Book_appointment for the patient ID obtained with the selected physician at the earliest available slot, making sure it fits within the doctor's available hours to provide a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com", "user_id": "P014"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine the most suitable physician for a routine check-up based on patient preferences and physician specialties."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P014", "physician_id": "selected_physician_id", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are polite, optimistic, organized, flexible. Search for patient records for user David Miller (david.miller979@email.com) to verify healthcare details using search_patients tool.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P028", "email": "david.miller979@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are cautious, patient, organized. First, search for patient details using email emily.garcia400@email.com to verify identity and authorization status. Once verified, search_patients for Emily Garcia to retrieve her medical history and insurance details. Then, think to analyze Emily Garcia's insurance details for coverage verification. If coverage is confirmed, proceed to book_appointment for Emily Garcia with Dr. Smith (doctor ID: D102) for a routine check-up on the next available slot, ensuring all insurance details are in order for a seamless appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Emily Garcia"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Emily Garcia", "doctor_id": "D102", "appointment_type": "routine check-up", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are logical, polite, cautious. \"search_patients\" with parameters: user_email=lisa.jones889@email.com, query=doctor availability for Dr. Smith",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "lisa.jones889@email.com", "query": "doctor availability for Dr. Smith"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are direct, logical, organized. \"Search_patients with email sarah.smith521@email.com to retrieve patient ID and current healthcare details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are direct, cautious. Search_patients for Sarah Smith using her email (sarah.smith521@email.com) to retrieve her patient ID and medical history. Verify insurance details for the retrieved patient ID to ensure coverage is active, as this is crucial for proceeding with any medical appointments. Think about available doctors based on Sarah Smith's medical needs and insurance coverage, considering specialists who are in-network to optimize her healthcare experience and minimize out-of-pocket expenses.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and medical history for Sarah Smith using the search_patients result."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Sarah Smith using her patient ID to ensure coverage is active."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Consider available doctors based on Sarah Smith's medical needs and insurance coverage, focusing on in-network specialists to minimize expenses."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, cautious, confident, direct. Search_patients using patient ID obtained to check existing medical records. Think to determine if patient Robert Brown needs a routine or emergency appointment based on medical records. After reviewing the records, if it is determined that Robert Brown requires an appointment, proceed to Book_appointment for patient ID with chosen doctor on the preferred date and time, ensuring insurance is verified. This process ensures that Robert receives the appropriate level of care in a timely manner, aligning with our commitment to patient-centered healthcare.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P014"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Robert Brown's medical records to determine if he needs a routine or emergency appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P014", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00", "insurance_verified": true, "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are polite, independent. Verify Emily Garcia’s insurance details to ensure coverage is active and valid for booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are organized, optimistic. First, search_patients with the parameter: email='robert.johnson197@email.com' to retrieve the patient ID and details. Once you have the patient ID, proceed to book_appointment with the parameters: patient_id=<retrieved_patient_id>, doctor_id='D123', date='2023-10-25', time='10:00 AM' to schedule a routine check-up. Finally, think to ensure an appointment confirmation email is sent to robert.johnson197@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P027", "doctor_id": "D123", "date": "2023-10-25", "time": "10:00 AM", "user_id": "P027"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are confident, organized, independent, polite. \"Search_patients for patient Lisa Williams using email lisa.williams792@email.com to retrieve patient ID and insurance details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are confident, logical. First, use search_patients to retrieve insurance details for David Miller to ensure his records are current. Next, use book_appointment to schedule a routine check-up with Dr. Smith for David Miller, ensuring the appointment is set within Dr. Smith's available hours. Finally, use think to confirm appointment booking details and send a confirmation email to David Miller, ensuring he is informed of the date, time, and any necessary preparations for his visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P028", "patient_name": "David Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P028", "patient_name": "David Miller", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirming the appointment details for David Miller and preparing to send a confirmation email."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are optimistic, cautious, patient. \"Search for patient Robert Jones using user ID 'robert.jones332@email.com' to retrieve health record ID and insurance details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P026", "email": "robert.jones332@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are cautious, confident. Search_patients using email emily.garcia400@email.com to retrieve Emily Garcia's patient ID and authorization status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are cautious, confident. \"book_appointment for Sarah Miller with doctor ID D123 for a routine check-up on available date\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_id": "P046", "doctor_id": "D123", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are cautious, flexible, organized. Search for patient records with the name Maria Johnson to verify her identity and retrieve her patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Maria Johnson", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are optimistic, flexible, polite, organized. First, search for patients to verify Sarah Williams' patient ID using her email sarah.williams853@email.com. Once her patient ID is confirmed, check Sarah Williams' insurance details to ensure she is eligible and covered for an appointment with Dr. Smith. After verifying her insurance coverage, proceed to book an appointment for Sarah Williams with Dr. Smith during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the patient ID for Sarah Williams from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Sarah Williams' patient ID is confirmed, check her insurance details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure Sarah Williams is eligible and covered for an appointment with Dr. Smith."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After verifying insurance coverage, proceed to book an appointment for Sarah Williams with Dr. Smith during available hours."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor": "Dr. Smith", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, logical, flexible, independent. search_patients for John Johnson using email john.johnson699@email.com to retrieve patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are direct, flexible, polite. Search_patients for Maria Smith using email maria.smith554@email.com to retrieve patient ID and insurance details. Then, think to verify insurance details for Maria Smith's coverage and eligibility for upcoming appointments. Once verified, book_appointment for Maria Smith with Doctor ID D456 on her preferred date and time, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details for Maria Smith's coverage and eligibility for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_id": "D456", "date": "2023-11-15", "time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are cautious, logical, optimistic, independent. First, search_patients by name 'Michael Miller' to verify patient ID and details, ensuring you have the correct information before proceeding. Once verified, book_appointment for patient ID P12345 with Dr. Smith on an available date and time that suits the patient's schedule. Finally, think about the patient's medical history to prepare for the upcoming appointment, ensuring you are ready to discuss any ongoing treatments or concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Michael Miller", "user_id": "P048"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P048", "doctor": "Dr. Smith", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P048"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Michael Miller's medical history to prepare for the appointment with Dr. Smith, focusing on any ongoing treatments or concerns."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are organized, confident, direct. Search_patient with user_id \"emily.jones379\" to verify patient details and insurance status. Once you have confirmed the insurance verification status for user_id \"emily.jones379\", proceed to book_appointment with doctor_id \"D456\" for a routine check-up, ensuring it falls within available hours. This process is crucial to maintain efficient scheduling and ensure that the patient's insurance covers the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "emily.jones379"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "doctor_id": "D456", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are direct, patient, organized, flexible. First, search_patients with email \"maria.johnson759@email.com\" to verify the patient ID and check their insurance status. Once you have confirmed the patient ID, search_patients for emergency appointments available for this patient ID. If an emergency appointment is available, proceed to book_appointment for the patient with the emergency status. This process ensures that urgent medical needs are addressed promptly, maintaining the quality of care and patient satisfaction.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023", "appointment_type": "emergency"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "appointment_type": "emergency", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are independent, logical, flexible. \"Search_patients with criteria: last name 'Johnson', first name 'John' to retrieve patient ID\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"last_name": "Johnson", "first_name": "John"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are flexible, organized, logical. First, search_patients for Sarah Miller to retrieve her patient ID and current healthcare provider details. Next, search_patients to retrieve Sarah Miller's medical history for her upcoming appointment with Dr. John Smith. Finally, think to assess if Sarah Miller needs any pre-appointment tests or documentation based on her medical history. This will ensure that Sarah is fully prepared for her appointment on October 25, 2023, at 10:00 AM with Dr. John Smith, and that all necessary information is available to facilitate a smooth consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Miller", "user_id": "P046"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Miller", "user_id": "P046", "details": "medical_history"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess Sarah Miller's medical history to determine if any pre-appointment tests or documentation are needed for her appointment with Dr. John Smith on October 25, 2023, at 10:00 AM."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are polite, independent, direct. Book_appointment for patient ID with the selected doctor during available hours, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P027"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance before booking appointment"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P027", "patient_id": "P027", "doctor_id": "D123", "time": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are independent, patient, flexible. Search_patients for Sarah Williams using email sarah.williams853@email.com to retrieve her patient ID and medical history. Check healthcare details for the retrieved patient ID to confirm any existing conditions or special requirements. Think to determine the most suitable primary care physician based on Sarah's medical history and physician specialties, ensuring the physician can address her specific healthcare needs effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Williams' patient ID and medical history using the search_patients function."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details for the retrieved patient ID to confirm any existing conditions or special requirements."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine the most suitable primary care physician based on Sarah's medical history and physician specialties, ensuring the physician can address her specific healthcare needs effectively."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are logical, cautious, direct, organized. First, search_patients with name \"Robert Brown\" and email \"robert.brown551@email.com\" to verify authorization and retrieve patient ID. Once you have the patient ID, proceed to search_patients to verify insurance information for the patient ID retrieved from Robert Brown. After confirming the insurance details, book_appointment for the patient ID retrieved from Robert Brown with Dr. Smith for cardiology on an available date and time. Ensure that the insurance verification is complete before booking the appointment to avoid any issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Brown", "email": "robert.brown551@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P003"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P003", "doctor": "Dr. Smith", "specialty": "cardiology", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are cautious, optimistic, polite, confident. First, search for patient records with email robert.garcia592@email.com to verify patient identity and retrieve patient ID. Once you have confirmed the patient ID, proceed to book an appointment for Robert Garcia with Dr. Smith (ID: D123) for the earliest available time slot. This ensures timely medical attention and maintains efficient scheduling within the healthcare facility.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor_id": "D123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are flexible, organized, patient. Verify insurance details for Maria Smith to ensure eligibility for booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are polite, logical, independent, optimistic. Search_patients for Robert Jones using email robert.jones332@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are confident, flexible, optimistic. Search_patients for user Emily Brown to retrieve patient ID and authorization status. Once you have the patient ID, verify insurance details for the same patient to ensure coverage before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are confident, organized, cautious, independent. First, search for patient details for user Sarah Davis (sarah.davis118@email.com) using the search_patients tool to gather necessary information. Once you have her patient profile, verify her insurance details using the think tool to ensure there are no issues with her coverage. This will allow you to proceed confidently with booking an appointment for Sarah Davis with Dr. Smith, ensuring that all insurance verifications are complete and accurate.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="think",
                kwargs={"action": "verify_insurance", "patient_email": "sarah.davis118@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.davis118@email.com", "doctor_name": "Dr. Smith", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are confident, organized, optimistic. First, search_patients with email sarah.williams602@email.com to retrieve Sarah's patient ID and insurance details. Then, book_appointment for Sarah with Dr. Smith (ID D567) for a routine check-up, ensuring the appointment is within available hours and insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P018", "doctor_id": "D567", "appointment_type": "routine check-up", "insurance_verified": true, "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are cautious, polite. First, assess the need for an appointment based on Sarah Brown’s healthcare history and current needs to ensure she receives appropriate care. Next, confirm Sarah Brown's insurance details and verify coverage eligibility for the desired appointment type, as this will help in understanding any financial implications. Finally, schedule a routine check-up for Sarah Brown with Dr. Jane Doe (Doctor ID: D567) during available hours, ensuring that all insurance coverage is in place for a smooth appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess Sarah Brown's healthcare history and current needs to determine if an appointment is necessary."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm Sarah Brown's insurance details to verify coverage eligibility for a routine check-up."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "doctor_id": "D567", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are flexible, optimistic, patient. First, verify Sarah Brown's insurance coverage for a routine check-up with Dr. John Smith using insurance ID I123456 to ensure that the necessary services are covered. Once the coverage is confirmed, proceed to book an appointment for Sarah Brown with Dr. John Smith using book_appointment with doctor ID D5678, user ID sarah.brown753@email.com, and her preferred slot. This will ensure a smooth and efficient process for Sarah's healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"insurance_id": "I123456", "user_id": "P025"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D5678", "user_id": "P025", "patient_email": "sarah.brown753@email.com", "preferred_slot": "2023-10-15T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are cautious, direct, polite. Search_patients with email robert.jones332@email.com to retrieve patient ID and insurance status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are direct, patient. First, search_patients to retrieve John's medical history using user ID john.johnson941@email.com. After reviewing his medical history, think about potential healthcare services John might need based on his medical history, such as specialized treatments or consultations. Once you have identified these needs, book_appointment for John with Doctor D456 at an available time slot, ensuring that his insurance is verified for the services required.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "email": "john.johnson941@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review John's medical history to identify potential healthcare services he might need, such as specialized treatments or consultations."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_email": "john.johnson941@email.com", "doctor_id": "D456", "service": "specialized_treatment", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are cautious, logical, polite. Use search_patients to find Emily Brown's patient ID and confirm her insurance details are up to date. Once verified, use search_patients with Emily Brown's patient ID to verify if she has any upcoming appointments or outstanding medical tests. This will ensure that Emily's healthcare needs are managed efficiently and that there are no gaps in her care plan.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Brown", "user_id": "P021"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P021", "user_id": "P021"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are confident, optimistic. Search_patients for Sarah Smith using email sarah.smith521@email.com to retrieve her patient ID and last visit details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are organized, patient. Determine the type of appointment David Miller needs by reviewing his recent medical history and symptoms. Then, look up available doctors within his insurance network who can accommodate the required appointment type, ensuring a seamless and efficient process for David's healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P028", "patient_name": "David Miller"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, logical. First, search_patients with email sarah.davis118@email.com to retrieve patient ID and authorization status. Once you have the patient ID, think to verify insurance details for this patient ID to ensure coverage is active and applicable for upcoming appointments. After confirming the insurance details, book_appointment for the patient ID with Dr. Smith at the earliest available time slot, ensuring that the verified insurance details are noted for the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and authorization status from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure coverage is active."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P047", "doctor": "Dr. Smith", "insurance_details": "verified_insurance_details", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are patient, polite. First, search for patient records for user Sarah Brown using her email sarah.brown426@email.com to verify her identity and retrieve her patient ID. Once you have confirmed her identity, check the healthcare details for Sarah Brown's patient ID to confirm her insurance coverage and verify eligibility. Finally, book an appointment for Sarah Brown with doctor D001 on the next available suitable date and time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Brown's patient ID from the search results to confirm her identity."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details for Sarah Brown's patient ID to confirm insurance coverage and verify eligibility."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_id": "D001", "date": "next_available_date", "time": "next_available_time", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, polite, cautious, patient. First, search_patients with email david.miller979@email.com to retrieve patient details for David Miller. Once you have confirmed your registration details, proceed to book_appointment for David Miller with Dr. Smith for a routine check-up on the next available date. Finally, search_patients to confirm any follow-up appointments needed for David Miller, ensuring all necessary healthcare steps are taken.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P028", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "date": "next available"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are direct, cautious. First, search for patients with the email 'david.williams693@email.com' to retrieve the patient ID and authorization status. Once you have the patient ID, check the healthcare details to verify David's insurance coverage status. Finally, book an appointment for David Williams with Dr. Smith, ensuring the appointment falls within the doctor's available hours and is covered by David's insurance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and authorization status from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details to verify insurance coverage using the patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P006", "doctor": "Dr. Smith", "time": "available_time_slot", "covered_by_insurance": true, "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are confident, polite, logical. Use think to verify insurance details for user Sarah Davis (sarah.davis118@email.com) to ensure eligibility for healthcare services.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P047", "email": "sarah.davis118@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are confident, polite, optimistic, patient. \"search_patients with user email robert.johnson741@email.com to retrieve patient ID and authorization status\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.johnson741@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are patient, independent, optimistic, polite. First, search for patient information for Emily Jones using her email emily.jones379@email.com to retrieve her patient ID. Once you have the patient ID, proceed to verify her insurance details. This process ensures that all necessary information is in place before any further healthcare services are provided, maintaining a seamless experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are cautious, flexible, direct, independent. Search_patients using Emily Garcia's email (emily.garcia400@email.com) to retrieve patient ID and details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are patient, confident, independent. First, search_patients with email robert.brown551@email.com to retrieve patient ID and insurance details. Once you have obtained the patient ID, think to verify insurance coverage for the patient ID retrieved from the previous task. This will ensure that the patient is eligible for further medical consultations and treatments under their current insurance plan.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for the retrieved patient ID to ensure eligibility for further consultations and treatments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are logical, cautious, confident, direct. First, search patients for Emily Davis (emily.davis525@email.com) to verify her patient ID and insurance details. Once verified, proceed to check for any existing medical conditions or ongoing treatments that might affect her upcoming visit. Finally, book an appointment for Emily Davis with Dr. Smith for a routine check-up, ensuring it fits within available hours and that her insurance coverage details are confirmed before finalizing the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify patient ID and insurance details for Emily Davis."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check for any existing medical conditions or ongoing treatments for Emily Davis."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are organized, independent. First, search for patient details using user ID for Robert Garcia to verify insurance status and authorization. Once verified, check healthcare details for Robert Garcia to ensure insurance coverage for the required service. This will help in confirming that the necessary services are covered before proceeding with further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are flexible, optimistic. Search for patient records for Robert Jones using email robert.jones332@email.com to verify insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are optimistic, logical, flexible, independent. Use the search_patients tool to find Robert Brown's patient ID and insurance details. Next, verify Robert Brown's insurance coverage for routine check-ups using the insurance provider database to ensure that his insurance plan covers the appointment. Finally, book an appointment for Robert Brown with Dr. Stevens on a date and time that aligns with his insurance coverage. Confirm the booking with Robert Brown via email (robert.brown624@email.com), including the appointment details and any preparation instructions he may need.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "name": "Robert Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Robert Brown's insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance coverage for routine check-ups using the insurance provider database."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "patient_id": "P017", "doctor": "Dr. Stevens", "date": "2023-11-10", "time": "10:00 AM", "insurance_verified": true, "email": "robert.brown624@email.com", "message": "Your appointment with Dr. Stevens is confirmed for November 10, 2023, at 10:00 AM. Please arrive 15 minutes early and bring your insurance card."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are confident, cautious. First, search for patients with the name \"Maria Smith\" and email \"maria.smith554@email.com\" to retrieve her patient ID and insurance details. Once you have obtained the patient ID, proceed to verify the insurance status for Maria Smith. This will ensure that her insurance is active and valid before scheduling any medical appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Maria Smith", "email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance status using the obtained patient ID to ensure it is active and valid."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are direct, organized, logical, independent. First, search for patients with the email robert.johnson741@email.com to retrieve his patient ID and insurance details. Once you have the patient ID, think to verify the insurance status to ensure it is active and covers the necessary medical services. After confirming the insurance, book an appointment for Robert Johnson with Dr. Smith on his preferred date and time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Robert Johnson."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance status to ensure it is active and covers the necessary medical services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor": "Dr. Smith", "date": "preferred_date", "time": "preferred_time", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are polite, confident, patient. Search_patients with parameter email \"sarah.brown426@email.com\" to retrieve patient ID and verify authorization for accessing healthcare information. Then, think to check if the patient ID from the previous task is authorized to access patient information and appointment booking. If the patient is authorized, proceed to book an appointment with the parameters patient ID, doctor ID, appointment date, and time, ensuring it is a routine appointment and falls within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if the retrieved patient ID is authorized to access healthcare information and appointment booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_id": "D456", "appointment_date": "2023-11-15", "appointment_time": "10:00", "appointment_type": "routine", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are flexible, confident, direct, cautious. Use search_patients with parameters: user_email=\"sarah.brown426@email.com\" to retrieve Sarah Brown's patient ID and insurance details. Once you have the patient ID, use think to verify insurance details for the retrieved patient ID, ensuring coverage is active for general consultations.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P039", "insurance_details": "retrieved_insurance_details"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are confident, flexible, organized, optimistic. First, search_patients with name \"Emily Garcia\" to verify patient ID and insurance details to ensure all information is current and accurate. Once verified, proceed to book_appointment for patient ID \"P12345\" with Dr. John Smith on 2023-11-15 at 10:00 AM for an initial consultation. This ensures that Emily Garcia's records are up to date before her appointment, facilitating a smooth check-in process and effective consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Garcia", "user_id": "P036"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor_name": "Dr. John Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are organized, optimistic. First, search for patient records for Sarah Williams using her email sarah.williams853@email.com to verify her identity and retrieve her patient ID. Once you have the patient ID, think to confirm if Sarah Williams' required medical service is covered by her insurance plan. After confirming coverage, book an appointment for Sarah Williams with Dr. John Smith using the patient ID and her preferred slot, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results and verify insurance coverage for the required medical service."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor_name": "Dr. John Smith", "preferred_slot": "2023-10-15T10:00:00", "insurance_verified": true, "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are direct, confident, patient. First, use the \"search_patients\" task with the parameter user_email as \"john.johnson941@email.com\" to retrieve John's patient ID and details. Next, apply the \"think\" task with the retrieved patient_id to verify John's insurance status. Finally, proceed with the \"book_appointment\" task using the verified patient_id and a doctor_id to schedule a routine check-up, ensuring all insurance details are confirmed for the booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "john.johnson941@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P037"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P037", "doctor_id": "D123", "appointment_type": "routine_checkup"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are organized, cautious. Search for patients with the name \"Sarah Williams\" to retrieve her patient ID and insurance details. Then, think to verify the insurance details for the patient ID found in the previous task to ensure accuracy before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Williams", "user_id": "P018"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details for the retrieved patient ID to ensure accuracy before proceeding with any further actions."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are cautious, confident, independent, logical. Search_patients with email \"lisa.williams792@email.com\" to retrieve patient ID and insurance details. Then, use the patient ID to search for past appointment history and medical records to assess the patient's healthcare needs. After reviewing the medical records, think to determine if the patient requires a routine check-up or follow-up appointment. If necessary, book_appointment for the patient with the appropriate doctor ID on an available date/time that suits their healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P045", "patient_id": "P045", "doctor_id": "doctor_id_determined_from_think_step", "date_time": "available_date_time_determined_from_think_step"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are cautious, direct. search_patients with user_email \"sarah.miller381@email.com\" to retrieve Sarah Miller's patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, organized. First, search patients with the name \"Lisa Williams\" to verify her patient ID and insurance details. Once you have confirmed her insurance information, check Lisa's insurance verification status for eligibility to book an appointment. This will ensure that she can proceed with scheduling an appointment without any issues related to insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "user_id": "P045"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the patient ID and insurance details for Lisa Williams from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check the insurance verification status for Lisa Williams to ensure eligibility for booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are patient, flexible, direct, cautious. Use `search_patients` to find patient David Williams using email david.williams693@email.com and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are patient, organized, direct, polite. \"think to prioritize Sarah Brown's request for an appointment based on urgency and doctor's availability\"",
        actions=[
            Action(
                name="think",
                kwargs={"task": "prioritize Sarah Brown's request for an appointment based on urgency and doctor's availability"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, optimistic, organized, cautious. Search for patient records using user email robert.brown731@email.com to retrieve the patient ID. Once you have the patient ID, verify the insurance status to ensure it is active. If the insurance is confirmed, proceed to book an appointment for the patient at their preferred time slot. This process ensures that the patient can receive timely medical care with verified insurance coverage, enhancing the efficiency and reliability of the healthcare service.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance status using the retrieved patient ID to ensure it is active."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_id": "P014", "preferred_time": "2023-10-15T10:00:00", "insurance_status": "active"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, logical, polite, confident. Use search_patients to locate patient details for Robert Brown using email robert.brown731@email.com. Once you have confirmed his details, use think to verify insurance information for Robert Brown to ensure eligibility for healthcare services. This is crucial as we need to confirm his coverage before proceeding with any medical appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P014", "patient_email": "robert.brown731@email.com", "task": "verify insurance information for Robert Brown to ensure eligibility for healthcare services"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are logical, cautious, polite. First, search_patients using Maria Johnson's email (maria.johnson759@email.com) to retrieve her patient ID and medical records. Once you have confirmed her details, proceed to check Maria Johnson's insurance details to verify coverage for upcoming medical appointments. This ensures that all necessary information is accurate and up-to-date before scheduling any medical services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are independent, optimistic. Retrieve available appointment slots for Dr. Smith for the upcoming week and book an appointment for Michael Miller with Dr. Smith for a routine check-up at an available time slot. This task is essential to ensure Michael receives timely healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve available appointment slots for Dr. Smith for the upcoming week."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are flexible, polite, optimistic. First, search_patients with email michael.miller534@email.com to retrieve patient ID and authorization status. Once you have verified authorization for accessing Michael Miller's healthcare information, proceed to search_patients with patient ID to find Michael Miller's primary care physician and available appointment slots. Finally, book_appointment for patient ID with primary care physician on the next available slot during the doctor's hours to ensure Michael receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P048"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P048", "doctor_id": "D456", "appointment_slot": "2023-11-01T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are independent, flexible, cautious, organized. First, think to determine if Maria Smith needs an emergency appointment based on recent health records. If an emergency appointment is not required, proceed to book an appointment for Maria Smith with doctor ID D123 on 2023-11-15 at 10:00 AM, ensuring it's within the doctor's available hours. This process ensures that Maria receives timely care while respecting the doctor's schedule.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are patient, direct, independent. Retrieve Sarah Brown's insurance details to verify coverage for upcoming appointments and verify if Dr. John Smith accepts Sarah Brown's insurance plan. These steps are crucial to ensure that Sarah can proceed with her healthcare needs without any financial surprises. Once you have confirmed that Dr. Smith accepts her insurance, you can proceed with booking an appointment for Sarah Brown on the earliest available date within Dr. Smith's working hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Brown's insurance details to verify coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Dr. John Smith accepts Sarah Brown's insurance plan."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once insurance is verified, proceed to book an appointment for Sarah Brown."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "doctor_name": "Dr. John Smith", "appointment_type": "routine", "date": "earliest available"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are organized, polite, flexible, direct. First, search for patient information for Sarah Williams using her email sarah.williams853@email.com to verify authorization. Once her authorization is confirmed, proceed to search healthcare items to find available doctors for a general check-up within Sarah Williams' insurance network. This will ensure that she has access to covered healthcare services and can receive the necessary care without unexpected expenses.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are direct, organized, flexible. Think about Robert's recent healthcare needs to determine the type of appointment required (routine or emergency).",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P027"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P027", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are optimistic, direct, cautious, organized. Search_patients with user ID lisa.williams792@email.com to retrieve patient details and authorization status. Think to verify insurance details for patient Lisa Williams before proceeding with any appointments. Book_appointment for Lisa Williams with doctor ID D567 during available hours, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "lisa.williams792@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Lisa Williams before proceeding with any appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P045", "doctor_id": "D567", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are cautious, optimistic, independent. Search for patient Maria Smith using email maria.smith256@email.com to retrieve patient ID and verify insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are organized, polite, independent. First, use `search_patients` with email \"robert.brown731@email.com\" to retrieve Robert Brown's patient details and verify authorization. Once authorization is confirmed, use `search_patients` to check Robert Brown's insurance details and confirm verification status. After confirming the insurance verification, use `book_appointment` with the patient ID, doctor ID, and verified insurance details to schedule Robert Brown's appointment during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com", "detail": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P014", "doctor_id": "D456", "insurance_details": "verified_insurance_789", "appointment_time": "2023-10-15T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, optimistic, direct. Search for patient Sarah Williams by email sarah.williams853@email.com to retrieve patient ID. Once you have the patient ID, search for available appointment slots for Dr. Smith, ensuring availability matches Sarah Williams' schedule. This is crucial to accommodate her needs efficiently and ensure she receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are patient, polite, confident, cautious. Search for patient Michael Miller using email michael.miller534@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are flexible, confident, patient. First, book an appointment for Michael Miller with Dr. Smith on 2023-10-15 at 10:00 AM, ensuring Dr. Smith is available. After securing this appointment, think about the insurance verification process for Michael Miller's appointment to ensure all necessary paperwork is in order before the visit.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Before booking the appointment, I need to verify Dr. Smith's availability on 2023-10-15 at 10:00 AM and ensure that Michael Miller's insurance is verified."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming Michael Miller's insurance is verified, I can proceed to book the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "doctor_name": "Dr. Smith", "patient_name": "Michael Miller", "appointment_date": "2023-10-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are organized, confident. \"search_patients with patient ID to find available appointment slots with Dr. Smith\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are polite, optimistic. First, search_patients with criteria: {patient_name: \"Emily Brown\"} to retrieve insurance details. Then, think to check if Emily Brown's insurance is verified and active. If the insurance is verified and active, proceed to book_appointment for Emily Brown with doctor ID 12345 at the next available time slot. Ensure that the insurance verification is completed before booking the appointment to avoid any issues during the visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Emily Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Emily Brown's insurance is verified and active."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "doctor_id": "12345", "patient_name": "Emily Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are independent, confident, polite, patient. Search_patients with name \"Emily Davis\" and email \"emily.davis525@email.com\" to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Davis", "email": "emily.davis525@email.com", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are polite, confident, optimistic, independent. First, search_patients with email sarah.smith521@email.com to retrieve her patient ID and medical history, as this information is crucial for understanding her healthcare needs. Next, search_patients to confirm Sarah Smith's insurance status and coverage details to ensure that her upcoming medical services are covered. Finally, think about the available doctors and their schedules to find a suitable time slot for Sarah Smith, considering her preference for a morning appointment. Once you have all the necessary information, proceed to book_appointment for user Sarah Smith with Dr. John Doe for a routine check-up on 12/10/2023 at 10:00 AM, ensuring that all steps are completed efficiently and with attention to detail.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_email": "sarah.smith521@email.com", "doctor_name": "Dr. John Doe", "appointment_date": "12/10/2023", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are confident, organized. Use search_patients with user email emily.jones379@email.com to retrieve Emily Jones's patient ID and insurance information. With the patient ID retrieved, check Emily Jones's medical history for any special considerations. Based on her medical history, think to determine if Emily requires a routine or an emergency appointment. Once you have determined the type of appointment needed, book an appointment for Emily Jones with doctor ID D456 during the available hours on the preferred date. This ensures that Emily receives timely and appropriate care based on her medical needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "emily.jones379@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Emily Jones's patient ID and insurance information from the search_patients result."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Emily Jones's medical history using her patient ID to identify any special considerations."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if Emily requires a routine or an emergency appointment based on her medical history."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "patient_id": "P007", "doctor_id": "D456", "appointment_type": "determined_appointment_type", "preferred_date": "2023-10-15", "available_hours": "09:00-11:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are logical, independent. First, search_patients with email \"sarah.williams853@email.com\" to retrieve patient ID and insurance details. Next, think to verify insurance coverage for the patient ID retrieved from search_patients to ensure that the upcoming medical services are covered. Finally, book_appointment for the patient ID with doctor ID on an available date and time that suits the patient's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance coverage for the retrieved patient ID to ensure upcoming medical services are covered."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, organized, cautious, flexible. First, search_patients to verify John Johnson's insurance details and eligibility for booking an appointment. Once verified, proceed to book_appointment for John Johnson with Dr. Smith (Doctor ID: D123) for a routine check-up, ensuring it fits within available hours. This ensures that all necessary preparations are in place for a smooth and efficient healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P029", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "patient_name": "John Johnson", "doctor_id": "D123", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are flexible, polite, patient. Search for patients with the criteria: name \"Robert Johnson\" and email \"robert.johnson741@email.com\" to retrieve their patient ID and insurance details. Then, verify the insurance details for the retrieved patient ID to ensure eligibility for appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming patient ID retrieved is 'P567' and insurance details are available."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, independent, direct, logical. Book_appointment for patient ID with Dr. John Smith, ensuring it aligns with his available hours",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "doctor_name": "Dr. John Smith", "patient_id": "P001", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are direct, confident, optimistic. First, search for patients with the name \"Sarah Williams\" to retrieve her patient ID and insurance details necessary for authorization. Once you have confirmed that Sarah Williams has the proper insurance coverage for a routine check-up, proceed to book an appointment for her with Dr. Smith on the next available date and time, ensuring that the slot is not reserved for emergencies. This will help streamline the process and ensure Sarah receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P018", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are cautious, optimistic. Search_patients with name \"Emily Brown\" and email \"emily.brown290@email.com\" to verify patient record and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Brown", "email": "emily.brown290@email.com", "user_id": "P021"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are organized, logical, cautious. First, check healthcare details for User: Emily Brown (emily.brown290@email.com) to verify insurance information. Once confirmed, search_patients to find available doctors for general consultation within Emily Brown's insurance network, ensuring she has access to covered healthcare professionals.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, verify the insurance information for Emily Brown to ensure she has access to covered healthcare professionals."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "email": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Now that Emily Brown's insurance details are verified, search for available doctors within her insurance network for a general consultation."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "insurance_network": "verified_insurance_network", "specialty": "general consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are flexible, cautious, patient. First, search for patient information for Sarah Miller using search_patients with email sarah.miller381@email.com to gather her medical history and ensure all records are up-to-date. Next, think about verifying Sarah Miller’s insurance details to ensure coverage for healthcare services, which is essential before scheduling any appointments. Finally, book_appointment for Sarah Miller with Dr. James Wilson on 2023-11-15 at 10:00 AM, considering her insurance coverage, to ensure a smooth and hassle-free consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com", "user_id": "P046"}
            ),
            Action(
                name="think",
                kwargs={"text": "Verify Sarah Miller's insurance details to ensure coverage for healthcare services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.miller381@email.com", "doctor_name": "Dr. James Wilson", "appointment_date": "2023-11-15", "appointment_time": "10:00", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are patient, flexible, confident, direct. Search_patients with email \"michael.brown235@email.com\" to verify patient authorization and retrieve patient ID. Once you have the patient ID, think to verify insurance details to ensure the patient is covered for the necessary procedures. This is crucial before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details to ensure the patient is covered for the necessary procedures."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are independent, direct. Search_patients for patient ID by using user email robert.jones332@email.com to verify identity and retrieve patient information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.jones332@email.com", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, direct, confident. \"think about Maria Smith's recent healthcare needs and preferences to determine possible upcoming appointments and medical checks\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Consider Maria Smith's recent healthcare needs and preferences to determine possible upcoming appointments and medical checks."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are polite, direct, organized, confident. First, search for patient information for Michael Miller using search_patients with email michael.miller534@email.com to gather necessary details. Next, think to verify if Michael Miller's insurance is accepted by the selected doctor, ensuring that the appointment will be covered. Finally, book an appointment for Michael Miller with doctor ID D123 using book_appointment for date 2023-11-15 at 10:00 AM, ensuring that the chosen time fits within Michael Miller's schedule and meets his healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Michael Miller's insurance is accepted by doctor ID D123 to ensure the appointment will be covered."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P048", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are organized, confident. Search for patient Robert Johnson with email robert.johnson197@email.com to retrieve patient ID and insurance details. Then, verify Robert Johnson's insurance details to ensure they are up-to-date and valid for booking appointments. This is crucial as it ensures Robert can seamlessly access healthcare services without any delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are patient, confident, independent. First, search_patients with user email robert.johnson197@email.com to retrieve the patient ID and insurance details. Then, think to verify insurance validity for the patient ID obtained from search_patients. Once the insurance is confirmed valid, proceed to book_appointment for the patient ID with Dr. Smith for a routine check-up, ensuring the appointment is within Dr. Smith's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance validity for the patient ID obtained from search_patients."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P027", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are cautious, flexible. Search_patients with criteria: user email 'maria.johnson759@email.com' to retrieve patient ID and insurance details. Think about the insurance verification status for patient ID retrieved from previous task. Ensure that the insurance verification is complete before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Maria Johnson."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance verification is complete for the retrieved patient ID."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are confident, patient, cautious, flexible. First, search_patients with email sarah.davis118@email.com to retrieve her patient ID and insurance details. Next, search_patients with the retrieved patient ID to check her medical history and any ongoing treatments. Finally, think to determine the best available doctor based on Sarah Davis's medical needs and preferences, ensuring the chosen doctor is well-suited for her routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P047"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are direct, organized, optimistic, logical. Search_patients for Emily Davis using email emily.davis525@email.com to retrieve her patient ID and insurance details. Then, think to verify these insurance details with her insurance provider. Once verification is complete, book_appointment for Emily Davis with Dr. Smith on 2023-10-15 at 10:00 AM. This ensures that her insurance is confirmed prior to the appointment, facilitating a smooth process for her healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details retrieved for Emily Davis with her insurance provider to ensure they are accurate and up-to-date."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor": "Dr. Smith", "date": "2023-10-15", "time": "10:00", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are flexible, polite, cautious, optimistic. Search for patient details using email robert.johnson741@email.com to verify insurance information and authorization status. Once you confirm that Robert Johnson has valid insurance for booking an appointment, proceed to book an appointment for him with Dr. Smith at the earliest available morning slot. Ensure that all appointments are accurately recorded in the healthcare system for Robert Johnson.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson741@email.com", "doctor_name": "Dr. Smith", "time_slot": "earliest_morning", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are independent, direct, logical, cautious. Verify insurance details for patient David Brown to ensure coverage for upcoming appointments. Once coverage is confirmed, book an appointment for David Brown with Dr. Smith on the available slot, ensuring it aligns with the doctor's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P020", "patient_name": "David Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for David Brown to ensure coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P020", "patient_name": "David Brown", "doctor_name": "Dr. Smith", "appointment_time": "2023-11-15T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are optimistic, polite. First, search for patient information for Robert Brown using email robert.brown731@email.com to verify authorization. Once authorization is confirmed, proceed to check healthcare details for Robert Brown to confirm insurance coverage and eligibility. This ensures that all necessary information is accurate and up-to-date before any further actions are taken in the healthcare process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are organized, independent, optimistic, confident. search_patients with email \"maria.smith256@email.com\" to retrieve patient ID and current healthcare provider details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are cautious, organized, confident, direct. Book_appointment for Lisa Williams with Dr. Smith for an emergency visit at the earliest available time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams", "doctor_name": "Dr. Smith", "appointment_type": "emergency"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are patient, confident, logical, organized. First, search for patient Robert Johnson in the system using email robert.johnson197@email.com to verify identity and retrieve medical history. Once his identity is confirmed and his medical history is reviewed, proceed to search for available appointment slots for Robert Johnson's preferred doctor within the next two weeks. This will ensure that his healthcare needs are addressed promptly and efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are polite, confident, direct, cautious. Please check the healthcare details for Robert Brown (robert.brown731@email.com) to verify his insurance coverage status. Once verified, search for available doctors specializing in cardiology within the healthcare system for Robert Brown. After identifying potential options, determine the best available cardiologist based on Robert Brown's insurance coverage and location.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com", "user_id": "P014"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance coverage status before proceeding with finding a cardiologist."}
            ),
            Action(
                name="search_patients",
                kwargs={"specialty": "cardiology", "location": "Robert Brown's location", "insurance_coverage": "verified", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are confident, direct, flexible, logical. Search for patient John Johnson using email john.johnson699@email.com to retrieve patient ID and details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, organized, logical. \"book_appointment for patient ID retrieved with doctor ID found at selected time slot with insurance verification\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P020", "email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID using the search_patients result."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Find available doctor ID and time slot for the appointment."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance before booking the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P020", "patient_id": "P020", "doctor_id": "available_doctor_id", "time_slot": "selected_time_slot", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are patient, optimistic. Retrieve patient details for Maria Smith using search_patients with email parameter set to maria.smith554@email.com. Once you have obtained her patient ID, verify her insurance details using think with the patient ID. After confirming her insurance, schedule an appointment for Maria Smith with Dr. Johnson using book_appointment with the patient ID, doctor ID D001, and her preferred time slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P013"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_id": "D001", "time_slot": "2023-11-10T10:00:00", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are direct, cautious, patient. Use search_patients to find patient details for Robert Johnson with email robert.johnson741@email.com. Once you have confirmed his details, use book_appointment to schedule a routine check-up for Robert Johnson with Dr. Smith on the available date and time. This ensures that Robert receives timely care and maintains his health effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson741@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are independent, flexible, cautious. Search_patients with name \"Sarah Davis\" and email \"sarah.davis118@email.com\" to verify patient record and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Davis", "email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, patient, direct. First, search_patients with parameters: email=\"emily.jones379@email.com\" to retrieve patient ID and authorization status. Once you have confirmed the patient ID and authorization, proceed to book_appointment with parameters: patient_ID=\"P001\", doctor_ID=\"D123\", preferred_date=\"2023-11-15\", preferred_time=\"10:00 AM\" to check the doctor's availability for scheduling the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_ID": "P001", "doctor_ID": "D123", "preferred_date": "2023-11-15", "preferred_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are polite, organized. Book_appointment for John Johnson with Dr. Smith for a routine check-up at the next available slot, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are confident, patient, cautious. Search_patients for Lisa Williams using email (lisa.williams792@email.com) to retrieve patient ID and medical history, and then check healthcare details for user Lisa Williams (lisa.williams792@email.com) to verify insurance coverage. This will ensure that her medical records are up-to-date and that her insurance details are confirmed before any further healthcare services are scheduled.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are flexible, confident. Search_patients for Robert Brown using email robert.brown624@email.com to retrieve patient ID and insurance details. Think to verify insurance details for patient ID obtained from search_patients, ensuring the information is accurate and up-to-date. Next, search_patients to check for available doctors and their schedules who accept the verified insurance, ensuring that the doctors are specialists in the required field. Once you have a list of available doctors, book_appointment for patient ID during doctor's available hours using verified insurance, ensuring it is not an emergency and fits within the patient's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Robert Brown from the search_patients response."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details obtained for Robert Brown to ensure they are accurate and up-to-date."}
            ),
            Action(
                name="search_patients",
                kwargs={"insurance": "verified_insurance_details", "specialty": "required_specialty"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the list of available doctors who accept the verified insurance and are specialists in the required field."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P017", "doctor_id": "selected_doctor_id", "insurance": "verified_insurance_details", "appointment_time": "doctor_available_time", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are polite, organized, logical, confident. First, search for Lisa Williams to verify her authorization for accessing patient records. Once authorization is confirmed, proceed to search for Lisa Williams' insurance details to verify her coverage. After confirming her insurance coverage, book an appointment for Lisa Williams with Dr. Smith at 10:00 AM on the next available Tuesday. Ensure all steps are completed in sequence to maintain accuracy and efficiency in handling patient appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "user_id": "P045"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "user_id": "P045", "action": "verify_authorization"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "user_id": "P045", "action": "verify_insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Lisa Williams", "doctor_name": "Dr. Smith", "appointment_time": "10:00 AM", "appointment_day": "next Tuesday", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, independent, organized. First, search_patients with email \"david.brown214@email.com\" to retrieve the patient ID and insurance details. Next, verify the insurance information for the retrieved patient ID to ensure it is up-to-date and covers necessary treatments. Finally, search_patients with the retrieved patient ID to check their medical history and determine if there are any immediate health concerns that require urgent attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are independent, flexible, direct. First, search for patient John Johnson using email john.johnson627@email.com to verify existing records. Once you have confirmed the records, proceed to search for the insurance details of John Johnson to verify coverage before booking an appointment. This ensures that all necessary information is accurate and up-to-date, facilitating a smooth appointment booking process in the healthcare system.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "search_type": "insurance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, logical. First, search_patients with user ID U789 to verify patient Emily Davis' details and insurance information to ensure accuracy. Next, think to confirm Emily Davis' insurance coverage details before finalizing the appointment, as this will prevent any billing issues. Finally, book_appointment for Emily Davis with Dr. Smith on 2023-11-15 at 10:00 AM, ensuring insurance verification is complete to provide a seamless experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Davis' insurance coverage details to ensure there are no billing issues before booking the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are patient, direct, organized. Search_patients for Robert Johnson to retrieve his patient ID and medical history. Then, think to verify if Robert Johnson's insurance covers the requested medical procedure. Once insurance coverage is confirmed, book_appointment for Robert Johnson with Dr. Smith on the next available date and time, ensuring all necessary details are communicated clearly to both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "user_id": "P027"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Robert Johnson's insurance covers the requested medical procedure."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P027", "doctor": "Dr. Smith", "date": "next_available_date", "time": "next_available_time", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are flexible, organized. Search for patient records with email sarah.smith521@email.com to verify identity and retrieve patient ID. Once the patient ID is confirmed, verify Sarah Smith's insurance details to ensure coverage for a routine check-up appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure coverage for a routine check-up."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are logical, polite. Search_patients for user with email lisa.jones889@email.com to retrieve patient ID and insurance information. Then, think to verify insurance details for the patient ID obtained from the previous step. This ensures that the patient is covered for their upcoming medical needs. Once the insurance verification is complete, proceed to book an appointment for the patient with Dr. Smith at the selected time slot. This sequence of actions ensures a smooth and efficient process for the patient's healthcare management.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance information from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the obtained patient ID to ensure coverage for upcoming medical needs."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "patient_id": "P050", "doctor": "Dr. Smith", "time_slot": "selected_time_slot"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are confident, polite, logical. Use search_patients to find the patient profile for John Johnson using the email john.johnson627@email.com. Once you have located the profile, use think to verify John Johnson's insurance details and ensure they are up to date for appointment booking. After confirming the insurance details, use book_appointment to schedule a routine check-up for John Johnson with Dr. Smith, ensuring the appointment is during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify John Johnson's insurance details are up to date"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson627@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are cautious, optimistic, independent, confident. First, search for patient records for Emily Garcia using her email emily.garcia400@email.com to verify insurance details. Once you have confirmed her insurance information, proceed to check her insurance verification status to ensure she is eligible for appointment booking. This process is crucial to ensure that Emily Garcia can seamlessly schedule her healthcare appointments without any issues related to insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are cautious, patient. First, search_patients to find the user ID for Sarah Smith (sarah.smith521@email.com) in the healthcare system. Once you have confirmed her user ID, think to verify Sarah Smith's insurance details for eligibility before proceeding to book an appointment. If her insurance is valid, book_appointment with doctor D123 for Sarah Smith for a routine check-up during available hours. If there are any issues with insurance eligibility or appointment availability, explore alternative options and communicate with Sarah to ensure her needs are met efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Sarah Smith's user ID is confirmed, verify her insurance details for eligibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If Sarah's insurance is valid, proceed to check doctor D123's available hours for booking a routine check-up."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If there are any issues with insurance eligibility or appointment availability, consider alternative options and communicate with Sarah to ensure her needs are met efficiently."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are confident, polite. Search for patient records in the database using Emily Davis's email (emily.davis525@email.com) to verify her identity and retrieve her patient ID. Then, search_patients using Emily Davis's patient ID to retrieve her medical history and current healthcare needs. Finally, think to determine the urgency of Emily Davis’s healthcare needs to assess if an emergency appointment is required.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess the urgency of Emily Davis's healthcare needs to determine if an emergency appointment is required."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are flexible, optimistic, polite, organized. Search for patient details for Maria Johnson using email maria.johnson759@email.com to verify insurance information. Once the insurance coverage is confirmed, book an appointment for Maria Johnson with Dr. Smith (Doctor ID: D456) on October 15, 2023, at 10:00 AM. Ensure that all details are accurate and that the insurance coverage is properly documented to facilitate a smooth appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.johnson759@email.com", "doctor_id": "D456", "appointment_date": "2023-10-15", "appointment_time": "10:00", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are organized, logical. book_appointment(patient ID, Dr. Smith, selected date and time) ensuring it aligns with available hours",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"patient ID": "P020", "doctor": "Dr. Smith", "selected date and time": "2023-10-25T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are polite, direct. First, search_patients for user Robert Johnson to retrieve his patient ID and verify authorization for information access. Once authorization is confirmed, proceed to search_patients for Robert Johnson's insurance details to verify coverage for upcoming appointments. This ensures that his insurance plan covers routine visits, which is necessary before booking any appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "user_id": "P024"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "user_id": "P024", "info_type": "authorization"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Robert Johnson", "user_id": "P024", "info_type": "insurance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are confident, organized. First, use the search_patients tool to find available doctors for a general check-up for Robert Johnson. Once you have identified potential doctors, use the think tool to determine Dr. Smith's available hours for booking an appointment. Finally, use the book_appointment tool to schedule a routine check-up for Robert Johnson with Dr. Smith on 2023-10-25 at 10:00 AM.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson", "service": "general check-up"}
            ),
            Action(
                name="think",
                kwargs={"doctor_name": "Dr. Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson", "doctor_name": "Dr. Smith", "date": "2023-10-25", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are flexible, logical, organized. First, search_patients to retrieve Sarah Miller's insurance details and verify coverage to ensure her visit with Dr. John Smith is covered. Once coverage is confirmed, proceed to book_appointment for Sarah Miller with Dr. John Smith on her preferred date and time, ensuring it is within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_name": "Dr. John Smith", "date": "2023-11-15", "time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are direct, organized, patient. Retrieve user authorization for accessing patient information for Maria Smith (maria.smith256@email.com) and then search_patients with user ID maria.smith256@email.com to retrieve Maria Smith's patient details. This process is essential for ensuring that all necessary information is available before scheduling any medical appointments, maintaining compliance with healthcare privacy regulations.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "maria.smith256@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are logical, polite, independent, organized. First, search for patient details using search_patients tool with parameters: email=maria.smith554@email.com to ensure you have the correct patient information. Once confirmed, verify insurance coverage for Maria Smith using think tool with parameters: insurance_id=INS789 to ensure her appointment will be covered. Finally, book an appointment for Maria Smith with Dr. John Doe using book_appointment tool with parameters: patient_id=P456, doctor_id=D123, time_slot=10:00 AM to secure her consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"insurance_id": "INS789"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_id": "D123", "time_slot": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, optimistic, patient, cautious. search_patients for Emily Garcia's medical history using user email emily.garcia400@email.com",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are organized, logical. \"search_patients for user ID U567 to verify insurance details for Robert Brown\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "U567", "patient_name": "Robert Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, cautious, confident, polite. Search_patients for John Johnson using email john.johnson941@email.com to retrieve his patient ID and medical history. Then, think to determine suitable doctors for John Johnson based on his medical history and insurance coverage, ensuring he receives the best possible care tailored to his needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are independent, optimistic. Book_appointment for Maria Smith with doctor available on the next weekday during office hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "name": "Maria Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith", "doctor_availability": "next_weekday", "appointment_type": "routine", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are cautious, optimistic. First, search for patient information using search_patients with your email emily.garcia400@email.com to verify your identity and insurance details. Next, verify your insurance details to ensure coverage for the upcoming appointment using think with available patient insurance data. Finally, book an appointment for yourself with Dr. Smith on the available date and time using book_appointment with the verified insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P036", "insurance_data": "verified_insurance_details"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "doctor": "Dr. Smith", "date": "2023-11-15", "time": "10:00 AM", "insurance_details": "verified_insurance_details"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are logical, cautious, polite, direct. \"Search_patients for Emily Davis in the system to retrieve her patient ID and recent visit history\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are confident, flexible, direct. First, search_patients with email sarah.williams853@email.com to retrieve her patient ID. Once you have the patient ID, check Sarah Williams' insurance details for coverage verification to ensure that her upcoming medical expenses are covered.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are cautious, polite, optimistic. book_appointment: Schedule an appointment for Maria Smith with doctor ID D123 during available hours",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "doctor_id": "D123", "patient_name": "Maria Smith", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are cautious, optimistic, polite, patient. First, search_patients for John Johnson to retrieve his patient ID and verify authorization for accessing his medical records. Once you have confirmed authorization, book_appointment for John Johnson with Dr. Smith (doctor ID D567) on the earliest available date. This sequence ensures that John Johnson's medical information is handled securely and that he receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P037", "doctor_id": "D567", "date": "2023-10-15", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, logical. Book_appointment for Maria Smith with Dr. John Doe for a routine check-up on the next available morning slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith", "doctor_name": "Dr. John Doe", "appointment_type": "routine check-up", "preferred_time": "morning"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are polite, confident, independent. First, search_patients for John Johnson using email: john.johnson699@email.com to retrieve patient ID and details. Next, check healthcare details for the patient ID retrieved in the previous task to ensure insurance information is up-to-date. Finally, book_appointment for the patient ID retrieved with the selected doctor during available hours, ensuring insurance verification is completed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search_patients response to proceed with checking healthcare details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance information is up-to-date for the retrieved patient ID before booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P029", "doctor_id": "selected_doctor_id", "appointment_time": "available_hour", "insurance_verified": true, "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are logical, organized. First, search_patients with the email sarah.brown426@email.com to verify user identity and retrieve the patient ID. Once you have the patient ID, use it to search_patients and retrieve the patient's medical history and preferred doctor. This information is crucial for ensuring that the patient receives consistent and personalized care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P039", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, independent, confident, cautious. Think about patient Sarah Davis's need for a follow-up appointment with Dr. Smith after her recent surgery, and search for Dr. Smith's available appointment slots for the upcoming week.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P047", "patient_name": "Sarah Davis"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for Dr. Smith's available appointment slots for the upcoming week."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, flexible, logical, direct. First, verify insurance details for David Miller using the think tool to ensure coverage for the upcoming appointment. Once his insurance details are confirmed, book an appointment for David Miller with Dr. Smith for a routine check-up using the book_appointment tool, ensuring it falls within available hours. This process is crucial to ensure that David's healthcare needs are met without any disruptions or unexpected costs.",
        actions=[
            Action(
                name="think",
                kwargs={"task": "Verify insurance details for David Miller to ensure coverage for the upcoming appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "David Miller", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are direct, polite, confident, optimistic. First, search_patients for patient with email lisa.jones889@email.com to verify authorization status. It is crucial to ensure that Lisa Jones is authorized for the requested services before proceeding. Once authorization is confirmed, search_patients to confirm any existing appointments for Lisa Jones to avoid conflicts. This step is essential to ensure her new appointment does not overlap with any current commitments, providing a seamless experience. If both conditions are met, proceed to book_appointment for Lisa Jones with doctor ID D123 on an available date and time. If any issues arise, such as lack of authorization or scheduling conflicts, please address them accordingly by notifying the appropriate department or contacting Lisa Jones for further clarification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "check_appointments": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "lisa.jones889@email.com", "doctor_id": "D123", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are cautious, organized. Begin by searching for patient records for user Michael Brown (michael.brown235@email.com) using the search_patients tool to retrieve patient ID and healthcare details. Once you have obtained the patient ID, proceed to verify the insurance coverage for this patient to ensure eligibility for appointment booking. This sequential approach will help in maintaining a smooth workflow and ensuring that all necessary information is gathered before proceeding to the next step in the healthcare process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are flexible, confident, patient, cautious. First, search_patients(email=\"robert.jones332@email.com\") to retrieve the patient ID and authorization status for Robert Jones. Once you have the patient ID, think(patient_ID=\"P123\") to verify his insurance details, ensuring that he is covered for a routine appointment. After confirming the insurance verification, proceed to book_appointment(patient_ID=\"P123\", doctor_ID=\"D456\", date=\"2023-10-12\", time=\"10:00\", appointment_type=\"routine\").",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_ID": "P123"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_ID": "P123", "doctor_ID": "D456", "date": "2023-10-12", "time": "10:00", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are confident, logical. Search_patients for patient Robert Johnson using email robert.johnson741@email.com to retrieve patient ID and insurance details. Then, think to verify insurance details for the retrieved patient ID and check coverage for upcoming appointments. This will ensure that Robert Johnson can proceed with his scheduled healthcare services without any financial or administrative issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details for Robert Johnson. Verify the insurance details to ensure coverage for upcoming appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are polite, organized, optimistic, cautious. First, search_patients for user Emily Brown (emily.brown290@email.com) to verify patient authorization. Once you have confirmed her authorization, think to confirm Emily Brown’s insurance details are up-to-date for her healthcare coverage. This will ensure that all necessary information is accurate and current before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "email": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm Emily Brown's insurance details are up-to-date for her healthcare coverage."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are optimistic, confident. Search for Emily Davis's patient profile in the healthcare system using her email (emily.davis525@email.com) to verify her information and access permissions. Once her profile is verified, proceed to verify Emily Davis's insurance coverage details and confirm her eligibility for a routine check-up appointment. After confirming her eligibility, book an appointment for Emily Davis with Dr. Smith (ID D123) on the next available date that fits the criteria, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Davis's insurance coverage details and confirm her eligibility for a routine check-up appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.davis525@email.com", "doctor_id": "D123", "appointment_type": "routine check-up", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are direct, polite, independent, organized. Use search_patients with parameter \"email\" set to \"david.brown214@email.com\" to retrieve David Brown's patient information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are confident, polite, logical. Search for patient information for David Miller using email david.miller979@email.com to verify identity and retrieve patient ID. Once you have successfully retrieved the patient ID, proceed to verify insurance details for David Miller to confirm eligibility for appointment booking. This ensures that David Miller can be scheduled for a medical consultation without any issues related to insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are confident, polite, organized, optimistic. Search for available doctors in the dermatology specialty for Emily Brown and book an appointment with Dr. Smith on the next available date during clinic hours. Once the appointment is booked, confirm the booking details and send a notification to Emily Brown's email emily.brown290@email.com to ensure she is informed about her upcoming visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "doctor_name": "Dr. Smith", "specialty": "dermatology", "patient_name": "Emily Brown", "patient_email": "emily.brown290@email.com", "appointment_date": "next_available", "clinic_hours": "9am-5pm"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are patient, logical, organized, optimistic. Search_patients with email sarah.williams602@email.com to retrieve patient ID and medical history authorization status. Then, use the patient ID to confirm Sarah's preferred doctor and their available hours. This information is crucial to ensure that Sarah's healthcare preferences are respected and to facilitate a smooth booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are confident, logical, direct. Search_patients with email robert.johnson197@email.com to retrieve patient ID and insurance details, then think to verify insurance coverage details for the patient ID retrieved. Ensure that the patient's insurance covers routine check-ups before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if the insurance covers routine check-ups for the retrieved patient ID."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are organized, flexible. First, search_patients with patient_email as robert.brown731@email.com to verify identity and retrieve patient ID. Once you have the patient ID, check healthcare details for patient ID P123 to confirm insurance status and coverage details. This will ensure that the patient is eligible for the services before proceeding with any appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming the patient ID retrieved from the search_patients call is P123, proceed to check healthcare details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, independent, organized, optimistic. Search_patients with email \"sarah.brown426@email.com\" to verify patient information and retrieve patient ID. Then, think to identify available doctors for a routine checkup based on Sarah Brown's healthcare needs, ensuring that you consider her medical history and preferences to provide the best care options.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are direct, independent, cautious. Search_patients for Sarah Smith using email sarah.smith521@email.com to verify identity and retrieve patient ID. Once you have the patient ID, think to determine if Sarah Smith's visit is routine or requires emergency attention. If the visit is routine, book_appointment for the patient ID with a selected doctor during available hours, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if Sarah Smith's visit is routine or requires emergency attention."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P033", "doctor_id": "selected_doctor_id", "time": "available_hour", "insurance_verified": true, "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are confident, organized, flexible, polite. First, search for patients using the email maria.miller855@email.com to retrieve Maria Miller's patient ID. Once you have confirmed her patient ID, proceed to book an appointment for Maria Miller with doctor D234 on the next available date and time, ensuring that her insurance verification is complete before finalizing the booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P042", "doctor_id": "D234", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are patient, optimistic, polite. Search_patients for Emily Garcia using email emily.garcia400@email.com to retrieve her patient ID and medical history. Think to determine the most appropriate doctor for Emily Garcia's upcoming consultation based on her medical history, ensuring she receives specialized care. Think to prioritize the urgency of Emily Garcia's consultation based on the retrieved medical history and symptoms, and assess if immediate attention is required.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Emily Garcia's patient ID and medical history to determine the appropriate doctor and urgency of her consultation."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are optimistic, patient, confident. First, search_patients with email \"david.williams693@email.com\" to retrieve patient ID and insurance information. Next, use the patient ID retrieved to check last appointment details and the doctor's available hours. Finally, think to determine the best available time for the patient and doctor based on the patient's schedule and the doctor's available hours, ensuring a seamless appointment booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are polite, logical, independent. First, search for the patient ID for Robert Johnson using the email robert.johnson741@email.com to verify his identity. Once the patient ID is confirmed, check the healthcare details associated with this ID to review Robert Johnson's medical history and insurance information. Finally, book an appointment with Dr. Smith (Doctor ID: D123) for Robert Johnson on an available date and time, ensuring that his insurance covers the general practice visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once the patient ID for Robert Johnson is retrieved, proceed to check his healthcare details."}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P024"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Johnson's insurance covers general practice visits before booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D123", "patient_id": "P024", "date": "available_date", "time": "available_time", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are cautious, patient, polite. Search_patients by name \"Emily Brown\" to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Brown", "user_id": "P021"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are independent, flexible. Think to evaluate if Sarah Brown needs to schedule a routine or emergency appointment. Once you determine the type of appointment needed, search_patients to find available doctors for Sarah Brown's required appointment type.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Evaluate if Sarah Brown needs a routine or emergency appointment based on her symptoms or condition."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are direct, optimistic. First, search_patients using Robert Garcia's patient ID to check insurance details and verify coverage for a general check-up. Next, think to determine if Robert Garcia's insurance covers the required medical service for a general check-up. Finally, search_patients to find available doctors for a general check-up within Robert Garcia's insurance network.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P005"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if Robert Garcia's insurance covers a general check-up."}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P005", "service": "general check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are organized, cautious. \"search_patients for user Sarah Brown using email sarah.brown426@email.com to retrieve patient ID and insurance details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "name": "Sarah Brown", "email": "sarah.brown426@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are direct, patient, independent, confident. Search_patients for John Johnson using email john.johnson941@email.com to retrieve patient ID and details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are polite, direct. Search_patients to retrieve insurance details for patient Emily Brown.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, direct, optimistic, confident. First, use the search_patients task with the parameter email=sarah.brown426@email.com to verify the identity of the user and retrieve the patient ID. Once you have confirmed the patient ID, proceed to book an appointment by using the book_appointment task with the parameters patientID=PID123, doctorID=D456, timeSlot=10:00AM, date=2023-10-15 to schedule an appointment. This ensures that Sarah Brown's identity is verified before confirming her appointment with the doctor, maintaining a seamless and secure booking process in the healthcare system.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patientID": "PID123", "doctorID": "D456", "timeSlot": "10:00AM", "date": "2023-10-15"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are optimistic, direct. Search_patients with user ID (emily.brown290@email.com) to retrieve patient information and verify authorization status. Then, think to determine if Emily Brown is eligible for a routine check-up based on retrieved patient information. This process is crucial to ensure that Emily receives the necessary healthcare services and that her insurance covers the routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Emily Brown is authorized to access patient information and check her insurance status for routine check-up eligibility."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are polite, cautious, independent, logical. Search for patient with user_id \"U001\" to retrieve medical history and existing conditions using search_patients tool.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "U001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are direct, organized. First, search for patient Sarah Brown using email sarah.brown753@email.com to retrieve her patient ID and insurance details. Once you have verified Sarah Brown's insurance details for coverage eligibility, proceed to book an appointment with a general practitioner for her, ensuring it fits within the available hours. This process is essential to ensure that Sarah receives timely medical attention and that her insurance covers the necessary services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P025", "doctor_type": "general practitioner", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are confident, optimistic, organized. Search_patients for Michael Miller using email michael.miller534@email.com to retrieve his patient ID and healthcare details. Then, think to verify Michael Miller's insurance details using the patient ID obtained from search_patients. This process ensures that all necessary information is accurate and up-to-date before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the patient ID obtained from search_patients to verify Michael Miller's insurance details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are cautious, flexible, organized, polite. Use book_appointment tool to schedule a routine check-up with the chosen doctor for Robert Garcia, ensuring it fits within available hours.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "appointment_type": "routine check-up", "doctor_id": "D123", "preferred_time": "2023-11-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are flexible, patient, cautious, confident. Search_patients with email \"david.miller979@email.com\" to retrieve patient ID and details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are flexible, confident, optimistic. \"search_patients for Emily Davis's recent visit history to identify any follow-up appointments needed\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Emily Davis", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, cautious, flexible, logical. First, verify insurance coverage for Robert Brown with policy ID XYZ123 before proceeding with booking. Once the insurance coverage is confirmed, book an appointment for Robert Brown with Dr. Smith for a routine check-up on the earliest available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown", "policy_id": "XYZ123"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are optimistic, confident. First, search_patients for Emily Jones using email emily.jones379@email.com to retrieve her patient ID. Once you have her patient ID, book_appointment for Emily Jones using patient ID P123 for Dr. Smith (doctor ID: D001) on available slot S456. After booking the appointment, check healthcare details for Emily Jones to confirm insurance pre-authorization status for slot S456, ensuring a smooth visit without any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "D001", "slot_id": "S456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are direct, patient. First, use `search_patients` to find the patient profile for Sarah Smith using her email sarah.smith521@email.com. Once you have confirmed her details, proceed to use `book_appointment` to schedule a routine check-up for Sarah Smith with Dr. John Doe (ID: D345) on October 25, 2023, at 10:00 AM. This sequence ensures that Sarah's appointment is accurately scheduled based on her existing profile information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.smith521@email.com", "doctor_id": "D345", "date": "2023-10-25", "time": "10:00", "appointment_type": "routine check-up", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, organized, flexible, direct. Search_patients using email maria.smith554@email.com to retrieve patient ID and any existing appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, organized. First, search_patients with patient ID to retrieve Robert Johnson's current healthcare provider and doctor's available hours. Once you have confirmed the available hours, proceed to book_appointment for Robert Johnson with doctor ID D234 during these hours, ensuring that his insurance coverage is valid. This will facilitate a seamless scheduling process and ensure that Robert receives timely medical attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P024"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor_id": "D234", "time": "10:00 AM", "insurance_valid": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, confident, logical. First, search_patients for Maria Smith using email maria.smith554@email.com to retrieve patient ID. Once you have the patient ID, use it to check insurance status and verify coverage to ensure that Maria Smith can proceed with her healthcare services without any issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search_patients result to verify Maria Smith's insurance coverage."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are patient, polite, direct, cautious. Search_patients for Maria Smith using email maria.smith554@email.com to retrieve patient ID and insurance details. Once the patient ID is obtained, check healthcare details for the patient ID retrieved to verify insurance coverage status. This will ensure that the insurance is active and valid before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013"}
            ),
            Action(
                name="think",
                kwargs={"note": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"note": "Check healthcare details for the retrieved patient ID to verify insurance coverage status."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are optimistic, polite. Search for Sarah Brown's patient profile using email sarah.brown753@email.com to verify her insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are optimistic, confident. First, search for Sarah Brown in the patient database to retrieve her patient ID and medical history. Next, verify Sarah Brown's insurance information to ensure coverage for her upcoming appointments. Finally, check Sarah Brown's medical history to ensure no conflicts with potential medications or treatments, as she prepares for her consultation with Dr. John Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "name": "Sarah Brown"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "name": "Sarah Brown", "action": "retrieve_medical_history"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "name": "Sarah Brown", "action": "verify_insurance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, independent. First, search_patients for Maria Smith using email maria.smith554@email.com to retrieve patient ID and insurance details. Next, think to check if Maria Smith's insurance is verified for appointment booking, ensuring that all necessary information is in place for a seamless process. Finally, book_appointment for Maria Smith using patient ID with the available slot for a routine check-up, facilitating her access to necessary healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Maria Smith's insurance is verified for appointment booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "appointment_type": "routine check-up", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are confident, direct, flexible. Search for patient Maria Smith using her email maria.smith256@email.com to retrieve her patient ID and verify authorization status. Once you have confirmed her authorization, check healthcare details for the obtained patient ID to confirm her insurance status and coverage details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Maria Smith's patient ID and authorization status from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If Maria Smith is authorized, proceed to check her healthcare details for insurance status and coverage."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are organized, direct, flexible. Use search_patients to retrieve available doctors for a routine check-up within the next week. Then, use think to decide on the best available doctor for Maria Smith's routine check-up based on retrieved information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "purpose": "routine check-up", "time_frame": "next week"}
            ),
            Action(
                name="think",
                kwargs={"criteria": "best available doctor for routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are logical, direct, flexible, patient. \"Search_patients to retrieve Lisa Jones' patient ID and medical history for authorization check.\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are organized, direct, independent, polite. Search_patients with name \"Sarah Miller\" to retrieve patient ID and authorization status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Miller", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are direct, independent. book_appointment for patient ID with preferred doctor on available date and time, ensuring insurance is verified",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are confident, cautious. Search_patient with email sarah.smith521@email.com to retrieve patient ID and insurance details. Then, think to determine the urgency of Sarah's healthcare needs based on her medical history and current symptoms. This will help prioritize her case and ensure she receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are optimistic, patient, direct, cautious. Search_patients for Sarah Brown using email sarah.brown426@email.com to retrieve patient ID and insurance details. Then, think to verify if Sarah Brown has valid insurance coverage for booking an appointment. This process is crucial to ensure that Sarah can proceed with scheduling her upcoming consultation without any financial concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Sarah Brown has valid insurance coverage for booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are confident, logical. Search for patient information using the email john.johnson627@email.com to verify identity and authorization status. Once verified, proceed to verify insurance details for user John Johnson to ensure coverage for upcoming appointments. After confirming insurance coverage, book an appointment with Dr. Smith for John Johnson on the earliest available date and time, ensuring it fits within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the identity and authorization status of John Johnson using the provided email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once verified, proceed to check insurance details for John Johnson."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm insurance coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_name": "Dr. Smith", "patient_email": "john.johnson627@email.com", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are optimistic, organized, patient. First, check insurance details for Sarah Williams to ensure coverage for her upcoming appointment. Once coverage is confirmed, book an appointment for Sarah Williams with Dr. John Smith (ID: D123) on the next available slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Sarah Williams to ensure coverage for her upcoming appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams", "doctor_id": "D123", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, flexible, organized, polite. Book_appointment for Sarah Miller with Dr. John Doe (Doctor ID: D123) for a cardiology check-up during the available slot on 2023-11-10 at 10:00 AM.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_id": "D123", "specialty": "cardiology", "appointment_date": "2023-11-10", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are logical, independent, organized. Search for patient record using email david.brown214@email.com to verify identity and retrieve patient ID. Then, search_patients using patient ID to retrieve David Brown's insurance details for verification. Finally, think to confirm if David Brown's insurance is verified and active for appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P020"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if David Brown's insurance is active and valid for appointment booking."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, direct, organized. First, search for patient's insurance details for Michael Miller using search_patients with email michael.miller534@email.com and verify insurance coverage. Once you have confirmed that Michael Miller's insurance covers appointments with Dr. Smith, proceed to search for available appointment slots with Dr. Smith using book_appointment with patient email michael.miller534@email.com and desired date October 25th, 2023. Finally, book an appointment for Michael Miller with Dr. Smith on October 25th, 2023, at 10 AM using book_appointment with patient email michael.miller534@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"email": "michael.miller534@email.com", "doctor": "Dr. Smith", "date": "2023-10-25"}
            ),
            Action(
                name="book_appointment",
                kwargs={"email": "michael.miller534@email.com", "doctor": "Dr. Smith", "date": "2023-10-25", "time": "10:00", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are independent, organized, confident, logical. First, search for patient information for David Brown using the think tool with email david.brown214@email.com to verify authorization. Once verified, schedule an appointment for David Brown with Dr. Smith using the book_appointment tool, ensuring insurance verification and availability.",
        actions=[
            Action(
                name="think",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.brown214@email.com", "doctor_name": "Dr. Smith", "insurance_verified": true, "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are polite, flexible, patient. Book_appointment for patient ID with cardiologist Dr. Smith on 2023-11-15, ensuring availability.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "doctor": "Dr. Smith", "specialty": "cardiology", "date": "2023-11-15"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are direct, confident, patient, flexible. First, search for patient records for Emily Jones using email emily.jones379@email.com to verify insurance details. Once the insurance verification is complete, book an appointment for Emily Jones with Dr. Smith during available hours on 2023-11-15 at 10:00 AM. Ensure that all steps are followed to maintain a seamless experience for the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.jones379@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are optimistic, direct, cautious. First, use `search_patients` to find the patient ID for David Brown using his email david.brown214@email.com. Next, use `think` to verify the insurance information for the retrieved patient ID to ensure everything is in order. Finally, use `book_appointment` to schedule a routine check-up for David Brown with Dr. Smith, making sure that the insurance verification is complete before proceeding.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P020"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are direct, patient, organized. Search for the earliest available appointment slot with Dr. John Doe that fits within Sarah Smith's schedule preferences.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Identify Sarah Smith's schedule preferences and Dr. John Doe's available hours."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check for the earliest available appointment slot that fits within Sarah Smith's schedule preferences."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance verification is completed before booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "doctor_name": "Dr. John Doe", "patient_name": "Sarah Smith", "appointment_time": "earliest_available_slot"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are patient, organized, cautious, polite. Search for patient information for Maria Miller using search_patients with email maria.miller855@email.com",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are independent, logical, polite. Search_patients with parameters: insurance_status=\"active\", patient_name=\"Maria Johnson\" to verify insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"insurance_status": "active", "patient_name": "Maria Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are direct, logical. Use search_patients to find Michael Miller's patient profile using email michael.miller534@email.com and verify authorization. Then, use think to verify insurance coverage for a cardiology appointment for Michael Miller.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com", "user_id": "P048"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance coverage for a cardiology appointment", "patient_email": "michael.miller534@email.com", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are optimistic, flexible, cautious, confident. First, search_patients with email \"emily.garcia400@email.com\" to verify patient information and authorization status. Once verified, proceed to search_patients to check insurance details for Emily Garcia to verify coverage. After confirming her insurance coverage, book_appointment for Emily Garcia with provider ID \"D123\" for a routine check-up, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com", "check_insurance": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.garcia400@email.com", "provider_id": "D123", "appointment_type": "routine check-up", "insurance_verified": true, "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are polite, optimistic, patient, flexible. Search for patients with the name \"John Johnson\" to retrieve patient ID and verify current healthcare details. Once you have the patient ID, search_patients using this ID to check for any existing appointments or recent visits. This will ensure that you have the most up-to-date information before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Johnson", "user_id": "P031"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P031", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are logical, organized. \"search_patients for patient with email maria.johnson759@email.com to verify insurance details\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are flexible, direct, polite, organized. Search_patients using Emily Brown's email (emily.brown290@email.com) to verify her patient record and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com", "user_id": "P021"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, logical, organized, patient. Use think to review Maria Smith's patient history and determine the need for a follow-up appointment.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P013", "task": "review Maria Smith's patient history to determine the need for a follow-up appointment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are flexible, polite, cautious, organized. Search_patients for David Williams to retrieve patient ID and medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "David Williams", "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, direct. Search for patient information using user ID robert.johnson741@email.com with proper authorization to confirm if Robert Johnson's insurance covers the appointment with Dr. Smith. Once confirmed, proceed to book an appointment for Robert Johnson with Dr. Smith for a routine check-up at the earliest available slot. This ensures that the patient is financially prepared for the consultation, streamlining the process and enhancing patient care efficiency.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P024", "email": "robert.johnson741@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P024", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are direct, confident, organized, cautious. Verify insurance coverage for Robert Johnson for a routine check-up with Dr. Emily Smith before booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P027", "patient_name": "Robert Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for Robert Johnson before booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are direct, flexible, optimistic, logical. Determine the type of appointment Emily Garcia needs (routine or emergency). Retrieve available appointment slots for Dr. Smith for routine visits. Schedule a routine appointment for Emily Garcia with Dr. Smith on an available date and time.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Determine the type of appointment Emily Garcia needs."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Emily Garcia needs a routine appointment."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve available appointment slots for Dr. Smith for routine visits."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Schedule a routine appointment for Emily Garcia with Dr. Smith on an available date and time."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine", "date": "2023-11-10", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are optimistic, cautious, independent. Search_patients for patient name \"Emily Jones\" to retrieve patient ID and verification of insurance coverage. Then, think to verify insurance status is active and up-to-date for the patient ID retrieved. Once confirmed, proceed to book_appointment for the patient ID with Dr. Smith (doctor ID D123) on the next available date and time slot. This ensures that Emily Jones can receive timely medical attention with her insurance coverage verified, maintaining a smooth and efficient healthcare process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Jones", "user_id": "P007"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status is active and up-to-date for the retrieved patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "D123", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are optimistic, logical, polite, flexible. First, use \"search_patients\" with user email \"maria.smith256@email.com\" to verify patient information and retrieve patient ID. Once you have the patient ID, use \"book_appointment\" to check the doctor's available hours for a routine check-up with the retrieved patient ID and Maria Smith's preferred date. After confirming the available hours and verifying Maria's insurance, use \"book_appointment\" to schedule a routine visit during the available hours for the patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.smith256@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "appointment_type": "routine_checkup", "preferred_date": "2023-11-15"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "appointment_type": "routine_checkup", "appointment_time": "confirmed_available_time", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are direct, organized. First, search for patient John Johnson using email john.johnson699@email.com to retrieve his patient ID and healthcare details. Once you have obtained the patient ID, proceed to verify the insurance details associated with this ID to ensure coverage is active and up-to-date. This will facilitate a smooth process for any upcoming medical appointments or treatments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are flexible, independent. Use `search_patients` to find patient John Johnson using email john.johnson699@email.com, and then use `think` to check if John Johnson's insurance is verified for Dr. Smith’s services. Once you have confirmed the insurance verification, proceed to use `book_appointment` to schedule a routine appointment for John Johnson with Dr. Smith on the next available slot. This ensures that John receives timely healthcare services without any insurance-related delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if John Johnson's insurance is verified for Dr. Smith's services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson699@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are organized, logical, direct, cautious. Use `search_patients` tool to check Emily Brown's medical history for any pre-existing conditions that may require special consideration.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are polite, patient. Use search_patients to find patient information for Lisa Jones with email lisa.jones889@email.com, ensuring proper authorization. Then, use think to determine the most suitable doctor for Lisa Jones considering her medical history and current needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
            Action(
                name="think",
                kwargs={"patient_email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are polite, flexible, organized, optimistic. First, perform the Search_patients task with parameters: user_id=\"emily.garcia400@email.com\", query=\"Emily Garcia\" to retrieve her patient ID and insurance details. Once you have the insurance details, proceed to the Think task with parameters: context=\"insurance details retrieved\", task=\"verify insurance information for Emily Garcia\" to ensure her insurance is valid and up-to-date. After confirming the insurance details, execute the Book_appointment task with parameters: patient_id=\"P12345\", doctor_id=\"D67890\", appointment_time=\"2023-11-15 10:00\", insurance_verified=True for Emily Garcia, ensuring her appointment is successfully scheduled.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "query": "Emily Garcia"}
            ),
            Action(
                name="think",
                kwargs={"context": "insurance details retrieved", "task": "verify insurance information for Emily Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor_id": "D67890", "appointment_time": "2023-11-15 10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are logical, optimistic, direct. First, use the search_patients tool with user ID emily.brown290@email.com to retrieve Emily Brown's patient profile and insurance details. This will allow you to confirm her insurance information and ensure that all records are up-to-date. Next, use the search_patients tool to verify Emily Brown’s insurance eligibility for a general consultation with provider ID P987. This step is crucial to ensure that her insurance plan covers the consultation, thereby avoiding any unexpected costs for the patient. Once her eligibility is confirmed, you can proceed with the necessary arrangements for her healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "emily.brown290@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "emily.brown290@email.com", "provider_id": "P987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are direct, polite, organized, cautious. Please search for patients with the email robert.brown731@email.com to retrieve their patient ID and insurance details. Once you have obtained the patient ID, think to verify the insurance details for patient ID P001 to ensure there is adequate coverage for any upcoming appointments. This is crucial to avoid any potential issues with insurance claims and to ensure the patient can receive necessary medical care without delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once I retrieve the patient ID for Robert Brown, I will verify the insurance details for patient ID P001 to ensure adequate coverage."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are organized, flexible, direct. \"search_patients for Sarah Miller using user ID sarah.miller381@email.com to retrieve patient details and verify authorization\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are flexible, direct, confident. Search_patients for Sarah Williams using email sarah.williams602@email.com to retrieve patient ID and medical history, then think to verify insurance coverage details for Sarah Williams before confirming the appointment. This ensures that all necessary information is in place to facilitate a smooth booking process and avoid any potential issues with insurance claims.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage details for Sarah Williams using the retrieved patient ID and medical history."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, flexible. Book an appointment for John Johnson with Doctor D456 on 2023-11-15 at 10:00 AM, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P031", "patient_id": "P031", "doctor_id": "D456", "appointment_date": "2023-11-15", "appointment_time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are polite, patient, direct, cautious. Use the Book_appointment tool to schedule an appointment for Maria Johnson with Dr. Smith (Doctor ID: D456) on a weekday between 9 am and 5 pm. Then, use the think tool to check if the scheduled appointment falls within Dr. Smith's available hours to ensure it aligns with his schedule.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P023", "patient_name": "Maria Johnson", "doctor_id": "D456", "date": "2023-10-18", "time": "10:00"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if the appointment for Maria Johnson with Dr. Smith on 2023-10-18 at 10:00 falls within Dr. Smith's available hours."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are organized, cautious, logical. Use think to review Sarah Davis's current healthcare needs and insurance details, then use think to identify available doctors who match Sarah Davis's healthcare needs based on her medical history. This will ensure that Sarah receives the most appropriate care tailored to her specific health requirements and insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P047", "patient_name": "Sarah Davis"}
            ),
            Action(
                name="think",
                kwargs={"task": "review Sarah Davis's current healthcare needs and insurance details"}
            ),
            Action(
                name="think",
                kwargs={"task": "identify available doctors who match Sarah Davis's healthcare needs based on her medical history"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are logical, cautious, independent. Search_patients with email sarah.miller381@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
]
