"""
Generated tasks for healthcare domain.
Generated at: 2025-08-04T00:38:48.222850
Total tasks: 550
"""

from tau_types import Task, Action

TASKS_TRAIN = [
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are cautious, logical, patient. Search_patients for Michael Miller using email michael.miller534@email.com to retrieve patient information and verify authorization. Then, think to check if Michael Miller has valid insurance on file for appointment booking purposes. This will ensure that any appointments made are covered under his insurance plan, avoiding unexpected costs and ensuring a smooth scheduling process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com", "user_id": "P048"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Michael Miller has valid insurance on file for appointment booking purposes."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are independent, flexible, logical, cautious. search_patients using Robert Jones's email (robert.jones332@email.com) to verify his patient ID and retrieve his healthcare details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are confident, polite, cautious, direct. Use `search_patients` to find patient information for Sarah Brown (sarah.brown753@email.com) to verify authorization. Once authorization is confirmed, use `think` to verify Sarah Brown's insurance details for coverage eligibility before proceeding with any further actions. This ensures that all necessary information is accurate and up-to-date, which is crucial for providing seamless healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify Sarah Brown's insurance details for coverage eligibility"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are independent, organized, confident. Book an appointment for Emily Brown with Dr. Smith on the earliest available date, ensuring insurance verification is complete. Then, search for any recent test results or medical records that Emily Brown may need to discuss during the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine", "insurance_verified": true}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown", "records_type": "test_results"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are logical, flexible, confident. First, search_patients with email \"sarah.brown426@email.com\" to retrieve patient ID and authorization status. Once you have obtained Sarah Brown's patient ID, use it to search_patients and check her insurance details to verify her coverage status. This ensures that all necessary information is gathered before proceeding with any further actions related to her healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P039", "info_type": "insurance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are confident, patient, direct. Search_patients with name \"Sarah Smith\" and email \"sarah.smith521@email.com\" to retrieve patient ID and insurance details. Think to verify insurance details for patient ID retrieved for validity and coverage. Book_appointment for patient ID retrieved with doctor ID found, within available hours, verifying insurance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Smith", "email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details for validity and coverage for the retrieved patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P033", "doctor_id": "retrieved_doctor_id", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are polite, logical. First, search for patient records using user email robert.johnson741@email.com to verify patient ID and insurance details. Next, think to determine if Robert Johnson needs an appointment based on recent healthcare visits and current health status. Finally, if no emergency is detected, book an appointment for Robert Johnson with doctor ID D567 during available hours, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Robert Johnson needs an appointment based on recent healthcare visits and current health status, ensuring no emergency is detected."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor_id": "D567", "insurance_verified": true, "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are flexible, direct. First, search_patients with email 'maria.smith256@email.com' to retrieve current insurance details. Then, think to verify if Maria Smith's insurance is valid for booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Maria Smith's insurance is valid for booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are independent, polite, logical. First, use the \"search_patients\" task with the parameters: {name: \"Maria Miller\", email: \"maria.miller855@email.com\"} to locate the patient in the system. Once you have retrieved the patient ID, proceed with the \"think\" task to verify the insurance details for the retrieved patient ID. This will ensure that Maria Miller's insurance is valid and can cover her upcoming medical needs. After confirming the insurance details, you can coordinate with the medical team to facilitate further actions, such as booking necessary appointments or treatments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Maria Miller", "email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, cautious, logical, organized. First, use the search_patients task with the parameter email=david.williams693@email.com to retrieve the patient ID and medical history. Then, use the search_patients task with the retrieved patientID to verify the insurance details. Once the insurance is verified, proceed to book an appointment for a routine check-up by using the book_appointment task with the parameters: patientID, doctorID, date, time, and insurance_verified=true. This sequence ensures that all necessary patient information and insurance verification are in place before scheduling the appointment, thereby streamlining the healthcare process efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patientID": "retrieved_patient_id"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patientID": "retrieved_patient_id", "doctorID": "D001", "date": "2023-11-15", "time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are flexible, logical. Search_patients with patient ID to check John's medical history and current health conditions. Then, think to identify any urgent health concerns for John Johnson based on his medical history. If any urgent issues are found, proceed to book_appointment for an emergency visit to ensure timely medical intervention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P031"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P031", "patient_id": "P031", "appointment_type": "emergency"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are optimistic, organized, confident. Use the `search_patients` tool to find patient Robert Johnson by email (robert.johnson197@email.com) to verify his identity and retrieve his patient ID. Then, use this patient ID to retrieve Robert Johnson's insurance details to ensure coverage before proceeding.",
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
        user_id="P018",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are optimistic, logical, independent. First, search_patients(email=\"sarah.williams602@email.com\") to retrieve Sarah Williams' patient ID and authorization status. Once you have confirmed her authorization, proceed to search_patients(patient_id=\"P12345\") to confirm her insurance status and eligibility. After verifying these details, book_appointment(patient_id=\"P12345\", doctor_id=\"D6789\", appointment_type=\"routine\", date=\"2023-11-15\", time=\"10:00 AM\") to ensure she has a scheduled appointment with Dr. Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P018"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P018", "doctor_id": "D6789", "appointment_type": "routine", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are flexible, logical, independent, optimistic. Use search_patients to retrieve Emily Brown's patient ID using her email emily.brown290@email.com.",
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
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are cautious, organized, flexible. Search for patient records for Maria Smith using email maria.smith554@email.com to verify existing information. Once you have accessed her records, retrieve Maria Smith's insurance details to confirm the validity of her insurance. This process is crucial to ensure that Maria Smith's insurance coverage is up-to-date and valid for her upcoming routine check-up with Dr. Johnson.",
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
        user_id="P021",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are direct, patient, optimistic, flexible. First, check healthcare details for patient Emily Brown to confirm insurance information. Once confirmed, book an appointment for a routine check-up with Dr. John Smith for Emily Brown during an available slot, ensuring insurance verification is complete. Finally, search for Emily Brown's recent medical history to prepare for the upcoming appointment, ensuring all necessary information is ready for Dr. Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown", "doctor_name": "Dr. John Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, independent, patient, polite. Search_patients with email sarah.williams853@email.com to retrieve patient ID and insurance information.",
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
        user_id="P039",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are polite, patient, independent. \"Search_patients with email sarah.brown426@email.com to retrieve patient ID and insurance details\"",
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
        user_id="P031",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are patient, polite, logical, independent. First, search for patients with the email john.johnson627@email.com to retrieve John Johnson's patient ID and medical history. Once you have this information, check the healthcare details for John Johnson to verify his insurance status and coverage, ensuring that his insurance covers the upcoming cardiology consultation appointment with Dr. Smith.",
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
        user_id="P006",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are organized, cautious. First, search_patients for user David Williams using email david.williams693@email.com to verify existing patient records. Next, think to determine if David Williams requires a routine visit or an emergency appointment based on his recent health inquiries. If it's determined that a routine visit is needed, book_appointment for David Williams with Dr. Smith on the next available slot, ensuring it's within office hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P006", "name": "David Williams", "email": "david.williams693@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "patient_name": "David Williams", "doctor_name": "Dr. Smith", "appointment_type": "routine", "time_slot": "next_available_within_office_hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are confident, patient. First, think to verify authorization for accessing Lisa Williams' patient information to ensure compliance with privacy regulations. Once authorization is confirmed, search_patients with email \"lisa.williams792@email.com\" to retrieve her patient ID and healthcare details. Next, check healthcare details for the retrieved patient ID to review her insurance information and eligibility.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are organized, logical. First, search_patients for Maria Johnson to verify patient ID and insurance status to ensure her records are up-to-date. Next, confirm that Maria Johnson's insurance is verified for upcoming appointments to avoid any billing issues. Finally, book_appointment for Maria Johnson with Dr. Smith during available hours for a routine check-up, ensuring her healthcare needs are met efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P023", "patient_name": "Maria Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P023", "patient_id": "P023", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are confident, direct, patient, polite. Search for patient records using email: sarah.brown426@email.com to verify patient ID and insurance details. Think to verify if Sarah Brown's insurance covers routine check-ups with Dr. Smith. Once confirmed, book an appointment for the patient ID with Dr. Smith on the next available slot, ensuring insurance coverage is confirmed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Brown's insurance details to check coverage for routine check-ups with Dr. Smith."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, confident, organized, cautious. Search for patient records using email robert.brown624@email.com to retrieve patient ID and insurance details. Then, think to verify if Robert Brown's insurance is valid and covers the required healthcare services. This is crucial to ensure that Robert Brown can receive the necessary treatment without any financial or administrative issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Robert Brown's insurance is valid and covers the required healthcare services."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are optimistic, flexible, cautious. First, search_patients with email \"sarah.smith521@email.com\" to retrieve the patient ID and authorization status. Once you have the patient ID, proceed to search_patients with the patient ID to check the insurance verification status. This process is crucial to ensure that Sarah Smith's insurance details are up-to-date, allowing us to proceed with scheduling her upcoming medical appointments without any delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are flexible, logical, independent, patient. Search for Robert Jones's insurance provider details to verify coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, organized, independent. Use search_patients to find Sarah Smith's patient profile using her email sarah.smith521@email.com. Once you have located her profile, use think to identify if Sarah Smith requires an emergency appointment based on her symptoms. If an emergency appointment is necessary, use book_appointment to schedule an appointment with Dr. Jones for Sarah Smith at 10:00 AM on the next available date, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"patient_profile": "Sarah Smith's profile data here"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P033", "doctor": "Dr. Jones", "time": "10:00 AM", "date": "Next available date", "insurance_verified": true, "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are patient, organized, cautious, direct. Search_patients for Lisa Williams using email lisa.williams792@email.com to verify patient ID and insurance status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are patient, confident, polite, independent. First, search_patients for any existing appointments for John Johnson to avoid scheduling conflicts. After confirming his schedule is clear, proceed to search_patients for available doctors specializing in general practice with open slots this week, ensuring that John Johnson can be accommodated without any overlap.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "John Johnson", "user_id": "P029"}
            ),
            Action(
                name="search_patients",
                kwargs={"specialty": "general practice", "availability": "this week", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are confident, logical. Search_patients to find David Brown's medical history and current healthcare needs. Then, think to determine the most suitable doctor for David Brown's current healthcare needs, considering his medical history and the specialties of available doctors at the clinic.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P020", "patient_name": "David Brown"}
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
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are flexible, confident. Search for patient Emily Davis using her email emily.davis525@email.com to retrieve her patient ID and current healthcare details, and then book an appointment for Emily Davis with Dr. Smith, a general medicine specialist, on the earliest available date this week. This will ensure that Emily receives timely medical attention and that all her healthcare information is up-to-date for the consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor_name": "Dr. Smith", "specialty": "general medicine", "date": "earliest_available_date_this_week", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are organized, optimistic. First, use the `search_patients` tool with parameters: { \"email\": \"sarah.davis118@email.com\" } to retrieve Sarah Davis's patient ID. Once you have the patient ID, use the `search_patients` tool with parameters: { \"patient_id\": \"P12345\" } to retrieve Sarah Davis's medical history. After reviewing the medical history, use the `think` tool with parameters: { \"task\": \"Assess Sarah Davis's medical history for any urgent healthcare needs.\" } to determine if there are any immediate concerns that need to be addressed. If no urgent needs are identified, proceed to schedule a routine check-up by using the `book_appointment` tool with parameters: { \"patient_id\": \"P12345\", \"doctor_id\": \"D67890\", \"appointment_type\": \"routine\", \"preferred_date\": \"2023-11-15\", \"time_slot\": \"10:00 AM\" }.",
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
                kwargs={"task": "Assess Sarah Davis's medical history for any urgent healthcare needs."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P047", "doctor_id": "D67890", "appointment_type": "routine", "preferred_date": "2023-11-15", "time_slot": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are logical, cautious, direct. First, search_patients to find patient records for Maria Smith using her email (maria.smith256@email.com) to ensure all her information is up-to-date. Once her records are verified, book_appointment for Maria Smith with Dr. Johnson (ID: D567) for a routine check-up, ensuring insurance is verified to avoid any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Maria Smith", "doctor_id": "D567", "appointment_type": "routine check-up", "insurance_verified": true, "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, optimistic, logical, direct. Search for patient records for Emily Garcia using email emily.garcia400@email.com to verify her information and insurance details. Then, think to confirm Emily Garcia's insurance details and ensure they are up-to-date for appointment booking. This process is essential to guarantee that the insurance information is accurate and current before proceeding with any medical appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com", "user_id": "P036"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details for Emily Garcia to ensure they are up-to-date before booking any appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are organized, independent, optimistic. Search for patient details using email david.miller979@email.com to verify identity and retrieve patient ID. Use the patient ID to check insurance details and verify coverage for upcoming appointments. Book an appointment for patient ID with Dr. Smith on the available date, ensuring it is during his working hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the patient ID to check insurance details and verify coverage for upcoming appointments."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure Dr. Smith has available working hours for the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P028", "doctor_name": "Dr. Smith", "date": "next_available_date", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, cautious. Search for patient details using email sarah.brown426@email.com to verify identity and retrieve patient ID.",
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
        user_id="P017",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are patient, optimistic, confident, direct. Search_patients for Robert Brown with email robert.brown624@email.com to verify existing patient record. Once verified, think to choose the best available doctor for Robert Brown based on availability and specialty, ensuring he receives the most appropriate care for his needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Brown", "email": "robert.brown624@email.com"}
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
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are flexible, independent, cautious. First, search_patients to verify insurance details for Sarah Brown before proceeding with appointment booking. Once her insurance details are confirmed, book_appointment with doctor ID D123 for Sarah Brown during available hours. Ensure that the insurance verification is complete to avoid any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P039", "patient_name": "Sarah Brown", "doctor_id": "D123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are confident, cautious. Use search_patients to find Sarah Williams (user ID: sarah.williams602) to retrieve her patient ID and healthcare details. Then, use think to determine the urgency of Sarah Williams' healthcare needs based on her symptoms and history. Finally, use book_appointment to schedule a routine appointment for Sarah Williams with Dr. Johnson at an available time slot, ensuring that her healthcare needs are addressed promptly and efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P018", "patient_id": "P018", "symptoms": "chronic headache, fatigue", "history": "mild hypertension, no recent hospitalizations"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "patient_id": "P018", "doctor_name": "Dr. Johnson", "appointment_type": "routine", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are confident, cautious. Search_patients for Sarah Brown using email sarah.brown753@email.com to retrieve patient ID and authorized information. Then, think to confirm the need for a cardiology appointment for Sarah Brown given her recent health check results.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
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
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, organized. First, search for Maria Johnson using her email maria.johnson759@email.com to retrieve her patient ID and verify her authorization. Once verified, proceed to search for Maria Johnson's previous visit history to check for any special notes or instructions that might be relevant for her upcoming appointment. Finally, book an appointment for Maria Johnson with Dr. Smith for a routine checkup, ensuring the time falls within Dr. Smith's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023", "authorization": true}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023", "visit_history": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor": "Dr. Smith", "appointment_type": "routine checkup", "time": "2023-11-15T10:00:00", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are patient, organized, cautious, confident. \"Search for patient Maria Johnson using email maria.johnson759@email.com to retrieve her patient ID and insurance details\"",
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
        user_id="P017",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are independent, flexible, patient. Search for patient information for Robert Brown using email robert.brown624@email.com to verify identity and authorization.",
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
        user_id="P039",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are confident, optimistic, cautious, independent. \"book_appointment for Sarah Brown with doctor_id=D123 on preferred date and time, considering doctor's available hours and emergency prioritization\"",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Brown", "doctor_id": "D123", "preferred_date": "2023-11-15", "preferred_time": "10:00", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are logical, polite, cautious, direct. Use book_appointment to schedule a routine check-up for Robert Brown with Dr. Smith on 2023-11-10 at 10:00 AM, ensuring insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P003", "patient_name": "Robert Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P003", "patient_id": "P003", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-10", "appointment_time": "10:00 AM", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are patient, polite. Use search_patients to find Sarah Williams' patient ID by searching with her email (sarah.williams602@email.com). Once you have the patient ID, use search_patients to retrieve Sarah Williams' medical history based on patient ID for doctor's review, ensuring that Dr. Smith has all necessary information before the appointment. After reviewing the medical history, use book_appointment to schedule a routine check-up for Sarah Williams with Dr. Smith on an available date and time, ensuring it fits within the doctor's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P018"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P018", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are confident, cautious, polite, logical. search_patients for Emily Garcia using email emily.garcia400@email.com to retrieve patient ID and verify insurance status",
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
        user_id="P018",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are direct, organized, patient, polite. Use the think tool to determine the type of healthcare service Sarah Williams needs based on her recent symptoms. Once you have identified the necessary service, use the search_patients tool to verify Sarah Williams' insurance details to ensure she is eligible for the required service. This will help streamline the process and ensure that Sarah receives timely care without any insurance-related delays.",
        actions=[
            Action(
                name="think",
                kwargs={"symptoms": "Sarah Williams' recent symptoms"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams", "email": "david.brown214@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, logical, polite. First, use `search_patients` to find patient details for David Brown with email david.brown214@email.com. Next, use `think` to verify David Brown's insurance details from his patient profile to ensure that his coverage is valid for the services at our clinic. Finally, use `book_appointment` to schedule an appointment with Dr. Smith for David Brown during available hours, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "David Brown", "email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify insurance details for David Brown to ensure coverage is valid for clinic services"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "David Brown", "doctor_name": "Dr. Smith", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, flexible, optimistic. search_patients(email=\"emily.garcia400@email.com\") to retrieve Emily Garcia's patient ID and insurance details",
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
        user_id="P036",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are polite, patient. First, search for patient details using search_patients with email emily.garcia400@email.com to verify identity and retrieve patient ID. Once you have the patient ID, verify insurance details for Emily Garcia using think to ensure coverage eligibility before booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance details for patient ID retrieved from previous step"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, direct. First, use the Search_patients tool to find available doctors for Michael Brown's requested specialty to ensure we have options if Dr. Smith is unavailable. Next, search for available appointment slots for Dr. Smith (doctor ID D001) based on Michael Brown's schedule to find a suitable time for his consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"specialty": "requested_specialty"}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D001", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are independent, cautious, logical. First, search for patient information for Sarah Davis using email sarah.davis118@email.com to verify her insurance details. Once her insurance coverage is confirmed and eligibility is ensured, proceed to book an appointment for Sarah Davis with Dr. Emily Johnson on the next available date during her office hours. This ensures a seamless process for Sarah Davis to receive timely medical care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.davis118@email.com", "doctor_name": "Dr. Emily Johnson", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are logical, flexible, confident. Check Sarah Williams' insurance details to verify coverage for upcoming appointments, and once confirmed, book an appointment for Sarah Williams with Dr. John Smith on the selected available slot. Ensure that the appointment aligns with her coverage terms to avoid any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Williams' insurance coverage details for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams", "doctor_name": "Dr. John Smith", "appointment_time": "2023-10-15T10:00:00", "verify_insurance": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are cautious, logical, organized, patient. Think to determine the best available appointment slot for Sarah Williams based on her schedule and Dr. Smith's availability.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are confident, flexible, optimistic, logical. First, search for patient Sarah Davis using her email sarah.davis118@email.com to verify her identity and retrieve her patient ID. Once her identity is confirmed, proceed to search_patients to find Sarah Davis' insurance details and verify coverage for healthcare services, ensuring that her routine check-up is covered. Finally, book_appointment for Sarah Davis with Dr. Smith (Doctor ID: D001) for a routine check-up on her preferred date, ensuring it aligns with the doctor’s available hours and her insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P047", "user_id": "P047"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P047", "doctor_id": "D001", "appointment_type": "routine check-up", "preferred_date": "2023-11-15", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are organized, logical, flexible, cautious. Search for patient information for user Sarah Miller (sarah.miller381@email.com) to verify insurance status.",
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
        user_id="P047",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are flexible, independent, confident, cautious. First, search_patients with the name \"Sarah Davis\" and email \"sarah.davis118@email.com\" to retrieve her patient ID and healthcare details. Next, think to determine if there are any upcoming appointments for the patient ID retrieved. Finally, search_patients to verify the insurance status for the patient ID retrieved to ensure coverage for any upcoming appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Davis", "email": "sarah.davis118@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P047", "detail": "upcoming_appointments"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P047", "detail": "insurance_status"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are polite, patient, organized. \"search_patients for user Sarah Brown (sarah.brown426@email.com) to retrieve patient ID and insurance details\"",
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
        user_id="P005",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are organized, confident, direct. First, search_patients with query \"Robert Garcia\" to verify patient ID and access authorization. Once verified, proceed to search_patients with patient ID \"RG592\" to retrieve available medical history and records. After confirming the patient's medical history, book_appointment with patient ID \"RG592\" and doctor ID \"D123\" for a routine check-up during available hours. Ensure that the appointment aligns with the patient's health needs and the doctor's availability.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"query": "Robert Garcia", "user_id": "P005"}
            ),
            Action(
                name="search_patients",
                kwargs={"query": "RG592", "user_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor_id": "D123", "appointment_type": "routine check-up", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are confident, optimistic. First, search for patient records for Maria Smith using email maria.smith256@email.com to verify existing healthcare details. Once you have confirmed her healthcare details, proceed to check her insurance status and eligibility to ensure she can receive the necessary medical services.",
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
        user_id="P029",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, confident, optimistic. First, search for patient John Johnson using email john.johnson699@email.com to verify his identity and retrieve his medical history. Once his identity is confirmed and medical history is retrieved, proceed to check his healthcare details to confirm insurance coverage and eligibility. This will ensure that all necessary information is accurate and up-to-date before any further actions are taken.",
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
        user_id="P026",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are flexible, logical, direct. search_patients(name=\"Robert Jones\") to retrieve patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are cautious, direct. Search for patient Sarah Williams using email sarah.williams853@email.com to retrieve patient ID. Once you have the patient ID, verify insurance details for the patient to ensure coverage is active and valid before proceeding with any further healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from search results to verify insurance details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are cautious, optimistic, patient, logical. Use the search_patients tool to locate the patient record for David Williams based on his email (david.williams693@email.com). Once you have confirmed his patient ID, use the book_appointment tool to schedule an appointment for patient ID P001 with Dr. Smith on the next available date, ensuring that his insurance is verified. This will help streamline the process and ensure that David receives the necessary care without any administrative delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P006", "doctor": "Dr. Smith", "date": "next_available", "insurance_verified": true, "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are logical, flexible. Use the think tool to verify the urgency of Sarah Williams's appointment request to determine if it qualifies as an emergency. Once the urgency is assessed, use the book_appointment tool to schedule an appointment for Sarah Williams with her preferred doctor during available hours, ensuring insurance verification is complete. This sequence ensures that Sarah receives timely medical attention while maintaining compliance with insurance requirements.",
        actions=[
            Action(
                name="think",
                kwargs={"appointment_request": "Sarah Williams's appointment request"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams", "doctor_name": "Dr. Smith", "appointment_time": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are optimistic, direct. Use book_appointment to schedule a routine check-up for Sarah Brown with Dr. Smith at 10:00 AM on March 15, ensuring the doctor's availability.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P039", "patient_name": "Sarah Brown", "doctor_name": "Dr. Smith", "appointment_time": "10:00 AM", "appointment_date": "2024-03-15", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are flexible, optimistic, direct, polite. Use `search_patients` tool to retrieve Michael Miller's patient ID using the email michael.miller534@email.com.",
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
        user_id="P033",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are confident, polite, direct. search_patients for patient ID using email sarah.smith521@email.com",
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
        user_id="P017",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are confident, independent, patient. First, search_patients with email \"robert.brown624@email.com\" to retrieve user information and verify authorization. Once you have confirmed his authorization, proceed to search_patients with the user ID obtained from the previous step to confirm his insurance status. After verifying that Robert Brown's insurance is active, book_appointment for the user ID obtained from the previous step with Dr. Smith at the verified time slot of 10:00 AM on March 15th.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P017"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "doctor": "Dr. Smith", "time": "10:00 AM", "date": "2023-03-15"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are logical, cautious, optimistic. First, search for patients with the email sarah.miller381@email.com to verify patient authorization. Once authorization is confirmed, proceed to book an appointment with doctor ID D123 for patient Sarah Miller, ensuring that her insurance status is verified. The appointment should be for a routine check-up on November 15, 2023, at 10:00 AM.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D123", "patient_email": "sarah.miller381@email.com", "appointment_date": "2023-11-15", "appointment_time": "10:00", "appointment_type": "routine check-up", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are patient, optimistic, cautious, flexible. First, search_patients for Emily Garcia with email emily.garcia400@email.com to retrieve her patient ID and insurance information. Once you have the necessary details, proceed to search_patients for available doctors who can address Emily Garcia's healthcare needs, prioritizing specialists if her records indicate a need for specialized care. After identifying a suitable doctor, book_appointment for Emily Garcia, ensuring the appointment is scheduled during the doctor's available hours and that her insurance coverage is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Emily Garcia", "email": "emily.garcia400@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "available doctors", "specialization": "specialist", "insurance": "retrieved_insurance_info"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor_id": "identified_doctor_id", "time": "doctor_available_time", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are organized, logical, confident. Search for patient information for Lisa Jones using email lisa.jones889@email.com to verify identity and retrieve patient ID. Then, check healthcare details for the retrieved patient ID to ensure insurance is up-to-date and verify eligibility for booking appointments. This process is crucial to ensure that Lisa Jones can seamlessly book an appointment with Dr. Smith, with all insurance details confirmed and in place, providing a smooth and efficient healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID for Lisa Jones from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming patient ID is retrieved, check healthcare details for insurance verification."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify eligibility for booking appointments based on insurance status."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are logical, flexible, optimistic, direct. First, search for patient John Johnson's details using his email john.johnson627@email.com to verify his identity. Once verified, proceed to search for available doctors who accept John Johnson's insurance plan for a general consultation to ensure he receives the appropriate care. After identifying suitable doctors, book an appointment for John Johnson with Doctor ID D345 for a general consultation at the earliest available time, ensuring a seamless and efficient healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify patient identity and insurance details for John Johnson."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available doctors who accept John Johnson's insurance plan."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Identify suitable doctors for a general consultation."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P031", "doctor_id": "D345", "appointment_type": "general consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are optimistic, confident, patient. Search_Patients with email robert.garcia592@email.com to retrieve patient ID and insurance details, then think about Robert Garcia's insurance coverage and verify eligibility for appointment booking. This process is crucial to ensure that Robert Garcia can smoothly schedule his necessary healthcare appointments without any financial or administrative hurdles.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details for Robert Garcia to verify his insurance coverage for appointment eligibility."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are direct, confident, cautious. First, think to confirm Maria Smith's insurance details are up-to-date for appointment booking, as this is crucial for processing her visit seamlessly. Once verified, proceed to book an appointment for Maria Smith with Dr. John Doe during available hours, ensuring that the insurance verification is complete to avoid any issues on the day of the appointment.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to verify Maria Smith's insurance details before booking her appointment with Dr. John Doe."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Maria Smith's insurance details are verified and up-to-date. Now, I can proceed to book the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith", "doctor_name": "Dr. John Doe", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are cautious, polite. \"search_patients with email sarah.miller381@email.com to verify patient status and retrieve patient ID\"",
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
        user_id="P006",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are optimistic, independent, logical, cautious. Search for patient records using email david.williams693@email.com to verify patient ID and insurance details, then proceed to book an appointment for David Williams with Dr. Smith on the next available slot, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P006", "doctor_name": "Dr. Smith", "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are confident, logical. First, search_patients with email michael.brown235@email.com to retrieve the patient ID and authorization status. Once you have obtained the patient ID, think to verify the insurance information for the retrieved patient ID. After confirming the insurance details, proceed to book_appointment for the patient with Dr. Smith during available hours. This ensures that the patient has a valid insurance plan before scheduling a consultation, streamlining the process and enhancing patient care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and authorization status from the search_patients response."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance information for the retrieved patient ID to ensure valid coverage."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P016", "doctor": "Dr. Smith", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, polite, independent. Use `search_patients` to find patient information for Sarah Brown with email sarah.brown753@email.com to verify her insurance status. Once her insurance is verified, use `book_appointment` to schedule a routine check-up for Sarah Brown with Dr. Smith, ensuring it aligns with the doctor's available hours. Finally, use `book_appointment` to send an appointment confirmation to Sarah Brown via email sarah.brown753@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown753@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P025"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown753@email.com", "confirmation": true, "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, patient, organized, flexible. First, check if John Johnson needs a follow-up appointment using the tool think. If a follow-up is necessary, proceed to book a follow-up appointment for John Johnson with Dr. Smith at 11:00 AM on 2023-11-22 using the book_appointment tool. This sequence ensures that John receives the necessary continuity of care after his initial visit.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P037", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_time": "11:00 AM", "appointment_date": "2023-11-22"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are organized, confident, logical. Book_appointment for Maria Smith with Dr. Johnson (Doctor ID: D345) on next available slot.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "doctor_id": "D345", "patient_name": "Maria Smith", "patient_email": "maria.smith256@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, patient, logical. First, search for patient Maria Smith using email maria.smith256@email.com to verify her identity. Once her identity is confirmed, check healthcare details for patient Maria Smith to confirm insurance status and coverage. This will ensure that all necessary information is accurate and up-to-date before proceeding with any further actions related to her healthcare needs.",
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
        user_id="P050",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are patient, cautious, flexible, polite. First, search for patient information using the user email lisa.jones889@email.com to verify identity and retrieve the patient ID. Once you have the patient ID, check the healthcare details to verify insurance status and coverage. After confirming the insurance coverage, proceed to book an appointment for the patient ID with Dr. Smith (doctor ID D123) on an available date and time. Ensure that the insurance is verified before finalizing the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P050", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00", "insurance_verified": true, "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are optimistic, logical. Use search_patients to find patient ID for Sarah Brown using email sarah.brown426@email.com, and then use think to verify insurance for the patient ID retrieved for Sarah Brown. This ensures that her insurance details are up-to-date and verified before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P039", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are confident, organized, polite, independent. First, search for patient Lisa Jones using email lisa.jones889@email.com to verify her details and retrieve her patient ID. Once you have confirmed her identity and obtained her patient ID, proceed to verify her insurance details to ensure she is eligible for booking an appointment. This process is crucial to maintain efficient scheduling and ensure that all appointments are covered by the patient's insurance plan.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are organized, flexible. Use the search_patients tool with Sarah Williams' email to retrieve her patient ID and any existing medical records. Next, use the search_patients tool with Sarah Williams' patient ID to verify her insurance coverage details. Finally, use the think tool to determine Sarah Williams' eligibility for booking an appointment based on current insurance information. This process ensures that Sarah Williams' appointment with Dr. Roberts is scheduled accurately and aligns with her insurance coverage, providing a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P018"}
            ),
            Action(
                name="think",
                kwargs={"insurance_details": "retrieved_insurance_details"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are organized, confident, patient, logical. First, search_patients for Sarah Brown with email sarah.brown426@email.com to verify patient information, ensuring all her details are up-to-date in the system. Next, search_patients for insurance details related to Sarah Brown to verify coverage, confirming her insurance plan is valid and active for upcoming appointments. Finally, search_patients for available doctors with specialty in general practice for Sarah Brown, so she can receive the appropriate care and guidance for her health needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Brown", "email": "sarah.brown426@email.com", "user_id": "P039"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Brown", "insurance_details": true, "user_id": "P039"}
            ),
            Action(
                name="search_patients",
                kwargs={"specialty": "general practice", "available_doctors": true, "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are independent, flexible, optimistic. Search for patient Maria Smith using email maria.smith256@email.com to retrieve her medical records. Then, check the insurance status for the patient ID associated with Maria Smith to ensure coverage for her upcoming appointments. Once the insurance is verified, proceed to book an appointment for Maria Smith with Dr. John Doe at the earliest available morning slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "user_id": "P019"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results to check insurance status."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status for the patient ID associated with Maria Smith."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once insurance is verified, find the earliest available morning slot for Dr. John Doe."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "doctor": "Dr. John Doe", "time_slot": "earliest_morning_slot", "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are confident, patient. Search for patient information using email john.johnson627@email.com to verify identity and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are cautious, direct. Search_patients with name \"Sarah Miller\" to retrieve patient ID and verify insurance details. Think to assess Sarah Miller's insurance coverage for general consultation to ensure it is valid and covers the necessary services. Book_appointment for patient ID retrieved with Dr. Smith for a general consultation on an available date and time, ensuring it aligns with Sarah Miller's insurance coverage and availability.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Miller", "user_id": "P046"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Sarah Miller to verify coverage for general consultation."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P046", "doctor": "Dr. Smith", "appointment_type": "general consultation", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are organized, direct, independent. First, search for patient information for Robert Johnson using email robert.johnson197@email.com with proper authorization to ensure all his details are up-to-date. Once verified, book an appointment for Robert Johnson with Dr. Smith on the next available date. This sequence ensures that Robert's information is current before scheduling, facilitating a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson197@email.com", "doctor_name": "Dr. Smith", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, polite, logical. First, search for patient information using the email maria.smith256@email.com to retrieve Maria Smith's patient ID and authorization status. Once you have the patient ID, verify the insurance details to confirm her coverage. After confirming the insurance, check available appointment slots for Dr. Johnson using Maria Smith's patient ID and her preferred date range to ensure a suitable time is available.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com", "user_id": "P019"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and authorization status for Maria Smith using her email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once the patient ID is obtained, verify Maria Smith's insurance details to confirm her coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After confirming insurance coverage, check available appointment slots for Dr. Johnson using Maria Smith's patient ID and her preferred date range."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are logical, cautious, direct. Search for patient information using patient ID P001 to verify Sarah Williams' insurance coverage, and then think to confirm Sarah Williams' insurance coverage details and eligibility for upcoming appointments. Once the insurance coverage is verified and eligibility is confirmed, proceed to book an appointment with Dr. John Smith (doctor ID D101) for Sarah Williams on October 15th, 2023, at 10:00 AM. This sequence ensures that all necessary insurance validations are completed before scheduling, maintaining efficiency and accuracy in patient care management.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Williams' insurance coverage and eligibility for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "doctor_id": "D101", "date": "2023-10-15", "time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are polite, logical, optimistic. Use `search_patients` to retrieve patient information for Sarah Williams using email sarah.williams602@email.com and verify authorization. Once authorization is confirmed, use `search_patients` to verify Sarah Williams' insurance details and eligibility for booking appointments. After confirming her eligibility, use `book_appointment` to schedule an appointment for Sarah Williams with Dr. John Smith on the next available slot, ensuring it is within the doctor's working hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018", "verify": "authorization"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018", "verify": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.williams602@email.com", "doctor_name": "Dr. John Smith", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are patient, polite, independent. Search_patients for Emily Jones using email emily.jones379@email.com to retrieve patient ID and medical history. Then, book_appointment for the retrieved patient ID with Dr. Smith for a routine check-up, ensuring it falls within available hours. This sequence is crucial to ensure Emily Jones is scheduled for her necessary routine health evaluation with Dr. Smith, leveraging the retrieved information for a seamless booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are polite, cautious, logical, optimistic. First, search for patient information for John Johnson using email john.johnson699@email.com to verify authorization. Once authorization is confirmed, proceed to book an appointment for John Johnson with Dr. Smith for a routine check-up on the next available date. This will ensure that all necessary information is up-to-date and that the appointment booking process is seamless and efficient for both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are organized, logical, direct. Retrieve patient profile for Lisa Jones using search_patients with email lisa.jones889@email.com to verify eligibility for services. Once eligibility is confirmed, verify insurance coverage for Lisa Jones using think to confirm eligibility before booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify eligibility for services for Lisa Jones"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance coverage for Lisa Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, flexible, logical. First, search_patients with email sarah.williams853@email.com to retrieve patient ID and healthcare details. Once you have obtained Sarah Williams' patient ID, check healthcare details for the patient ID retrieved to verify insurance status and coverage. After confirming her insurance details, search healthcare items to find available doctors specializing in general practice within Sarah Williams' network.",
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
        user_id="P037",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, independent, confident, logical. First, search for patient John Johnson's insurance details using user ID U12345 to verify coverage for future appointments. Once coverage is confirmed, search_patients for available doctors with the specialty in general medicine and working hours compatible with John Johnson's schedule. Finally, book_appointment for John Johnson with doctor D45678 on the preferred date and time, ensuring it falls within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_id": "P037"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "specialty": "general medicine", "availability": "compatible with John Johnson's schedule"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_id": "P037", "doctor_id": "D45678", "date": "2023-11-15", "time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, organized, optimistic. Search for patient records using user email sarah.brown753@email.com to verify patient identity and retrieve patient ID. Once you have the patient ID, check healthcare details to confirm insurance information and coverage. After confirming the insurance details, book an appointment for the patient with Dr. John Doe on the earliest available date, ensuring that the appointment aligns with the verified insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from the search results to verify insurance details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details using the patient ID to confirm insurance information and coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After confirming insurance details, book an appointment for the patient with Dr. John Doe on the earliest available date."}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_name": "Dr. John Doe", "patient_id": "P025", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are flexible, confident, optimistic, polite. First, check healthcare details for Emily Garcia's insurance verification status to ensure coverage. Once confirmed, proceed to book an appointment for Emily Garcia with doctor ID D101 on 2023-11-15 at 10:00 AM. This ensures that her insurance details are up-to-date before scheduling her visit, providing a smooth and efficient healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia", "doctor_id": "D101", "appointment_date": "2023-11-15", "appointment_time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, cautious, optimistic. First, search for patient information of Emily Jones using email emily.jones379@email.com to ensure you have the correct and most recent data. Once confirmed, verify her insurance details to ensure they are up-to-date, as this is crucial before scheduling any medical appointments.",
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
        user_id="P013",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are confident, logical, independent, direct. Search for patient details for Maria Smith (maria.smith554@email.com) to verify identity and insurance information.",
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
        user_id="P018",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are logical, polite. First, use `search_patients` to verify if Sarah Williams has any pending lab results that need to be discussed during her visit. Once confirmed, proceed to use `book_appointment` to schedule an appointment for Sarah Williams with Dr. Smith on the earliest available slot for a routine check-up. This ensures that any outstanding lab results can be reviewed and discussed with Dr. Smith during her appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams", "check_pending_lab_results": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "earliest_available_slot": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are polite, organized, direct, optimistic. First, search for patient information for Robert Johnson using email robert.johnson741@email.com with proper authorization to ensure his records are up-to-date. Once you have verified his information, proceed to book an appointment for Robert Johnson with Dr. Smith on the earliest available date for a routine check-up.",
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
        user_id="P036",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are organized, logical, polite, flexible. Use search_patients to find patient information for user Emily Garcia using email emily.garcia400@email.com and obtain patient ID.",
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
        user_id="P036",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, organized, polite, independent. \"search_patients\" with parameters: {user_email: \"emily.garcia400@email.com\", search_criteria: {name: \"John Doe\", date_of_birth: \"1985-06-15\"}}",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "emily.garcia400@email.com", "search_criteria": {"name": "John Doe", "date_of_birth": "1985-06-15"}}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, polite. First, use the \"search_patients\" tool to find the patient record for Maria Johnson using her email (maria.johnson759@email.com) and verify authorization to access her healthcare details. Once authorization is confirmed, proceed to use the \"search_patients\" tool to check Maria Johnson's medical history for any recent visits or ongoing treatments. Based on this information, use the \"think\" tool to prioritize Maria Johnson's appointment by assessing the urgency of her medical needs and aligning it with available slots with her preferred doctor.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023", "action": "check_medical_history"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P023", "action": "prioritize_appointment", "criteria": "urgency_of_medical_needs"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are cautious, organized, independent, direct. First, use search_patients with patient email 'maria.smith554@email.com' to retrieve Maria Smith's healthcare details. Once you have accessed her details, use think to determine if Maria Smith's insurance is verified for appointment booking. This sequence ensures that Maria Smith's insurance status is confirmed before proceeding with any appointment scheduling, maintaining an efficient and organized workflow in the healthcare setting.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Determine if Maria Smith's insurance is verified for appointment booking"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, polite, logical. First, search for patient records for Maria Johnson using email maria.johnson759@email.com to verify insurance details. Once you have confirmed her insurance coverage, proceed to verify Maria Johnson's insurance coverage specifically for cardiology appointments. After ensuring that her insurance covers cardiology, book an appointment with Dr. Smith for Maria Johnson on the available date, making sure all insurance details are confirmed beforehand.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Maria Johnson to ensure coverage for cardiology appointments."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm Maria Johnson's insurance covers cardiology appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.johnson759@email.com", "doctor_name": "Dr. Smith", "specialty": "cardiology", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are confident, patient, cautious. Use think to determine if Sarah Brown requires an emergency appointment or a routine check-up based on her recent healthcare interactions. Once you have determined that a routine check-up is appropriate, use book_appointment to schedule a routine check-up for Sarah Brown with Dr. Smith (Doctor ID: D567) using her patient ID, ensuring insurance verification.",
        actions=[
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_id": "D567", "appointment_type": "routine check-up", "insurance_verified": true, "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are patient, polite. Use \"search_patients\" to find patient profile for John Johnson using email john.johnson699@email.com.",
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
        user_id="P014",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are direct, logical. Use the tool \"search_patients\" to find patient Robert Brown using email robert.brown731@email.com to verify his insurance details. Once you have confirmed that his insurance is valid, use the tool \"think\" to determine Robert Brown's eligibility for a routine check-up based on the insurance verification results. This ensures that Robert Brown can receive the necessary healthcare services without any issues related to coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"insurance_status": "valid"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, patient. Book_appointment for Sarah Williams with Dr. John Smith on the earliest available slot for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams", "doctor_name": "Dr. John Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are organized, patient, flexible. Use search_patients to find Robert Brown using his email robert.brown551@email.com and retrieve his patient ID.",
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
        user_id="P001",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are polite, optimistic, direct. First, search for Sarah Williams (sarah.williams853@email.com) in the patient database to verify her account details using search_patients. Once her account is verified, proceed to book a general check-up appointment for Sarah Williams with Dr. Smith during available hours using book_appointment with Sarah's patient ID and Dr. Smith's schedule ID. This ensures that Sarah receives timely care and maintains her health routine effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams853@email.com", "user_id": "P001"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P001", "doctor_schedule_id": "D001", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are independent, optimistic. Search for patient records for Emily Garcia using email emily.garcia400@email.com to verify insurance details.",
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
        user_id="P017",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are patient, flexible, optimistic. Use the `search_patients` tool to find available appointment slots for Dr. Emily Hart (doctor ID: D102) for user Robert Brown. Once you have identified available slots, use the `book_appointment` tool to schedule an appointment for Robert Brown with Dr. Emily Hart on October 15th at 10:00 AM. After booking the appointment, use the `book_appointment` tool to send an appointment confirmation to Robert Brown via email.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D102", "user_id": "P017"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D102", "patient_name": "Robert Brown", "appointment_date": "2023-10-15", "appointment_time": "10:00", "user_id": "P017"}
            ),
            Action(
                name="book_appointment",
                kwargs={"email": "robert.brown@email.com", "message": "Your appointment with Dr. Emily Hart is confirmed for October 15th at 10:00 AM.", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are direct, confident. book_appointment: schedule appointment for Sarah Williams with doctor ID D123 on available date and time",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Williams", "doctor_id": "D123", "user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are direct, organized, flexible, polite. Use book_appointment tool to schedule a routine appointment with Dr. Smith for Robert Garcia on 2023-11-15 at 10:00 AM.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "appointment_type": "routine", "contact_email": "maria.johnson759@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are flexible, logical, cautious. Begin by searching for patient records using the search_patients tool with the parameter user_email=maria.johnson759@email.com to obtain the patient_id. Once you have the patient_id, use the think tool to determine the most suitable doctor for Maria Johnson's healthcare needs, ensuring the doctor is available for an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.johnson759@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P023", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are flexible, patient. Search for patient Robert Johnson using email robert.johnson741@email.com to retrieve patient ID and insurance details. Then, check insurance status for Robert Johnson using the retrieved patient ID to ensure coverage for healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are logical, independent, optimistic, patient. First, search_patients to find Robert Brown's patient ID using the email robert.brown731@email.com. Once you have the patient ID, check healthcare details for the patient ID found from search_patients to verify his insurance status. After confirming his insurance, search healthcare items to find available doctors for a routine check-up, ensuring that the selected doctor can accommodate Robert Brown's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are independent, flexible, optimistic. Search for patient records with the name \"Robert Garcia\" to verify identity and retrieve patient ID.",
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
        user_id="P019",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are direct, optimistic, polite, patient. First, search for the patient profile with the email maria.smith256@email.com using the search_patients tool to retrieve the patient ID and check the authorization status. Once you have confirmed that the patient is authorized, verify the insurance details for the retrieved patient ID to confirm coverage. This step is crucial to ensure that the patient can proceed with booking an appointment without any financial issues.",
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
        user_id="P046",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are direct, cautious, polite, logical. Search for patient information for Sarah Miller (sarah.miller381@email.com) to verify insurance status",
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
        user_id="P037",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are cautious, optimistic. Search for patient John Johnson's profile using email john.johnson941@email.com to verify insurance details.",
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
        user_id="P036",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, optimistic, independent. First, search_patients using email emily.garcia400@email.com to retrieve Emily Garcia's patient ID and medical history. Once you have confirmed her identity and gathered the necessary information, proceed to check healthcare details for patient Emily Garcia (emily.garcia400@email.com) to verify her insurance coverage. This will ensure that her upcoming medical appointments and treatments are covered, providing a seamless healthcare experience.",
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
        user_id="P025",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are direct, organized, confident. Book an appointment for Sarah Brown with Dr. John Smith at 2 PM on 12th March 2023.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "doctor_name": "Dr. John Smith", "appointment_time": "2023-03-12T14:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are organized, direct. Search for patient details using search_patients with email maria.miller855@email.com to verify patient information.",
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
        user_id="P032",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are polite, optimistic. First, search for patient Emily Davis using the email emily.davis525@email.com and verify authorization to access her records. Once access is confirmed, verify her insurance details to ensure coverage for the selected doctor and appointment type. Finally, book an appointment for Emily Davis with the general practitioner, making sure it fits within the doctor's available hours and is covered by her insurance.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization to access Emily Davis's records."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once authorization is confirmed, proceed to verify Emily's insurance details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure the insurance covers the selected doctor and appointment type."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After verifying insurance, check the doctor's available hours for booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.davis525@email.com", "doctor_type": "general practitioner", "appointment_type": "routine", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, cautious, confident, organized. First, search_patients for user Sarah Williams with email sarah.williams602@email.com to retrieve patient ID and authorization status. Then, think to determine if Sarah Williams has proper authorization to access patient records. This process ensures compliance with healthcare privacy regulations by verifying that only authorized personnel can access sensitive patient information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "name": "Sarah Williams", "email": "sarah.williams602@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Sarah Williams has proper authorization to access patient records based on the retrieved patient ID and authorization status."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are optimistic, confident. First, search_patients for Emily Brown using email emily.brown290@email.com to retrieve her patient ID and details. Once you have confirmed her patient ID and insurance details, book_appointment for Emily Brown with Dr. John Smith on October 17th at 10:00 AM, ensuring insurance has been verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P021", "doctor": "Dr. John Smith", "date": "2023-10-17", "time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are polite, direct, logical. Retrieve Michael Brown's patient ID using search_patients with email michael.brown235@email.com.",
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
        user_id="P046",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are flexible, organized. Search for patient information for Sarah Miller using email sarah.miller381@email.com to verify insurance details.",
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
        user_id="P050",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are patient, confident, independent, polite. book_appointment for patient ID obtained earlier with Dr. Johnson for an emergency visit, prioritizing over routine appointments",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "doctor_name": "Dr. Johnson", "appointment_type": "emergency"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, patient, cautious, organized. Search_patients for Robert Jones using email robert.jones332@email.com to retrieve patient ID. Then, think to determine available appointment types based on Robert Jones' insurance coverage. This will ensure that you can verify the types of appointments Robert is eligible for under his current plan, allowing you to proceed with booking an appropriate appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com"}
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
        user_id="P029",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are polite, patient. Think to determine the need for an appointment based on John Johnson's healthcare details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P029", "patient_name": "John Johnson"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "patient_id": "P029", "appointment_type": "routine", "insurance_verified": true, "preferred_time": "2023-11-10T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, confident. Search for patient records using the email robert.brown551@email.com to verify identity and retrieve patient ID. Then, search for available doctors who specialize in general practice and are compatible with the patient's insurance. Once a suitable doctor is found, book an appointment for the patient ID with the selected doctor during their available hours for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search_patients response and verify insurance compatibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Select a suitable doctor from the search_doctors response based on availability."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P003", "doctor_id": "selected_doctor_id", "appointment_type": "routine check-up", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are confident, patient, independent. Use the think tool to determine the best available appointment slot with Dr. Smith for a routine check-up, ensuring it aligns with the clinic's schedule and patient preferences. Once the slot is identified, use the book_appointment tool to schedule an appointment for Lisa Williams with Dr. Smith on 2023-10-20 at 10:00 AM, ensuring all necessary details are accurately recorded in the system.",
        actions=[
            Action(
                name="think",
                kwargs={"task": "Determine the best available appointment slot with Dr. Smith for a routine check-up, ensuring it aligns with the clinic's schedule and patient preferences."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams", "doctor_name": "Dr. Smith", "appointment_date": "2023-10-20", "appointment_time": "10:00 AM", "appointment_type": "routine check-up", "patient_email": "emily.garcia400@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are cautious, polite, flexible. First, search_patients for Robert Brown using email robert.brown731@email.com to retrieve his patient ID. Once you have the patient ID, book_appointment for Robert Brown for a routine check-up with doctor ID D456 at an available time slot. After booking the appointment, verify insurance details for Robert Brown to confirm coverage for the routine check-up with doctor ID D456.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P014", "doctor_id": "D456", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are direct, polite, patient. First, search for patient details using user ID emily.garcia400@email.com to retrieve medical history and insurance information. Then, proceed to search_patients for Emily Garcia's insurance provider to verify coverage for cardiology consultations. Once coverage is confirmed, book_appointment with Dr. Smith (cardiologist) for Emily Garcia during her available hours next week.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "email": "emily.garcia400@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "insurance_provider": "Emily Garcia's Insurance Provider"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "doctor": "Dr. Smith", "specialty": "cardiology", "patient_email": "emily.garcia400@email.com", "date": "next week", "time": "available hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are cautious, flexible, optimistic. First, search for the patient record for Maria Smith using her email maria.smith554@email.com to verify her patient details. Once verified, proceed to check Maria Smith's insurance details to ensure there are no issues before booking her appointment. Finally, book an appointment with Dr. John Doe for a routine check-up, ensuring it falls within the doctor's available hours and is convenient for Maria.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Smith's patient details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Maria Smith's insurance details to ensure there are no issues."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.smith554@email.com", "doctor_name": "Dr. John Doe", "appointment_type": "routine check-up", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are flexible, cautious. First, search for patient information using user ID robert.johnson197@email.com to verify authorization for accessing healthcare details. Once authorization is confirmed, check healthcare details for user Robert Johnson to confirm insurance status and eligibility for appointment booking. After validating his insurance, book an appointment for Robert Johnson with Dr. Smith at 10:00 AM on November 15, 2023.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "robert.johnson197@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P027", "doctor": "Dr. Smith", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, patient, optimistic. Book_appointment for Sarah Smith with her healthcare provider during available hours, ensuring insurance verification",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith", "appointment_type": "routine", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are organized, confident, polite. Search for patient information using email sarah.brown426@email.com to retrieve patient ID and insurance details.",
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
        user_id="P017",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are organized, flexible, polite, optimistic. First, search_patients with email robert.brown624@email.com to retrieve patient ID and healthcare details. Once you have obtained this information, think to assess if Robert Brown requires an emergency appointment based on his healthcare details. If the criteria for an emergency appointment are met, proceed to book_appointment for Robert Brown with doctor ID D456 during available hours. If no emergency is determined but a follow-up visit is required, ensure to book_appointment for Robert Brown with doctor ID D456 for a follow-up visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P017", "doctor_id": "D456", "appointment_type": "emergency", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are flexible, direct, logical. Search_patients for Sarah Brown using email sarah.brown753@email.com to retrieve patient ID and healthcare details.",
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
        user_id="P014",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are independent, logical, confident. Use `search_patients` to find the patient record for Robert Brown with email robert.brown731@email.com. Then, use `think` to verify insurance details for Robert Brown to ensure coverage for upcoming appointments. Finally, use `book_appointment` to schedule a routine check-up for Robert Brown with Dr. Smith on the available date and time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance details for Robert Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, polite. First, search_patients for any existing appointments for Emily Jones to avoid scheduling conflicts. Once you have confirmed there are no conflicts, book_appointment for Emily Jones with Dr. Smith at 10:00 AM on the next available date, ensuring it aligns with Dr. Smith’s available hours. This will help maintain an efficient schedule and provide Emily with timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Emily Jones", "user_id": "P007"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Emily Jones", "doctor_name": "Dr. Smith", "appointment_time": "10:00 AM", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are polite, optimistic, flexible. First, Search_patients with parameters: user_email=robert.johnson197@email.com to retrieve patient ID and insurance status. Next, Think to confirm authorization to access Robert Johnson's healthcare information based on retrieved patient details. Once authorization is confirmed, Book_appointment with parameters: patient_ID=P123, doctor_ID=D456, appointment_type=routine, date=2023-11-15, time=10:00 AM if within doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Maria Smith is authorized to access Robert Johnson's healthcare information based on the retrieved patient details."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_ID": "P123", "doctor_ID": "D456", "appointment_type": "routine", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are confident, direct, polite. First, search_patients with name 'Lisa Jones' to verify patient ID and insurance details. Once you have confirmed her identity, proceed to search_patients to confirm Lisa Jones' insurance provider and coverage details. Finally, book_appointment for Lisa Jones with Dr. Smith during available hours for a routine check-up, ensuring that her insurance coverage is valid for the scheduled appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones", "user_id": "P050"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones", "user_id": "P050"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P050", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are logical, confident, optimistic, flexible. First, think about Robert Brown's healthcare needs and verify his insurance details to ensure coverage for upcoming medical services. Next, search_patients for Robert Brown using email robert.brown731@email.com to access his medical records and review any past recommendations for screenings or vaccinations. Finally, book_appointment for Robert Brown at a clinic for any recommended screenings or vaccinations, ensuring insurance verification aligns with the services scheduled.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance details to ensure coverage for upcoming medical services."}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Robert Brown's medical records for any past recommendations for screenings or vaccinations."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_email": "robert.brown731@email.com", "service": "recommended screenings or vaccinations", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, logical, direct. Search for patient using email michael.miller534@email.com to retrieve user ID and insurance information. Once you have the patient ID, verify the insurance details. If the insurance is verified, proceed to book an appointment for the patient with the appropriate doctor ID during available hours. Ensure each step is completed accurately to maintain efficient patient care and scheduling.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "doctor_id": "D123", "appointment_time": "2023-10-15T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are cautious, optimistic. Search for patient information for Sarah Miller (sarah.miller381@email.com) to verify insurance details, and then think to confirm insurance coverage for Sarah Miller's upcoming appointment. Once insurance coverage is confirmed, proceed to book an appointment for Sarah Miller with Dr. Smith on 2023-11-15 at 10:00 AM. Ensure all steps are completed accurately to facilitate a seamless healthcare experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "email": "sarah.miller381@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Sarah Miller before proceeding with appointment booking."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm insurance coverage for Sarah Miller's upcoming appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_email": "sarah.miller381@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are confident, logical, polite, flexible. Use search_patients to find Robert Garcia's patient record using email robert.garcia592@email.com. Once his record is located, use book_appointment to schedule an appointment for Robert Garcia with Dr. Smith on 2023-11-15 at 10:00 AM, ensuring insurance verification is complete. This process is crucial to ensure Robert receives timely care and that all administrative details are handled efficiently.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.garcia592@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "insurance_verified": true, "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are optimistic, logical, independent. First, think to check insurance status for patient Emily Jones with insurance ID required to ensure coverage for her upcoming healthcare needs. Next, think to confirm if Emily Jones requires any specific medical tests before her appointment with Dr. Smith, as this will help in preparing a comprehensive care plan. Finally, book_appointment for patient Emily Jones with Dr. Smith on an available date and time, ensuring that any necessary lab tests are scheduled beforehand to provide Dr. Smith with all relevant information during the consultation.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Check insurance status for Emily Jones to ensure coverage for her healthcare needs."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm if Emily Jones requires any specific medical tests before her appointment with Dr. Smith."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Book an appointment for Emily Jones with Dr. Smith, ensuring any necessary lab tests are scheduled beforehand."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones", "doctor_name": "Dr. Smith", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are optimistic, independent. Search for patient records of Michael Brown using email michael.brown235@email.com to verify his identity and retrieve patient ID.",
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
        user_id="P029",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are logical, independent, confident, patient. \"think about the insurance requirements for scheduling an appointment for John Johnson\"",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Consider the insurance requirements for scheduling an appointment for John Johnson."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are patient, organized. First, search_patients for insurance details of user Maria Smith to verify coverage. Once coverage is confirmed, book_appointment for an emergency visit for Maria Smith with Dr. John Doe, prioritizing it over routine visits to ensure she receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith", "doctor_name": "Dr. John Doe", "appointment_type": "emergency"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are organized, patient, independent. Search for patient records for John Johnson using the email john.johnson699@email.com to verify identity. Once verified, check healthcare details for patient John Johnson to confirm insurance coverage status. This will ensure that all necessary information is accurate and up-to-date before proceeding with any further actions related to his healthcare management.",
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
        user_id="P028",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, organized, flexible, cautious. Use the search_patients tool to find patient details for David Miller using email david.miller979@email.com. Once you have confirmed his details, use the book_appointment tool to schedule a routine check-up for David Miller with Dr. Smith, ensuring the appointment is within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
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
        user_id="P046",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are logical, patient. Search for patient Sarah Miller using email sarah.miller381@email.com to retrieve her patient ID.",
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
        user_id="P005",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are organized, direct, flexible, polite. First, execute the \"search_patients\" task with the parameter {\"email\": \"robert.garcia592@email.com\"} to retrieve the patient profile and authorization status. Once you have obtained the patient ID from the search results, proceed to \"think\" to verify the insurance details associated with this patient ID. This ensures that the patient is covered for the services required. After confirming the insurance details, if everything is in order, move on to book an appointment by using the \"book_appointment\" task with parameters {\"patient_id\": \"obtained_patient_id\", \"doctor_id\": \"selected_doctor_id\", \"appointment_type\": \"general check-up\", \"preferred_date\": \"next available date\"}. Ensure that the appointment falls within the doctor's available hours to provide a seamless experience for both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor_id": "selected_doctor_id", "appointment_type": "general check-up", "preferred_date": "next available date"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are confident, flexible, cautious. Search_patient with patient_email 'sarah.miller381@email.com' to retrieve patient ID and authorization status. Once you have the patient ID, use it to check insurance details and verify coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "sarah.miller381@email.com", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are logical, independent. Use book_appointment to schedule an emergency appointment for David Williams with Dr. Smith, ensuring insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P006", "patient_name": "David Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "patient_name": "David Williams", "doctor_name": "Dr. Smith", "appointment_type": "emergency", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are confident, organized, cautious. Search for patient records using user ID robert.brown551@email.com to verify patient information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P003", "email": "robert.brown551@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are polite, flexible, logical, optimistic. First, search_patients with email sarah.brown426@email.com to retrieve patient ID and insurance details. If the patient is not found, politely inform the requester and offer assistance in verifying the email or checking for alternative contact information. Once you have the patient ID and insurance details, verify insurance coverage for the patient. If the insurance coverage is not confirmed, inform the patient about the issue and provide guidance on resolving it with their insurance provider. If the insurance coverage is confirmed, proceed to book_appointment for the patient ID with the selected doctor during available hours. After successfully booking the appointment, send a confirmation email to sarah.brown426@email.com with the appointment details and a checklist to ensure she is prepared for her visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "If the patient is not found, I will inform the requester politely and offer assistance in verifying the email or checking for alternative contact information."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once I have the patient ID and insurance details, I will verify insurance coverage for the patient."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If the insurance coverage is not confirmed, I will inform the patient about the issue and provide guidance on resolving it with their insurance provider."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If the insurance coverage is confirmed, I will proceed to book an appointment for the patient ID with the selected doctor during available hours."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor_id": "doctor_id_from_available_hours", "appointment_time": "selected_available_time", "user_id": "P039"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After successfully booking the appointment, I will send a confirmation email to sarah.brown426@email.com with the appointment details and a checklist to ensure she is prepared for her visit."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are patient, independent, cautious, polite. First, search_patients with email 'maria.smith554@email.com' to retrieve patient ID and insurance details. Then, think to verify if Maria Smith has the required insurance information for appointment booking. This will ensure that the appointment can be scheduled smoothly and without any issues related to insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Maria Smith has the required insurance information for appointment booking."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are optimistic, flexible, logical, direct. First, search for patient details using user email lisa.jones889@email.com to verify authorization for accessing medical records. Once authorization is confirmed, verify insurance coverage for Lisa Jones before finalizing the appointment. This ensures that we have all necessary information and coverage details in place to provide seamless healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, patient, cautious, flexible. \"Book appointment for patient Sarah Miller with Dr. John Doe on 2023-11-15 at 10 AM\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_id": "P046", "doctor_name": "Dr. John Doe", "appointment_date": "2023-11-15", "appointment_time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, organized, confident, optimistic. First, use the tool `search_patients` with parameters: user_email=michael.brown235@email.com to retrieve patient record and insurance details. Then, use the tool `think` to verify if insurance details are valid and up-to-date for the patient. This process ensures that the patient’s insurance information is current before proceeding with any appointments, which is crucial for seamless healthcare service delivery.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "michael.brown235@email.com"}
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
        user_id="P014",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are independent, polite. Retrieve patient information for Robert Brown using email robert.brown731@email.com with proper authorization. Once you have verified the insurance details for Robert Brown to ensure coverage for upcoming appointments, book an appointment for him with Dr. Smith on November 16th at 10:00 AM. Ensure all insurance details are verified before confirming the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com", "user_id": "P014"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details for Robert Brown before proceeding with booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.brown731@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-16", "appointment_time": "10:00", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are patient, flexible, optimistic, direct. First, search for patient information for Lisa Williams using email lisa.williams792@email.com to verify authorization. Once authorization is confirmed, verify insurance details for patient Lisa Williams to ensure eligibility for appointment booking. This process is crucial to maintain compliance with healthcare regulations and to provide seamless service to the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the authorization status of Lisa Williams based on the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "If authorization is confirmed, proceed to verify insurance details for Lisa Williams."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, confident, flexible, organized. Use think tool to check available appointment slots for selected doctor within the next week.",
        actions=[
            Action(
                name="think",
                kwargs={"task": "check available appointment slots for selected doctor within the next week"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are organized, flexible, patient. Search for patient records using the name \"David Miller\" and email \"david.miller979@email.com\" to verify identity and obtain patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "David Miller", "email": "david.miller979@email.com", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are independent, organized. Search_patients for Robert Johnson using email robert.johnson741@email.com to verify patient ID and insurance details, then think to determine if Robert Johnson requires an emergency appointment based on recent health records or symptoms.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
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
        user_id="P007",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, organized, polite. Use search_patients to identify available doctors for Emily Jones based on her healthcare needs. Once you have identified that Dr. Smith is available, use book_appointment to schedule a routine check-up for Emily Jones with Dr. Smith during his available hours. After booking the appointment, use search_patients to retrieve Emily Jones's past medical records for Dr. Smith's review to ensure he has all the necessary information for her upcoming consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones", "needs": "routine check-up"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones", "records": "past medical records"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are flexible, independent, polite. Use the search_patients tool to retrieve Robert Brown's medical history for the upcoming appointment, ensuring all recent changes in his health status are noted. Then, use the think tool to assess if any of these changes require a specialist referral before proceeding to use the book_appointment tool to schedule a routine check-up for Robert Brown with Dr. Smith during available hours, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P017", "task": "Assess if any recent changes in Robert Brown's health status require a specialist referral"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are polite, direct, patient, cautious. Search for patient information using email maria.smith256@email.com to verify identity and retrieve patient ID.",
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
        user_id="P036",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are independent, cautious, polite. Use think to determine Emily Garcia's preferred doctors and specialties based on her previous visits, and then use think to identify available appointment slots for Dr. Smith, Emily Garcia's preferred physician, in the upcoming week.",
        actions=[
            Action(
                name="think",
                kwargs={"query": "Determine Emily Garcia's preferred doctors and specialties based on her previous visits."}
            ),
            Action(
                name="think",
                kwargs={"query": "Identify available appointment slots for Dr. Smith, Emily Garcia's preferred physician, in the upcoming week."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are direct, organized, patient, logical. First, use the search_patients tool to find patient by email sarah.smith521@email.com to verify identity and retrieve patient ID. Once Sarah Smith's identity is confirmed, proceed to use the search_patients tool to find Sarah Smith's insurance status and details to ensure coverage for the upcoming visit. Finally, use the search_patients tool to find available appointment slots with the chosen doctor for Sarah Smith, and then use the book_appointment tool to schedule an appointment for Sarah Smith with the selected doctor during their available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P033", "info_type": "insurance"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P033", "info_type": "appointments", "doctor": "chosen_doctor"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P033", "doctor": "chosen_doctor", "appointment_time": "selected_time_slot", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are patient, optimistic, organized, direct. Search_patients with email robert.brown731@email.com to retrieve patient ID and verify authorization. Once the patient ID is retrieved and authorization is confirmed, search_patients with the patient ID to verify insurance details. This process ensures that the patient is eligible for services covered by their insurance, allowing us to proceed efficiently with their healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, confident, organized. First, search_patients for any upcoming appointments for Lisa Jones to avoid scheduling conflicts. Once confirmed that there are no conflicts, check healthcare details for user Lisa Jones to confirm insurance provider and coverage status. Finally, book_appointment for Lisa Jones with Dr. Smith on 2023-09-15 at 10:00 AM, ensuring insurance is verified to facilitate a smooth appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones", "check_appointments": true}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones", "check_healthcare": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones", "doctor_name": "Dr. Smith", "date": "2023-09-15", "time": "10:00 AM", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are organized, patient, direct, independent. Search_patients with email \"robert.jones332@email.com\" to retrieve patient ID and insurance details",
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
        user_id="P050",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are organized, flexible, direct, independent. Search for patient Lisa Jones using email lisa.jones889@email.com to verify her identity and retrieve her medical records. Then, think to review Lisa Jones's medical history and identify any outstanding health concerns or routine check-up needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
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
        user_id="P013",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are direct, cautious. Search_patients with name \"Maria Smith\" and email \"maria.smith554@email.com\" to verify patient identity and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Maria Smith", "email": "maria.smith554@email.com", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are logical, cautious. Search for patient details with email sarah.brown753@email.com to verify authorization for accessing healthcare information, and then search_patients for Sarah Brown's insurance details to verify coverage eligibility for the appointment. This process is crucial to ensure that Sarah Brown is authorized to access healthcare services and that her insurance covers the upcoming appointment. Once these verifications are complete, you can proceed with further actions such as booking her appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Brown", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are optimistic, direct, confident, polite. First, search for patient John Johnson by email (john.johnson627@email.com) to retrieve his patient ID and details. Once you have the patient ID, check the insurance details to ensure coverage for his upcoming appointment. This will help us confirm that John is fully covered, allowing us to proceed smoothly with scheduling his healthcare needs.",
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
        user_id="P006",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, patient, flexible, organized. First, check healthcare details for patient David Williams to review current insurance status and coverage. Once you have confirmed the insurance details, book an appointment for David Williams with Dr. Smith on 2023-11-15 at 10:00 AM, ensuring it falls within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P006", "patient_name": "David Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "patient_name": "David Williams", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are patient, flexible, optimistic. Search for patient details using email maria.smith554@email.com to verify identity and retrieve patient ID. Then, check healthcare details for the retrieved patient ID to confirm insurance status and eligibility, ensuring the patient is covered for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the retrieved patient ID to check healthcare details for insurance status and eligibility."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are confident, optimistic. First, search for patients with the name \"Michael Miller\" and email \"michael.miller534@email.com\" to retrieve the patient ID and insurance details. Once you have the patient ID, think to verify the insurance coverage to ensure it is active and covers the necessary medical services. This will help in facilitating a seamless appointment booking process for Michael Miller.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Michael Miller", "email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once I have the patient ID and insurance details, I will verify the insurance coverage to ensure it is active and covers the necessary medical services."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are polite, patient, cautious. search_patients with email sarah.smith521@email.com to retrieve patient ID and information",
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
        user_id="P025",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are confident, cautious, independent, polite. Search for any upcoming available appointment slots for Sarah Brown's preferred doctor within the next two weeks.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Find Sarah Brown's preferred doctor and check their available appointment slots within the next two weeks."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, independent, organized. First, search for Robert Garcia's patient profile using email robert.garcia592@email.com to verify insurance coverage. Once verified, proceed to check Robert Garcia's insurance details before confirming the appointment booking. Finally, search for available appointment slots for Dr. Smith within the next two weeks to ensure a timely consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for Robert Garcia before proceeding."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Robert Garcia's insurance details to ensure coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available appointment slots for Dr. Smith within the next two weeks."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are organized, optimistic, independent, patient. Search for patients by locating Maria Smith using her email maria.smith554@email.com to verify her insurance details. Once the insurance verification for Maria Smith is confirmed, book an appointment for her with the selected doctor, ensuring it fits within their available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com", "user_id": "P013"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Smith's insurance details before proceeding to book an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.smith554@email.com", "doctor_id": "D001", "appointment_time": "2023-10-15T10:00:00", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are direct, confident, cautious. Search for Sarah Williams (sarah.williams853@email.com) in the patient database to retrieve her patient ID. Once you have her patient ID, check the healthcare details for Sarah Williams to verify insurance coverage. This will ensure that her insurance is in place before proceeding with any further appointments or treatments.",
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
        user_id="P007",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are cautious, logical, independent, patient. First, check healthcare details for user Emily Jones (emily.jones379@email.com) to verify insurance coverage. Once insurance coverage is confirmed, proceed to book an appointment for Emily Jones with Dr. Smith on 2023-11-15 at 10:00 AM, ensuring there are no conflicts with existing appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.jones379@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are cautious, direct, polite. Use search_patients to find patient Sarah Davis using email sarah.davis118@email.com to verify her identity.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are polite, optimistic, organized. Search for patient John Johnson using email john.johnson699@email.com to retrieve patient ID and healthcare information. Then, verify insurance details for the retrieved patient ID to ensure eligibility for appointment booking. This is important to confirm that the patient can be scheduled for a consultation without any issues related to coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and healthcare information for John Johnson."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure eligibility for appointment booking."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are independent, confident, organized, optimistic. Search for patient records using patient email: david.williams693@email.com to verify patient ID and insurance details. Once verified, think to determine the available doctors based on David Williams' healthcare needs and insurance coverage.",
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
        user_id="P047",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are optimistic, confident, patient, independent. Search_patients to find available doctors for Sarah Davis's healthcare needs, ensuring that the selected doctor specializes in her specific medical condition. After identifying a suitable doctor, Book_appointment for Sarah Davis with Dr. John Smith on the available date and time slot to address her healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P047", "patient_name": "Sarah Davis", "condition": "specific medical condition"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P047", "patient_name": "Sarah Davis", "doctor_name": "Dr. John Smith", "date": "2023-10-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are organized, independent, optimistic. First, search_patients with email \"emily.jones379@email.com\" to retrieve the patient ID and authorization status. Once you have the patient ID, confirm the insurance coverage status and details to ensure the patient is eligible for a routine visit. Finally, book_appointment for the patient ID with doctor ID during available hours for a routine visit, ensuring the patient receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and authorization status from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check the insurance coverage status and details using the patient ID to ensure eligibility for a routine visit."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "doctor_id", "appointment_type": "routine", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are confident, patient, logical. Search for patient Sarah Miller's insurance details using her email sarah.miller381@email.com to verify coverage.",
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
        user_id="P021",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are cautious, independent, logical, polite. First, search for patient records for Emily Brown using user ID emily.brown290@email.com to verify current healthcare details and authorization status. Once verified, proceed to book an appointment for Emily Brown with Dr. Smith at the earliest available slot within authorized hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "email": "emily.brown290@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "patient_email": "emily.brown290@email.com", "doctor_name": "Dr. Smith"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are logical, cautious, flexible, patient. Book_appointment for Michael Miller with Dr. Smith on the next available slot for a routine check-up, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Michael Miller before booking an appointment."}
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
        user_id="P037",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are direct, patient. First, search for patient information for John Johnson using the search_patients tool with email john.johnson941@email.com to verify identity and retrieve patient ID. Once you have the patient ID, verify insurance details for John Johnson using the think tool to confirm coverage and eligibility for healthcare services. This will ensure that John is covered for his upcoming medical needs and can proceed with scheduling appointments without any issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P037", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are polite, cautious, patient. book_appointment for David Williams with Dr. Smith on 2023-10-25 at 10:00 AM if available",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P006", "patient_name": "David Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "patient_name": "David Williams", "doctor_name": "Dr. Smith", "appointment_date": "2023-10-25", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, confident. First, search_patients with patient ID to retrieve healthcare details for Robert Garcia. Then, think to determine if Robert Garcia requires an emergency appointment based on the retrieved healthcare details. Ensure that the decision is made swiftly and accurately to provide timely care for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P005", "user_id": "P005"}
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
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are patient, polite. First, use search_patients with the email emily.davis525@email.com to retrieve Emily Davis's patient ID and medical history. Next, use think to determine Emily Davis's current insurance provider and verify coverage details for healthcare services. Finally, use think to identify if Emily Davis requires a routine check-up or has an urgent healthcare need based on her medical history, ensuring that insurance verification is completed before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Determine Emily Davis's current insurance provider and verify coverage details for healthcare services", "patient_id": "P032", "user_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"task": "Identify if Emily Davis requires a routine check-up or has an urgent healthcare need based on her medical history", "medical_history": "extracted_medical_history_from_previous_call", "insurance_verification": "completed", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are optimistic, polite, logical. First, search for patient Robert Brown using the search_patients tool with the email robert.brown624@email.com to verify existing records. Once confirmed, verify Robert Brown's insurance details to ensure they are up-to-date and valid for booking an appointment. Finally, book an appointment for Robert Brown with Dr. Smith using the book_appointment tool, ensuring the time slot is confirmed and insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.brown624@email.com", "doctor_name": "Dr. Smith", "appointment_time": "2023-11-15T10:00:00", "insurance_verified": true, "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are organized, direct. Search for patient records for Sarah Williams (sarah.williams602@email.com) using search_patients tool to verify her insurance information and medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "email": "sarah.williams602@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, organized, flexible. Search for patient records using email robert.johnson197@email.com to retrieve patient ID, and then check healthcare details for the retrieved patient ID to confirm insurance status. This will ensure the patient is covered for upcoming medical services, which is essential before proceeding with any healthcare appointments.",
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
        user_id="P006",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are independent, flexible. Use book_appointment tool to schedule an appointment for David Williams with Dr. Smith (Doctor ID: D102) for a routine check-up at 10:00 AM on November 15th, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "patient_name": "David Williams", "doctor_id": "D102", "appointment_date": "2023-11-15", "appointment_time": "10:00", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are direct, confident. search_patients: Find patient record for Emily Garcia using email emily.garcia400@email.com to retrieve her medical history.",
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
        user_id="P007",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are optimistic, direct, logical, polite. Think about the specific healthcare needs of Emily Jones to identify the appropriate specialist for her condition, ensuring that Dr. Smith, a renowned cardiologist, is the right fit. Then, search_patients to retrieve available appointment slots for Dr. Smith (doctor ID: D456) to align with Emily Jones's schedule, considering her availability and urgency of care.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Emily Jones needs to see a cardiologist, and Dr. Smith is a renowned cardiologist. I will check Dr. Smith's available appointment slots."}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor_id": "D456", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are confident, patient, cautious. Use think to identify available appointment slots for Dr. Smith during his working hours. Once an available slot is found, use book_appointment with parameters \"Emily Brown\", \"Dr. Smith\", \"2023-11-15 10:00 AM\" to schedule a routine check-up. After booking the appointment, use think to confirm if Emily Brown's appointment requires insurance pre-authorization to ensure a smooth visit.",
        actions=[
            Action(
                name="think",
                kwargs={"query": "Identify available appointment slots for Dr. Smith during his working hours"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Emily Brown", "doctor_name": "Dr. Smith", "appointment_time": "2023-11-15 10:00 AM"}
            ),
            Action(
                name="think",
                kwargs={"query": "Confirm if Emily Brown's appointment requires insurance pre-authorization"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are cautious, logical, patient, flexible. Begin by searching for patient information for Sarah Smith using email sarah.smith521@email.com to verify her insurance details. Once the insurance verification is complete, proceed to book an appointment for Sarah Smith with the selected doctor, ensuring that all insurance details are correctly processed. After the initial appointment is booked, search for any necessary follow-up appointments that Sarah Smith may need. If a follow-up is required, book an appointment for her with the same doctor, ensuring that the 24-hour cancellation policy is adhered to.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.smith521@email.com", "doctor_id": "D123", "appointment_type": "initial", "insurance_verified": true, "user_id": "P033"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.smith521@email.com", "doctor_id": "D123", "appointment_type": "follow-up", "insurance_verified": true, "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are organized, polite, flexible. Use tool search_patients with parameters: {email: \"sarah.brown426@email.com\"} to retrieve patient ID and verify authorization.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are independent, direct, logical. First, search_patients(email=\"emily.garcia400@email.com\") to retrieve patient ID and insurance details. Once you have verified the insurance information, proceed to book_appointment(patient_id=\"P123\", doctor_id=\"D456\", time_slot=\"2023-11-15T10:00:00\") to secure a general check-up. This ensures that Emily Garcia has her insurance details confirmed before scheduling her appointment, maintaining an efficient and seamless process in the healthcare system.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor_id": "D456", "time_slot": "2023-11-15T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are optimistic, cautious. First, search_patients(user_id=\"sarah.davis118@email.com\", search_criteria=\"insurance_status\", value=\"verified\") to ensure that Sarah Davis has verified insurance, which is necessary for scheduling appointments. Next, think(task=\"Check doctor's available hours for Dr. John Smith for routine appointments\") to find a suitable time slot for a routine check-up. Once you have confirmed the availability, proceed to book_appointment(patient_id=\"sarah.davis118@email.com\", doctor_id=\"D123\", appointment_type=\"routine\", time_slot=\"next available\") to secure a routine appointment with Dr. John Smith for Sarah Davis.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P047", "search_criteria": "insurance_status", "value": "verified"}
            ),
            Action(
                name="think",
                kwargs={"task": "Check doctor's available hours for Dr. John Smith for routine appointments"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P047", "doctor_id": "D123", "appointment_type": "routine", "time_slot": "next available"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are organized, independent, optimistic, cautious. First, search for any existing appointments for Robert Garcia to avoid scheduling conflicts. Once confirmed that there are no conflicts, proceed to book an appointment for Robert Garcia with Dr. Smith on the earliest available date for a routine check-up. Finally, send a confirmation email to robert.garcia592@email.com with the appointment details and insurance verification status, ensuring that all information is accurate and up-to-date for a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005", "name": "Robert Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "date": "2023-11-01", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are flexible, organized, confident. Use book_appointment to schedule a routine appointment for John Doe with Dr. Smith on Tuesday at 10:00 AM, ensuring it fits within available hours.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"patient_name": "John Doe", "doctor_name": "Dr. Smith", "appointment_type": "routine", "date": "Tuesday", "time": "10:00 AM", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are organized, polite, direct, independent. First, search for patient information using user email robert.brown731@email.com to verify authorization. Once authorization is confirmed, check healthcare details to verify Robert Brown's insurance coverage for cardiology appointments. Finally, book an appointment for Robert Brown with Dr. Smith (cardiologist) on 2023-11-15 at 10:00 AM, ensuring it aligns with Dr. Smith’s available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization for Robert Brown using the provided email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Robert Brown's insurance coverage for cardiology appointments."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure Dr. Smith is available on 2023-11-15 at 10:00 AM for a cardiology appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "doctor": "Dr. Smith", "specialty": "cardiology", "date": "2023-11-15", "time": "10:00", "patient_email": "robert.brown731@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are logical, cautious, optimistic, direct. First, search_patients with email emily.jones379@email.com to retrieve Emily Jones's patient ID and insurance details. Next, think to verify if Emily Jones's insurance covers the required healthcare services she needs for her upcoming treatment. Finally, think to identify a suitable doctor for Emily Jones based on her healthcare needs, ensuring the doctor specializes in her required treatment area.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="think",
                kwargs={"reason": "Verify if Emily Jones's insurance covers the required healthcare services for her upcoming treatment."}
            ),
            Action(
                name="think",
                kwargs={"reason": "Identify a suitable doctor for Emily Jones based on her healthcare needs, ensuring the doctor specializes in her required treatment area."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are optimistic, direct, cautious. First, search for Maria Smith's patient profile using her email maria.smith554@email.com to verify her identity. Once her identity is confirmed, proceed to check Maria Smith's insurance verification status in her patient profile. This will ensure that all necessary information is up-to-date and accurate before any medical services are scheduled.",
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
        user_id="P045",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are cautious, confident, organized, polite. Search for patient records for Lisa Williams using email lisa.williams792@email.com to verify patient ID and authorization.",
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
        user_id="P029",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are polite, logical, confident, flexible. Verify insurance details for patient John Johnson before booking an appointment. Once the insurance details have been confirmed, proceed to book an appointment for John Johnson with Dr. Smith on the earliest available date. This ensures that all necessary information is in place for a seamless appointment scheduling process, enhancing the efficiency of our healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "John Johnson", "user_id": "P029"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for John Johnson before proceeding to book an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "John Johnson", "doctor_name": "Dr. Smith", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are confident, optimistic, cautious, direct. Search for patient with email robert.brown551@email.com to retrieve patient ID and authorization status",
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
        user_id="P032",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are organized, flexible, polite. Begin by searching for patient records for Emily Davis using the email emily.davis525@email.com to verify her identity and insurance details. Once you have confirmed her identity, proceed to verify Emily Davis's insurance coverage to ensure it is valid and covers the required healthcare services she needs. After confirming her insurance, search for available appointment slots with Dr. Smith, ensuring that the availability aligns with Emily's schedule preferences.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Davis's identity and insurance details to ensure they are correct."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Emily Davis's identity and insurance are verified, proceed to check her insurance coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After confirming insurance coverage, check Dr. Smith's available appointment slots that match Emily's schedule preferences."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are patient, organized. First, search for patient Lisa Jones using email lisa.jones889@email.com to verify patient details. After confirming her identity, search_patients for Lisa Jones to retrieve her insurance information for verification. Once her insurance is verified, proceed to book an appointment for Lisa Jones with Dr. Smith (ID: D123) at 10:00 AM on 10/25/2023.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "lisa.jones889@email.com", "doctor_id": "D123", "appointment_time": "10:00 AM", "appointment_date": "10/25/2023", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are logical, polite, direct. First, search_patients for user Maria Smith (maria.smith256@email.com) to retrieve patient ID and insurance details. Once you have the patient ID, think to verify insurance coverage for a routine check-up to ensure that the service is covered without additional costs. After confirming the insurance coverage, proceed to book_appointment for the patient ID with the appropriate doctor ID on the earliest available date and time for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details for Maria Smith from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance coverage for a routine check-up to ensure it is covered without additional costs."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "patient_id": "P019", "doctor_id": "appropriate_doctor_id", "date": "earliest_available_date", "time": "earliest_available_time", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are patient, independent. First, search_patients for Robert Brown using email robert.brown624@email.com to retrieve patient ID. Once you have the patient ID, check healthcare details for patient ID P001 to confirm insurance status. This will ensure that Robert Brown can book an appointment with Dr. Smith on an available date and time, with verified insurance coverage, facilitating a smooth and efficient healthcare experience.",
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
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are polite, direct. Search for patient records using email john.johnson627@email.com to retrieve patient ID and insurance details. Then, verify insurance details for the retrieved patient ID to ensure eligibility for booking an appointment. This process is essential to confirm that the patient can be scheduled for a routine check-up with Dr. Smith, ensuring a smooth and efficient healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "user_id": "P031"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID to ensure eligibility for booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are independent, organized, polite, flexible. First, search_patients with email: \"emily.davis525@email.com\" to retrieve patient ID and insurance details. Once you have the patient ID, use it to search_patients with patient ID to retrieve available medical history and current healthcare needs. After reviewing the medical history, think to determine if any retrieved lab results require follow-up appointments or consultations. If necessary, proceed to book_appointment with patient ID for a follow-up consultation with Dr. Smith during available hours to ensure Emily receives the appropriate care.",
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
                kwargs={"thought": "Review the retrieved medical history and lab results to determine if any require follow-up appointments or consultations."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor": "Dr. Smith", "appointment_type": "follow-up consultation", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are organized, logical, direct, cautious. Begin by searching for patient information for Sarah Davis using email sarah.davis118@email.com to ensure proper authorization. Once authorization is confirmed, verify insurance details for Sarah Davis before proceeding with appointment booking. After verifying insurance, check available appointment slots for Dr. John Smith (Doctor ID: D1001) to find a suitable time for Sarah Davis's appointment next week.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are direct, patient. Search_patients for user Sarah Brown (sarah.brown426@email.com) to retrieve patient ID and insurance details. Then, think about the insurance verification status for the patient ID retrieved in the previous task. Once you have confirmed that the insurance is verified, proceed to book an appointment for Sarah Brown with Dr. John Smith (doctor ID D123) for a general consultation on 2023-10-25 at 10:00 AM. Ensure that all patient and insurance information is accurately recorded and communicated to avoid any issues during the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details for Sarah Brown from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check the insurance verification status for the retrieved patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P039", "patient_id": "P039", "doctor_id": "D123", "date": "2023-10-25", "time": "10:00", "appointment_type": "general consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are independent, cautious. Use `search_patients` to find the patient record for Robert Johnson using the email robert.johnson197@email.com. Then, use `think` to evaluate the best available time slot for Robert Johnson based on Dr. Smith's schedule and Robert's availability, ensuring the appointment aligns with both parties' preferences for a weekday morning.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Evaluate the best available time slot for Robert Johnson based on Dr. Smith's schedule and Robert's availability, ensuring the appointment aligns with both parties' preferences for a weekday morning.", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are patient, optimistic. First, search_patients with email \"sarah.brown426@email.com\" to verify patient profile and authorization status, ensuring that Sarah Brown's insurance information is up-to-date. Once you have confirmed that Sarah Brown's insurance is verified for booking an appointment, proceed to book_appointment for Sarah Brown with the primary care physician during available hours. Make sure to double-check that the insurance verification is current before finalizing the appointment to ensure a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.brown426@email.com", "doctor_type": "primary care physician", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, direct, confident. First, search for patient information using search_patients with parameters: patient_email=maria.smith554@email.com, authorization_code=AUTH123. Next, think to verify if Maria Smith has valid insurance coverage for booking an appointment. Once insurance coverage is confirmed, search for available doctors using search_patients with parameters: specialty=\"General Practitioner\", location=\"Maria's preferred clinic location\", insurance_accepted=\"Yes\". Finally, book_appointment for Maria Smith using book_appointment with parameters: patient_id=PAT890, doctor_id=DOC567, appointment_time=\"chosen available slot\", insurance_verified=\"Yes\".",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "maria.smith554@email.com", "authorization_code": "AUTH123"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"specialty": "General Practitioner", "location": "Maria's preferred clinic location", "insurance_accepted": "Yes"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_id": "DOC567", "appointment_time": "chosen available slot", "insurance_verified": "Yes"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are flexible, confident. Search patients with user email michael.brown235@email.com to retrieve patient ID and healthcare details, then check healthcare details for the retrieved patient ID to verify insurance status. This process is essential to ensure that the patient is covered for any upcoming medical services and to facilitate a smooth healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and healthcare details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details to verify insurance status for the retrieved patient ID."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are flexible, organized, cautious, direct. First, check Dr. Smith's available hours to schedule an appointment for a routine check-up. Once you have identified the available slots, book an appointment for the routine check-up using the patient ID. After securing the routine check-up, proceed to book a cardiology consultation on the same day as the routine check-up, ensuring both appointments align for the patient's convenience.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to check Dr. Smith's available hours for scheduling a routine check-up."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "appointment_type": "check_availability", "doctor": "Dr. Smith"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Now that I have Dr. Smith's available hours, I will book a routine check-up."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "appointment_type": "routine_checkup", "doctor": "Dr. Smith", "patient_id": "P050"}
            ),
            Action(
                name="think",
                kwargs={"thought": "I need to book a cardiology consultation on the same day as the routine check-up."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "appointment_type": "cardiology_consultation", "doctor": "Dr. Smith", "patient_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, flexible. Verify insurance details for user Robert Johnson to confirm coverage for the intended medical services. Once the insurance verification is complete, book an appointment for Robert Johnson with Dr. Smith using appointment ID A123 during available hours. Finally, notify Robert Johnson of the confirmed appointment details via email robert.johnson741@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Robert Johnson to confirm coverage for the intended medical services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P024", "patient_name": "Robert Johnson", "doctor_name": "Dr. Smith", "appointment_id": "A123", "email": "robert.johnson741@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, logical, polite. Search for patient details for Robert Garcia using search_patients with email robert.garcia592@email.com",
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
        user_id="P001",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are patient, confident, logical, flexible. Begin by verifying the insurance details for patient ID P001 to ensure all information is accurate and up-to-date. Once the insurance verification is complete, proceed to book an appointment for Sarah Williams with Dr. Smith at the earliest available date at 10 AM. After successfully booking the appointment, confirm the appointment booking for Sarah Williams using the insurance verification ID IV789 to finalize the process and ensure all records are properly updated.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Williams", "doctor_name": "Dr. Smith", "appointment_time": "10:00 AM"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details using the insurance verification ID IV789 before confirming the appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are direct, cautious, flexible. Use think to verify insurance details for Maria Johnson to ensure coverage is active. After confirming her insurance status, use book_appointment to finalize the appointment booking for Maria Johnson, ensuring that the appointment aligns with both her availability and the clinic's schedule.",
        actions=[
            Action(
                name="think",
                kwargs={"task": "verify insurance details for Maria Johnson to ensure coverage is active"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Maria Johnson", "patient_email": "maria.johnson@email.com", "user_id": "P023", "appointment_date": "2023-10-15", "appointment_time": "10:00", "doctor_id": "D001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are confident, direct, independent, cautious. Book a routine check-up appointment for Lisa Williams with Dr. Smith on October 17th at 2:00 PM.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams", "doctor_name": "Dr. Smith", "date": "2023-10-17", "time": "14:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are direct, polite. First, search_patients for user ID using email david.miller979@email.com to verify the patient's identity. Once confirmed, proceed to book_appointment for user David Miller with Dr. Smith during available hours, ensuring that his healthcare needs are promptly addressed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P028", "doctor": "Dr. Smith", "patient_email": "david.miller979@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are cautious, optimistic. First, search for patient John Johnson using email john.johnson627@email.com with the 'search_patients' tool to verify patient information. Next, think to verify insurance details for patient John Johnson to ensure eligibility for appointment booking. Once eligibility is confirmed, book an appointment for John Johnson with Dr. Smith (Doctor ID: D123) for a routine check-up using the 'book_appointment' tool, ensuring it falls within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for John Johnson to ensure eligibility for appointment booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson627@email.com", "doctor_id": "D123", "appointment_type": "routine check-up", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, patient. First, search for any existing appointments for patient ID P001 to avoid scheduling conflicts. Once you confirm there are no conflicts, book an appointment for patient ID P001 with Dr. Smith for a routine check-up on the next available date during his working hours. Finally, update patient ID P001's appointment record to include insurance verification status to ensure all necessary information is in place for the upcoming visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "date": "next available date", "time": "during working hours"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are cautious, organized. First, search for patient records using email maria.johnson759@email.com to retrieve patient ID. Once you have the patient ID, verify insurance for the retrieved patient ID with insurance provider Aetna.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from the search results and proceed to verify insurance."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are independent, optimistic. First, use the search_patients tool with parameters: user_email=robert.garcia592@email.com to retrieve Robert Garcia's patient ID and medical history. Next, use the think tool to verify Robert Garcia's insurance coverage and eligibility for healthcare services. Finally, use the think tool to identify doctors available for consultation that match Robert Garcia's medical needs based on his history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.garcia592@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify insurance coverage and eligibility for healthcare services for Robert Garcia based on his patient ID and medical history."}
            ),
            Action(
                name="think",
                kwargs={"task": "Identify doctors available for consultation that match Robert Garcia's medical needs based on his medical history."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are patient, optimistic, independent. Use the `book_appointment` tool to schedule a routine check-up for Robert Brown with Dr. Smith, ID D456, on the available date and time.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "doctor_id": "D456", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are optimistic, flexible. First, search_patients using email lisa.williams792@email.com to retrieve patient ID and verify authorization. Once you have the patient ID, search_patients using patient ID to retrieve insurance details for verification to ensure coverage for the upcoming consultation. After verifying insurance details, book_appointment for patient ID with Dr. Smith for a general consultation on the next available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P045"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P045", "doctor": "Dr. Smith", "appointment_type": "general consultation", "date": "next_available_date", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are flexible, logical. search_patients with parameters \"email: sarah.smith521@email.com\" to retrieve patient ID and insurance details.",
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
        user_id="P006",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are optimistic, direct, logical. Use the `search_patients` tool to find the patient ID for David Williams using his email david.williams693@email.com. Once you have retrieved the patient ID, use the `think` tool to verify the insurance details for David Williams to ensure that his routine check-up is covered. After confirming the insurance verification, use the `book_appointment` tool to schedule a routine check-up for David Williams during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.williams693@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P006", "task": "verify_insurance_coverage", "details": "routine check-up"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P006", "appointment_type": "routine check-up", "user_id": "P006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are optimistic, flexible, confident, patient. First, think about whether Emily Garcia requires an appointment with a primary care physician or a specialist based on her current healthcare needs. Next, search_patients to check Emily Garcia's healthcare records for any specialist recommendations that might guide your decision. If a specialist is recommended, proceed to search_patients to retrieve the schedule of Dr. John Smith (doctor ID D123) for available appointment slots. Finally, book_appointment to schedule an appointment for Emily Garcia with Dr. John Smith on an available date/time slot that suits her needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "doctor_id": "D123"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia", "doctor_id": "D123", "appointment_time": "2023-11-10T10:00:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are cautious, independent, direct. First, search for patient Sarah Williams using search_patients with email sarah.williams602@email.com to retrieve her patient ID. Once you have obtained her patient ID, verify insurance coverage for this patient before proceeding with any further actions. This ensures that all necessary coverage is in place, which is crucial for a seamless healthcare experience.",
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
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are flexible, organized, direct. Use search_patients with user email john.johnson627@email.com to retrieve patient ID and insurance details. Once you have the patient ID, use think to verify insurance details for the retrieved patient ID to ensure they are current and valid before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P031", "action": "verify_insurance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are optimistic, cautious, independent. \"search_patients with email emily.jones379@email.com to retrieve patient ID and medical history\"",
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
        user_id="P029",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are logical, polite, direct. Search for patient John Johnson using email john.johnson699@email.com to retrieve patient ID and insurance details.",
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
        user_id="P046",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are direct, optimistic. Book an appointment for Sarah Miller with Dr. John Smith for a routine check-up on 2023-11-15 at 10:00 AM.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_name": "Dr. John Smith", "date": "2023-11-15", "time": "10:00 AM", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are confident, organized. Search_patients with name 'Sarah Brown' and email 'sarah.brown753@email.com' to retrieve patient ID and insurance details. Think about the insurance verification status for patient ID retrieved from the previous task. Search_patients for available doctors specializing in cardiology for patient ID retrieved, ensuring insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Brown", "email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"specialization": "cardiology", "patient_id": "P025", "insurance_status": "verified"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are optimistic, organized. search_patients with user_email \"david.miller979@email.com\" to retrieve patient ID",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "david.miller979@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are flexible, direct, optimistic. Book appointment for John Johnson with Dr. Smith on October 15th at 10:00 AM",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_name": "John Johnson", "doctor_name": "Dr. Smith", "appointment_date": "2023-10-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are direct, flexible, independent, logical. Search_patients with parameter user_email as \"maria.miller855@email.com\" to retrieve patient ID and insurance information. Then, use the retrieved patient ID to check for any existing appointments or medical history. This will help in understanding the patient's current healthcare needs and ensuring that any new appointments are scheduled appropriately, taking into account past medical interactions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance information from the search_patients response."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the retrieved patient ID to check for any existing appointments or medical history."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are patient, cautious, polite. Search for patient records using email sarah.brown753@email.com to verify her details and insurance information.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Verify the email address for Sarah Brown before proceeding with the search."}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are confident, organized, logical, patient. Search for patient Robert Brown using email robert.brown551@email.com to retrieve patient ID and authorized details.",
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
        user_id="P023",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are patient, flexible, confident, logical. Use the `search_patients` tool to find patient Maria Johnson's profile using her email maria.johnson759@email.com. Once you have located her profile, use the `search_patients` tool to check if Maria Johnson has any existing appointments. After confirming her current appointment status, use the `think` tool to confirm Maria's preferred appointment date and time falls within Dr. Smith's available hours. This ensures that Maria can be accommodated without scheduling conflicts and aligns with Dr. Smith's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="think",
                kwargs={"task": "Confirm Maria Johnson's preferred appointment date and time falls within Dr. Smith's available hours."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are optimistic, polite. Search for patient Emily Davis using email emily.davis525@email.com to verify existing records, and then check the healthcare details of Emily Davis to confirm her insurance status and coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are independent, polite, patient. Use `search_patients` to find Robert Johnson's patient profile using email robert.johnson197@email.com. Once you have accessed his profile, use `think` to verify Robert Johnson's insurance status to ensure he is covered for medical appointments. After confirming his insurance coverage, use `book_appointment` to schedule an appointment for Robert Johnson during the doctor's available hours, ensuring that the insurance coverage is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify insurance status for Robert Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson197@email.com", "user_id": "P027", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are organized, flexible, direct, confident. Search for patient details using user email \"sarah.davis118@email.com\" to verify patient identity and retrieve medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, direct. First, use search_patients with parameters: email (lisa.jones889@email.com) to retrieve Lisa Jones' patient ID and verify her insurance status. Next, use think to determine the specific healthcare services Lisa Jones needs based on her last visit and current health status. Finally, use think to check if Lisa's insurance covers the required healthcare services and determine the next steps.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "determine healthcare services needed based on Lisa Jones' last visit and current health status"}
            ),
            Action(
                name="think",
                kwargs={"task": "check if Lisa Jones' insurance covers the required healthcare services and determine the next steps"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are independent, optimistic, organized. First, search for patient Emily Garcia's profile using email emily.garcia400@email.com to verify her identity. Once her identity is confirmed, check Emily Garcia's insurance details to verify her coverage. This will ensure that her insurance is valid and applicable for her upcoming healthcare needs.",
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
        user_id="P007",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are logical, flexible, confident, independent. \"think with context: Ensure Emily Jones can book an appointment during available hours\"",
        actions=[
            Action(
                name="think",
                kwargs={"context": "Ensure Emily Jones can book an appointment during available hours"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "patient_id": "P007", "appointment_type": "routine", "insurance_verified": true, "preferred_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are cautious, organized, polite. First, search_patients with email 'emily.jones379@email.com' to retrieve the patient ID and authorization status. Once you have the patient ID, use it to get insurance details for Emily Jones by searching the patients' records. After verifying the insurance details, proceed to search_patients with the patient ID and preferred doctor to find available appointment slots for routine visits. Ensure that all steps are completed accurately to facilitate a smooth booking process for Emily Jones.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P007", "search_type": "insurance_details"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P007", "preferred_doctor": "Dr. Smith", "search_type": "appointment_slots", "visit_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are cautious, organized. Use the think tool to determine if Robert Brown requires an emergency appointment based on his reported symptoms of severe chest pain and shortness of breath. If an emergency appointment is not necessary, use the search_patients tool to find available cardiologists for Robert Brown's required specialization. Once a suitable doctor is found, use the book_appointment tool to schedule a routine appointment with Dr. Smith for Robert Brown on 2023-11-15 at 10:00 AM.",
        actions=[
            Action(
                name="think",
                kwargs={"symptoms": "severe chest pain and shortness of breath"}
            ),
            Action(
                name="search_patients",
                kwargs={"specialization": "cardiology"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_name": "Dr. Smith", "patient_name": "Robert Brown", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, polite, organized, logical. Search for patient records using the email lisa.jones889@email.com to verify identity and retrieve patient ID. Once you have the patient ID, check healthcare details to confirm insurance coverage and eligibility. This ensures that the patient is covered for any upcoming appointments, which is crucial for seamless healthcare service delivery.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are organized, independent, flexible. \"search_patients to retrieve Sarah Brown’s insurance details and verify coverage for upcoming appointment\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown", "information": "insurance_details"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are optimistic, confident, polite. Search_patients for user Maria Smith to verify her insurance status and gather patient ID. Once you have confirmed her insurance details and obtained her patient ID, proceed to book_appointment for Maria Smith with Dr. Johnson on the next available slot, considering her non-emergency status. This will ensure that Maria is properly registered and scheduled for her consultation, streamlining her visit and enhancing her overall healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P019", "patient_name": "Maria Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P019", "patient_id": "P019", "doctor_name": "Dr. Johnson", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are direct, logical. First, search_patients with user_id \"emily.garcia400@email.com\" to retrieve Emily Garcia's patient profile. Once you have confirmed her details and availability, proceed to book_appointment for Emily Garcia with Dr. Smith, ID D101, on the next available slot that fits her schedule. Ensure that the appointment aligns with her healthcare needs and preferences.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "email": "emily.garcia400@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "patient_email": "emily.garcia400@email.com", "doctor_id": "D101", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are logical, patient. Before booking an appointment for your routine check-up with Dr. Smith, verify your insurance details to ensure coverage for the visit. Once the insurance verification is complete, proceed to book the appointment and then send the appointment confirmation details to john.johnson699@email.com.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P029"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for coverage of routine check-up with Dr. Smith."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "confirmation_email": "john.johnson699@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are logical, confident, patient. Search for patient Lisa Jones using her email lisa.jones889@email.com to retrieve her patient ID and details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are cautious, logical. First, search_patients with user email maria.miller855@email.com to retrieve patient ID and insurance details. Once you have the patient ID, think to verify insurance details for the patient ID retrieved from the previous search. After ensuring the insurance details are accurate, book_appointment for the patient ID retrieved with doctor ID found during available hours, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details for the retrieved patient ID to ensure accuracy before proceeding."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P042", "doctor_id": "available_doctor_id", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, patient. First, search_patients with email \"maria.miller855@email.com\" to verify patient identity and retrieve patient ID. Next, use the retrieved patient ID to search_patients and verify the current insurance status to ensure it is active. Finally, book_appointment with the patient ID, preferred date, time, and doctor's ID if the routine appointment is confirmed, ensuring all details are accurate and the patient is informed of the booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P042"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P042", "date": "2023-11-15", "time": "10:00", "doctor_id": "D123", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are optimistic, flexible, patient. Search for available doctors within the healthcare system specializing in cardiology for David Brown, and then check doctor's availability for Dr. Samantha Green (ID D456) to schedule an appointment for David Brown.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"specialty": "cardiology", "user_id": "P020"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D456", "patient_name": "David Brown", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are optimistic, polite, direct, patient. Use the search_patients tool with John's email (john.johnson627@email.com) to retrieve his patient ID and medical history. After obtaining John's medical history, use the think tool to determine the most suitable doctor for his condition. Finally, use the book_appointment tool to tentatively schedule an appointment for John Johnson with the selected doctor, using his patient ID and preferred time slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"medical_history": "retrieved_medical_history_data"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P031", "doctor_id": "selected_doctor_id", "time_slot": "2023-11-15T10:00:00", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are cautious, confident, organized. First, search for patient John Johnson to retrieve his patient ID and insurance information. Once you have retrieved this information, verify the insurance details with the provider to ensure they are accurate and up-to-date. After confirming the insurance details, book an appointment for John Johnson with doctor D123 on 2023-10-20 at 10:00 AM, ensuring that the insurance verification is completed to facilitate a smooth appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P031", "patient_id": "P031", "doctor_id": "D123", "date": "2023-10-20", "time": "10:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are organized, independent, optimistic, direct. Search for patient records for Sarah Miller using email sarah.miller381@email.com to verify existing appointment history. Once her records are accessed, check healthcare details for Sarah Miller to confirm insurance information is up-to-date for appointment booking. This ensures a seamless booking process for her upcoming appointment with Dr. Smith.",
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
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are organized, direct. Search_patients for patient ID using email michael.brown235@email.com to verify identity and retrieve patient details.",
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
        user_id="P037",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are flexible, direct, optimistic, organized. First, search for patient records using user ID 'john.johnson941' to verify eligibility for appointment scheduling. Once eligibility is confirmed, book an appointment for John Johnson with Dr. Smith (doctor ID D123) on the next available date, ensuring it fits within available hours. This step is crucial to maintain a streamlined process for patient care and ensure that John receives timely medical attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "john.johnson941"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P037", "patient_id": "P037", "doctor_id": "D123", "appointment_date": "next_available", "appointment_time": "within_available_hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are polite, cautious. First, search for the patient record using the email robert.johnson741@email.com to verify identity and retrieve medical history. Once the identity is confirmed, proceed to check healthcare details for Robert Johnson to confirm his insurance information is up to date. This ensures that all necessary information is verified before any further actions are taken, maintaining a smooth and efficient workflow in the healthcare process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are independent, direct, cautious, optimistic. Search for patient Maria Smith using the search_patients tool with email maria.smith554@email.com to retrieve her patient ID and insurance details. Once you have obtained the patient ID, verify her insurance details to ensure she is eligible for booking appointments. After confirming her insurance eligibility, search for available routine appointment slots with her primary care physician using the book_appointment tool.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "insurance_verified": true, "appointment_type": "routine", "doctor_id": "D789", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are optimistic, flexible, cautious. First, search for patient information using the email maria.miller855@email.com to retrieve user ID and medical history. Once you have Maria Miller's user ID, proceed to search_patients to check her insurance status and verify coverage for a general consultation. This will ensure that Maria's appointment with Dr. John Smith (doctor ID D123) can be scheduled without any issues regarding coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P042", "patient_id": "P042", "check_insurance": true, "service": "general consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, confident. Search for patient Sarah Brown using email sarah.brown753@email.com to retrieve patient ID and insurance details. Once you have retrieved the patient ID, verify the insurance details to ensure coverage. After confirming the insurance, book an appointment for Sarah Brown with Dr. John Smith (Doctor ID: D123) on the next available slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Sarah Brown."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance details to ensure coverage for Sarah Brown."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P025", "doctor_id": "D123", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are independent, direct. First, search for patient records using the email robert.brown624@email.com to verify identity and obtain the patient ID. Once you have confirmed the patient ID as P001, proceed to check the healthcare details to confirm the insurance status and eligibility for appointment booking. After confirming eligibility, verify the insurance details for patient ID P001 with the insurance provider Blue Cross (Insurance ID I456) specifically for cardiology services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify that the patient ID is P001 before proceeding."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check healthcare details to confirm insurance status and eligibility for appointment booking."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details with Blue Cross for cardiology services for patient ID P001."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are flexible, direct, organized. First, search for the patient record of Emily Jones using her email emily.jones379@email.com to verify her identity. Once verified, check the healthcare details for Emily Jones to confirm her insurance status and coverage, ensuring that all information is up-to-date and accurate for any upcoming medical needs.",
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
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are independent, cautious. First, search_patients for Sarah Miller using email sarah.miller381@email.com to retrieve her patient ID. Once you have her patient ID, think about the patient's current insurance status and verify if it's up-to-date for Sarah Miller (user ID: SM381). After confirming her insurance details, proceed to book_appointment for Sarah Miller with Dr. Johnson on available slot ID S204 for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Miller's patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Sarah Miller's insurance is up-to-date using her patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P046", "doctor_id": "Dr. Johnson", "slot_id": "S204", "appointment_type": "routine check-up", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are cautious, organized, independent. First, search_patients with user ID robert.garcia592@email.com to retrieve Robert Garcia's patient profile. Then, think to verify if Robert Garcia's insurance details are up-to-date and valid. This sequence ensures that all necessary information is accurate before proceeding with any appointments, maintaining a smooth and efficient healthcare process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "robert.garcia592@email.com"}
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
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are flexible, organized, polite, confident. Search for patient Lisa Williams using her email (lisa.williams792@email.com) to retrieve her patient ID and medical history. Once you have verified that her insurance details are up-to-date, proceed to book an appointment for Lisa Williams with Dr. John Smith on the upcoming Wednesday at 10:00 AM. Ensure that the insurance verification is complete before confirming the appointment to provide a seamless experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com", "user_id": "P045"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and medical history for Lisa Williams."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Lisa Williams."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P045", "doctor": "Dr. John Smith", "datetime": "upcoming Wednesday 10:00 AM", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are polite, logical, direct, organized. search_patients with parameter email=\"robert.johnson197@email.com\" to retrieve patient ID and healthcare details",
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
        user_id="P028",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are confident, independent, direct. book_appointment: Schedule routine check-up for David Miller with Dr. Smith during available hours, ensuring insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P028", "patient_name": "David Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P028", "patient_name": "David Miller", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are independent, direct, polite. book_appointment for patient ID with Dr. Smith during available hours, ensuring insurance verification is complete",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P016", "doctor": "Dr. Smith", "patient_id": "P016", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are direct, polite, patient, cautious. Search for patient records using email sarah.brown753@email.com to verify her identity and retrieve her patient ID.",
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
        user_id="P042",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are independent, direct. First, search for Maria Miller's patient record using her email maria.miller855@email.com to verify her identity. Once her identity is confirmed, check insurance details for Maria Miller to ensure coverage for upcoming appointments. Finally, book an appointment with Dr. Smith (Doctor ID: D123) for Maria Miller on the next available morning slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com", "user_id": "P042"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Miller's identity using her patient record details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Maria Miller's insurance details to ensure coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.miller855@email.com", "doctor_id": "D123", "time_slot": "next_available_morning", "user_id": "P042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, logical, organized, flexible. First, search_patients to find Robert Garcia by email (robert.garcia592@email.com) and retrieve the patient ID. Once you have the patient ID, check if there are any existing appointments scheduled for him. If no appointments are scheduled, proceed to book_appointment for the patient ID with Dr. Smith on the next available slot, ensuring that insurance verification is complete. This sequence ensures that Robert Garcia receives timely medical attention while adhering to administrative protocols.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor": "Dr. Smith", "insurance_verified": true, "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, optimistic, polite, independent. First, use search_patients to find patient information for Robert Garcia using his email robert.garcia592@email.com. Once you have his information, verify Robert Garcia's insurance details to ensure coverage for upcoming appointments. Finally, book_appointment for Robert Garcia with Dr. Emily Carter for a routine check-up at the next available slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Garcia's insurance details to ensure coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.garcia592@email.com", "doctor_name": "Dr. Emily Carter", "appointment_type": "routine check-up", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are optimistic, logical, direct. Search_patients for David Miller using email david.miller979@email.com to retrieve patient ID and insurance details. Think to verify insurance coverage for David Miller using retrieved insurance details. Book_appointment for David Miller with Dr. Sarah Johnson (Doctor ID: D567) on 2023-11-15 at 10:00 AM, ensuring insurance is verified and it fits within the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for David Miller."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for David Miller using retrieved insurance details."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P028", "doctor_id": "D567", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are patient, logical. First, search for patient using email david.brown214@email.com to retrieve patient ID and details. Then, check healthcare details for the retrieved patient ID to confirm insurance coverage and validity. This will ensure that David Brown's insurance is active and covers the services needed before proceeding with any appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and details for David Brown from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the retrieved patient ID to check healthcare details for insurance coverage and validity."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are optimistic, logical, patient. \"search_patients: Retrieve Emily Garcia's patient ID using email emily.garcia400@email.com\"",
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
        user_id="P007",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are patient, direct. First, verify Emily Jones's insurance coverage with the provider to ensure that her plan covers appointments with Dr. Smith. Once coverage is confirmed, proceed to book an appointment for Emily Jones with Dr. Smith (ID: D456) on March 16th at 10:00 AM. This will help streamline the scheduling process and avoid any potential issues with insurance claims.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Jones's insurance coverage for appointments with Dr. Smith."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones", "doctor_id": "D456", "appointment_date": "2024-03-16", "appointment_time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are cautious, direct, confident. Search for patient David Williams using the email david.williams693@email.com to retrieve his patient ID and medical history. Then, verify the insurance details for the retrieved patient ID to ensure coverage for his upcoming appointments. This is crucial to confirm that David's insurance will cover his medical needs, allowing for a smooth and uninterrupted healthcare experience.",
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
        user_id="P016",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are organized, direct, confident. First, use the search_patients tool to retrieve Michael Brown's profile using the email michael.brown235@email.com. Once you have accessed his profile, verify his insurance information to ensure it is up-to-date. After confirming the insurance details, use the book_appointment tool to schedule a cardiology appointment for Michael Brown with Dr. Smith during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance information for Michael Brown to ensure it is up-to-date."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "michael.brown235@email.com", "doctor_name": "Dr. Smith", "specialty": "cardiology", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are confident, flexible, direct. Use search_patients to find patient Robert Johnson by email robert.johnson741@email.com for verification. Once verified, use think to check Robert Johnson's insurance status and verify coverage for upcoming appointments. After confirming insurance coverage, use book_appointment to schedule a routine appointment for Robert Johnson with Dr. Smith on 2023-11-15 at 10:00 AM, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "check insurance status and verify coverage for upcoming appointments for Robert Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson741@email.com", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are flexible, confident, direct. Check healthcare details for user Lisa Jones (lisa.jones889@email.com) to verify insurance status and eligibility for booking an appointment. Once eligibility is confirmed, search for available doctors specializing in general medicine for Lisa Jones, considering her insurance coverage, to ensure she can receive care without unexpected costs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P050", "email": "lisa.jones889@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status and eligibility for Lisa Jones before proceeding to search for doctors."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once eligibility is confirmed, search for available doctors specializing in general medicine who accept Lisa's insurance."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are cautious, independent, organized, confident. First, search for patient information for Emily Davis using user ID emily.davis525@email.com to verify authorization. Once authorization is confirmed, proceed to search_patients to verify Emily Davis's insurance details with insurance ID INS-789456 for eligibility. After confirming her insurance eligibility, book an appointment for Emily Davis with Dr. Smith on the earliest available date, ensuring that all insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_email": "emily.davis525@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "insurance_id": "INS-789456"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_email": "emily.davis525@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, logical, polite. First, search_patient using email robert.johnson741@email.com to retrieve patient ID and verify authorization. Next, search_patient to verify Robert Johnson's insurance information for eligibility and coverage details. Once insurance is verified, book_appointment for Robert Johnson with Dr. Smith (Doctor ID: D123) during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "verify_insurance": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P024", "doctor_id": "D123", "patient_email": "robert.johnson741@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are cautious, patient, independent, flexible. Use the \"search_patients\" tool to retrieve patient details for Robert Brown using the email robert.brown624@email.com, ensuring proper authorization is provided.",
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
        user_id="P047",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are patient, polite. First, search_patients with email sarah.davis118@email.com to retrieve patient ID and insurance details. Once you have the patient ID, check if there are any existing appointments by searching_patients with patient ID P001. If no appointments are found, proceed to book_appointment for patient ID P001 with doctor ID D123 for a routine check-up on 2023-11-15 at 10:00 AM, ensuring insurance verification is completed.",
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
                name="book_appointment",
                kwargs={"patient_id": "P047", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00", "appointment_type": "routine check-up", "insurance_verification": true, "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are organized, patient, flexible, confident. Use search_patients with email \"sarah.brown753@email.com\" to retrieve Sarah Brown's patient ID and medical history. Then, use search_patients with patient ID to check Sarah Brown's last appointment date and doctor details. Finally, use think to determine if Sarah Brown is due for a routine check-up based on last appointment date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P025"}
            ),
            Action(
                name="think",
                kwargs={"last_appointment_date": "2023-06-15"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are patient, polite, cautious. First, search_patients with email robert.johnson197@email.com to retrieve patient ID and insurance details. Once you have confirmed the insurance information, think to verify insurance coverage for user Robert Johnson's healthcare plan to ensure that his upcoming appointments are covered.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After retrieving Robert Johnson's patient ID and insurance details, verify his insurance coverage for upcoming appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are cautious, independent, logical, polite. Search for patient Maria Johnson's record in the database using email maria.johnson759@email.com, and once you have confirmed her details, book an appointment for her with Dr. Smith on the earliest available date, ensuring insurance verification is completed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.johnson759@email.com", "doctor_name": "Dr. Smith", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are direct, logical, optimistic. Use `search_patients` with parameters: insurance_id=\"INS12345\" to verify insurance coverage for John Johnson.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"insurance_id": "INS12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are cautious, organized, optimistic. First, search for patient information for Emily Brown using email emily.brown290@email.com with proper authorization to ensure all records are up-to-date. Once you have verified her details, proceed to verify insurance details for Emily Brown to ensure coverage for upcoming medical services. This will help in confirming her eligibility for the necessary treatments and appointments.",
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
        user_id="P039",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are direct, organized, flexible, confident. Search for available appointment slots with Dr. John Smith for a routine check-up and book an appointment for Sarah Brown on the next available weekday slot. Ensure that the appointment aligns with Dr. Smith's schedule and is convenient for Sarah. Once the appointment is confirmed, promptly notify Sarah Brown via email (sarah.brown426@email.com) about the confirmed appointment date and time, ensuring she has all the necessary details for her visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "email": "sarah.brown426@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P039", "doctor_name": "Dr. John Smith", "patient_name": "Sarah Brown", "appointment_type": "routine check-up", "preferred_day": "weekday", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are polite, cautious, independent, optimistic. Search for patient records for Sarah Davis using email sarah.davis118@email.com to retrieve her patient ID. Once you have obtained her patient ID, check healthcare details to verify insurance coverage for her upcoming appointments. After confirming her insurance details, search for available doctors specializing in general practice within Sarah's insurance network to ensure she receives the appropriate care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Davis's patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use Sarah Davis's patient ID to verify her insurance coverage for upcoming appointments."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available doctors specializing in general practice within Sarah's insurance network."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are cautious, flexible, confident. Search for user Lisa Jones (lisa.jones889@email.com) in the patient database using the search_patients tool to verify her details and insurance status. Once her insurance coverage is confirmed, proceed to book an appointment for Lisa Jones with Dr. Smith for a routine check-up using the book_appointment tool, ensuring it falls within Dr. Smith's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "lisa.jones889@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are polite, optimistic. search_patients for Sarah Brown using email sarah.brown753@email.com to retrieve patient ID and insurance information",
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
        user_id="P027",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are optimistic, patient. Search for patient details with email robert.johnson197@email.com to verify identity and insurance status.",
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
        user_id="P042",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are independent, optimistic. First, search_patients with email \"maria.miller855@email.com\" to verify patient identity and retrieve patient ID. Once you have the patient ID, check healthcare details for the retrieved patient ID to confirm insurance information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from the search_patients response."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are flexible, cautious, optimistic, organized. First, think to determine if Michael Brown has any existing appointment needs based on recent medical history. Then, search_patients with patient ID to check for any urgent medical conditions or existing treatment plans. Finally, think to assess if an emergency appointment is needed based on the retrieved medical conditions.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Determine if Michael Brown has any existing appointment needs based on recent medical history."}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P016"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess if an emergency appointment is needed based on the retrieved medical conditions."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are independent, direct. search_patients for Maria Miller using email maria.miller855@email.com to retrieve patient ID and insurance information",
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
        user_id="P031",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are logical, patient, independent. First, search_patients for John Johnson using email john.johnson627@email.com to retrieve patient ID and insurance information. Next, think to verify John's insurance eligibility for upcoming appointments to ensure that his insurance plan covers the services he requires. Once you have confirmed the insurance eligibility, book_appointment for John Johnson with Dr. Smith for a routine check-up, ensuring the appointment falls within Dr. Smith's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify John's insurance eligibility for upcoming appointments to ensure that his insurance plan covers the services he requires."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P031", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are polite, patient, flexible, cautious. \"search_patients to confirm Emily Jones's doctor availability for routine check-up\"",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Emily Jones", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are logical, flexible. First, search for patient records with the name \"Sarah Smith\" to verify her identity and retrieve her patient ID. Once you have confirmed her identity and obtained her patient ID, proceed to search for available doctors specializing in general medicine to find suitable appointment slots for Sarah Smith.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Smith", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Sarah Smith's patient ID is retrieved, proceed to find available doctors."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are confident, organized, direct, polite. Use search_patients with user ID michael.brown235 to retrieve a list of available doctors for a general check-up. Then, use think to determine the most suitable doctor for Michael Brown based on his preferences and doctor's specialties. Finally, use book_appointment to schedule a routine check-up for Michael Brown with doctor ID D567 on the available date and time, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "michael.brown235"}
            ),
            Action(
                name="think",
                kwargs={"task": "determine the most suitable doctor for Michael Brown based on his preferences and doctor's specialties"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P016", "doctor_id": "D567", "patient_id": "P016", "appointment_type": "routine check-up", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are logical, organized, patient, optimistic. First, search_patients using user email robert.johnson741@email.com to retrieve Robert Johnson's patient ID and medical history. Once you have retrieved the patient ID, verify insurance details for the patient ID to ensure coverage for upcoming appointments. This will help in confirming that Robert Johnson is eligible for the necessary medical services without any financial hindrances.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are confident, patient, cautious. Use think to determine Sarah Williams' healthcare needs and priorities based on her medical history and upcoming events, and then use think to prioritize the urgency of her healthcare appointments based on her current medical condition and insurance coverage. This will ensure that her most pressing health issues are addressed promptly and within her insurance plan's guidelines.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P018", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P018", "task": "Determine Sarah Williams' healthcare needs and priorities based on her medical history and upcoming events."}
            ),
            Action(
                name="think",
                kwargs={"user_id": "P018", "task": "Prioritize the urgency of Sarah Williams' healthcare appointments based on her current medical condition and insurance coverage."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are patient, logical, independent, organized. Search_patients with email \"robert.johnson741@email.com\" to retrieve patient ID and insurance details. Think to verify insurance information for the patient ID retrieved from search_patients to ensure that all coverage is up-to-date and there are no discrepancies. Once the insurance verification is completed, Book_appointment for the patient ID with their preferred doctor at the selected available slot, ensuring that the appointment aligns with the patient's schedule and the doctor's availability.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search_patients response."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance information for the retrieved patient ID to ensure coverage is up-to-date."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor_id": "preferred_doctor_id", "slot": "selected_available_slot", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are optimistic, confident, organized, direct. First, search for patient details for Emily Garcia using email emily.garcia400@email.com to verify authorization. Once verified, proceed to book an appointment for Emily Garcia with Dr. Smith, ensuring it is scheduled on the next available date during office hours. Finally, notify Emily Garcia about her upcoming appointment details, including the date, time, and location, and inform her of any necessary preparations she needs to make prior to her visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.garcia400@email.com", "doctor_name": "Dr. Smith", "appointment_date": "next_available", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are optimistic, cautious, direct, independent. First, think about Robert Brown's insurance status and verify insurance details before proceeding with appointment booking. Once the insurance details are confirmed, verify whether Robert Brown's insurance covers visits to Dr. Smith (Doctor ID: D456). If coverage is confirmed, proceed to book an appointment for Robert Brown with Dr. Smith (Doctor ID: D456) on the next available date during office hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P014"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Robert Brown's insurance covers visits to Dr. Smith (Doctor ID: D456)."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "doctor_id": "D456", "date": "next_available", "time": "office_hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are confident, flexible, direct, organized. First, search for patient records of Sarah Davis using email sarah.davis118@email.com to verify her identity. Once her identity is confirmed, check healthcare details for Sarah Davis to confirm her insurance information and coverage. This will ensure that her insurance is valid and covers the necessary services before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are optimistic, polite. Search_patients for Robert Brown using email robert.brown624@email.com to retrieve user ID and healthcare details. Once you have the necessary information, think to verify user Robert Brown's insurance information and check for authorization to access healthcare services. After confirming the insurance details, book_appointment for Robert Brown with Doctor ID D123 on 2023-11-15 at 10:00 AM, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance information and check for authorization to access healthcare services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "doctor_id": "D123", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are optimistic, independent, cautious. First, assess Maria Johnson's request for an appointment to determine if it's routine or emergency. Once you have established the nature of her request, verify if Maria Johnson's insurance is valid and covers the requested healthcare services. Finally, determine the optimal time slot for Maria Johnson's appointment based on her preferences and Dr. Smith's availability, ensuring that the appointment aligns with her insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P023", "patient_name": "Maria Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess Maria Johnson's request to determine if it's routine or emergency."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Johnson's insurance is valid and covers the requested healthcare services."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine optimal time slot for Maria Johnson's appointment based on her preferences and Dr. Smith's availability."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P023", "patient_name": "Maria Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine", "time_slot": "10:00 AM", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, polite, direct. Search_patients with name \"John Johnson\" to retrieve patient ID and verify authorization for accessing healthcare information. Once authorization is confirmed, think to determine the best available doctor for John Johnson based on availability and specialization, ensuring the doctor is well-suited to address his healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization for accessing John Johnson's healthcare information."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine the best available doctor for John Johnson based on availability and specialization."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are independent, confident, patient. First, search for patient information using email sarah.brown426@email.com to verify authorization for booking. Once authorization is confirmed, verify insurance details for Sarah Brown to ensure coverage for booking an appointment. This process ensures that Sarah Brown can be scheduled for a consultation with Dr. John Smith without any financial or administrative issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Sarah Brown has authorization for booking."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Sarah Brown's insurance details to ensure coverage for consultation with Dr. John Smith."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are flexible, polite. Think to determine available doctors for a cardiology appointment for user Lisa Williams and then book an appointment for Lisa Williams with Dr. John Doe on 2023-11-15 at 10:00 AM, ensuring insurance is verified.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to determine the available doctors for a cardiology appointment for Lisa Williams."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P045"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Now that I have access to patient information, I will proceed to book an appointment with Dr. John Doe for Lisa Williams."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P045", "patient_name": "Lisa Williams", "doctor_name": "Dr. John Doe", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM", "specialty": "Cardiology", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are direct, polite. Search for patient information using email sarah.brown753@email.com to verify identity and retrieve patient ID. Then, book an appointment for the retrieved patient ID with Dr. John Smith on the earliest available date. This is crucial as the patient requires a follow-up consultation to discuss recent test results and adjust treatment plans if necessary.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com", "user_id": "P025"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P025", "doctor_name": "Dr. John Smith", "date": "earliest_available_date", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are cautious, patient. First, retrieve Michael Miller's healthcare profile using proper authorization to confirm his insurance and contact details. Once you have verified his insurance coverage for cardiology consultations, proceed to book an appointment for Michael Miller with Dr. Smith on the next available date during her office hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P048", "patient_name": "Michael Miller", "doctor_name": "Dr. Smith", "specialty": "Cardiology"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are organized, optimistic, logical, flexible. search_patients for Emily Jones's insurance details to verify coverage before booking an appointment",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are patient, cautious, optimistic. search_patients with user_id \"P001\" to retrieve healthcare details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are direct, polite. Search_patients using patient ID to check for any existing appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are logical, optimistic, organized, confident. First, retrieve Emily Davis's insurance information to verify coverage. Once you have confirmed that her insurance covers Dr. John Smith's services, proceed to book an appointment with Dr. John Smith for Emily Davis on the next available date. After securing the appointment, promptly notify Emily Davis of her upcoming appointment details with Dr. John Smith, ensuring she has all the necessary information.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Davis's insurance coverage for Dr. John Smith's services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "doctor_name": "Dr. John Smith", "appointment_date": "next available"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are cautious, polite, independent. First, search for patient information for Robert Johnson using email robert.johnson197@email.com to verify authorization. Once authorization is confirmed, proceed to check Robert Johnson's insurance details to ensure coverage for his upcoming appointments. This will help in coordinating his healthcare needs efficiently and avoid any potential billing issues.",
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
        user_id="P045",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are optimistic, polite, confident, cautious. First, search_patients with user email \"lisa.williams792@email.com\" to check for existing records and retrieve patient ID. Then, think to verify Lisa Williams' insurance details and confirm coverage for upcoming appointments. Once insurance coverage is confirmed, proceed to book_appointment with the retrieved patient ID, the appropriate doctor ID, and an available slot for Lisa Williams' routine check-up, ensuring that all details are accurate for a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "lisa.williams792@email.com"}
            ),
            Action(
                name="think",
                kwargs={"reasoning": "Verify Lisa Williams' insurance details to confirm coverage for upcoming appointments."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P045", "doctor_id": "appropriate_doctor_id", "slot": "available_slot", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are optimistic, flexible, polite, logical. First, use the \"search_patients\" task with parameters: {email: \"maria.smith256@email.com\"} to retrieve the patient ID and details for Maria Smith. Once you have the patient ID, proceed with the \"think\" task using parameters: {patient_ID: retrieved_patient_ID, action: \"check insurance validity\"} to verify Maria's insurance details and ensure she is eligible for coverage. After confirming insurance validity, use the \"think\" task again with parameters: {patient_ID: retrieved_patient_ID, action: \"determine appointment type\"} to assess whether Maria requires an emergency or routine appointment. Finally, if her insurance is valid and the appointment type is determined, proceed with the \"book_appointment\" task using parameters: {patient_ID: retrieved_patient_ID, doctor_ID: preferred_doctor_ID, appointment_type: determined_appointment_type, time_slot: available_time_slot} to schedule her appointment with the appropriate doctor at a suitable time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_ID": "retrieved_patient_ID", "action": "check insurance validity"}
            ),
            Action(
                name="think",
                kwargs={"patient_ID": "retrieved_patient_ID", "action": "determine appointment type"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_ID": "retrieved_patient_ID", "doctor_ID": "preferred_doctor_ID", "appointment_type": "determined_appointment_type", "time_slot": "available_time_slot"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are optimistic, direct, flexible, logical. Use search_patients tool to retrieve Maria Smith's medical history using her email maria.smith256@email.com.",
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
        user_id="P024",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are polite, confident. First, use the Search_patients function with User: Robert Johnson (robert.johnson741@email.com) to retrieve the patient ID. Once you have obtained the patient ID, proceed to Search_patients with the patient ID to check for any existing appointments or medical history. This will ensure that all relevant information is reviewed before making any further healthcare decisions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user": "Robert Johnson", "email": "robert.johnson741@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are logical, optimistic, cautious, independent. Search_patients using email emily.garcia400@email.com to retrieve patient ID and existing healthcare details. Then, think to verify Emily Garcia's insurance details for eligibility and coverage to ensure she can proceed with the necessary medical services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Garcia's insurance details for eligibility and coverage to ensure she can proceed with the necessary medical services."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are optimistic, polite. First, search_patients with email \"michael.brown235@email.com\" to retrieve patient profile and insurance details. Then, think to verify insurance details for patient ID P235 and confirm coverage for upcoming appointments. By ensuring the insurance coverage is confirmed, you can assist in providing a seamless healthcare experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for patient ID P235 to confirm coverage for upcoming appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are organized, direct, cautious. First, use the \"search_patients\" task with parameters: user_email=sarah.miller381@email.com, search_criteria=\"Jane Smith\", authorization_code=\"AUTH123\" to locate Jane Smith's patient records. Once you have confirmed her identity and reviewed her insurance details, proceed with the \"book_appointment\" task using parameters: patient_id=\"P001\", doctor_id=\"D123\", appointment_type=\"routine\", date=\"2023-10-20\", time=\"10:00 AM\", user_email=sarah.miller381@email.com to schedule a routine appointment for her. Ensure all details are accurate to maintain a smooth process for both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.miller381@email.com", "search_criteria": "Jane Smith", "authorization_code": "AUTH123"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P046", "doctor_id": "D123", "appointment_type": "routine", "date": "2023-10-20", "time": "10:00 AM", "user_email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are flexible, patient. Search_patients with name 'Lisa Jones' to check existing healthcare records and ensure all information is up-to-date. Once verified, book_appointment for Lisa Jones with Dr. Smith (ID: D101) for a routine check-up during available hours, ensuring that her healthcare needs are addressed promptly.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P050", "patient_name": "Lisa Jones", "doctor_id": "D101", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are organized, direct, patient, cautious. Begin by searching for Sarah Smith's patient ID and medical history to ensure all her records are up-to-date. Once you have verified her details, proceed to book an appointment for Sarah Smith with her preferred doctor. Ensure the appointment is scheduled within the doctor's available hours and confirm that it aligns with Sarah's insurance coverage for a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "patient_name": "Sarah Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_id": "P033", "doctor_id": "D123", "appointment_time": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are independent, patient, optimistic, cautious. Search for patient details using the name \"Robert Johnson\" and email \"robert.johnson197@email.com\" to verify identity and retrieve patient ID.",
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
        user_id="P028",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are logical, cautious, organized. \"search_patients with email 'david.miller979@email.com' to retrieve patient ID and details\"",
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
        user_id="P033",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are direct, optimistic. First, search for patient information for Sarah Smith using user ID sarah.smith521@email.com to verify authorization. Once authorization is confirmed, proceed to search_patients to verify insurance details for Sarah Smith using the same user ID. After ensuring that her insurance is verified, search for Dr. Thompson's available hours for the upcoming week to find a suitable appointment slot. Finally, book_appointment for Sarah Smith with Dr. Thompson during the available hours, ensuring the appointment is not an emergency.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "email": "sarah.smith521@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "email": "sarah.smith521@email.com", "insurance_verification": true}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P033", "doctor_name": "Dr. Thompson", "availability": "upcoming_week"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P033", "patient_email": "sarah.smith521@email.com", "doctor_name": "Dr. Thompson", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are logical, flexible. Search for patient details using patient email robert.johnson197@email.com to verify identity and retrieve medical history.",
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
        user_id="P020",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are patient, independent. Use the `search_patients` tool to find the patient record for David Brown using the email david.brown214@email.com. Once you have located the record, use the `think` tool to verify authorization for accessing David Brown's medical records, ensuring compliance with healthcare privacy regulations. After confirming authorization, use the `book_appointment` tool to schedule a general consultation for David Brown with Dr. Smith on the next available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "verify_authorization", "patient_email": "david.brown214@email.com", "requester_name": "Michael Miller", "requester_email": "michael.miller534@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.brown214@email.com", "doctor_name": "Dr. Smith", "appointment_type": "general consultation", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are confident, optimistic. Search for Robert Garcia's patient profile using email robert.garcia592@email.com to confirm authorization for access to healthcare information. Once authorization is confirmed, book an appointment for Robert Garcia with Dr. Emily Thompson for a routine check-up on the earliest available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.garcia592@email.com", "doctor_name": "Dr. Emily Thompson", "appointment_type": "routine check-up", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are flexible, confident. Search_patients with patient_ID P00123 for healthcare details and medical history to ensure all necessary information is up-to-date. Then, think to confirm insurance coverage is valid for the desired healthcare service, ensuring that the patient can proceed with the recommended treatment without any financial concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_ID": "P00123"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm insurance coverage is valid for the desired healthcare service."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are cautious, optimistic. First, use the Search_patients tool to find the patient ID for Maria Johnson using her email (maria.johnson759@email.com) for authorization purposes. Once you have retrieved her patient ID, proceed to use the Search_patients tool again to find all upcoming appointments for Maria Johnson. Finally, utilize the Book_appointment tool to schedule a routine check-up for Maria Johnson with Dr. Smith, ensuring it fits within available hours and does not conflict with any existing appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "user_id": "P023"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P023", "user_id": "P023"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is David Miller and your email is david.miller979@email.com. You are logical, organized. First, search for patient records for Sarah Brown using the search_patients tool with email sarah.brown753@email.com to verify existing records. Once her records are confirmed, check healthcare details for Sarah Brown using the think tool to ensure all personal and medical information is up to date, as accurate data is crucial for her ongoing care. Finally, verify insurance information for Sarah Brown using the think tool to confirm coverage before proceeding to book an appointment. This ensures that her routine check-up with Doctor D456 can be scheduled smoothly without any coverage issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"action": "check_healthcare_details", "patient_name": "Sarah Brown", "email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"action": "verify_insurance", "patient_name": "Sarah Brown", "email": "sarah.brown753@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are direct, organized. First, search for patient Emily Garcia using email emily.garcia400@email.com to verify existing records in our healthcare database. Once her records are confirmed, proceed to book an appointment for Emily Garcia with Dr. John Smith, ensuring it fits within his available hours and aligns with Emily's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.garcia400@email.com", "doctor_name": "Dr. John Smith", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are logical, independent. Search for patient John Johnson's profile using email john.johnson941@email.com to verify insurance details.",
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
        user_id="P019",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are organized, logical. First, search_patients with filters: {\"email\": \"maria.smith256@email.com\"} to retrieve patient ID and insurance information. Once you have the patient ID, think to verify insurance details for the retrieved patient ID to ensure coverage for the appointment. After confirming the insurance details, search_patients with filters: {\"doctor_availability\": \"available_hours\"} to find available doctors for a routine appointment. Finally, book_appointment with parameters: {\"patient_id\": \"retrieved_patient_id\", \"doctor_id\": \"available_doctor_id\", \"appointment_type\": \"routine\", \"time\": \"available_slot\"} to schedule the appointment, ensuring a seamless experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"filters": {"email": "maria.smith256@email.com"}}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"filters": {"doctor_availability": "available_hours"}}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "doctor_id": "available_doctor_id", "appointment_type": "routine", "time": "available_slot"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, independent, logical. Book_appointment for patient ID with Doctor A123 on date D2023-11-15 at time T10:00, ensuring it's within available hours.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P047", "doctor_id": "A123", "date": "D2023-11-15", "time": "T10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are direct, logical. Search_patients with email \"sarah.miller381@email.com\" to retrieve Sarah Miller's patient ID and insurance information. Think to verify if Sarah's insurance information is up-to-date and valid for appointment booking, as this is crucial for ensuring a smooth scheduling process. Book_appointment for patient ID with Dr. Smith, checking available slots for the next week, ensuring it's within Dr. Smith's available hours, to provide Sarah with timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.miller381@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Miller's patient ID and insurance information to verify its validity and ensure it is up-to-date."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Sarah's insurance information is valid and up-to-date for appointment booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P046", "doctor": "Dr. Smith", "date": "next_week", "user_id": "P046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are independent, logical. Use think to determine the type of appointment David Brown needs based on his recent medical history.",
        actions=[
            Action(
                name="think",
                kwargs={"user_id": "P020", "patient_name": "David Brown", "recent_medical_history": "Review David Brown's recent medical history to determine the type of appointment needed."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are direct, patient, confident, independent. Search for patient Michael Brown in the healthcare system using email michael.brown235@email.com, and verify his insurance details to ensure coverage for upcoming appointments.",
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
        user_id="P013",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are direct, optimistic. First, check healthcare details for Maria Smith to confirm her insurance coverage and eligibility for booking appointments. Next, think about Maria Smith's healthcare needs and verify if any upcoming appointments require scheduling. Finally, book an appointment for Maria Smith with Dr. John Doe (Doctor ID: D123) for a general check-up, ensuring it's during his available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "patient_name": "Maria Smith", "doctor_id": "D123", "appointment_type": "general check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are confident, polite, organized, flexible. Use \"search_patients\" to find Robert Brown's patient ID using email robert.brown551@email.com.",
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
        user_id="P003",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are organized, direct, flexible. Search for patient details of Robert Brown using email robert.brown551@email.com to verify identity and authorization.",
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
        user_id="P050",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are confident, logical. think with parameters: { \"goal\": \"Verify if Lisa Jones has current insurance information on file\" }",
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
        user_id="P018",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are confident, polite, direct. First, search for patient records for Sarah Williams using email sarah.williams602@email.com to verify her insurance details. Once the insurance verification is complete, proceed to book an appointment for Sarah Williams with Dr. John Smith for a routine check-up, ensuring the appointment falls within the available hours. This is crucial to ensure that her insurance coverage is valid for the upcoming visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.williams602@email.com", "doctor_name": "Dr. John Smith", "appointment_type": "routine check-up", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are flexible, confident. Search for patient Maria Smith using email maria.smith554@email.com to confirm her identity and retrieve her patient ID. Then, think to determine if Maria Smith requires an emergency appointment based on her medical history. If her medical history indicates a need for urgent care, proceed to book an appointment for Maria Smith with Dr. John Doe using her patient ID and a preferred time slot, ensuring it aligns with the doctor's available hours. This will ensure that Maria receives timely and appropriate medical attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor": "Dr. John Doe", "time_slot": "preferred_time_slot", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are independent, direct, cautious, optimistic. First, search for patient records using Emily Garcia's email (emily.garcia400@email.com) to verify her patient ID. Once you have confirmed her patient ID, retrieve Emily Garcia's insurance details to verify her coverage eligibility. After confirming her insurance coverage, proceed to book an appointment for Emily Garcia with Dr. John Smith on October 15th at 10:00 AM, ensuring that all insurance verification processes are complete to guarantee a seamless appointment experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.garcia400@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Garcia's patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Emily Garcia's insurance details using her patient ID to verify coverage eligibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance coverage is verified before proceeding to book an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P036", "doctor": "Dr. John Smith", "date": "2023-10-15", "time": "10:00", "user_id": "P036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are logical, cautious, polite, patient. First, search_patients for Michael Brown's patient ID using email michael.brown235@email.com. Once you have obtained the patient ID, proceed to search_patients for Michael Brown's medical history using the patient ID. After reviewing the medical history, think to identify the need for any routine or follow-up appointments based on the information gathered. This process will ensure that Michael Brown receives timely and appropriate healthcare services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P016"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Michael Brown's medical history to determine if there is a need for any routine or follow-up appointments."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, cautious, independent, flexible. Use the search_patients tool with parameters (name: \"John Doe\", date_of_birth: \"1980-05-15\") to retrieve his medical records. Then, use the think tool to check if the retrieved patient records include valid insurance information. This will ensure that John Doe's upcoming medical appointments are covered, providing seamless care and preventing unexpected expenses.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "John Doe", "date_of_birth": "1980-05-15"}
            ),
            Action(
                name="think",
                kwargs={"task": "Check if the retrieved patient records include valid insurance information for John Doe."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are direct, confident. search_patients with email emily.davis525@email.com to verify patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are independent, patient, flexible. Search for patient Robert Garcia using email robert.garcia592@email.com to retrieve patient ID and insurance details.",
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
        user_id="P021",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are confident, cautious. Search_patients for Emily Brown's insurance details to verify coverage status. Once you have confirmed the insurance coverage, think about Emily Brown's insurance status to determine if she is eligible for appointment booking. If eligible, proceed to book_appointment for Emily Brown with Dr. Smith (doctor ID D123) on the available slot, ensuring insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "name": "Emily Brown", "email": "emily.brown290@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Emily Brown's insurance covers appointments with Dr. Smith and if she is eligible for booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "doctor_id": "D123", "patient_name": "Emily Brown", "email": "emily.brown290@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are flexible, cautious. Search for patient Emily Davis using her email (emily.davis525@email.com) to verify her details and authorization status.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are organized, polite, confident, independent. First, search_patients to retrieve Robert Johnson's insurance provider details for verification. Once the insurance provider is confirmed, think to determine available doctors for a routine check-up based on Robert Johnson's insurance coverage. Finally, book_appointment for Robert Johnson with Dr. Smith on 2023-11-15 at 10:00 AM, confirming insurance and availability.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P027", "patient_name": "Robert Johnson"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Johnson's insurance provider details to ensure Dr. Smith is covered under his plan."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P027", "patient_name": "Robert Johnson", "doctor_name": "Dr. Smith", "date": "2023-11-15", "time": "10:00 AM", "insurance_provider": "Verified Insurance Provider"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are logical, direct, independent, confident. search_patients(email=\"david.miller979@email.com\") to find David Miller's medical history and current healthcare needs",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.miller979@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are logical, polite, confident. Search_patients for Sarah Brown using user email sarah.brown426@email.com to retrieve patient ID and details. Then, think to determine the need for a routine or emergency appointment based on retrieved patient details. This will ensure that Sarah Brown receives the appropriate level of care in a timely manner, reflecting the high standards of our healthcare practice.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.brown426@email.com"}
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
        user_id="P013",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are polite, logical, optimistic, patient. Search for patient information for Maria Smith to verify contact details and insurance information.",
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
        user_id="P036",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, organized, independent. search_patients with criteria: patient_email=\"emily.garcia400@email.com\" to retrieve user ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_email": "emily.garcia400@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are organized, patient, direct, cautious. First, search for patients with the email \"robert.johnson741@email.com\" to retrieve Robert Johnson's patient ID and details. Once you have identified the correct patient, think to verify Robert Johnson’s insurance coverage status before proceeding with appointment booking. After confirming his insurance coverage, book an appointment for Robert Johnson with Dr. Smith on his preferred date and time, ensuring that all insurance details are in order to avoid any complications.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Robert Johnson's patient ID and details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Johnson's insurance coverage status before proceeding with appointment booking."}
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
        user_id="P023",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are polite, flexible, cautious. First, search for patient Maria Johnson using her email maria.johnson759@email.com to verify her details in our healthcare database. Once her information is confirmed, proceed to verify Maria Johnson's insurance details to ensure she has coverage for a routine check-up, as she is due for her annual examination.",
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
        user_id="P033",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are patient, direct, optimistic, flexible. Use the `search_patients` tool to find patient details for Sarah Smith using email 'sarah.smith521@email.com' to verify her identity and retrieve necessary healthcare information. Once her identity is verified, use the `search_patients` tool to check Sarah Smith's insurance details for coverage verification. After confirming her insurance coverage, use the `book_appointment` tool to schedule an appointment for Sarah Smith with Dr. John Doe during his available hours. Ensure all steps are completed efficiently to provide a seamless experience for the patient.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com", "info_type": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.smith521@email.com", "doctor_name": "Dr. John Doe", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are independent, cautious, patient, logical. Search_patients for patient ID associated with Robert Garcia's email robert.garcia592@email.com to verify identity and retrieve patient details. Once verified, Book_appointment for Robert Garcia with Dr. Smith at the earliest available time slot, ensuring it fits within Robert's preferred times. Finally, Think to verify if the booked appointment for Robert Garcia requires any prior medical tests or documentation, ensuring all necessary preparations are made for the consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.garcia592@email.com", "user_id": "P005"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor": "Dr. Smith", "user_id": "P005"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify if the booked appointment for Robert Garcia requires any prior medical tests or documentation.", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are logical, cautious, independent. Book an appointment for Sarah Smith with Dr. Johnson for a routine check-up, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_name": "Sarah Smith", "user_id": "P033"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Smith's insurance before booking the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Smith", "doctor_name": "Dr. Johnson", "appointment_type": "routine check-up", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are confident, direct. First, search_patients to retrieve Robert Jones’s patient ID and medical history for his upcoming check-up. Then, check healthcare details for user Robert Jones (robert.jones332@email.com) to verify his insurance status for routine appointments. Finally, think to identify Robert Jones's preferred appointment time based on his calendar availability, and book_appointment for Robert Jones with Dr. Smith on the preferred date, ensuring it is within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones"}
            ),
            Action(
                name="think",
                kwargs={"query": "Identify Robert Jones's preferred appointment time based on his calendar availability"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P026", "patient_id": "P026", "doctor_name": "Dr. Smith", "appointment_date": "preferred_date", "appointment_time": "preferred_time"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are polite, patient, direct. search_patients for Lisa Jones to retrieve her patient ID and insurance details for verification.",
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
        user_id="P025",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are confident, logical, optimistic, flexible. Search for Sarah Brown in the patient database to retrieve her insurance details for verification. Once you have retrieved the insurance details, think about whether Sarah Brown's insurance is accepted by the healthcare system. This is crucial to ensure that her healthcare services will be covered.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P025", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Sarah Brown's insurance is accepted by the healthcare system."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are logical, polite. Search patients using email michael.miller534@email.com to obtain patient ID. Once you have the patient ID, verify insurance details for the patient to confirm coverage for a routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are direct, logical. Use \"book_appointment\" to schedule a routine check-up for Robert Garcia with Dr. Smith, ensuring it fits within available hours.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are direct, flexible. Book appointment for Emily Brown with Dr. Smith on October 14, 2023, at 10:00 AM, ensuring insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P021", "patient_name": "Emily Brown", "doctor_name": "Dr. Smith", "appointment_date": "2023-10-14", "appointment_time": "10:00 AM", "verify_insurance": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are logical, polite, confident, independent. Search_patients for user John Johnson to retrieve patient ID and verify authorization for accessing information. Once authorization is confirmed, proceed to search_patients to check available doctors for John Johnson's required healthcare service, ensuring that the selected doctor is available within the necessary time frame for an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_name": "John Johnson"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_id": "P037", "action": "verify_authorization"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P037", "patient_id": "P037", "action": "check_available_doctors", "service": "required_healthcare_service", "time_frame": "necessary_time_frame"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are independent, organized, confident. First, search_patients for Robert Jones's insurance information to verify coverage, ensuring that his healthcare services are covered under his current plan. Once coverage is confirmed, book_appointment for Robert Jones with his healthcare provider during an available time slot, coordinating with his schedule to ensure convenience. Finally, search_patients to find any pending test results for Robert Jones, as it is crucial to have this information ready for his upcoming appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones", "information_type": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones", "provider": "healthcare provider", "preferred_time": "next available", "confirmation": "yes"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P026", "patient_name": "Robert Jones", "information_type": "pending test results"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are organized, independent, flexible. Search for patient records of Michael Miller using email michael.miller534@email.com to verify authorization for access.",
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
        user_id="P045",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are confident, direct, cautious. Search_patients for Lisa Williams using email lisa.williams792@email.com to retrieve patient ID and insurance details. Then, think to verify if Lisa's insurance details allow for appointment booking. This is crucial to ensure that Lisa can proceed with her healthcare needs without any financial or administrative barriers.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if Lisa's insurance details allow for appointment booking."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Smith and your email is sarah.smith521@email.com. You are direct, cautious, independent. First, search for patient information for Robert Johnson using email robert.johnson197@email.com to verify his identity. Once verified, check insurance details for Robert Johnson to ensure his coverage is active for upcoming appointments. Finally, book an appointment with Dr. Emily Stevens (ID: D567) for Robert Johnson for a routine check-up on his preferred date and time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D567", "patient_email": "robert.johnson197@email.com", "appointment_type": "routine check-up", "preferred_date": "2023-11-15", "preferred_time": "10:00", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are polite, optimistic, cautious. Search for patient with email michael.miller534@email.com to retrieve patient ID and insurance details. Verify insurance details for patient ID retrieved to ensure coverage for upcoming services. Book appointment with doctor D101 for patient ID retrieved on next available slot within doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thoughts": "Retrieve the patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thoughts": "Verify the insurance details to ensure coverage for upcoming services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D101", "patient_id": "P048", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Robert Jones and your email is robert.jones332@email.com. You are organized, logical, confident, independent. Verify insurance details for John Johnson to ensure coverage for the upcoming appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "patient_name": "John Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are flexible, organized. Book_appointment with Dr. John Smith (doctor ID D567) for a routine cardiology check-up for Sarah Brown, ensuring it falls within the available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P039", "doctor_id": "D567", "patient_name": "Sarah Brown", "appointment_type": "routine check-up", "specialty": "cardiology"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are cautious, organized. First, search for patient records using the user ID sarah.williams853@email.com to verify her insurance details. Once the insurance is confirmed, use the Book_appointment tool to schedule an appointment with Dr. Smith for Sarah Williams. Ensure that the appointment aligns with her insurance coverage to avoid any discrepancies.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001", "email": "sarah.williams853@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_email": "sarah.williams853@email.com", "doctor_name": "Dr. Smith", "appointment_time": "2023-11-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are flexible, cautious. First, search_patients with email \"maria.johnson759@email.com\" to verify user authorization, ensuring that Maria Johnson is eligible for further processing. Once authorization is confirmed, proceed to search_patients for Maria Johnson's insurance details for verification to confirm her coverage and eligibility for services. After verifying her insurance, book_appointment for Maria Johnson with doctor ID D123 during available hours to ensure she receives timely medical attention.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "maria.johnson759@email.com", "info_type": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.johnson759@email.com", "doctor_id": "D123", "user_id": "P023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are patient, confident, flexible, independent. First, search for the patient ID associated with the email robert.johnson197@email.com using the search_patients tool. Once you have the patient ID, book a routine check-up appointment for Robert Johnson with Dr. Smith at the earliest available slot. Ensure that the booking is confirmed and all details are accurate before proceeding.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P027", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are independent, optimistic, polite. Search_patients for user Sarah Brown with email sarah.brown426@email.com to retrieve patient ID and insurance details. Then, think to verify insurance for the retrieved patient ID to ensure eligibility before booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Sarah Brown", "email": "sarah.brown426@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance for the retrieved patient ID to ensure eligibility before booking an appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are optimistic, polite. First, search_patients with user_email: emily.jones379@email.com to retrieve patient ID and insurance details. Then, think to verify if the insurance details are up-to-date for user Emily Jones. This process is crucial to ensure that Emily Jones' insurance information is current before her upcoming medical appointments, which helps in providing seamless healthcare services and avoiding any billing issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "emily.jones379@email.com"}
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
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are polite, direct, organized. Search for the patient Maria Johnson in the system using her email maria.johnson759@email.com. Once you have located her profile, verify Maria Johnson's insurance details to ensure they are valid and up-to-date. This is crucial to confirm her eligibility before proceeding with any appointments.",
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
        user_id="P031",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are patient, organized. First, search for patient ID associated with email john.johnson627@email.com using the search_patients tool to ensure you have the correct patient information. Next, check for any existing appointments for this patient ID using the search_patients tool to avoid scheduling conflicts. Finally, once you have confirmed there are no conflicts, check available appointment slots for this patient ID with Dr. Smith using the search_patients tool, and proceed to book an appointment on the next available slot using the book_appointment tool.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P031"}
            ),
            Action(
                name="search_patients",
                kwargs={"doctor": "Dr. Smith", "patient_id": "P031"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P031", "doctor": "Dr. Smith", "slot": "NEXT_AVAILABLE_SLOT", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are patient, independent. Search for patient records using email maria.johnson759@email.com to retrieve patient ID and details.",
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
        user_id="P032",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are flexible, cautious, patient. Book_appointment for Emily Davis with Dr. John Smith (Doctor ID: D123) on October 15, 2023, at 10:00 AM, verifying insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis", "doctor_id": "D123", "date": "2023-10-15", "time": "10:00", "verify_insurance": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are direct, polite, organized. First, search for patient records of Robert Brown using email robert.brown731@email.com to verify authorization status. Once verified, search healthcare items for available doctors who specialize in cardiology for Robert Brown. After identifying a suitable cardiologist, book an appointment for Robert Brown with Dr. Smith on an available date ensuring it aligns with Robert's schedule.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P014"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "doctor_specialty": "cardiology", "doctor_name": "Dr. Smith", "appointment_date": "2023-11-15"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are direct, cautious, polite, flexible. Search_patient using email robert.brown731@email.com to retrieve patient ID and details for Robert Brown.",
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
        user_id="P018",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are optimistic, logical, patient. Search_patients with email sarah.williams602@email.com to retrieve Sarah Williams' patient ID and insurance details.",
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
        user_id="P016",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are confident, logical, optimistic, direct. Search for patients by locating Michael Brown using the email michael.brown235@email.com to retrieve his patient ID and insurance details. Once you have confirmed the insurance details for Michael Brown's patient ID and verified his eligibility, proceed to book an appointment for him with the selected doctor. Ensure the appointment slot is within the available hours and that all insurance verifications are complete to facilitate a seamless booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com", "user_id": "P016"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Michael Brown's patient ID and insurance details from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Michael Brown's insurance eligibility for booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P016", "doctor_id": "selected_doctor_id", "appointment_time": "2023-10-25T10:00:00", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are flexible, cautious. Search_patients with email emily.davis525@email.com to verify patient identity and retrieve patient ID.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P033",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are logical, direct, cautious, optimistic. Search_patients using email sarah.smith521@email.com to retrieve patient ID and insurance details. Then, check healthcare details for Sarah's insurance to verify coverage for general practitioner visits. This will ensure that when you proceed to book an appointment with Dr. John Doe (GP123) for Sarah Smith (PatientID567) at 10:00 AM on the earliest available date, all insurance coverage details are confirmed, facilitating a smooth booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.smith521@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and insurance details for Sarah Smith using the email provided."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for general practitioner visits using Sarah's insurance details."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P033", "doctor_id": "GP123", "time": "10:00 AM", "date": "earliest available", "user_id": "P033"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are flexible, optimistic, patient. First, search for patient details using the email maria.smith554@email.com to retrieve the patient ID and insurance information. Next, verify the insurance coverage for the retrieved patient ID to ensure that an appointment can be booked. Finally, search for available appointment slots for the doctor associated with the retrieved patient ID, considering the patient's preferred time slots, to facilitate a smooth scheduling process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance information from the search_patients result."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming the patient ID retrieved is 'P456' and insurance information is available."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance coverage for patient ID 'P456'."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming insurance verification is successful."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available appointment slots for the doctor associated with patient ID 'P456'."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assuming the patient's preferred time slots are between 10 AM and 2 PM."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are independent, polite, direct, logical. First, search for patient information using patient email robert.johnson741@email.com to verify identity and retrieve patient ID. Once you have the patient ID, check the insurance details to ensure coverage is active before proceeding with appointment booking. Finally, book an appointment for the patient ID with Dr. Smith for the earliest available morning slot, ensuring it aligns with the patient's insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor": "Dr. Smith", "time": "earliest_morning_slot", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, cautious, optimistic. Search_patients with email robert.brown731@email.com to retrieve Robert Brown's patient ID and insurance details. Then, check healthcare details for the patient ID obtained to verify insurance information and ensure it is up-to-date. This process is crucial to confirm that Robert's insurance coverage is current before proceeding with any further healthcare services, ensuring a seamless experience for both the patient and the healthcare provider.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Robert Brown's patient ID and insurance details from the search results."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are logical, confident. Search for patient records for Robert Brown using search_patients tool with email robert.brown624@email.com.",
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
        user_id="P007",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are independent, organized, direct, confident. Use the search_patients tool to find patient details for Emily Jones using email emily.jones379@email.com. Once you have confirmed her details, use the book_appointment tool to schedule a consultation for Emily Jones with Dr. Smith on the next available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com", "user_id": "P007"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "emily.jones379@email.com", "doctor_name": "Dr. Smith", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are patient, direct, flexible, organized. Check healthcare details for patient Emily Davis to confirm insurance status and coverage. Once confirmed, book an appointment with Dr. John Smith (Doctor ID: D101) for Emily Davis at the earliest available time within the doctor's hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P032", "patient_name": "Emily Davis"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P032", "doctor_id": "D101", "patient_name": "Emily Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are cautious, direct. Search_patients with name \"Robert Brown\" and email \"robert.brown551@email.com\" to retrieve patient ID and insurance details. Then, think to verify insurance details for the patient ID retrieved from the previous task. This process ensures that Robert Brown's insurance information is accurate and up-to-date before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Robert Brown", "email": "robert.brown551@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the patient ID retrieved from the previous search to ensure accuracy."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are flexible, patient, polite, optimistic. Search_patients for Lisa Williams using email lisa.williams792@email.com to retrieve patient ID and insurance information. Then, think to verify insurance coverage for the patient ID retrieved in the previous step to ensure that the routine check-up is covered.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage for the retrieved patient ID to ensure the routine check-up is covered."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are polite, confident, organized, optimistic. Search for patient Maria Miller's healthcare records using email maria.miller855@email.com",
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
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are logical, optimistic, confident. think: Analyze Emily Brown's recent medical history to determine if any routine check-ups are due.",
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
        user_id="P003",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are optimistic, cautious, organized, confident. Search_patients for Robert Brown's insurance details and verify coverage for upcoming appointments",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P003", "patient_name": "Robert Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are confident, optimistic, direct. Search for patients with the name \"Lisa Jones\" to verify user details and check for existing records.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Jones", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are direct, flexible, polite. Search_patients for Robert Jones using email robert.jones332@email.com to retrieve patient ID and healthcare details. Once you have the patient ID, verify the insurance details for Robert Jones to ensure his coverage is up-to-date before proceeding with any further actions.",
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
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are organized, cautious, confident. Search for patient Robert Brown in the system using email robert.brown551@email.com to verify insurance details.",
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
        user_id="P025",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are confident, logical, direct, polite. Search_patients for Sarah Brown using user ID sarah.brown753@email.com to retrieve her healthcare details. Think about Sarah's current health status and any existing conditions for appointment preparation. Book_appointment for Sarah Brown with Dr. Smith for a routine check-up, ensuring it fits within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Sarah Brown's healthcare details to understand her current health status and any existing conditions."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Sarah Brown", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P025"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are organized, optimistic, independent, flexible. Search for patient information using email maria.smith554@email.com to verify identity and obtain necessary details. Think to determine if Maria Smith requires an emergency or routine visit based on her request. Once you have verified her identity and assessed her needs, proceed accordingly to ensure she receives the appropriate level of care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Smith's identity and assess her request to determine if it requires an emergency or routine visit."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P013", "appointment_type": "emergency", "patient_email": "maria.smith554@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are logical, direct, patient. search_patients with email \"maria.smith256@email.com\" to verify patient identity and retrieve patient ID",
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
        user_id="P024",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, patient. Search_patients with email robert.johnson741@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are optimistic, patient. Search for patients with the name Emily Brown to retrieve her patient ID and verify her authorization status.",
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
        user_id="P026",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are independent, polite, flexible, direct. Search for patient information for Robert Jones using email robert.jones332@email.com to verify identity and insurance status. Verify insurance details for Robert Jones to ensure eligibility for booking an appointment with Dr. Smith. Book appointment for Robert Jones with Dr. Smith (Doctor ID: D001) on the selected date and time slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com", "user_id": "P026"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.jones332@email.com", "doctor_id": "D001", "date": "2023-11-15", "time_slot": "10:00 AM", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are independent, direct, flexible. First, search for patient records in the system using Robert Brown's email (robert.brown624@email.com) to retrieve his patient ID. Once you have the patient ID, check healthcare details for Robert Brown's insurance coverage and verify its current status to ensure it is active. Finally, book an appointment with Dr. Smith for Robert Brown for a routine check-up on the next available date, ensuring that his insurance is verified for the scheduled appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com", "user_id": "P017"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID from the search results for Robert Brown."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Robert Brown's insurance coverage details using the retrieved patient ID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify that Robert Brown's insurance is active."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P017", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "date": "next_available_date", "insurance_verified": true, "user_id": "P017"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P026",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are polite, optimistic, patient, confident. Search for patient with email robert.jones332@email.com to retrieve patient ID and medical history. Once you have the patient ID, book an appointment for them with Dr. Smith during an available slot, ensuring insurance coverage is verified. This is crucial for maintaining a seamless experience for the patient and ensuring that all necessary preparations are in place for their upcoming visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.jones332@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P026", "doctor": "Dr. Smith", "user_id": "P026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are optimistic, direct, flexible. First, search for patient John Johnson using email john.johnson699@email.com to verify his identity and retrieve his patient ID. Once you have the patient ID, check the healthcare details to review his medical history and insurance information, ensuring everything is up-to-date and there are no outstanding issues. Finally, search for available appointment slots for Dr. Smith (ID: D101) in cardiology and book an appointment for John Johnson for the earliest available routine check-up slot, ensuring it aligns with his healthcare needs and insurance coverage.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com", "user_id": "P029"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID for John Johnson from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the patient ID to check John Johnson's healthcare details, including medical history and insurance information."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure John Johnson's insurance information is up-to-date and there are no outstanding issues."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available appointment slots for Dr. Smith (ID: D101) in cardiology."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Book the earliest available routine check-up slot for John Johnson, ensuring it aligns with his healthcare needs and insurance coverage."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P029", "doctor_id": "D101", "appointment_type": "routine check-up", "user_id": "P029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are cautious, confident, direct. First, search_patients with name 'Maria Miller' to retrieve patient ID and verify authorization. Once you have confirmed authorization, check healthcare details for the retrieved patient ID to confirm insurance status and coverage. This sequence ensures that Maria Miller's insurance information is up-to-date and accurate before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Maria Miller", "user_id": "P042"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization for patient information access."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once authorization is confirmed, proceed to check healthcare details for insurance status and coverage."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are logical, optimistic. First, search for patient details using email robert.brown731@email.com to verify identity and retrieve patient ID. Once you have the patient ID, verify insurance details to confirm coverage eligibility. After confirming the insurance coverage, book an appointment for the patient ID with Dr. Smith on the earliest available date next week.",
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
                kwargs={"thought": "Verify insurance details using the retrieved patient ID to confirm coverage eligibility."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check Dr. Smith's schedule for the earliest available appointment next week."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P014", "doctor": "Dr. Smith", "date": "next_week_earliest_available", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are organized, patient, polite. First, search_patients for Maria Smith using email maria.smith256@email.com to retrieve her patient ID and insurance details. Once you have the patient ID, check healthcare details to verify Maria's insurance status and coverage. After confirming her insurance, proceed to book_appointment for Maria Smith with the chosen cardiologist, ensuring that the appointment time is within the available hours and that her insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details for Maria Smith from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Smith's insurance status and coverage using her patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "doctor_specialty": "cardiologist", "appointment_time": "chosen_time_within_available_hours", "insurance_verified": true, "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are patient, logical. First, check Sarah Williams' insurance details for eligibility verification using user ID sarah.williams853@email.com to ensure her coverage includes dermatology consultations. Once verified, proceed to book an appointment for Sarah Williams with Dr. Johnson on the earliest available date that matches her schedule. Finally, confirm the booking details with Sarah Williams via email at sarah.williams853@email.com to ensure she is informed and prepared for her consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001", "email": "sarah.williams853@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Sarah Williams' insurance covers dermatology consultations."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_email": "sarah.williams853@email.com", "doctor_name": "Dr. Johnson", "specialty": "dermatology", "earliest_date": true}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm the booking details with Sarah Williams via email."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are logical, flexible, direct, independent. First, use the \"search_patients\" tool to find patient details for David Brown using the email david.brown214@email.com. Next, utilize the \"search_patients\" tool to check if David Brown has any existing appointments with Dr. Smith in the next month. If there are no conflicts, proceed to use the \"book_appointment\" tool to schedule a routine visit for David Brown with Dr. Smith next Tuesday at 10:00 AM, ensuring it fits within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com", "user_id": "P020"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com", "doctor": "Dr. Smith", "date_range": "next_month", "user_id": "P020"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "david.brown214@email.com", "doctor": "Dr. Smith", "date": "next_tuesday", "time": "10:00 AM", "appointment_type": "routine", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are cautious, direct, confident. Search for patient John Johnson using email john.johnson941@email.com to retrieve patient ID and verify authorization status. Once you have confirmed the authorization, use the patient ID obtained to check insurance details and verify coverage for a routine appointment. After confirming coverage, search available appointment slots for Dr. Smith to determine available times for routine visits, ensuring that you find the earliest available slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "verify_authorization": true}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "get_insurance_details": true}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "check_coverage": "routine appointment"}
            ),
            Action(
                name="book_appointment",
                kwargs={"doctor": "Dr. Smith", "appointment_type": "routine", "find_earliest_slot": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are optimistic, confident, cautious, direct. Search for patients using the user email sarah.williams602@email.com to retrieve the patient ID and insurance details. Once you have the patient ID, check the healthcare details to confirm the insurance status and eligibility.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are cautious, logical. Retrieve the patient profile for Michael Brown using email michael.brown235@email.com. Determine the type of appointment Michael Brown needs by assessing whether it is routine or emergency. Identify available doctors for Michael Brown's required appointment type to ensure he receives timely and appropriate care.",
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
        user_id="P017",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are polite, direct. Search for patient information using the email robert.brown624@email.com to verify identity and authorization.",
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
        user_id="P047",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are polite, flexible, patient, optimistic. First, use \"search_patients\" to find patient information for Sarah Davis using email sarah.davis118@email.com, ensuring proper authorization. Once her information is located, proceed to use \"search_patients\" to verify insurance details for Sarah Davis, checking for coverage eligibility. After confirming her insurance coverage, use \"book_appointment\" to schedule a routine check-up for Sarah Davis with Dr. Smith on the chosen date and time, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047", "check_insurance": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "sarah.davis118@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "date": "2023-11-15", "time": "10:00 AM", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are direct, optimistic, patient. Use the `search_patients` tool to verify insurance details for patient Robert Brown, ensuring coverage is valid and updated. Once insurance verification is complete, use the `book_appointment` tool to schedule a regular check-up for Robert Brown with Dr. Smith at the next available time slot. Ensure that all necessary authorizations are in place for Robert Brown before proceeding with the appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P014", "patient_name": "Robert Brown", "doctor_name": "Dr. Smith", "appointment_type": "regular check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are cautious, polite, logical. Search_patients with email sarah.williams602@email.com to retrieve Sarah Williams' patient ID and healthcare details.",
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
        user_id="P029",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are patient, flexible, polite, organized. First, use the search_patients tool to find patient information for John Johnson using email john.johnson699@email.com, ensuring proper authorization is confirmed. Once the patient information is verified, proceed to check available appointment slots for John Johnson with Dr. Smith using the book_appointment tool, ensuring the slots are within the doctor's available hours. This will facilitate a smooth scheduling process by ensuring all necessary patient details are accurate and up-to-date before confirming an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P029", "email": "john.johnson699@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "patient_email": "john.johnson699@email.com", "doctor_name": "Dr. Smith", "appointment_type": "routine", "preferred_time": "within available hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are optimistic, flexible. Search for Sarah Davis’s patient profile using email sarah.davis118@email.com to verify her details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com", "user_id": "P047"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are independent, patient, flexible. Search for patients with name \"Lisa Williams\" to retrieve patient ID and profile details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"name": "Lisa Williams", "user_id": "P045"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are organized, direct. Search_patients using user email (david.brown214@email.com) to retrieve patient ID and insurance details. Then, think to verify if the retrieved insurance details cover the required medical services. This will ensure that any necessary treatments or procedures can be scheduled without unexpected costs or coverage issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search results. Verify if the insurance covers the required medical services."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Robert Garcia and your email is robert.garcia592@email.com. You are optimistic, patient. First, search for patient records for Emily Garcia using email emily.garcia400@email.com to verify her current healthcare provider. Once you have confirmed her provider, proceed to verify Emily Garcia's insurance coverage, ensuring it is up-to-date and valid. This verification is crucial before any further steps can be taken in managing her healthcare needs.",
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
        user_id="P037",
        instruction="Your name is Robert Brown and your email is robert.brown551@email.com. You are polite, flexible. Search_patients for John Johnson using email john.johnson941@email.com to retrieve patient ID and insurance details.",
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
        user_id="P037",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are polite, patient, direct. First, use the search_patients tool to retrieve John Johnson's patient ID using his email (john.johnson941@email.com). Once you have his patient ID, proceed to use the search_patients tool to check if John Johnson has valid insurance information on file. After confirming the insurance details, use the book_appointment tool to schedule a routine check-up for John Johnson with Dr. Smith (Doctor ID: D101) at 10:00 AM on 15th November, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P037", "check_insurance": true}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P037", "doctor_id": "D101", "date": "2023-11-15", "time": "10:00", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are flexible, polite, patient, independent. Use `search_patients` to find patient ID for Robert Brown using email robert.brown731@email.com. Once you have the patient ID, use `think` to verify insurance details for the patient, ensuring coverage for the requested cardiology consultation service. After confirming insurance coverage, use `book_appointment` to schedule an appointment for Robert Brown with Dr. Smith during available hours at the downtown clinic, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown731@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P014", "service": "cardiology consultation"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P014", "doctor": "Dr. Smith", "location": "downtown clinic", "user_id": "P014"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are logical, polite, optimistic. First, search for patient Emily Brown using email emily.brown290@email.com to verify her identity and retrieve her patient ID. Once you have confirmed her patient ID, retrieve available appointment slots for Dr. Smith for that patient ID. This will help ensure that Emily can schedule her necessary follow-up appointment with Dr. Smith at a convenient time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com", "user_id": "P021"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Emily's patient ID is retrieved, I will proceed to check Dr. Smith's available appointment slots for her."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P031",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are direct, cautious. First, search for patient John Johnson's record using email john.johnson627@email.com to verify identity and authorization status. Once verified, search_patients for John Johnson's insurance details to confirm coverage eligibility for his upcoming appointment. After confirming insurance coverage, book_appointment for John Johnson with Dr. Smith (Doctor ID: D101) for a routine check-up during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "user_id": "P031"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson627@email.com", "user_id": "P031", "info_type": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson627@email.com", "doctor_id": "D101", "appointment_type": "routine check-up", "user_id": "P031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are logical, organized, independent. Use book_appointment to schedule an appointment for Robert Garcia with Dr. Smith during available hours, ensuring insurance verification is complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P005", "patient_name": "Robert Garcia", "doctor_name": "Dr. Smith", "appointment_type": "routine", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are logical, cautious, polite, optimistic. First, search for patient details using the search_patients tool with user ID \"david.brown214@email.com\" and verify authorization to ensure you have the correct access to his records. Once authorized, proceed to search for insurance verification details for David Brown using the available patient information and confirm his eligibility for a routine appointment. Finally, use the Book_appointment tool to schedule a routine appointment with Dr. Smith for David Brown on the next available date during office hours, ensuring that the appointment details are accurate before notifying him via email.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "david.brown214@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify authorization to access David Brown's records."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "david.brown214@email.com", "authorized": true}
            ),
            Action(
                name="think",
                kwargs={"thought": "Proceed to search for insurance verification details for David Brown."}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "david.brown214@email.com", "action": "insurance_verification"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm David Brown's eligibility for a routine appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P020", "patient_id": "P020", "doctor": "Dr. Smith", "appointment_type": "routine", "date": "next_available", "time": "office_hours"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are flexible, organized, polite, confident. search_patients with email \"robert.johnson197@email.com\" to retrieve patient ID and insurance details",
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
        user_id="P033",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are polite, direct, organized. Search for patient with email sarah.smith521@email.com to retrieve patient ID and insurance information",
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
        user_id="P006",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, independent. Think about David Williams' current healthcare needs and prioritize upcoming tasks to ensure he receives timely care. Next, consider the available doctors for David Williams based on his healthcare needs and select the most suitable option. Finally, book an appointment for David Williams with doctor D123 during available hours to address his immediate health concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P006", "patient_name": "David Williams"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Consider David Williams' healthcare needs and prioritize tasks accordingly."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Identify available doctors for David Williams based on his healthcare needs."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P006", "patient_id": "P006", "doctor_id": "D123", "appointment_time": "2023-10-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are patient, cautious. First, use search_patients to confirm David Brown's patient ID using his email david.brown214@email.com to ensure accurate identification. Once confirmed, use search_patients to verify David Brown's insurance details for appointment eligibility, ensuring he can receive care without issues. Finally, use think to check available hours for Dr. Smith, who is David Brown's preferred doctor, and book_appointment to schedule a routine check-up for David Brown with Dr. Smith during the available hours, ensuring a seamless healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "david.brown214@email.com", "info": "insurance"}
            ),
            Action(
                name="think",
                kwargs={"task": "check available hours for Dr. Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P020", "doctor": "Dr. Smith", "appointment_type": "routine check-up", "time": "available_hours", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are cautious, polite. Search for patient details using search_patients tool with patient ID P001 to retrieve contact information and medical history.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P003",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are cautious, organized, flexible. First, search for the patient ID for user Robert Brown (robert.brown551@email.com) to retrieve patient details. Once you have the patient ID, check the healthcare details to verify Robert Brown's insurance coverage. After confirming the insurance coverage, book an appointment for Robert Brown with Dr. Smith using the available slot on October 10, 2023, at 10:00 AM. Ensure that the insurance verification is complete before proceeding with the booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown551@email.com", "user_id": "P003"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID for Robert Brown from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's insurance coverage using the patient ID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance verification is complete before proceeding with booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P003", "doctor": "Dr. Smith", "datetime": "2023-10-10T10:00:00", "user_id": "P003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are patient, cautious. book_appointment for Sarah Brown with Dr. Thompson on 2023-11-15 at 10:00 AM",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P039", "patient_name": "Sarah Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P039", "patient_name": "Sarah Brown", "doctor_name": "Dr. Thompson", "appointment_date": "2023-11-15", "appointment_time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are confident, polite. Check healthcare details for user Michael Brown to confirm insurance coverage and eligibility for booking an appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are cautious, organized, polite. Begin by searching patients with user ID \"U602\" to retrieve Sarah Williams' healthcare details. Next, book an appointment for Sarah Williams with Dr. John Smith (ID: D456) for a routine check-up. After booking the appointment, think about the process to verify insurance coverage for Sarah Williams' scheduled appointment to ensure there are no issues with billing or coverage on the day of the visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "U602"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage before booking the appointment to ensure there are no issues with billing or coverage on the day of the visit."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "doctor_id": "D456", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are independent, confident. First, search_patients for patient ID matching david.brown214@email.com to verify authorization for accessing detailed information. Once authorization is confirmed, proceed to book_appointment for patient ID david.brown214@email.com with Dr. Smith for the next available routine check-up slot. This ensures that the patient's privacy is respected while efficiently scheduling their healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P020", "email": "david.brown214@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P020", "patient_id": "P020", "doctor": "Dr. Smith", "appointment_type": "routine check-up"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P001",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are flexible, independent, cautious. Think about Sarah Williams' previous healthcare appointments to assess her preferred times and doctors. Next, consider available doctors matching Sarah Williams' healthcare needs and insurance coverage to ensure compatibility. Finally, think about doctor availability to find open appointment slots that fit Sarah Williams' schedule preferences, ensuring a smooth booking process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Sarah Williams' previous appointments to determine her preferred times and doctors."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Identify available doctors who match Sarah Williams' healthcare needs and insurance coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check doctor availability to find open appointment slots that fit Sarah Williams' schedule preferences."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P001", "patient_name": "Sarah Williams", "doctor_id": "D123", "appointment_time": "2023-11-15T10:00:00", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P037",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are organized, logical, optimistic. First, search for patient records of John Johnson using email john.johnson941@email.com to verify insurance details. Once the insurance details are verified, proceed to book an appointment for John Johnson with Dr. Smith for a general check-up at the earliest available time slot. This sequence ensures that John Johnson's insurance is confirmed before scheduling his appointment, streamlining the process and preventing any potential issues during his visit.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson941@email.com", "user_id": "P037"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "john.johnson941@email.com", "doctor_name": "Dr. Smith", "appointment_type": "general check-up", "user_id": "P037"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P047",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are polite, patient. Search_patients with email sarah.davis118@email.com to retrieve Sarah Davis's patient ID and details. Think to verify Sarah Davis's insurance details and ensure they are up-to-date for appointment booking. Search for available appointment slots with Sarah Davis's primary care physician within the next two weeks.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.davis118@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Sarah Davis's insurance details to ensure they are up-to-date before booking an appointment."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available appointment slots with Sarah Davis's primary care physician within the next two weeks."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are organized, flexible, direct, independent. First, search_patients with email robert.johnson741@email.com to retrieve the patient ID and authorization status, ensuring you have the correct information to proceed. Next, think to verify the insurance status for the patient ID retrieved from search_patients, as confirming insurance coverage is crucial for booking medical services. Finally, book_appointment for the patient ID with the appropriate doctor ID during available hours if the insurance is verified, ensuring the patient receives the necessary medical attention promptly.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and authorization status from the search_patients response to proceed with insurance verification."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the insurance status for the retrieved patient ID to ensure coverage before booking an appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor_id": "appropriate_doctor_id", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are cautious, optimistic. First, search_patients for Sarah Miller's medical history to assess the urgency of her appointment needs. Next, think to determine if Sarah Miller requires a routine or emergency appointment based on the information gathered from her medical history. Finally, book_appointment for Sarah Miller with doctor ID \"D123\" on the next available date for a routine check-up, ensuring that her health needs are addressed promptly and effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P046", "patient_name": "Sarah Miller", "doctor_id": "D123", "appointment_type": "routine"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are cautious, flexible, logical, direct. Search_patients for patient_id to check insurance details and verify coverage. Think to determine if the required appointment is routine or emergency based on patient symptoms. Book_appointment for patient_id with doctor_id at selected time_slot, ensuring insurance verification is completed.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"patient_id": "P007"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check the patient's symptoms to determine if the appointment is routine or emergency."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "D123", "time_slot": "2023-10-15T10:00:00", "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are patient, cautious. Search for patient Michael Miller using email michael.miller534@email.com to verify identity and retrieve patient ID.",
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
        user_id="P042",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are cautious, logical. Search_patients with email maria.miller855@email.com to retrieve patient ID and insurance details, then think to verify insurance details for the retrieved patient ID to ensure coverage. This process is crucial to confirm that the patient is eligible for the medical services they need before proceeding with any appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.miller855@email.com"}
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
        instruction="Your name is Lisa Jones and your email is lisa.jones889@email.com. You are logical, polite, direct, optimistic. Search for patient information for Robert Johnson using his email (robert.johnson741@email.com) to verify identity and insurance details. Once his insurance is verified and eligibility for healthcare services is confirmed, proceed to book an appointment for Robert Johnson with Dr. Smith (Doctor ID: D001) for a routine check-up during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson741@email.com", "doctor_id": "D001", "appointment_type": "routine check-up", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are independent, flexible, cautious. Book_appointment for Robert Brown with Dr. Smith, ID D789, on his preferred date and time, ensuring it aligns with the doctor's available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "patient_name": "Robert Brown", "doctor_id": "D789", "appointment_date": "2023-11-15", "appointment_time": "10:00"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are polite, confident. First, search_patients with user email robert.johnson741@email.com to retrieve patient ID and insurance details. Once you have obtained the insurance information, think to verify insurance eligibility for Robert Johnson based on the retrieved insurance details. This process ensures that Robert Johnson is eligible for coverage for his upcoming medical appointment, thereby preventing any potential issues with billing or treatment authorization.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details for Robert Johnson from the search_patients response."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance eligibility for Robert Johnson using the retrieved insurance details to ensure coverage for his upcoming medical appointment."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Maria Miller and your email is maria.miller855@email.com. You are logical, organized, confident. \"search_patients for Robert Garcia using email robert.garcia592@email.com to retrieve patient ID and insurance details\"",
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
        user_id="P006",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are patient, confident, organized. search_patients to find David Williams' preferred doctor or previous consultation history",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P006", "patient_name": "David Williams"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are cautious, logical, organized, direct. Think about Maria Johnson's upcoming healthcare needs and review her recent medical history to ensure comprehensive care planning. After thoroughly understanding her medical background, think about potential doctors available for Maria Johnson's healthcare requirements, ensuring they align with her specific needs and preferences.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P023", "patient_name": "Maria Johnson"}
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
        instruction="Your name is Maria Johnson and your email is maria.johnson759@email.com. You are independent, patient, optimistic. search_patients with email \"lisa.williams792@email.com\" to retrieve patient ID and insurance details",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are cautious, polite, logical, direct. Search for Patient ID for Robert Johnson using email robert.johnson741@email.com in the healthcare system. Once you have retrieved the Patient ID, proceed to retrieve healthcare details for this Patient ID to check medical history and insurance information. After confirming the insurance details, verify the insurance coverage to ensure eligibility for appointment booking.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com", "user_id": "P024"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the Patient ID for Robert Johnson using the provided email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once the Patient ID is retrieved, proceed to get healthcare details for this Patient ID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance coverage to ensure eligibility for appointment booking."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are optimistic, organized, confident. Use search_patients with user ID sarah.williams602 to retrieve Sarah Williams' patient record and verify insurance status. Once insurance verification is complete, use book_appointment to schedule a routine check-up with Dr. John Smith (Doctor ID: D102) for Sarah Williams on October 15, 2023, at 10:00 AM. Finally, use search_patients to confirm Sarah Williams' contact information and preferred method of communication for appointment reminders to ensure she receives timely notifications about her upcoming appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "sarah.williams602"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P018", "doctor_id": "D102", "patient_id": "P018", "date": "2023-10-15", "time": "10:00"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "sarah.williams602"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P021",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are independent, flexible. Search_patients using email emily.brown290@email.com to verify patient identity and retrieve recent visit history. Then, think to assess if Emily Brown requires any follow-up appointments based on recent visit history. This will ensure that Emily receives timely care and any necessary interventions are scheduled promptly, maintaining the high standard of patient care our healthcare facility is known for.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.brown290@email.com"}
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
        user_id="P005",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are direct, logical, flexible, independent. Search_patients for Robert Garcia using email robert.garcia592@email.com to retrieve his patient ID and medical history.",
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
        user_id="P048",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are direct, confident, logical, independent. First, use search_patients to verify if Michael Miller (michael.miller534@email.com) is already registered in the healthcare system. Once confirmed, use think to ensure Michael Miller's insurance details are up-to-date and valid for appointment booking, as this is crucial for a seamless scheduling process. Finally, use book_appointment to schedule an appointment for Michael Miller with Dr. Smith (ID: D1023) on the next available slot, ensuring he receives timely care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify insurance details for Michael Miller to ensure they are up-to-date and valid for appointment booking."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "michael.miller534@email.com", "doctor_id": "D1023", "user_id": "P048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P045",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are independent, confident, polite. Search_patients with email lisa.williams792@email.com to retrieve patient ID and insurance information. Then, think to verify insurance details for the patient ID retrieved to ensure coverage is valid for upcoming medical services.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.williams792@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the patient ID retrieved to ensure coverage is valid for upcoming medical services."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Michael Brown and your email is michael.brown235@email.com. You are logical, patient, independent, cautious. First, verify your insurance details to ensure coverage for appointments within the healthcare system. Next, search for available primary care doctors and identify Dr. Smith as an option. Then, book an appointment for yourself with Dr. Smith on the next available date and time. Finally, confirm the appointment booking details with yourself via email at michael.brown235@email.com to ensure all information is accurate and complete.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P016"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "insurance_verification": true}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "search_criteria": "primary care doctor"}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "doctor_name": "Dr. Smith"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P016", "doctor_name": "Dr. Smith", "appointment_type": "routine", "next_available": true}
            ),
            Action(
                name="search_patients",
                kwargs={"user_id": "P016", "confirmation_email": "michael.brown235@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P023",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are cautious, patient, logical. Begin by using the search_patients task with the parameter user_email=maria.johnson759@email.com to retrieve Maria Johnson's user ID and check her authorization status. Once you have confirmed her user ID as U001, proceed to the think task with the parameter user_id=U001 to determine the most suitable doctor for her upcoming consultation. After identifying the appropriate doctor, ensure Maria Johnson's insurance status is verified by using the think task with the parameter insurance_status=verified to confirm that her insurance covers the consultation. Finally, book her appointment by using the book_appointment task with the parameters user_id=U001, doctor_id=D123, date=2023-10-15, time=10:00, and appointment_type=consultation to secure her slot for the consultation.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.johnson759@email.com"}
            ),
            Action(
                name="think",
                kwargs={"user_id": "U001"}
            ),
            Action(
                name="think",
                kwargs={"insurance_status": "verified"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "U001", "doctor_id": "D123", "date": "2023-10-15", "time": "10:00", "appointment_type": "consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P042",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are cautious, independent, polite. Begin by conducting a search_patients for user Maria Miller with email maria.miller855@email.com to retrieve patient ID and insurance details. Once you have obtained the patient ID, think to verify insurance coverage for the retrieved patient ID to ensure that the patient is eligible for the required services. After confirming the insurance coverage, proceed to book_appointment for the patient ID with doctor D123 for the earliest available slot, ensuring that the insurance has been verified to avoid any future complications.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P042", "name": "Maria Miller", "email": "maria.miller855@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and insurance details from the search_patients response. Verify the insurance coverage for the retrieved patient ID to ensure eligibility for services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P042", "patient_id": "P042", "doctor_id": "D123", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P014",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are direct, organized. Search for patient information for Robert Brown using email robert.brown731@email.com to verify identity and retrieve patient ID. Once verified, think to determine the next steps needed for scheduling a routine check-up appointment for Robert Brown, considering his medical history and preferred timings to ensure a smooth and efficient scheduling process.",
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
        user_id="P031",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are polite, direct, patient. First, search_patients for John Johnson's medical history to review past appointments and treatments, ensuring all information is up-to-date. Once you have verified the medical history, proceed to book_appointment for John Johnson with Dr. Smith (ID: D100) for a cardiology consultation during available hours, ensuring continuity of care and addressing any ongoing health concerns.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P031", "patient_name": "John Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P031", "patient_name": "John Johnson", "doctor_id": "D100", "specialty": "cardiology", "appointment_type": "consultation"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P028",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are confident, polite, organized, independent. Book an appointment with Dr. Smith (doctor ID: D123) for David Miller using the book_appointment tool, ensuring it aligns with available slots.",
        actions=[
            Action(
                name="book_appointment",
                kwargs={"doctor_id": "D123", "patient_id": "P028", "appointment_type": "routine", "user_id": "P028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are cautious, optimistic, confident. First, use search_patients with parameters: user_email=\"maria.smith554@email.com\" to retrieve your patient ID and medical records. Then, use think to identify the type of appointment you need based on your medical records, such as a follow-up consultation or a specialist visit. Finally, use search_patients with parameters: appointment_type=<Identified Appointment Type> to find available doctors who can accommodate your needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={}
            ),
            Action(
                name="search_patients",
                kwargs={"appointment_type": "<Identified Appointment Type>"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P017",
        instruction="Your name is Robert Brown and your email is robert.brown624@email.com. You are patient, optimistic, logical. search_patients with email \"robert.brown624@email.com\" to verify patient identity and retrieve patient ID",
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
        user_id="P019",
        instruction="Your name is David Williams and your email is david.williams693@email.com. You are independent, optimistic, direct, flexible. Search_patients with email 'maria.smith256@email.com' to retrieve patient ID and verify authorization. Then, search_patients with patient ID retrieved to check for any pending lab results. If there are abnormal lab results indicating a need for further evaluation, think to determine the necessity of scheduling a follow-up appointment based on lab results.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P019"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine necessity of scheduling a follow-up appointment based on lab results"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P027",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are optimistic, organized, patient, direct. First, use \"search_patients\" to retrieve the medical history for user Robert Johnson (robert.johnson197@email.com) with proper authorization. Next, use \"think\" to verify insurance coverage for Robert Johnson before booking any appointments. Once insurance coverage is confirmed, use \"book_appointment\" to schedule a non-emergency appointment for Robert Johnson with Dr. Smith at 3 PM on the next available date.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson197@email.com", "user_id": "P027"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify insurance coverage for Robert Johnson"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "robert.johnson197@email.com", "doctor_name": "Dr. Smith", "appointment_time": "15:00", "appointment_date": "next_available", "user_id": "P027"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are polite, logical, organized. First, search for patient Emily Davis using her email emily.davis525@email.com to retrieve her patient ID. Once you have her patient ID, verify that Emily Davis's insurance covers appointments with doctor D123. After confirming the insurance coverage, proceed to book an appointment for Emily Davis with doctor D123 on October 18, 2023, at 10:00 AM. Ensure that the insurance verification is complete before finalizing the appointment.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com", "user_id": "P032"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Emily Davis's patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Emily Davis's insurance coverage for appointments with doctor D123."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure insurance verification is complete before proceeding to book the appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor_id": "D123", "date": "2023-10-18", "time": "10:00", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P019",
        instruction="Your name is Emily Davis and your email is emily.davis525@email.com. You are organized, logical. First, search_patients with email \"maria.smith256@email.com\" to retrieve patient ID and insurance information. Once you have verified the insurance details for the patient ID retrieved from search_patients, proceed to book_appointment for the patient during the doctor's available hours, ensuring to prioritize if it is an emergency. This process is crucial for maintaining efficient patient care and ensuring that all necessary information is accurate and up-to-date before scheduling medical appointments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith256@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P019", "insurance_verified": true, "emergency": false, "user_id": "P019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Sarah Brown and your email is sarah.brown753@email.com. You are optimistic, independent, flexible, direct. Your task is to search for patient Robert Johnson using his email robert.johnson741@email.com to retrieve his patient ID. Once you have the patient ID, verify his insurance details to ensure coverage for his upcoming cardiology appointments. After confirming the insurance coverage, search for available doctors specializing in cardiology for Robert Johnson's patient ID to facilitate his continued care.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for the retrieved patient ID."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Search for available cardiology specialists for Robert Johnson's patient ID."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P020",
        instruction="Your name is Sarah Brown and your email is sarah.brown426@email.com. You are optimistic, confident, direct. Search for patient records using user email david.brown214@email.com to retrieve patient ID and insurance details.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "david.brown214@email.com", "user_id": "P020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are independent, optimistic, patient, polite. Use search_patients to find patient records for Maria Smith based on her email (maria.smith554@email.com) to ensure her information is up-to-date. Then, use book_appointment to schedule a routine check-up for Maria Smith with Dr. John Doe, ID D102, at 2 PM on March 15, 2024, ensuring her healthcare needs are met in a timely manner.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "maria.smith554@email.com", "doctor_id": "D102", "date": "2024-03-15", "time": "14:00", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is John Johnson and your email is john.johnson699@email.com. You are confident, polite, cautious. \"search_patients to retrieve Robert Garcia's patient ID using email robert.garcia592@email.com\"",
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
        user_id="P023",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are optimistic, logical, organized. Use search_patients with parameters: user_email=maria.johnson759@email.com to retrieve patient ID and insurance details. Then, use think to verify insurance coverage for the patient ID retrieved in the previous task. Once insurance coverage is confirmed, proceed to book an appointment for the patient with parameters: patient_id=PAT456, doctor_id=DOC123, appointment_time=10:00 AM, date=2023-11-15. This ensures that the patient can receive timely medical care without any insurance issues.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "maria.johnson759@email.com"}
            ),
            Action(
                name="think",
                kwargs={"patient_id": "P023"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P023", "doctor_id": "DOC123", "appointment_time": "10:00 AM", "date": "2023-11-15"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is John Johnson and your email is john.johnson941@email.com. You are cautious, patient, direct. Search for patient John Johnson using email john.johnson699@email.com to retrieve patient ID and medical history. Check patient John Johnson's medical history to determine if an emergency appointment is necessary. Based on the emergency status, prioritize and search for the earliest available appointment slot.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "john.johnson699@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID and medical history for John Johnson using the provided email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check the medical history to determine if an emergency appointment is necessary."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P029", "patient_id": "P029", "is_emergency": true, "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P005",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are patient, direct, logical, optimistic. Search for patient records using the query \"Robert Garcia\" to verify existing healthcare details. Once you have retrieved the patient ID, use it to access Robert Garcia's insurance information for verification. This will ensure that all patient data is accurate and up-to-date before proceeding with any further healthcare actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"query": "Robert Garcia", "user_id": "P005"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P048",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are polite, optimistic. Search for patient records using the email michael.miller534@email.com to verify identity and retrieve patient ID. Once you have confirmed Michael Miller's identity and gathered his patient ID, think to determine the appropriate specialist for an appointment based on Michael Miller's current healthcare needs, ensuring that the specialist can address his specific conditions effectively.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.miller534@email.com", "user_id": "P048"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Michael Miller's patient ID is retrieved, evaluate his healthcare needs to determine the appropriate specialist for his conditions."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P018",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are independent, direct, logical. Search for patient ID for Sarah Williams using email sarah.williams602@email.com for verification, and then check healthcare details for the retrieved patient ID to confirm insurance status. This process is crucial to ensure that Sarah Williams' insurance coverage is active and valid, which is necessary before proceeding with any medical appointments or treatments.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.williams602@email.com", "user_id": "P018"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the patient ID for Sarah Williams from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the retrieved patient ID to check healthcare details and confirm insurance status."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P039",
        instruction="Your name is Sarah Williams and your email is sarah.williams602@email.com. You are patient, flexible. First, search for patient records using Sarah Brown's email (sarah.brown426@email.com) to verify her patient ID and insurance status. Once insurance verification is completed, book an appointment for Sarah Brown with Dr. Smith on the next available slot. Ensure that all necessary patient details are accurately recorded to facilitate a smooth appointment process.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown426@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P039", "doctor": "Dr. Smith", "appointment_type": "routine", "user_id": "P039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is John Johnson and your email is john.johnson627@email.com. You are organized, logical, flexible. Search for patient details using email maria.smith554@email.com to verify identity and retrieve patient ID. Then, verify insurance status for the retrieved patient ID to ensure coverage for upcoming appointments. This process is crucial to confirm the patient's eligibility for healthcare services and to facilitate a smooth scheduling experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance status using the retrieved patient ID."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P007",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are independent, flexible, logical, confident. Search for doctor availability in the system using Emily Jones's insurance network and healthcare needs, and then book an appointment for Emily Jones with Dr. Smith (Doctor ID: D123) for a routine check-up, ensuring it aligns with available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P007", "patient_name": "Emily Jones", "doctor_id": "D123", "appointment_type": "routine check-up", "insurance_network": "verified"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P029",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are flexible, patient. Search for patient details of John Johnson using the email john.johnson699@email.com to verify insurance information. Once you have confirmed the insurance details, verify insurance details for John Johnson to ensure coverage for the appointment with Dr. Smith. This process is crucial to ensure that John Johnson's appointment is covered and there are no issues on the day of the appointment.",
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
        user_id="P007",
        instruction="Your name is Maria Smith and your email is maria.smith256@email.com. You are logical, confident, direct. First, search_patients with email emily.jones379@email.com to retrieve her patient ID and authorization status. Once you have confirmed her authorization status, proceed to book_appointment for Emily Jones with the selected doctor and timeslot, ensuring that insurance verification is complete. This process is crucial to ensure that Emily's healthcare needs are met efficiently and without any administrative delays.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.jones379@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P007", "doctor_id": "D456", "timeslot": "2023-11-15T10:00:00", "insurance_verified": true, "user_id": "P007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P006",
        instruction="Your name is Sarah Davis and your email is sarah.davis118@email.com. You are patient, flexible, independent. Use `search_patients` to locate patient David Williams by email (david.williams693@email.com) for authorization verification.",
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
        user_id="P046",
        instruction="Your name is Sarah Williams and your email is sarah.williams853@email.com. You are logical, polite. search_patients: Retrieve patient ID and insurance details for Sarah Miller (sarah.miller381@email.com)",
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
        user_id="P017",
        instruction="Your name is Robert Brown and your email is robert.brown731@email.com. You are polite, confident. First, search for patient information for Robert Brown (robert.brown624@email.com) using the search_patients tool with authorization token \"AUTH12345\" to ensure you have the correct medical records. Next, check Robert Brown's medical history and any existing conditions using the same search_patients tool and authorization token to understand his current health status. Finally, verify Robert Brown's eligibility for a routine check-up using the think tool with his insurance details and medical history. Once eligibility is confirmed, proceed to book an appointment for Robert Brown with doctor_id \"D456\" on date \"2023-11-15\" at an available time slot using the book_appointment tool with insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com", "authorization_token": "AUTH12345"}
            ),
            Action(
                name="search_patients",
                kwargs={"email": "robert.brown624@email.com", "authorization_token": "AUTH12345"}
            ),
            Action(
                name="think",
                kwargs={"insurance_details": "provided_insurance_details", "medical_history": "retrieved_medical_history"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P017", "doctor_id": "D456", "date": "2023-11-15", "time_slot": "available_time_slot", "insurance_verification": "verified"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is Robert Johnson and your email is robert.johnson197@email.com. You are optimistic, polite, flexible, direct. Search for patient details for Michael Brown to verify insurance and authorization status.",
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
        user_id="P005",
        instruction="Your name is Michael Miller and your email is michael.miller534@email.com. You are logical, patient, optimistic, organized. Use search_patients with parameters: user_email=robert.garcia592@email.com to retrieve patient ID and insurance status. Once you have confirmed that the insurance is verified, book an appointment using book_appointment with parameters: patient ID, doctor ID, date '2023-11-15', time '10:00 AM', ensuring it falls within available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_email": "robert.garcia592@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P005", "doctor_id": "D456", "date": "2023-11-15", "time": "10:00 AM"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P050",
        instruction="Your name is Robert Johnson and your email is robert.johnson741@email.com. You are confident, organized, patient. Search for patient details using email lisa.jones889@email.com to verify identity and check insurance information. Once verified, proceed to check healthcare details for Lisa Jones to confirm her current insurance coverage and eligibility for appointment booking. This ensures that all necessary information is accurate and up-to-date before proceeding with any further actions.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "lisa.jones889@email.com", "user_id": "P050"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Jones and your email is emily.jones379@email.com. You are patient, cautious, flexible. First, search_patients for Robert Johnson using email robert.johnson741@email.com to verify his patient record and authorization status. Once his record is confirmed and authorization is verified, book_appointment for Robert Johnson with Dr. Smith for a routine check-up, ensuring it falls within available hours. This sequence ensures that Robert's information is accurate and his appointment is scheduled efficiently, contributing to a smooth healthcare experience.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_name": "Robert Johnson", "doctor_name": "Dr. Smith", "appointment_type": "routine check-up", "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P032",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are flexible, organized, optimistic. Search_patients with email emily.davis525@email.com to retrieve patient ID and authorization status. Think to verify insurance details for patient Emily Davis using patient ID retrieved, ensuring that her insurance covers the necessary services. Book_appointment for patient ID of Emily Davis with the selected doctor ID at the earliest available time, coordinating with her insurance coverage to avoid any unexpected expenses.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "emily.davis525@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve patient ID and authorization status for Emily Davis."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify insurance details for Emily Davis using the retrieved patient ID."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P032", "doctor_id": "selected_doctor_id", "user_id": "P032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P016",
        instruction="Your name is David Brown and your email is david.brown214@email.com. You are direct, optimistic, flexible. Use search_patients to retrieve Michael Brown's medical history by searching with email michael.brown235@email.com. Then, use think to verify if Michael's insurance details are up-to-date and valid for the healthcare services needed. Once the insurance verification is complete, use book_appointment to schedule a routine check-up for Michael Brown with doctor ID D456 during available hours.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "michael.brown235@email.com"}
            ),
            Action(
                name="think",
                kwargs={"task": "Verify if Michael Brown's insurance details are up-to-date and valid for healthcare services."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_email": "michael.brown235@email.com", "doctor_id": "D456", "appointment_type": "routine check-up", "user_id": "P016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P036",
        instruction="Your name is Maria Smith and your email is maria.smith554@email.com. You are patient, direct, polite. Book_appointment for Emily Garcia with doctor ID D456 at 10:00 AM on the next available weekday, subject to insurance verification.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia"}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P036", "patient_name": "Emily Garcia", "doctor_id": "D456", "time": "10:00 AM", "date": "next_weekday", "insurance_verified": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P024",
        instruction="Your name is Emily Brown and your email is emily.brown290@email.com. You are organized, patient, cautious. First, use search_patients to locate the patient ID for Robert Johnson using the email robert.johnson741@email.com. Once you have the patient ID, use search_patients to retrieve Robert Johnson's insurance information and verify his coverage details to ensure there are no issues. After confirming the insurance coverage, use book_appointment to schedule a routine appointment for Robert Johnson with Dr. Smith at 2:00 PM on 2023-11-15, making sure that the insurance is verified.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "robert.johnson741@email.com"}
            ),
            Action(
                name="search_patients",
                kwargs={"patient_id": "P024", "info_type": "insurance"}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P024", "doctor": "Dr. Smith", "time": "14:00", "date": "2023-11-15", "insurance_verified": true, "user_id": "P024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P046",
        instruction="Your name is Emily Garcia and your email is emily.garcia400@email.com. You are logical, cautious. Search_patients for user Sarah Miller with email sarah.miller381@email.com to verify existing patient records and retrieve patient ID. Once the patient ID is confirmed, search Sarah Miller's medical history to provide to the healthcare provider before the appointment. This ensures that the doctor has all necessary information for a comprehensive routine check-up.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"user_id": "P046", "name": "Sarah Miller", "email": "sarah.miller381@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P025",
        instruction="Your name is Lisa Williams and your email is lisa.williams792@email.com. You are direct, patient. Retrieve insurance details for user Sarah Brown (sarah.brown753@email.com) to verify coverage, ensuring she is eligible for routine check-ups. Once coverage is confirmed, search for available doctors in Sarah Brown's network who can provide routine check-ups and book a routine appointment with Dr. John Smith (Doctor ID: D102) for her at the earliest available time.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "sarah.brown753@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Sarah Brown's insurance details to verify coverage for routine check-ups."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure Sarah Brown is eligible for routine check-ups under her insurance coverage."}
            ),
            Action(
                name="think",
                kwargs={"thought": "After confirming insurance coverage, search for available doctors in Sarah Brown's network."}
            ),
            Action(
                name="book_appointment",
                kwargs={"user_id": "P025", "doctor_id": "D102", "appointment_type": "routine", "patient_email": "sarah.brown753@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="P013",
        instruction="Your name is Sarah Miller and your email is sarah.miller381@email.com. You are optimistic, polite, logical, organized. First, search for patient Maria Smith using email maria.smith554@email.com to retrieve her patient ID and authorization status. Once you have confirmed her identity and authorization, proceed to verify Maria Smith's insurance details to ensure coverage for her upcoming appointment. After confirming her insurance coverage, book an appointment for Maria Smith with the available general practitioner, ensuring it is within the doctor's available hours. This sequence ensures that Maria's visit is authorized, covered, and scheduled efficiently, providing a seamless experience for her healthcare needs.",
        actions=[
            Action(
                name="search_patients",
                kwargs={"email": "maria.smith554@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve Maria Smith's patient ID and authorization status from the search results."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Maria Smith's insurance details using her patient ID to ensure coverage for her upcoming appointment."}
            ),
            Action(
                name="book_appointment",
                kwargs={"patient_id": "P013", "doctor_id": "available_gp_id", "appointment_time": "chosen_time_within_doctor_hours", "user_id": "P013"}
            ),
        ],
        outputs=[]
    ),
]
