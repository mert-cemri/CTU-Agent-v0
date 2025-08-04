"""
Generated tasks for telecom domain.
Generated at: 2025-08-04T01:56:09.822800
Total tasks: 580
"""

from tau_types import Task, Action

TASKS_TRAIN = [
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are flexible, independent, polite. Please begin by using the Lookup_customer_by_phone task to retrieve Linda's account information using her phone number. Once you have accessed her account, proceed with the Get_customer_lines task to list all active lines associated with Linda Davis's account. This will help us ensure that all active lines are correctly accounted for and managed under her account in our telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda's phone number", "user_id": "TC048"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "Linda's account ID", "user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are direct, optimistic, organized. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify the identity of Robert Jones. Once verified, get_bill_details for account ID \"A6549\" to review any outstanding charges he may have. If there are unpaid charges, proceed to suspend_line for line ID \"L9876\" due to non-payment, ensuring that Robert Jones is notified of the suspension. If Robert Jones needs further assistance with payment options, transfer_to_human_agents with context \"Customer Robert Jones needs assistance with payment options\" for additional support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC119"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A6549", "user_id": "TC119"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "user_id": "TC119"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "Customer Robert Jones needs assistance with payment options", "user_id": "TC119"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are organized, logical, flexible, direct. First, perform a Lookup_customer_by_phone using the phone number associated with Mary Davis to verify her account identity. Once her identity is confirmed, proceed to Get_customer_lines for Mary Davis's account to list all active lines. This will help ensure that we have the most accurate and up-to-date information about her account status and services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Davis's phone number", "user_id": "TC020"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC020", "user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are organized, confident, flexible, independent. First, lookup_customer_by_phone with phone_number '555-0123' to verify Linda Miller's identity for account access. Once her identity is confirmed, proceed to get_customer_lines with customer_id 'C12345' to list all active lines associated with Linda Miller's account. This will ensure you have the necessary information to assist her with any inquiries regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC091"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC091", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are cautious, independent, logical, confident. First, use the lookup_customer_by_phone with phone_number=\"555-0183\" to verify the identity of Michael Jones, ensuring that you are interacting with the correct customer. Once verification is successful, proceed to get_customer_lines for customer_id=\"C12345\" to view all active lines associated with Michael Jones. After identifying the active lines, use get_line_details for line_id=\"L67890\" to check the current plan and usage details. This will allow you to analyze whether a plan change could be beneficial for Michael Jones based on his current usage and charges.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0183"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC042"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are independent, patient, polite, direct. First, lookup Mary's account using her email mary.johnson4713@email.com to verify her identity. Once her identity is confirmed, check if any lines are currently suspended in Mary's account. This will help ensure that we have accurate information before proceeding with any further actions related to her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.johnson4713@email.com", "user_id": "TC071"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "mary.johnson4713@email.com", "user_id": "TC071"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are independent, cautious, patient, logical. First, lookup_customer_by_phone with phone_number=555-0123 to verify the customer's identity for account access. Once identity is confirmed, proceed to get_bill_details for customer_id=CU12345 to review the current billing status and any outstanding charges. This will ensure you have the necessary information to assist the customer effectively with their telecom account inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC006"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC006", "user_id": "TC006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are patient, direct, polite. Please verify the identity of Robert Brown using his email (robert.brown4015@email.com) to access his account details. Once his identity is confirmed, proceed to get the bill details for Robert Brown's account to determine the current billing cycle and any outstanding balance. This information will help ensure that Robert is informed about his billing status and can facilitate any further discussions he may wish to have regarding his account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown4015@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are direct, polite, organized, cautious. First, lookup_customer_by_phone with phone_number: \"555-1234\" to verify Michael Garcia's identity and retrieve customer ID. Once you have confirmed the customer ID, proceed to get_customer_lines with customer_id: \"C789\" to list all active lines under Michael Garcia's account. Finally, use get_line_details with line_id: \"L456\" to view current plan and usage details for Michael Garcia's primary line, ensuring you have the necessary information before discussing any potential plan adjustments with the customer.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC051"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Mary Miller and your email is mary.miller8461@email.com. You are polite, cautious. First, lookup_customer_by_phone with phone number \"555-1234\" to verify Robert Johnson's identity. Once verified, proceed to get_bill_details for the customer's ID to review his outstanding balance and payment history. If there is an outstanding balance, transfer_to_human_agents with the customer ID and issue details for a payment arrangement discussion to ensure the matter is resolved promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC072"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC072", "user_id": "TC072"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC072", "issue_details": "Outstanding balance requires payment arrangement discussion", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are independent, flexible, direct. Use lookup_customer_by_phone with phone number \"123-456-7890\" to verify Mary Johnson's identity. With verified identity, use get_customer_lines for user Mary Johnson to list all active lines. Select line L123 from the list and use get_line_details to retrieve the current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC071"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are logical, patient, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of Robert Williams, who has reported an issue with his billing. Once his identity is confirmed, proceed to get_bill_details for customer ID C001 to review the last billing cycle charges and ensure there are no discrepancies. This will help in understanding any payment issues before taking further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC080"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC080", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are confident, organized, optimistic. First, get line details for line ID L5678 to check the current plan and status, ensuring you have the correct information before proceeding. Next, process a plan change for line L5678 to a higher data plan effective next billing cycle, as the customer has requested an upgrade due to increased data usage needs. Finally, calculate the pro-rated charges for the plan change for customer ID, so the customer is accurately billed for the transition period.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC141", "operation": "plan_change", "line_id": "L5678", "new_plan": "higher_data_plan", "effective_date": "next_billing_cycle"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are organized, confident. First, use lookup_customer_by_phone with phone number 555-1234 to verify Linda Davis's identity and retrieve her customer ID. Once you have confirmed her identity and obtained her customer ID, use get_customer_lines with customer ID C4055 to list all active lines under Linda Davis's account. Finally, use get_line_details with line ID L6789 to check the current plan and data usage for Linda Davis's primary line. This sequence will help you ensure that Linda Davis's account details are accurate and up-to-date, which is essential for providing her with the best service options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC048"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC048", "user_id": "TC048"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L6789", "user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Mary Miller and your email is mary.miller8461@email.com. You are optimistic, logical, independent, polite. First, lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify the identity of Robert Jones, who has reported an issue with his mobile service. Once his identity is confirmed, get_customer_lines for customer_id: \"C5323\" to retrieve all active lines associated with his account. After identifying the specific line in question, get_line_details for line_id: \"L98765\" to check the current plan and usage, ensuring that his service is functioning correctly and identifying if there are any discrepancies or issues that need to be addressed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC123"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L98765"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC061",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are cautious, logical, confident, patient. First, lookup_customer_by_phone with phone_number: \"555-1234\" to verify the identity of Patricia Davis. Once her identity is confirmed, proceed to get_customer_lines for customer_id: \"patricia.davis1886\" to retrieve all active lines. This will allow us to ensure that we have the correct information before taking further action on her account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC061"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC061", "user_id": "TC061"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are polite, optimistic, direct, confident. First, lookup_customer_by_phone with phone number '555-123-4567' to verify Jennifer Brown's account. Then, get_line_details for line ID 'L5678' to check current plan and usage. Finally, think about whether Jennifer Brown's usage exceeds her current plan limits.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC062"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC062"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Consider whether Jennifer Brown's usage exceeds her current plan limits based on the retrieved line details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are logical, polite, flexible. First, lookup_customer_by_phone using Linda Garcia's associated phone number to retrieve her customer ID. Once you have obtained her customer ID, proceed to get_customer_lines for Linda Garcia's account to list all active lines. With the list of active lines, focus on line ID L5678 and get_line_details to verify its eligibility for a plan upgrade.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Garcia's phone number", "user_id": "TC127"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC127", "user_id": "TC127"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are confident, patient, polite. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify the identity of Mary Miller. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C8461\" to retrieve all active lines associated with Mary Miller. This process will help ensure that you have the correct customer information before reviewing her account details in a telecom context.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC102", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are polite, independent, confident. Verify the identity of user Michael Davis using the email michael.davis7894@email.com to ensure secure account access. Once verified, proceed to lookup the customer by phone to retrieve the customer ID associated with Michael Davis. After obtaining the customer ID, get the customer lines to list all active lines under his account. This sequence of actions is crucial to provide accurate information and support for Michael Davis's telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.davis7894@email.com", "user_id": "TC069"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC069", "user_id": "TC069"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are independent, confident. First, perform a lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Linda Miller's identity. Once verified, proceed to get_bill_details for user_id \"LM7970\" to review the latest billing statement and payment status, ensuring Linda is informed about her telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "LM7970"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are logical, direct. First, lookup_customer_by_phone with phone_number=555-1234 to verify customer identity for Jennifer Jones. Once verified, proceed to get_customer_lines with customer_id=JJ7047 to retrieve all active lines for Jennifer Jones, ensuring you have a comprehensive view of her account. Finally, get_line_details with line_id=L9876 to check current plan and usage details for the primary line, allowing you to assess if there are any potential data overage charges that need to be addressed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC130"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are logical, organized. First, perform a lookup_customer_by_phone using the phone number provided by Patricia Miller to verify her identity. Once her identity is confirmed, proceed to get_customer_lines for Patricia Miller to retrieve all active lines on her account. This sequence ensures that Patricia's identity is verified before accessing sensitive account information, which is crucial for maintaining security and privacy in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_by_Patricia_Miller", "user_id": "TC028"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC028", "user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are organized, polite. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of user Michael Johnson. Once verified, proceed to get_customer_lines for customer_id \"CUST12345\" to retrieve the active lines associated with Michael Johnson. Finally, if line \"LINE67890\" is confirmed to be active, get_line_details for this line to check the current plan and usage details. If necessary, you may then suspend_line for line_id \"LINE67890\" due to a lost device, ensuring Michael Johnson is aware of the 30-day resumption policy.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC133"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE67890"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE67890", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are organized, optimistic. First, verify the identity of user Michael Garcia using email michael.garcia5750@email.com to ensure secure access to his account. Once verified, lookup_customer_by_phone using Michael Garcia's verified phone number to retrieve his account details. Finally, get_customer_lines for Michael Garcia to list all active lines associated with the account, ensuring an accurate overview of his current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "verified_phone_number_of_michael_garcia"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are organized, cautious, confident, flexible. Verify your identity by checking your email robert.brown6285@email.com against the account records to ensure it matches. Once your identity is confirmed, use your phone number to retrieve your customer ID. With the verified customer ID, list all active lines under your account to review their current status and data usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are polite, confident. First, perform the Get_customer_lines task for James Brown to retrieve all active lines on his account. Once you have the list of active lines, proceed with the Get_line_details task for each line to check their current usage and plan details. This will help you gather the necessary information to provide James Brown with informed recommendations on potential plan adjustments based on his usage patterns, ensuring he receives optimal service and value from his telecom provider.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC145", "customer_name": "James Brown"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC145", "line_id": "line_001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC145", "line_id": "line_002"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC145", "line_id": "line_003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are flexible, confident, direct, optimistic. First, lookup_customer_by_phone with phone number 555-123-4567 to verify the identity of user Jennifer Smith. Once her identity is confirmed, get_bill_details for customer ID C9988 to review last month's charges and payments. After reviewing the bill details, calculate the total outstanding amount for customer ID C9988 to inform Jennifer Smith about her current balance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC023"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC023", "user_id": "TC023"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "total_charges - total_payments"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are direct, independent, confident. Get bill details for Patricia Smith's account to review recent charges and payment status.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are polite, organized, confident. Please get the bill details for Robert Jones to review his outstanding balance and payment history. Once you have reviewed the details, process the payment for Robert Jones using the provided payment method, and note the processing time. This will ensure that the payment is recorded accurately and promptly, allowing us to maintain a seamless service for Robert.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC119"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review the bill details for Robert Jones to ensure accuracy before proceeding with payment."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "outstanding_balance"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Process the payment for Robert Jones using the provided payment method."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "payment_processing_time"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Note that the payment processing may take 1-2 business days to reflect on the account."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are direct, patient, logical. First, verify customer identity using the email mary.jones9465@email.com to access account details. Once verified, proceed to get_customer_lines for the retrieved customer ID to view all active lines under the account. This will help ensure that Mary Jones's account is secure and that you have accurate information about her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.jones9465@email.com", "user_id": "TC147"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC147", "user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are polite, optimistic. First, perform a lookup_customer_by_phone with phone number 555-123-4567 to verify the identity of Michael Miller. Once his identity is confirmed, proceed to get_customer_lines for customer ID 1001 to identify eligible lines for an upgrade. This will ensure that Michael Miller can seamlessly transition to a plan that better suits his needs, enhancing his overall experience with our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC054"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC054", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are confident, patient. \"lookup_customer_by_phone with phone number '555-1234' to verify John Smith's identity\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are optimistic, cautious. lookup_customer_by_phone with phone number \"555-1234\" to verify identity for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are flexible, direct. \"lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Jennifer Davis\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are direct, cautious. lookup_customer_by_phone with phone_number \"555-0123\" to verify identity for Linda Davis (user ID required for subsequent tasks)",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are polite, optimistic. First, please lookup_customer_by_phone with phone number 555-123-4567 to verify the identity of John Smith as we have received a request related to his account. Once his identity is confirmed, proceed to suspend_line with line ID L1002 for customer John Smith due to non-payment. This ensures compliance with our billing policies while maintaining a fair process for all customers.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC081"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1002", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are patient, logical, confident. First, verify customer identity for user John Garcia with email john.garcia3458@email.com before accessing account details to ensure security compliance. Once verified, lookup_customer_by_phone using the phone number associated with John Garcia's account to retrieve the customer ID. With the customer ID in hand, get_customer_lines to list all active and suspended lines on the account. This will allow you to confirm the status of each line. If line ID L9876 is active, proceed to suspend_line for line ID L9876 due to a temporary request from John Garcia, ensuring that his needs are met while maintaining account security and service integrity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia3458@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC015", "customer_id": "TC015"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC015", "line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are flexible, cautious, patient, polite. Please begin by looking up the customer using their phone number, which is \"555-123-4567\". Once you have retrieved the customer information, proceed to get the customer lines associated with their account using the customer ID you found. This will help us verify the details before taking any further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC120"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC120", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are patient, polite, flexible. lookup_customer_by_phone with phone number 555-1234 to verify Robert Davis's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are direct, cautious. Get line details to verify if the customer is eligible for a data plan upgrade.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC015"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are direct, independent, logical. Get bill details for Mary Miller’s account using customer ID to review outstanding balance.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC102", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are patient, cautious, logical. First, verify user identity for Linda Johnson using email linda.johnson5357@email.com to ensure you are interacting with the correct account holder. Once her identity is confirmed, proceed to get_customer_lines for Linda Johnson's account to list all active lines. This will help you identify and confirm the specific line ID L12345 that needs to be suspended due to her request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.johnson5357@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC060", "email": "linda.johnson5357@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC060", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are confident, independent, cautious. Get line details for Mary's primary line to check current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC071", "phone_number": "Mary's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC071"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC071", "line_id": "Mary's primary line ID"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC024",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are flexible, cautious, organized, optimistic. First, perform a lookup_customer_by_phone with phone_number=\"555-1234\" to verify the identity of Jennifer Davis. Once her identity is confirmed, proceed to get_customer_lines with customer_id=\"C001\" to retrieve all active lines associated with her account. Finally, use get_line_details with line_id=\"L123\" to check the data usage and plan details for Jennifer's primary line, ensuring she is on the best plan for her needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC024"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are polite, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify Jennifer Brown's identity. Once verified, proceed to get_bill_details for customer ID C1234 to review her outstanding balance and due date. This sequence will ensure that you have the necessary information to discuss her account status accurately and provide her with the best options for resolving any issues with her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC026"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC026", "user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are patient, polite. Suspend_line for line ID L123 as requested by James Jones due to temporary inactivity.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC106", "line_id": "L123", "reason": "Requested by James Jones due to temporary inactivity"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are direct, independent. Retrieve customer details using lookup_customer_by_phone with parameters: phone_number=\"555-0199\", user_email=\"jennifer.jones5314@email.com\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0199", "user_email": "jennifer.jones5314@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are direct, flexible. Lookup customer by phone number \"555-1234\" to verify identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are independent, patient, polite. Suspend line L001 under Patricia Smith's account due to non-payment, if required.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC112", "phone_number": "Patricia Smith"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC112", "customer_id": "TC112"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC112", "line_id": "L001"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC112", "customer_id": "TC112"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC112", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are independent, organized, optimistic, patient. First, verify the identity of user Patricia Smith using the email patricia.smith7071@email.com to ensure secure access to her account details. Once Patricia's identity is confirmed, proceed to suspend line L1234 upon her request to temporarily halt services while she reviews her latest billing statement and payment status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.smith7071@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC113", "line_id": "L1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are confident, optimistic. First, lookup Patricia Johnson's account details using her phone number to verify her identity and ensure you have the correct account information. Once you have confirmed the account details, retrieve all active lines associated with Patricia Johnson's account to assess her current telecom services and identify any potential issues or opportunities for service upgrades.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Johnson's phone number", "user_id": "TC096"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are polite, organized. \"lookup_customer_by_phone with phone_number '555-123-4567' to verify Jennifer Miller's account identity\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are optimistic, logical. First, lookup_customer_by_phone with phone number 555-1234 to verify Linda Davis's identity. Once her identity is confirmed, proceed to get_customer_lines for customer ID C001 to retrieve all active lines for Linda Davis. This will help ensure that we have the correct customer information before reviewing her account details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC150"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC150", "user_id": "TC150"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are independent, optimistic, polite, flexible. Verify the identity of user Michael Jones using email michael.jones4016@email.com for account access. Once his identity is confirmed, suspend line L9876 temporarily for Michael Jones due to a reported lost device. This ensures that unauthorized usage is prevented while he arranges for a replacement.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.jones4016@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC042", "line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are patient, organized, logical, cautious. \"Lookup Linda Johnson's account using phone number associated with linda.johnson5357@email.com for identity verification.\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.johnson5357@email.com", "user_id": "TC060"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are direct, patient. First, use lookup_customer_by_phone with phone number 555-1234 to verify Mary's account identity. Once verified, use get_customer_lines with customer ID C4135 to retrieve all active lines for Mary. This process will ensure that we have accurate information about her account before proceeding with any further actions related to her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC063"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC063", "user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC139",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are flexible, organized. First, verify the identity of user Michael Smith by sending a verification code to michael.smith4429@email.com. Once his identity is confirmed, lookup_customer_by_phone using the phone number associated with Michael Smith to retrieve the customer ID. This process is crucial to ensure that we are providing account details to the correct individual and maintaining the security of our telecom services.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to verify the identity of Michael Smith by sending a verification code to his email."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"message": "Please send a verification code to michael.smith4429@email.com to verify his identity."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Michael Smith's identity is confirmed, I will proceed to look up his customer ID using his phone number."}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC139", "phone_number": "associated_phone_number_of_michael_smith"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are independent, polite, patient, confident. First, lookup_customer_by_phone with phone number 555-0123 to verify identity for account access. Once the identity is confirmed, get_bill_details for user ID U1234 to review the outstanding balance and payment history. This will help in understanding the customer's current financial obligations with our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "U1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are optimistic, organized, patient, flexible. Retrieve customer account details using lookup_customer_by_phone with the phone number associated with Linda Garcia. Once you have the account details, verify Linda Garcia's identity using her email address linda.garcia4634@email.com to ensure secure access. After verifying her identity, get all customer lines for Linda Garcia using get_customer_lines with her verified account ID. This sequence of actions will help ensure that Linda Garcia's account is accurately accessed and managed, providing her with a seamless experience in managing her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number_for_linda_garcia"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve account details for Linda Garcia using her phone number."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Linda Garcia's identity using her email address."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure secure access to Linda Garcia's account."}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "verified_account_id_for_linda_garcia", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are direct, organized, flexible, cautious. Lookup customer by phone number 555-1234 to verify identity for Jennifer Johnson. Once her identity is confirmed, get customer lines for the user ID associated with Jennifer Johnson to review her active services. This will help ensure that all her telecom services are accurately accounted for and up to date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are organized, direct, logical, confident. First, perform a lookup_customer_by_phone using the phone number associated with Jennifer Smith's account to verify her identity. Once her identity is confirmed, proceed to get_bill_details for Jennifer Smith to review her latest bill and outstanding balance. This sequence will ensure that you have the necessary information to assist her with any inquiries regarding her telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number", "user_id": "TC023"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC023", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are organized, cautious. Get_bill_details for Jennifer Jones's account to review outstanding charges and payment history.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC130"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are polite, logical, optimistic. First, lookup_customer_by_phone with phone number 555-1234 to verify identity for Robert Jones. Once his identity is confirmed, proceed to suspend_line for line ID L456 with reason 'customer request' after identity verification. This ensures that the customer's request is handled promptly and securely, maintaining trust and satisfaction in our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC144"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "reason": "customer request", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are independent, cautious, organized, logical. Verify customer identity for user Mary Jones using email mary.jones9465@email.com.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.jones9465@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are polite, organized. First, verify customer identity using email robert.williams8770@email.com for account access to ensure security and confirm authorization. Once verified, get bill details for the account associated with phone number 555-1234 to review payment status. This will help determine the appropriate next steps regarding any outstanding balances.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC067", "email": "robert.williams8770@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are cautious, independent, polite, patient. lookup_customer_by_phone with phone_number '555-0123' to verify identity of Jennifer Jones for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are cautious, flexible, patient. Verify customer identity using email james.davis6038@email.com for account access. Once verified, lookup_customer_by_phone using the phone number associated with James Davis to retrieve the customer ID. With the customer ID in hand, get_bill_details to review outstanding balance and payment history, ensuring accurate billing information is available for customer support in the telecom sector.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.davis6038@email.com", "user_id": "TC065"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC065", "user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are optimistic, polite, confident. First, verify the identity of Robert Brown using his email robert.brown2463@email.com to ensure secure account access. Once his identity is confirmed, proceed to lookup_customer_by_phone using Robert Brown's verified phone number to retrieve his account information. After accessing his account, get_bill_details for Robert Brown to review his outstanding balance and payment history, ensuring he has all the necessary information to manage his telecom services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "verified_phone_number", "user_id": "TC029"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC029", "user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are independent, patient. First, lookup_customer_by_phone with phone number '123-456-7890' to verify identity for accessing Mary Brown's account. Once verified, get_customer_lines for customer ID 'C789' to retrieve all active lines associated with Mary Brown. This will ensure you have the necessary details to assist her with any inquiries about her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC063"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC063", "user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are logical, optimistic. First, lookup customer by phone number 555-1234 to verify identity for user Jennifer Williams. Once her identity is confirmed, proceed to get bill details for user Jennifer Williams to check the outstanding balance. This will help ensure accurate billing information is provided to the customer, enhancing their satisfaction and trust in our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC131"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_name": "Jennifer Williams", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are confident, optimistic, organized. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Michael Williams' identity. Once verified, get_bill_details for account_id \"A98765\" to review his outstanding balance and recent transactions. This will help determine if any further action, such as suspending a line due to non-payment, is necessary.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A98765", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are optimistic, patient, flexible. First, lookup customer by phone number 555-123-4567 to verify identity. Once verified, get bill details for customer ID C001 to check outstanding balance. If there is a significant outstanding balance, proceed to suspend line with line ID L001 for customer ID C001 due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC145"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC145", "user_id": "TC145"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "customer_id": "TC145", "user_id": "TC145"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC135",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are patient, polite. Retrieve bill details for James Jones for the current billing cycle to check the outstanding amount. Then, calculate the total overdue amount for James Jones based on the retrieved bill details. This will help ensure that James is aware of his current financial obligations with our telecom service and can plan his payments accordingly.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC135"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["outstanding_amount", "overdue_amount"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are independent, direct, flexible, polite. First, perform the task \"lookup_customer_by_phone\" with the parameter phone_number=\"555-1234\" to identify the customer associated with this phone number. Once you have obtained the customer ID, proceed to \"get_bill_details\" with the parameters customer_id=\"C001\" and billing_cycle=\"2023-09\" to retrieve the billing details for the specified cycle. This sequence will help you assist a customer who has inquired about their September bill after confirming their identity through their phone number.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC146", "billing_cycle": "2023-09"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are optimistic, logical, confident. First, get the bill details for the account of James Jones to review the latest bill and outstanding balance. Then, calculate the total amount due, including any late fees, for the account of James Jones. This will help ensure that all financial information is accurate before proceeding with further steps to manage the account effectively.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC106", "customer_name": "James Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are independent, confident, flexible, direct. First, verify the identity of user Linda Garcia using the provided email linda.garcia4634@email.com to ensure secure access to her account. Once her identity is confirmed, proceed to lookup_customer_by_phone using Linda Garcia's phone number to retrieve her customer account details. Finally, get_customer_lines for Linda Garcia to review all active and suspended lines on her account, ensuring she has the necessary information to manage her telecom services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC127", "phone_number": "Linda's Phone Number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are patient, cautious, independent, organized. First, perform a Lookup_customer_by_phone with phone number 555-1234 to verify the identity of Robert Davis. Once his identity is confirmed, proceed to Get_customer_lines for the customer ID retrieved from the previous step to list all active lines associated with his account. Finally, use the Get_line_details for line ID L001 to check the current plan and usage details, ensuring Robert Davis is on the most suitable plan for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC032"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC032", "user_id": "TC032"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are organized, patient, flexible, confident. lookup_customer_by_phone with phone_number: \"123-456-7890\" to verify identity for John Miller",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are confident, patient, direct, cautious. \"lookup_customer_by_phone with phone_number: '555-0123' to verify identity for Michael Garcia\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are optimistic, organized, independent, direct. Lookup customer by phone number 555-1234 to retrieve account information for John Davis. Once you have the account information, get bill details for John Davis to review outstanding balance and payment history. This will help determine if any further action, such as suspension of services, is necessary due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC074"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_name": "John Davis", "user_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are cautious, patient, flexible. lookup_customer_by_phone with phone_number 123-456-7890 to verify identity for user Jennifer Davis",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are optimistic, confident. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity for user John Williams. Once verified, proceed to get_customer_lines for customer_id \"C001\" to retrieve active lines associated with John Williams. Finally, use get_line_details for line_id \"L123\" to check the current plan and usage for John Williams' primary line, ensuring he has the optimal plan for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC031"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are direct, logical. Lookup_customer_by_phone with Robert Davis's phone number to retrieve customer account details, then Get_customer_lines for Robert Davis to view all active lines associated with his account. This will help you verify the number of lines he has and ensure that his account is set up correctly, which is crucial for providing accurate customer support in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Davis's phone number", "user_id": "TC032"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC032", "user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are independent, patient, polite, cautious. First, lookup customer by phone number to retrieve Robert Brown's account details. Once you have accessed his account, get customer lines associated with Robert Brown's account to view all active services. Finally, get line details for the primary line to check the current plan and usage status, ensuring that the plan is suitable for an upgrade to a higher data plan for the next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number", "user_id": "TC073"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "Robert Brown's account ID", "user_id": "TC073"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary line ID", "user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are logical, direct, polite, flexible. lookup_customer_by_phone with phone_number='+1234567890' to verify Robert Brown's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are logical, polite. Please begin by using the lookup_customer_by_phone task with the phone number linked to john.smith6383@email.com to verify the customer's identity. Once you have retrieved the customer ID, proceed to the get_customer_lines task to list all active lines associated with this customer. After identifying the specific line of interest, use the get_line_details task for the line ID to access its usage and plan information. This sequence of tasks will help ensure that you have a comprehensive understanding of the customer's current telecom services and can assist them effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "john.smith6383@email.com", "user_id": "TC016"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC016", "user_id": "TC016"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are optimistic, patient, cautious, confident. First, perform a Lookup_customer_by_phone using the phone number associated with Jennifer Jones to verify her identity as part of our routine customer verification process. Once her identity is confirmed, proceed to Get_customer_lines for her verified account to list all active lines associated with Jennifer Jones. This will help ensure that we have an accurate overview of her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Jones' phone number", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are confident, independent, polite, organized. Begin by looking up the customer using the phone number 123-456-7890 to retrieve their account ID. Once you have the account ID, proceed to get the customer lines associated with this account to ensure all lines are active and properly linked. Finally, check the line details for line ID L001 to review the current plan and data usage, ensuring the customer is on the most suitable plan for their needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC092"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "A123", "user_id": "TC092"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are independent, optimistic, confident, cautious. Use get_line_details with line ID L6789 to check the current plan and usage details for John Miller's primary line.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L6789", "user_id": "TC104"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are cautious, logical. Use lookup_customer_by_phone with phone number 555-1234 to verify Patricia Miller's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are logical, polite, organized. First, verify the identity of Robert Jones using his email robert.jones1563@email.com to ensure secure access to his account. Once verified, proceed to get_customer_lines for Robert Jones to retrieve a list of all active lines on his account. Finally, for each active line, get_line_details to check usage and plan details, ensuring Robert has the most suitable plans for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones1563@email.com", "user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "robert.jones1563@email.com", "user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L002", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are independent, direct. suspend_line for line_id \"LINE456\" due to customer request for temporary suspension",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE456", "reason": "Customer request for temporary suspension", "user_id": "TC109"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are logical, direct, optimistic, independent. First, lookup customer by phone number 555-1234 to verify account access for Robert Williams. Once his identity is verified, proceed to get customer lines associated with Robert Williams' account to ensure you have the correct details. After confirming the associated lines, get line details for line ID L9876 to check the current plan and usage. If everything is in order and a loss of device is reported, suspend line L9876 temporarily to prevent unauthorized usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC080"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC080", "user_id": "TC080"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC080"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "reason": "Loss of device reported", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are confident, logical. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity before accessing account details for Robert Johnson. Once verified, proceed to get_customer_lines for customer ID C9087 to retrieve all active lines associated with Robert Johnson’s account. This will ensure you have the necessary information to assist with any inquiries regarding his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC072"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC072", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are optimistic, patient, independent. suspend_line for line ID L1234 with reason \"requested by customer for temporary suspension\"",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC060", "line_id": "L1234", "reason": "requested by customer for temporary suspension"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are confident, polite. First, perform a Lookup_customer_by_phone with phone number 555-1234 to verify identity for John Smith. Once verified, proceed to Get_customer_lines for the user ID obtained from the previous step to list all active lines associated with John Smith's account. Finally, use Get_line_details for line ID L003 to verify eligibility for a plan upgrade, ensuring John Smith has the best options available for his telecom needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC081"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are cautious, organized, polite. First, lookup customer by phone number 555-1234 to retrieve the customer ID and associated account details. Once you have the customer ID, use it to get customer lines using customer ID C102 to list all active lines under the account. This will help us ensure that we have the most accurate and up-to-date information on the customer's active lines, which is crucial for providing excellent service and addressing any potential issues with their telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC104"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC104", "user_id": "TC104"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are organized, direct, flexible. First, verify customer identity using the email james.brown3113@email.com to access account details. Once verified, suspend line L1001 for user James Brown due to a requested temporary hold. If the customer requests to resume service within the 30-day window before disconnection, proceed to calculate prorated charges for resuming line L1001 before the end of the billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown3113@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC145", "line_id": "L1001"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC145"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC145", "line_id": "L1001", "action": "prorate"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are organized, flexible, patient, direct. Suspend line L12345 on Linda's account due to a reported lost device, ensuring suspension is within policy limits. Once the suspension is confirmed, resume Linda's suspended line L12345 within the 30-day policy limit for resumption. Ensure that all actions are documented in the system and that Linda is informed of the suspension and subsequent resumption, maintaining compliance with company policies.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC091"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC091", "line_id": "L12345", "reason": "Lost device reported"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC091", "line_id": "L12345", "action": "confirm"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC091", "line_id": "L12345", "action": "resume", "within_policy": true}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are polite, direct, confident. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Patricia Johnson's identity as she has contacted us with a query regarding her account. After confirming her identity, proceed to get_customer_lines for the customer ID associated with Patricia Johnson to review all active lines under her account. Finally, get_line_details for line ID L7890 to check current data usage and plan details, as Patricia has expressed concerns about her data consumption and wishes to understand her plan better.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC096"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC096", "user_id": "TC096"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L7890", "user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are independent, cautious. First, perform a Lookup_customer_by_phone with phone number 555-123-4567 to verify customer identity for Jennifer Jones. Once her identity is confirmed, proceed to Get_customer_lines for customer ID C7047 to retrieve all active lines under her account. This sequence will ensure that you have verified the correct customer before accessing her account details, which is crucial for maintaining security and providing accurate information in a telecom setting.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC130"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC130", "user_id": "TC130"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are polite, direct, organized, cautious. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of John Williams. Once verified, proceed to get_customer_lines for the customer ID retrieved from the previous step to list all active lines associated with John Williams. After obtaining the list of active lines, think to evaluate if a plan upgrade is necessary for line ID 7890 by considering the current plan and usage details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC098"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC098", "user_id": "TC098"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "7890", "user_id": "TC098"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Evaluate if a plan upgrade is necessary based on the current plan and usage details for line ID 7890."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are cautious, independent, logical. First, lookup_customer_by_phone with phone number 555-1234 to verify customer Patricia Brown's identity. Once her identity is confirmed, proceed to get_line_details for line ID L2002 to check her current plan and usage. This will ensure that any necessary adjustments can be made before considering further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC056"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L2002", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are patient, direct, cautious, independent. Get_line_details for the primary line of John Williams to check current plan and usage. Based on the gathered information, think about potential plan upgrades for John Williams, considering his current usage and preferences.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC098", "phone_number": "John Williams' primary phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC098", "customer_id": "TC098"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC098", "line_id": "John Williams' primary line ID"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Based on the current plan and usage details retrieved, consider potential plan upgrades for John Williams."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are independent, polite, organized. \"lookup_customer_by_phone with phone number 555-1234 to verify identity for account access\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are optimistic, logical. First, lookup_customer_by_phone for the phone number associated with John Brown to verify his identity. Once his identity is confirmed, proceed to get_customer_lines for John Brown's account to review the lines he has subscribed to. This sequence ensures that you have the correct customer before accessing sensitive account information, which is crucial for maintaining security and providing accurate service in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "John Brown's phone number", "user_id": "TC124"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC124", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are patient, polite, independent. First, use the lookup_customer_by_phone task with the phone number associated with Jennifer Jones to verify her identity. Once Jennifer's identity is confirmed, proceed to get_customer_lines using the customer ID from her account to list all active lines. This process ensures that we have accurate information on her account before any further actions are taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer's phone number", "user_id": "TC130"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC130", "user_id": "TC130"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are organized, patient, cautious, direct. First, lookup_customer_by_phone with phone number linked to user email mary.jones9465@email.com to verify identity for account access. Once the customer's identity is verified, retrieve the customer ID and use it to get_customer_lines to list all active lines under the account. This process will help ensure that the customer can manage their telecom services effectively and address any issues related to their active lines.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "linked to user email mary.jones9465@email.com", "user_id": "TC147"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC147", "user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are optimistic, logical, independent. Get bill details for customer ID to review outstanding balance and due date",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC074", "customer_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are cautious, optimistic. lookup_customer_by_phone with phone_number='555-0123' to verify identity for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are cautious, flexible. Get_line_details for line ID L12345 from John Smith's account to check current plan and usage.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC081", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are polite, independent, cautious, flexible. \"lookup_customer_by_phone with customer_phone='555-1234' to verify Linda's account access\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"customer_phone": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are optimistic, polite. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify Robert Brown's account. Once verified, proceed to get_customer_lines for user ID 2463 to list all active lines under Robert Brown's account. After identifying the relevant line, get_line_details for line ID 987654 to check current plan and usage details. These steps will help ensure that Robert Brown's account is accurately assessed, and any necessary actions can be taken to address his telecom needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "2463"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "987654"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are organized, patient. First, use lookup_customer_by_phone(phone_number=\"555-1234\") to verify identity and access Mary's account. Once her identity is confirmed, proceed with get_customer_lines(customer_id=\"C001\") to retrieve all active lines associated with Mary's account. Finally, use get_line_details(line_id=\"L001\") to obtain usage details for Mary's primary phone line, ensuring that any recent changes or additional data applied to her line are accurate and up-to-date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC138"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are independent, logical. First, use the lookup_customer_by_phone with phone_number '555-0143' to verify the identity of Jennifer Davis. Once her identity is confirmed, proceed to get_customer_lines for customer_id 'C1234' to list all active lines associated with her account. This will help ensure that all lines under her account are correctly identified for any further action or inquiry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0143", "user_id": "TC085"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC085", "user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are flexible, independent. First, verify customer identity using email jennifer.smith8259@email.com before accessing account details. Once identity verification is successful, lookup customer account using the phone number associated with Jennifer Smith. After accessing the account, check billing details for Jennifer Smith's account to verify any outstanding payments.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.smith8259@email.com", "user_id": "TC143"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC143"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are independent, logical, optimistic, direct. First, lookup_customer_by_phone with parameters: phone_number=\"555-123-4567\" to identify the customer associated with this contact number. Once you have the customer ID, proceed to get_customer_lines with parameters: customer_id=\"C1234\" to retrieve all active lines under this account. After identifying the specific line in question, use get_line_details with parameters: line_id=\"L5678\" to gather detailed information about the line's current status and any recent activity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC141"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are flexible, patient, polite, logical. \"lookup_customer_by_phone with phone number 555-1234 to verify identity and retrieve customer ID\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are confident, direct, flexible, optimistic. First, lookup the customer by phone using the phone number associated with Jennifer Davis to verify her identity. Once her identity is confirmed, proceed to get customer lines for the verified account to review all active lines under Jennifer Davis. This will ensure that we have an accurate overview of her account in order to address any service inquiries or updates she may need.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Davis's phone number", "user_id": "TC085"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC085", "user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are patient, cautious, independent. Lookup customer by phone number +1234567890 to verify identity for Robert Williams.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are independent, logical. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity for James Jones. Once verified, get_bill_details for the billing account ID associated with James Jones to review his outstanding balance. This sequence ensures that you have the necessary information to address any billing inquiries effectively, providing a seamless customer service experience in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC106"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"billing_account_id": "associated_billing_account_id", "user_id": "TC106"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are organized, logical, flexible. \"lookup_customer_by_phone\" with phone number \"555-123-4567\" to verify identity of John Smith (john.smith6383@email.com)",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are flexible, patient, cautious, independent. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify Michael Jones' account identity to ensure you are accessing the correct customer information. Once verified, proceed to get_line_details with line_id 'L7890' to check current plan details for Michael Jones' primary line, as he is considering upgrading to a premium plan. This sequence will help provide accurate and relevant information to assist Michael Jones effectively in making an informed decision about his plan upgrade.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L7890", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are patient, logical. First, lookup_customer_by_phone with phone_number '123-456-7890' to verify Robert Garcia's account. Once verified, get_customer_lines for customer_id 'C1024' to list all active lines associated with Robert Garcia. After identifying the active lines, get_line_details for line_id 'L5678' to check the current plan and usage, ensuring you have the correct line before proceeding with any changes. If everything matches Robert Garcia's request, suspend_line for line_id 'L5678' to temporarily suspend service as requested.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC003"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "user_id": "TC003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are organized, cautious, polite. First, perform a Lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Mary Smith's account access. Once verified, proceed to Get_customer_lines for the customer ID retrieved from the previous step to view all active lines associated with Mary Smith's account. Finally, use the Get_line_details for line ID L98765 to check the current plan and usage details, ensuring that the line is ready for any necessary changes or updates.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC138"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC138", "user_id": "TC138"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L98765", "user_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are organized, confident, patient, polite. First, perform a Lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of Michael Johnson, ensuring you have the correct customer details. Once verified, proceed to Get_line_details for line_id \"L123\" to check the current plan and usage details. This information will help you assess whether the current plan meets Michael Johnson's usage needs, allowing you to provide informed recommendations or adjustments if necessary.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC133"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are organized, patient, logical. lookup_customer_by_phone with phone_number '555-123-4567' to verify Jennifer Williams' account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are patient, cautious, independent, direct. First, verify customer identity for John Brown using email john.brown8493@email.com to access account details. Once identity verification is complete, get bill details for John Brown's account to review recent charges and payment history. This process is crucial to ensure that John Brown's account information is accurate and up-to-date, allowing us to provide the best possible service and address any discrepancies in billing for our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.brown8493@email.com", "user_id": "TC124"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "john.brown8493@email.com", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are optimistic, polite, logical, independent. \"Lookup customer by phone for Jennifer Davis using phone number 555-1234 to verify identity\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are cautious, polite, organized, direct. First, lookup_customer_by_phone with phone_number \"555-0123\" to verify identity for accessing account details. Once the identity is verified, proceed to get_customer_lines for customer_id \"C001\" to review all active lines on the account. After reviewing the active lines, get_line_details for line_id \"L1001\" to check the current data usage and plan details, ensuring that the line is eligible for the requested action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC026"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are optimistic, confident, independent. First, perform a Lookup_customer_by_phone using the phone number associated with Patricia Smith to ensure her identity is verified. Once verified, proceed to Get_customer_lines for Patricia Smith to review her active phone lines, which will help in assessing her current telecom services and any potential needs for updates or changes.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Smith's phone number", "user_id": "TC113"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC113", "user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are organized, patient. Suspend a line with line ID L12345 on Patricia Johnson's account due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC096", "phone_number": "L12345"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC096", "customer_id": "TC096"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC096", "line_id": "L12345"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC096", "customer_id": "TC096"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC096", "line_id": "L12345", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are organized, optimistic, cautious, flexible. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify identity and access account details for John Brown. Once you have confirmed John's identity, proceed to get_customer_lines with customer_id \"C8493\" to retrieve all active lines associated with John's account. This will allow you to provide John with a comprehensive overview of his current services and assist him with any inquiries regarding his telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC124"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC124", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are optimistic, confident. Process a plan change for line L001 to the new selected plan, effective next billing cycle",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC144", "line_id": "L001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the current plan details and eligibility for a plan change."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Proceed with the plan change for line L001 to the new selected plan, effective next billing cycle."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are polite, confident. First, get_line_details for line ID L789 to verify eligibility for a plan upgrade. Once eligibility is confirmed, calculate the cost difference between the current plan and the potential upgrade for line ID L789. This will provide a clear understanding of the financial implications for the customer, ensuring they are well-informed before making a decision.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789", "user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are flexible, patient. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify Linda Miller's identity. Once verified, get_customer_lines for customer_id 'C001' to list all active lines. This will ensure that you have the correct customer information before proceeding with any service changes or inquiries related to her account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC091"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC091", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are polite, patient. First, use `lookup_customer_by_phone` with the phone number associated with Robert Jones to verify account access. Once access is verified, use `get_customer_lines` with the customer ID retrieved from Robert Jones' account details to list his active lines. Finally, use `get_line_details` with the line ID from Robert Jones' active lines to check his current plan and data usage, ensuring that you have a comprehensive understanding of his current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Jones' phone number", "user_id": "TC109"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC109", "user_id": "TC109"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "retrieved_line_id", "user_id": "TC109"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are confident, patient, logical. First, lookup customer by phone number to retrieve account details for Robert Williams, ensuring you have the correct customer information. Once you have verified the account details, proceed to get customer lines for Robert Williams to identify all active lines associated with his account. This will help you provide accurate service and support for any inquiries or issues he may have regarding his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_phone_number", "user_id": "TC067"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC067", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are optimistic, direct. Verify the identity of user Jennifer Johnson using email jennifer.johnson5907@email.com for account access. Once verified, lookup the customer by phone number associated with Jennifer Johnson to retrieve the customer ID. With the customer ID obtained, get customer lines to review the current telecom services Jennifer Johnson is subscribed to.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.johnson5907@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC149", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are patient, cautious, flexible. Suspend line with line ID L12345 for non-payment due to a billing issue.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC144"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "non-payment due to a billing issue"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are polite, flexible, cautious. Access bill details for James Brown's account to review current charges and payment status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC145"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC145"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are patient, cautious, polite. First, lookup customer by phone number (555-123-4567) to verify identity for Jennifer Smith's account access. Once her identity is confirmed, proceed to get customer lines for Jennifer Smith to identify active services linked to her account. This will ensure that we have accurate information on the services she is currently using, which is essential for providing her with the best possible support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC023"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Jennifer Smith", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are confident, direct, flexible, polite. Please lookup_customer_by_phone with phone number 555-0123 to verify identity for user Robert Jones (robert.jones5323@email.com). Once verified, proceed to get_customer_lines with customer ID C5323 to list active lines associated with Robert Jones. After identifying the relevant line, use get_line_details with line ID L12345 to view the current plan and usage details. This sequence will help ensure that Robert Jones is correctly identified and his active line details are accurately reviewed for any customer service inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC123", "user_id": "TC123"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are direct, polite. First, verify the identity of customer Mary Johnson using her email (mary.johnson4713@email.com) to ensure secure account access. Once her identity is confirmed, proceed to get customer lines for the account associated with Mary Johnson to view all active lines. After reviewing the active lines, suspend the line with line ID L98765 due to Mary Johnson's request, ensuring that the line can be resumed within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.johnson4713@email.com", "user_id": "TC071"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "mary.johnson4713@email.com", "user_id": "TC071"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L98765", "user_id": "TC071", "suspend_duration": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are organized, independent, polite. lookup_customer_by_phone(phone_number=\"555-123-4567\")",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are independent, patient. First, lookup_customer_by_phone with phone number associated with Robert Jones to verify identity. Once verified, get_bill_details for account linked to Robert Jones to review outstanding balance and any recent charges. Finally, calculate total outstanding balance including any late fees for Robert Jones's account to ensure accurate billing information is available for further discussions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number_of_Robert_Jones", "user_id": "TC144"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "account_linked_to_Robert_Jones", "user_id": "TC144"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "outstanding_balance + late_fees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are optimistic, cautious, direct. suspend_line for line ID 7890 with reason \"customer request\" to temporarily halt service",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC006", "line_id": "7890", "reason": "customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are confident, independent, direct. lookup_customer_by_phone with phone_number=\"+1234567890\" to verify identity of Jennifer Smith",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are confident, polite. First, verify the identity of user Linda Miller using email linda.miller1663@email.com for account access to ensure security. Once verified, get bill details for Linda's account to review outstanding payments and due dates to understand her billing status. If there are overdue payments, proceed to suspend the line with the specific line ID for Linda's account due to non-payment, ensuring compliance with company policy.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.miller1663@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC019"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC019", "line_id": "specific_line_id_for_linda"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are patient, optimistic, direct, logical. Get line details for line ID L5678 to check current service status.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are flexible, direct, patient, optimistic. First, verify the identity of the user Linda Miller using her email address linda.miller1663@email.com. Once her identity is confirmed, proceed to look up Linda Miller's account using the verified email to retrieve her customer ID and associated phone numbers. Finally, use the customer ID to get the details of active customer lines associated with Linda Miller to check usage and plan information, ensuring all data is up-to-date and accurate for providing optimal customer support in the telecom sector.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, verify Linda Miller's identity using her email address."}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.miller1663@email.com", "user_id": "TC019"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Linda's identity is confirmed, retrieve her customer ID and associated phone numbers."}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "linda.miller1663@email.com", "user_id": "TC019"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Use the customer ID to get the details of active customer lines."}
            ),
            Action(
                name="get_line_details",
                kwargs={"customer_id": "TC019", "user_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are logical and patient. First, use the Lookup_customer_by_phone task to retrieve John's account information using his phone number. Once you have accessed his account, proceed with the Get_customer_lines task to list all active and suspended lines associated with his account. This will help in providing a comprehensive overview of John's telecom services and assist in addressing any queries he might have regarding his account status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "John's phone number", "user_id": "TC124"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "John's account ID", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are optimistic, polite, flexible, patient. First, verify the identity of the user Robert Jones using his email robert.jones1563@email.com before accessing account details. Once verified, use lookup_customer_by_phone with the phone number provided by Robert to retrieve his customer account details. With the customer ID obtained, use get_customer_lines to retrieve a list of all active lines on Robert's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_by_robert", "user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC144", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are independent, patient, direct. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify identity for account access. Once identity is confirmed, proceed to get_bill_details for user_id \"john.smith6987\" to retrieve the outstanding balance and due date. This sequence ensures that you can securely access the customer's account and provide them with accurate billing information, which is crucial for maintaining customer trust and satisfaction in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "john.smith6987"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are logical, optimistic. \"lookup_customer_by_phone with phone_number '555-0199' to verify Patricia Smith's account\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0199"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are direct, organized. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Jennifer Smith's account. Once verified, proceed to get_customer_lines with customer_id \"C9988\" to retrieve all active lines under Jennifer Smith's account. This will help ensure we have accurate information about her current services for a billing inquiry she submitted.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC023"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC023", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are independent, cautious, direct, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of Jennifer Brown. Once her identity is confirmed, proceed to get_line_details for line ID L5678 to check the current plan and usage. This will ensure that all necessary information is reviewed before taking further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC062"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are organized, direct, cautious, flexible. First, get bill details for Robert Jones's account to review outstanding charges and payment history. Once you have gathered this information, calculate the total amount due on Robert Jones's account, including any late fees or penalties. This will ensure you have a comprehensive understanding of his financial obligations before proceeding with any further actions.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC123", "customer_name": "Robert Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are polite, cautious. Get_line_details for line ID L1234 to check current plan and usage details",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC036", "line_id": "L1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are independent, direct, patient, cautious. First, lookup_customer_by_phone with phone_number: \"123-456-7890\" to verify Patricia Miller's account. Once her account is verified, proceed to get_customer_lines for customer_id: \"C3252\" to retrieve all active lines on Patricia Miller's account. This will help ensure that all active services are correctly associated with her account, providing a comprehensive view of her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC028"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC028", "user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are optimistic, direct. First, verify the identity of Robert Williams using his email robert.williams3479@email.com. Once his identity is confirmed, proceed to retrieve all customer lines associated with Robert Williams. After obtaining the list of lines, check the current status of each line to ensure they are functioning correctly. If any line, such as line ID L12345, is found to be active and needs to be temporarily suspended due to a billing issue or customer request, proceed to suspend that line under Robert Williams' account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.williams3479@email.com", "user_id": "TC006"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "robert.williams3479@email.com", "user_id": "TC006"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC006"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "Billing issue", "user_id": "TC006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are cautious, direct. First, use the Lookup_customer_by_phone task with the phone number +1234567890 to verify the identity of Michael Garcia. Once his identity is confirmed, proceed to Get_customer_lines for customer Michael Garcia to retrieve all active lines under his account. This process ensures that we are dealing with the correct customer and allows us to manage his account efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890", "user_id": "TC051"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Michael Garcia", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are polite, independent, organized. First, lookup_customer_by_phone with phone_number '123-456-7890' to verify identity for Robert Jones. After confirming the identity, get_customer_lines for customer_id 'CUST12345' to retrieve active lines associated with Robert Jones. Once you have the list of active lines, get_line_details for line_id 'LINE67890' to check the current plan and usage, ensuring all information is up-to-date for any further customer service actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are patient, optimistic, independent. Please begin by using the lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify Linda Davis's identity. Once her identity is confirmed, proceed to get_customer_lines for user_id=\"U3121\" to retrieve active phone lines for Linda Davis. This will help ensure that we have accurate information on her current services and can assist her effectively with any inquiries or changes she may need regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "U3121"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are optimistic, cautious. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity for user James Brown (james.brown7392@email.com)",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are organized, patient. Lookup_customer_by_phone with phone number 555-1234 to verify identity for Robert Brown.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are patient, confident, flexible, organized. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Patricia Brown's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are direct, cautious, optimistic. First, verify customer identity for Robert Brown using email robert.brown4954@email.com to ensure the account holder's authenticity. Once verified, get bill details for Robert Brown's account to review any outstanding balance that may have led to service issues. If there is an outstanding balance, suspend line ID L12345 due to non-payment to prevent further charges. Ensure each step is completed thoroughly to maintain service integrity and customer trust.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown4954@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "robert.brown4954@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "user_id": "TC129"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are optimistic, flexible, polite. Please begin by performing a lookup_customer_by_phone with phone number \"555-123-4567\" to verify Mary Jones's account. Once you have confirmed her account details, proceed to get_bill_details for user \"Mary Jones\" to review the latest billing statement and outstanding balance. This will help us ensure that we have accurate information before taking any further action regarding her service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC013"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user": "Mary Jones", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are independent, cautious, direct. lookup_customer_by_phone(phone_number=\"555-1234\")",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are polite, logical, flexible. To assist a customer in accessing their telecom account, first verify the identity of Linda Davis using her email, linda.davis8880@email.com, to ensure secure access to her account details. Once verified, proceed to get_customer_lines for Linda Davis using her customer ID to list all active lines on the account, ensuring she has the necessary information about her current services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis8880@email.com", "user_id": "TC150"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC150", "user_id": "TC150"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are flexible, independent. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify identity for user Jennifer Williams. Once her identity is confirmed, proceed to get_customer_lines for user_id \"jennifer.williams6918@email.com\" to retrieve all active lines associated with her account. This process ensures accurate customer service and account management in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "jennifer.williams6918@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are logical, flexible, patient, independent. \"lookup_customer_by_phone with phone number 555-1234 to verify identity and retrieve customer ID for James Brown\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are confident, independent, patient, logical. \"lookup_customer_by_phone with phone_number '555-1234' to verify identity of user Robert Jones\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are organized, logical, flexible, confident. First, get customer lines for account ID 987654 to list all active lines. After identifying the active lines, proceed to get line details for line ID L12345 to check the current plan and usage. This will help in assessing whether the customer is on the most suitable plan based on their current usage patterns.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "987654", "user_id": "TC073"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are patient, polite. Please lookup_customer_by_phone with phone_number 555-0123 to retrieve the customer ID and account details. Once you have the customer ID, get_bill_details for customer_id C123 to check the outstanding balance and payment history. If an outstanding balance is confirmed, transfer_to_human_agents for payment assistance to ensure the customer receives the necessary support to resolve their billing issue.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC063"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC063", "user_id": "TC063"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are logical, confident, optimistic. Begin by verifying the identity of user Robert Brown using his email robert.brown4015@email.com to ensure you are accessing the correct account. Once verified, proceed to look up customer Robert Brown by using the phone number associated with his account to obtain his customer ID. With the customer ID in hand, retrieve all active lines for Robert Brown to gain a comprehensive view of his current telecom services. This sequential approach will ensure you have accurate and detailed information to assist Robert Brown effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown4015@email.com", "user_id": "TC073"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC073", "user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are direct, cautious, polite. \"get_bill_details\" for customer ID associated with phone number \"555-123-4567\" to review outstanding balance",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are optimistic, polite, patient, direct. lookup_customer_by_phone(phone_number=\"555-1234\") to retrieve Linda Davis's customer ID and account details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are patient, logical, organized, cautious. Verify identity of user James Brown (james.brown6693@email.com) to access account details.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC089", "reason": "Verify identity of user James Brown (james.brown6693@email.com) to access account details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are polite, logical, optimistic, patient. Suspend_line using line ID L456 due to customer request for temporary suspension",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are organized, polite. First, lookup_customer_by_phone using Michael Johnson's registered phone number to retrieve customer account information. Once you have accessed his account, get_customer_lines associated with Michael Johnson's account to view all active lines. This will help us ensure that all lines are functioning properly and address any potential issues promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Johnson's registered phone number", "user_id": "TC134"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC134", "user_id": "TC134"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are confident, direct, polite, optimistic. lookup_customer_by_phone with phone_number \"555-1234\" to verify Patricia Johnson's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC040",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are cautious, polite, flexible. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify Patricia Brown's account. Once verified, proceed to get_customer_lines for customer_id 'C12345' to list all active lines associated with her account. Finally, get_line_details for line_id 'L67890' to check the current plan and usage, ensuring all information is up-to-date before taking any further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC040"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are optimistic, organized, flexible, logical. Use lookup_customer_by_phone with phone number \"555-1234\" to verify identity for user Linda Smith.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are polite, patient, cautious. First, use the Lookup_customer_by_phone with phone number 555-1234 to verify the identity of Michael Johnson. Once his identity is confirmed, proceed to Get_bill_details for customer ID C1023 to review his current charges and payment status. This will ensure that you have accurate information before discussing any potential billing discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC133"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC133", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are optimistic, independent, flexible. Verify the identity of user James Brown by confirming his email address (james.brown3113@email.com) and phone number before proceeding with account access. Once verified, use `lookup_customer_by_phone` to find customer details for James Brown using his verified phone number. This process ensures that you have the correct information to manage his telecom account effectively, maintaining both security and customer satisfaction.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "verified_phone_number"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are organized, optimistic. First, lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify Patricia Brown's account. Once verified, proceed to get_customer_lines for customer_id=\"C12345\" to list active lines under Patricia Brown's account, ensuring all lines are accurately accounted for to assist with her telecom service review.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC094"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC094", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are confident, direct, flexible. Get all customer lines for Mary Davis to review her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC020", "customer_name": "Mary Davis"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC020", "customer_name": "Mary Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are patient, independent. Suspend line with line ID L12345 for Michael Davis, due to non-payment, ensuring suspension rules are followed.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "non-payment", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are flexible, confident, patient, organized. Get_customer_lines for Mary Davis to list all active lines under her account.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC020", "customer_name": "Mary Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are optimistic, flexible. First, verify customer identity for Mary Miller using her email mary.miller8461@email.com to access account details. Once verified, proceed to lookup Mary's account using the verified email to retrieve her phone number for further actions. After obtaining her phone number, get_customer_lines to list all active and suspended lines on Mary's account for review. This will enable you to identify any lines that have been suspended for less than 30 days. For such lines, offer Mary the option to resume service and confirm her decision, ensuring a seamless experience in managing her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.miller8461@email.com", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "mary.miller8461@email.com", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are logical, optimistic, independent. Suspend line ID L12345 temporarily for user James Brown due to reported theft.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC116", "line_id": "L12345", "reason": "Reported theft", "reported_by": "Michael Jones", "contact_email": "michael.jones2722@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are direct, independent, polite, organized. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of Robert Williams. Once his identity is confirmed, proceed to get_bill_details for customer_id \"C12345\" to review any outstanding balance he may have. If an outstanding balance is confirmed and payment has not been made, suspend_line for line_id \"L67890\" due to non-payment, ensuring to add a note for Robert Williams explaining the suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC080"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "note": "Line suspended due to non-payment. Please contact customer service to resolve the issue.", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are confident, polite. Get line details for the primary line on James Davis's account to check current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC065", "phone_number": "James Davis"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC065", "customer_id": "TC065"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC065", "line_id": "primary_line"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are polite, logical, patient. First, get_line_details for line ID L67890 to review eligibility for plan upgrade. Once eligibility is confirmed, calculate cost difference for upgrading line ID L67890 to the next tier plan. This will help the customer understand the financial implications before proceeding with the plan upgrade.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC133"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "cost_difference", "line_id": "L67890", "current_plan": "basic", "new_plan": "premium"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are optimistic, logical. \"suspend_line for line ID 'L001' due to customer request for temporary suspension\"",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "customer request for temporary suspension", "user_id": "TC104"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are independent, patient, flexible. First, verify the identity of Robert Brown using email robert.brown5816@email.com before accessing his account details. Once verified, lookup the customer by phone number 555-0123 to retrieve the account ID for Robert Brown. This will ensure that you have the correct account information to proceed with any further actions related to his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are patient, optimistic, flexible, direct. Get_line_details for line ID L12345 to check current plan and usage details.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC067", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are cautious, patient, logical. Begin by using lookup_customer_by_phone with Patricia Smith's phone number to verify her identity and access her account details. Once her identity is confirmed, proceed to get_customer_lines for Patricia Smith to retrieve a list of all her active telecom lines. This process will ensure that you have accurate information about her account and can provide her with detailed assistance regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Smith's phone number", "user_id": "TC112"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC112", "user_id": "TC112"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC139",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are optimistic, patient. First, lookup customer by phone number using Michael Smith's phone number to verify identity for account access. Once Michael Smith's identity is verified, get customer lines for verified user Michael Smith to retrieve a list of active phone lines. This will allow us to ensure that all active lines are accounted for and properly managed, enhancing customer satisfaction and operational efficiency.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Smith's phone number", "user_id": "TC139"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC139", "user_id": "TC139"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are independent, polite. Get_line_details for line ID L123 to check current plan and usage details.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are direct, polite, independent. First, lookup customer by phone number using the phone number associated with Jennifer Johnson's account to confirm her identity and retrieve her account details. Then, proceed to suspend line with line ID L1234 due to a request from Jennifer Johnson, ensuring compliance with her service modification request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Johnson's phone number", "user_id": "TC149"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1234", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are independent, polite, confident, logical. Think to determine if Robert Jones is eligible for a plan upgrade based on usage patterns and current plan details. Once eligibility is confirmed, use specific line ID to change the plan for Robert Jones's line to the selected new plan, effective next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC123", "phone_number": "Robert Jones's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC123"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC123", "line_id": "specific line ID for Robert Jones"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if Robert Jones is eligible for a plan upgrade based on usage patterns and current plan details."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "eligibility criteria for plan upgrade"}
            ),
            Action(
                name="think",
                kwargs={"thought": "If eligible, proceed to change the plan for Robert Jones's line."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC123"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Select the new plan for Robert Jones's line."}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC123", "line_id": "specific line ID for Robert Jones"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Confirm the plan change will take effect on the next billing cycle."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are direct, confident. lookup_customer_by_phone with phone_number=\"555-1234\" to verify user identity for Linda Davis",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are cautious, confident. Suspend line L001 temporarily due to the requested account hold by Linda Davis. After suspending the line, confirm the suspension and provide Linda with reinstatement options, ensuring she understands that the service can be resumed upon her request within the 30-day suspension period.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC107"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC107", "line_id": "L001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC107", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are confident, flexible, direct, polite. First, use the lookup_customer_by_phone task with phone_number: \"555-123-4567\" to verify the customer's identity. If the identity verification is successful, proceed to the next step. If the verification fails, politely inform the customer that you are unable to proceed without proper verification and suggest they contact customer support for further assistance. Once the identity is confirmed, use the get_customer_lines task for user_id: \"JJ5907\" to retrieve all active lines associated with the customer. If there are any issues retrieving the customer lines, apologize for the inconvenience and recommend the customer try again later or reach out to customer support for immediate help.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "JJ5907"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is John Garcia and your email is john.garcia3458@email.com. You are organized, patient. First, lookup_customer_by_phone with phone number 555-1234 to verify Robert Garcia's identity as part of the routine customer verification process. Once verified, proceed to get_line_details for line ID L456 to retrieve current plan and usage details, ensuring you have the necessary information to discuss any potential changes or upgrades with the customer.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC046"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are optimistic, confident, direct. Use `get_line_details` to verify if line ID L6543 is eligible for a data plan upgrade.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC035", "line_id": "L6543"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are logical, optimistic, flexible, organized. Begin by verifying the customer identity for user Robert Williams using the email robert.williams3951@email.com to ensure account security. Once verified, proceed to lookup the customer by phone using the verified phone number to retrieve Robert Williams' account details. After accessing the account, get the customer lines for Robert Williams to list all active lines on the account. This will provide a comprehensive view of the services associated with the customer, allowing you to manage the account effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.williams3951@email.com", "user_id": "TC080"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "verified_phone_number", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are cautious, logical, flexible. First, verify the identity of the user Jennifer Jones using her email jennifer.jones5314@email.com before accessing her account details. Once her identity is confirmed, check the current billing details for Jennifer Jones' account to confirm the billing cycle and amount due. This process is crucial to ensure that Jennifer receives accurate billing information and maintains seamless service with our telecom company.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.jones5314@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are confident, direct, polite. lookup_customer_by_phone with parameter phone_number set to \"555-1234\" to verify identity and retrieve customer ID and account status for Mary Jones",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are flexible, organized, patient. Use lookup_customer_by_phone with phone number 555-123-4567 to verify Jennifer Smith's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC143"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are logical, organized, polite, confident. First, verify customer identity using Patricia Smith's email (patricia.smith8398@email.com) to access her account details. Once her identity is confirmed, proceed to get customer lines for Patricia Smith's account to view both active and suspended lines. Finally, get line details for Patricia Smith's primary line to check her current plan and usage, ensuring she has the appropriate data plan for her needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.smith8398@email.com", "user_id": "TC112"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "patricia.smith8398@email.com", "user_id": "TC112"}
            ),
            Action(
                name="get_line_details",
                kwargs={"email": "patricia.smith8398@email.com", "line_id": "primary", "user_id": "TC112"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are logical, polite. lookup_customer_by_phone with phone_number \"555-1234\" to verify John Garcia's account identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are optimistic, logical, direct. First, verify Jennifer Williams' identity using email jennifer.williams6918@email.com for account access to ensure security compliance. Once her identity is confirmed, get_bill_details for Jennifer Williams' account ID to review any outstanding balance, which is crucial for maintaining her telecom services without interruption. If there are any payment issues or she requires further assistance, transfer_to_human_agents to discuss flexible payment options and provide personalized support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.williams6918@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC131"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are polite, optimistic. First, verify customer identity using Patricia Johnson's email (patricia.johnson6047@email.com) before accessing account details. Once her identity is confirmed, get bill details for Patricia Johnson's account to review the latest charges and payment status. This process ensures that we maintain account security and provide accurate billing information, which is crucial for discussing any potential discrepancies or concerns she may have with her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.johnson6047@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are flexible, optimistic, independent, organized. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify identity for user Michael Jones. Once identity is confirmed, proceed to get_customer_lines with customer_id \"C4016\" to retrieve all active phone lines associated with Michael Jones. This will help ensure that we have the correct account details before discussing any plan changes or updates.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC042"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC042", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are cautious, logical. suspend_line(line_id=\"L8901\", reason=\"Customer Request\") to temporarily suspend service for line L8901",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L8901", "reason": "Customer Request", "user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are direct, cautious, independent. First, verify the identity of Robert Brown using his email robert.brown4015@email.com before accessing his account. Once his identity is confirmed, lookup the customer by phone number associated with Robert Brown to retrieve his customer ID. With the customer ID in hand, get customer lines for Robert Brown to list all active lines, ensuring you have a comprehensive view of his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown4015@email.com", "user_id": "TC073"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC073", "user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are confident, patient. First, verify customer identity for Robert Brown using email robert.brown4954@email.com to access account details. Once verified, get bill details for Robert Brown's account to review outstanding balance and payment history. After reviewing, calculate the total amount due for Robert Brown's account including any late fees or adjustments. This process will ensure you have all necessary information to assist Robert Brown effectively with his telecom account inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown4954@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC129"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["outstanding_balance", "late_fees", "adjustments"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are independent, optimistic, patient, cautious. First, lookup_customer_by_phone with phone number '555-0199' to verify Michael Williams' account identity. Once his identity is confirmed, get_bill_details for account ID 'C1023' to review outstanding balance and payment due date, ensuring all information is accurate for customer service purposes in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0199", "user_id": "TC007"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "C1023", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are flexible, polite, independent. First, use the Lookup_customer_by_phone task with phone number 555-123-4567 to verify the identity of Mary Smith. Once her identity is confirmed, proceed with the Get_customer_lines task for customer ID 4137 to retrieve all active lines associated with Mary Smith's account. This will ensure you have the correct information before discussing any account details with her.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC138"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC138", "user_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are direct, organized, confident. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Michael Jones' identity. Once verified, get_customer_lines for user Michael Jones to retrieve all active lines, ensuring you have a comprehensive view of his current services. After identifying his active lines, get_line_details for line ID L001 to check the current plan and usage, as this will provide insights into his data consumption patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC083", "customer_name": "Michael Jones"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC083", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are direct, independent. Use lookup_customer_by_phone with michael.miller4797@email.com to retrieve Michael Miller’s account details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.miller4797@email.com", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are direct, patient. First, lookup_customer_by_phone with phone_number '555-1234' to verify customer identity for account access. Once verified, proceed to get_customer_lines for customer_id 'C7392' to retrieve all active lines associated with the account. This will allow us to ensure the customer has access to all their services and address any potential issues with their telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC116"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC116", "user_id": "TC116"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are independent, organized, direct. A customer has called in to request the suspension of one of their phone lines due to temporary non-use. First, lookup_customer_by_phone(phone_number=\"555-123-4567\") to identify the customer and retrieve their customer ID. Then, use the customer ID to get_customer_lines(customer_id=\"C123456\") to find all active lines associated with the customer. Once you have identified the correct line that the customer wishes to suspend, proceed to suspend_line(line_id=\"L789012\", reason=\"customer request\").",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC130"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L789012", "reason": "customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are direct, polite, confident. First, lookup_customer_by_phone with phone number 555-0173 to verify identity for Robert Garcia. Once his identity is confirmed, proceed to get_customer_lines for the customer ID retrieved from the previous step to list all active lines under his account. After identifying the relevant line, get_line_details for line ID L12345 to check its current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0173", "user_id": "TC003"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC003", "user_id": "TC003"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are polite, organized, logical. Robert Williams has contacted customer service to request assistance with his account. First, lookup_customer_by_phone with phone number provided by Robert Williams to verify identity. Once his identity is confirmed, proceed to get_customer_lines for verified customer Robert Williams to list all active lines on his account. After identifying the specific line, get_line_details for line ID L102 to check the current plan and data usage, as Robert is considering changes due to his upcoming temporary travel.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_by_robert_williams", "user_id": "TC067"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC067", "user_id": "TC067"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L102", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are independent, confident, polite, logical. First, lookup customer by phone number 555-0123 to verify Mary Miller's identity for account access. Once her identity is verified, proceed to get bill details for the account associated with Mary Miller to review the outstanding balance. Finally, calculate the total amount due for Mary Miller's account to provide her with accurate payment options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC102"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC102", "user_id": "TC102"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "sum(bill_details.outstanding_balance)", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are cautious, patient. Get_bill_details for Robert Davis to review outstanding balance and payment history.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC032", "customer_name": "Robert Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are logical, patient, polite. First, verify customer identity using Michael Miller's email (michael.miller4797@email.com) to ensure secure account access. Once verified, proceed to lookup_customer_by_phone using the phone number associated with Michael Miller's account to retrieve his customer ID. With the customer ID, get_customer_lines for Michael Miller's account to identify all active lines, ensuring you have a comprehensive understanding of his current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.miller4797@email.com", "user_id": "TC054"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC054", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are polite, confident. First, verify the identity of user Robert Jones with email robert.jones1563@email.com to ensure secure handling of his account. Once his identity is confirmed, proceed to get details for line L12345 associated with Robert Jones to review his current plan and usage. Based on this information, initiate a plan change request for line L12345 to upgrade Robert Jones to a higher data plan, ensuring he has sufficient data for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones1563@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC144", "line_id": "L12345"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC144", "line_id": "L12345", "reason": "Request to upgrade to a higher data plan"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are flexible, organized. Get_line_details for line ID L789 to verify eligibility for plan upgrade",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are organized, patient, logical, confident. First, verify customer identity using the email address robert.davis2812@email.com for account access. Once the identity is confirmed, proceed to get the list of all active lines for customer Robert Davis to check usage details. This process will ensure that we have the correct account information and can provide accurate data on his current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.davis2812@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are confident, polite, optimistic. First, verify customer identity for Robert Brown using email robert.brown6285@email.com to access account details. Once verified, get_bill_details for Robert Brown to review outstanding charges and payment history. If there are unpaid charges, proceed to suspend_line for line ID L1234 due to non-payment, ensuring Robert Brown is informed about the suspension and provided with details on how to resolve the issue to resume service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1234", "reason": "Non-payment", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are direct, cautious, patient, optimistic. First, lookup_customer_by_phone with phone number 555-1234 to verify customer identity for Jennifer Davis. Once verified, proceed to get_line_details for line ID L9876 to check current plan and usage details. Finally, think to determine if a data refill is needed based on current usage and plan, considering Jennifer's recent increase in data consumption and her upcoming billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC085"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC085"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Evaluate if a data refill is needed based on Jennifer's current plan and usage details, considering her recent increase in data consumption and upcoming billing cycle."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are logical, polite, organized, independent. First, lookup_customer_by_phone with phone_number '555-0123' to verify the identity of Michael Garcia. Once verified, proceed to get_customer_lines for customer_id 'C12345' to list all active lines associated with Michael Garcia's account. This will help ensure that all customer inquiries are addressed accurately and efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC051"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC051", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are cautious, independent. Retrieve get_bill_details using customer ID to obtain the latest billing information for Robert Jones.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are flexible, confident. First, use lookup_customer_by_phone with phone_number \"555-1234\" to verify Linda Miller's account. Once verified, proceed to use get_customer_lines with customer_id \"CM1663\" to retrieve all active lines for Linda Miller. Finally, use get_line_details with line_id \"L102\" to check the current plan and status of Linda Miller's primary line, ensuring all information is up-to-date for any necessary adjustments or customer inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC019"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are optimistic, cautious, organized, flexible. First, perform a lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Jennifer Davis's account. Once her account is verified, proceed to get_customer_lines for customer_id \"C12345\" to list all active lines on Jennifer Davis's account. This will help ensure that all lines are correctly associated with her account before any further actions are taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC085"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC085", "user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are organized, cautious, optimistic, direct. A customer has called requesting assistance with their account. First, lookup_customer_by_phone with parameters: phone_number=\"555-0123\" to identify the customer. Once you have the customer ID, proceed to get_customer_lines with parameters: customer_id=\"C34567\" to review all active lines associated with the account. After identifying the specific line in question, execute get_line_details with parameters: line_id=\"L89012\" to gather detailed information about that line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC028"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L89012"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are cautious, confident. First, lookup_customer_by_phone with phone number 555-0134 to verify identity for Mary Brown. Once her identity is confirmed, transfer_to_human_agents with context \"Mary Brown requests plan upgrade options for line ID L5678\" to provide her with detailed information on available plans.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0134", "user_id": "TC063"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "Mary Brown requests plan upgrade options for line ID L5678", "user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are direct, patient, cautious, optimistic. Suspend line with line ID L12345 for account associated with James Brown due to reported issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC116", "phone_number": "N/A"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC116"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC116", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are independent, flexible. lookup_customer_by_phone with phone number 555-1234 to verify identity for James Brown",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are optimistic, organized. Get bill details for Robert Jones to review the latest billing statement and any outstanding payments.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is John Garcia and your email is john.garcia3458@email.com. You are flexible, polite. First, perform a lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Robert Garcia's account identity. Once verified, proceed to get_customer_lines for customer_id \"C001\" to retrieve all active lines under Robert Garcia's account. Finally, for the primary line identified, execute get_line_details for line_id \"L123\" to check the current plan and usage details, ensuring that Robert is on the best plan for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC046"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC046", "user_id": "TC046"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are flexible, logical. Get line details for the primary line on Robert Brown's account to check current plan and usage. Then, think about available options for Robert Brown to upgrade his mobile plan based on current usage. This will help ensure that Robert Brown is on the most suitable plan for his needs, optimizing both his service experience and cost efficiency.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC120", "phone_number": "Robert Brown's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC120", "customer_id": "TC120"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC120", "line_id": "primary line ID for Robert Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are logical, flexible. Lookup customer by phone number 555-1234 to verify account identity for Jennifer Jones.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are optimistic, logical, polite. First, lookup_customer_by_phone with phone number 555-0123 to verify identity for account access. Once the customer's identity is confirmed, proceed to get_line_details for line ID L789012 to check the current plan and usage. After reviewing the line details, calculate data usage for line ID L789012 to determine if a data refill is needed. If the usage exceeds 90%, transfer_to_human_agents with a request to add a data refill for line ID L789012, ensuring the customer continues to enjoy uninterrupted service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC038"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789012", "user_id": "TC038"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "usage / total_data * 100"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"request": "Add a data refill for line ID L789012", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are logical, optimistic, polite, patient. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of user Robert Jones, ensuring that we are assisting the correct individual. Once verified, proceed to get_customer_lines for customer_id \"CUST001\" to retrieve all active phone lines associated with Robert Jones, so we can provide detailed assistance. Finally, get_line_details for line_id \"LINE123\" to check the current plan and usage details, enabling us to offer precise information about his plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC144", "user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE123", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are organized, polite, flexible, logical. First, verify the identity of user James Davis using the email james.davis6038@email.com to access his account details. Once his identity is confirmed, proceed to get the bill details for James Davis using the customer ID to review any outstanding balance. This process is crucial to ensure that all account information is accurate and up-to-date, which will help in maintaining a smooth billing cycle and customer satisfaction within our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.davis6038@email.com", "user_id": "TC065"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC065", "user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are confident, direct, independent. Verify the identity of user Linda Davis using email linda.davis3121@email.com for account access. Once verified, lookup customer by phone number 555-0123 to retrieve account details for Linda Davis. After confirming her account details, get customer lines associated with Linda Davis's account to check active services, ensuring all information is accurate and up to date for any necessary follow-up actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC035"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "555-0123", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are polite, patient. First, perform a Lookup_customer_by_phone with the parameter phone_number set to \"555-123-4567\" to verify your identity as John Smith. Once verified, proceed with Get_customer_lines for the user identified as John Smith to retrieve all associated phone lines. After identifying the relevant line, use Get_line_details for line ID L001 to check the current status and plan details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC081"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are patient, independent. First, lookup Mary's customer account using her phone number 555-1234 to retrieve account details. Then, get bill details for Mary Johnson to verify the latest charges and payment status. This process is essential to ensure that her account is up-to-date and to provide her with accurate information regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC071"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_name": "Mary Johnson", "user_id": "TC071"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are confident, flexible, direct. Use lookup_customer_by_phone with phone number 123-456-7890 to retrieve customer Patricia Williams' account details. Once you have the account details, proceed to Get_customer_lines for Patricia Williams to identify all active lines associated with her account. After identifying the active lines, use Get_line_details for line ID L001 to check the current plan and usage details. This information will help you understand her current service and usage patterns, allowing you to have an informed discussion when you Transfer_to_human_agents to discuss potential plan upgrades and promotions available for Patricia Williams.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC092"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC092", "user_id": "TC092"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC092"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC092", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC061",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are direct, polite. First, lookup Patricia Davis by phone number to verify her identity for account access. Once her identity is confirmed, get customer lines for Patricia Davis to list all active services associated with her account. Finally, get bill details for Patricia Davis’s account to review recent charges and payments, ensuring she is informed about her current financial obligations and any discrepancies can be addressed promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia's phone number", "user_id": "TC061"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC061", "user_id": "TC061"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC061", "user_id": "TC061"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are direct, patient, independent, cautious. Lookup_customer_by_phone with phone number 555-1234 to verify identity for accessing John Brown's account. Once verified, proceed to Get_customer_lines for customer ID C8493 to retrieve the list of active lines under John Brown's account. This process is crucial to ensure that only authorized individuals can access sensitive account information and manage the services associated with John Brown's telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC124"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC124", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are optimistic, flexible. First, get bill details for the account associated with phone number 123-456-7890 to verify the outstanding balance. Once you have confirmed the outstanding balance and ensured it matches the expected amount, process a payment of $100 for the account. Note the payment processing time to ensure it aligns with our standard transaction timelines. This sequence of actions will help maintain accurate financial records and ensure customer satisfaction in our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC108"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the outstanding balance matches the expected amount."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "outstanding_balance - 100"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure the payment processing time aligns with our standard transaction timelines of 1-2 business days."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are patient, organized, polite. Get_customer_lines for Robert Garcia's account to list all active and suspended lines.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC003", "customer_name": "Robert Garcia"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are direct, confident, polite. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify customer identity for Robert Garcia",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are logical, cautious. Verify customer identity for Mary Johnson using email mary.johnson8773@email.com to access account details.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC093", "reason": "Customer identity verification required for account access"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are optimistic, logical, patient, confident. First, use the lookup_customer_by_phone with phone_number \"123-456-7890\" to verify the user's identity for account access. Once the identity is confirmed, proceed to get_customer_lines for user_id \"john.smith6383@email.com\" to retrieve all active lines associated with the account. This will help ensure that the user has access to their current services and can manage their telecom needs effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are organized, patient, direct. First, use the Lookup_customer_by_phone task with the phone number associated with Jennifer Johnson to retrieve her account details. Once you have the account information, proceed to Get_customer_lines for Jennifer Johnson's account to list all active lines she currently has. After identifying the active lines, focus on the Get_line_details for line ID L234567 to check the current plan and usage details. This will help determine if there is a need to adjust the plan or usage, ensuring Jennifer Johnson's telecom needs are met efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Johnson's phone number", "user_id": "TC149"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "Account ID retrieved from previous step", "user_id": "TC149"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L234567", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are independent, direct, flexible, cautious. First, lookup customer by phone number 555-1234 to verify identity for James Brown. After successfully verifying his identity, proceed to get customer lines for James Brown to ensure all his active lines are up-to-date and functioning correctly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC089"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "James Brown", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are flexible, direct. First, use lookup_customer_by_phone with parameters: phone_number=555-123-4567 to verify identity for John Garcia. Once verified, proceed to use get_customer_lines with parameters: customer_id=JGarcia3458 to retrieve all active lines for John Garcia, ensuring you have a comprehensive view of his account. Finally, use get_line_details with parameters: line_id=L9876 to check current plan and usage details for John Garcia's primary line, as this information is crucial for advising him on potential plan upgrades or adjustments based on his current usage patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC015"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are direct, optimistic, flexible, polite. First, lookup customer by phone using Michael Johnson’s phone number to verify his identity. Once verified, proceed to suspend line L23456 temporarily due to inactivity reported by Michael Johnson. This action ensures that the line remains secure and prevents unauthorized use while it is not needed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Johnson's phone number", "user_id": "TC133"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L23456", "reason": "Temporary suspension due to inactivity", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are direct, cautious. First, get bill details for Michael Garcia's account to review the outstanding balance. Once you have reviewed the balance, calculate the total amount due, including any late fees, for Michael Garcia's bill. This will ensure that you have a comprehensive understanding of the financial obligations before proceeding with any further actions.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC051", "customer_name": "Michael Garcia"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are flexible, logical, patient. lookup_customer_by_phone with phone_number '555-0123' to verify Patricia Miller's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC061",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are independent, cautious, polite. First, lookup_customer_by_phone with phone number (555-0123) to verify Patricia Davis's identity for account access. Once her identity is confirmed, proceed to get_customer_lines for customer Patricia Davis to retrieve a list of active lines. This will help ensure that all active services are accurately accounted for and managed effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC061"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Patricia Davis", "user_id": "TC061"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are organized, flexible, independent, direct. First, perform a Lookup_customer_by_phone with phone number 555-1234 to verify the identity of Robert Garcia. Once verified, proceed to Get_customer_lines for user Robert Garcia to list all active lines associated with his account. After identifying the active lines, execute a Suspend_line for line ID L002 to temporarily halt service as requested by Robert Garcia. This sequence ensures that the correct line is suspended while maintaining accurate records of active services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC003", "customer_name": "Robert Garcia"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC003", "line_id": "L002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are independent, polite. First, get bill details for the current billing cycle for Robert Brown's account to ensure all charges are accurate and up-to-date. Then, calculate the total amount due on Robert Brown's account including any late fees to understand the full payment required. This sequence will help in managing your telecom expenses effectively.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are organized, cautious. First, use the lookup_customer_by_phone task with phone_number: \"+1234567890\" to verify the identity of John Davis. Once verified, proceed to get_customer_lines with customer_id: \"C12345\" to retrieve the active lines associated with John Davis. After identifying the relevant line, use the get_line_details task with line_id: \"L67890\" to check the current plan and usage details. This sequence ensures that you have the necessary information to assist John Davis effectively with his telecom service inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC074"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are patient, direct, logical. First, lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify the identity of Jennifer Brown, who has requested a temporary suspension of her phone line due to an extended overseas trip. Once her identity is confirmed, proceed to suspend_line for line_id=\"L5678\" with reason=\"Customer Request\" to ensure her service is paused during her absence.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "reason": "Customer Request", "user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are direct, cautious, independent. Resume suspended line L12345 for John Miller within 30-day grace period upon payment confirmation",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC104"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC104"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC104", "line_id": "L12345"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC104"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC104", "line_id": "L12345", "action": "resume"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are confident, optimistic. Lookup the phone number associated with James Brown's account using his email james.brown7392@email.com. Once you have identified the phone number, retrieve all customer lines for that number to identify active services. This will help ensure that James Brown's account is up-to-date and all services are functioning as expected.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown7392@email.com", "user_id": "TC116"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "retrieved_phone_number", "user_id": "TC116"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are independent, direct. lookup_customer_by_phone with phone_number=\"555-0198\" to verify identity for Michael Garcia",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0198"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are logical, cautious, patient. First, lookup customer by phone number to retrieve Linda Davis's account information. Next, get customer lines for Linda Davis to identify all active lines associated with her account, ensuring that all services are accounted for. Finally, get bill details for Linda Davis to review outstanding balances and payment history, so you can have a comprehensive understanding of her financial obligations and prepare for any necessary discussions with a human agent.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC107"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are independent, confident, direct. lookup_customer_by_phone(phone_number=\"555-123-4567\") to verify Patricia's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are logical, direct. First, lookup_customer_by_phone with phone_number=555-1234 to verify account for Jennifer Smith. Once her account is verified, proceed to get_line_details for line_id=L67890 to check her current plan and usage. This will help us ensure that her current plan meets her usage needs effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC143"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are direct, organized. Retrieve billing details for Robert Jones to check the last payment date, and then calculate the overdue amount on Robert Jones' account based on the latest bill. This information is crucial for our telecom company to assess his account status and ensure we provide accurate financial advice.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC109", "customer_name": "Robert Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are independent, logical. First, get bill details for Michael Davis's account to confirm the outstanding balance. Once you have confirmed the balance, if there is a non-payment issue, suspend the line for line ID L001 on Michael Davis's account. This sequence ensures that you are aware of the billing status before taking action to suspend the line, which is crucial for maintaining accurate account management in the telecom industry.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC136"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC136", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are confident, polite, flexible. First, lookup_customer_by_phone with phone_number '123-456-7890' to verify identity for Michael Williams. Once identity is confirmed, get_line_details for line_id 'L67890' to confirm eligibility for plan upgrade. If Michael Williams is eligible and wishes to proceed, transfer_to_human_agents with customer_id 'C12345' for assistance with plan change.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC007", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are logical, independent, direct. First, get line details for line ID L002 to review eligibility for plan upgrades or changes. Once eligibility is confirmed, calculate the cost difference for John Brown if line L002 is upgraded to a premium plan. This will help John understand the financial implications of the upgrade and make an informed decision.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC124", "line_id": "L002"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC124"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "(premium_plan_cost - current_plan_cost)"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are independent, polite, cautious. Process a plan change request for line ID L9876 to upgrade to a higher data plan, effective next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC083"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC083"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC083", "line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are patient, direct, logical. lookup_customer_by_phone with phone number \"123-456-7890\" to verify Mary Jones's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are patient, optimistic, direct, cautious. Get details for line ID L123 to verify eligibility for plan upgrade, then think to assess best plan change options for line ID L123 based on usage patterns. As a customer service representative at a telecom company, you need to ensure that the customer is eligible for an upgrade and that the new plan will suit their usage needs effectively. First, check the current plan details, contract terms, and any promotional offers available for line ID L123. Once eligibility is confirmed, analyze the customer's usage patterns, such as data consumption, call frequency, and international usage, to recommend the most suitable plan options.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC116"}
            ),
            Action(
                name="think",
                kwargs={"thoughts": "Assess the current plan details, contract terms, and promotional offers for eligibility of plan upgrade for line ID L123."}
            ),
            Action(
                name="think",
                kwargs={"thoughts": "Analyze the customer's usage patterns such as data consumption, call frequency, and international usage to recommend the most suitable plan options."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are polite, optimistic, patient, flexible. Begin by verifying customer identity for Linda Davis using her email linda.davis8880@email.com. Once her identity is confirmed, proceed to retrieve bill details for the current billing cycle for Linda Davis's account to review outstanding charges. After reviewing the bill details, calculate the total amount due for Linda Davis's account, including any late fees or additional charges, to ensure she has an accurate understanding of her financial obligations.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Begin by verifying customer identity for Linda Davis using her email."}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis8880@email.com"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once identity is confirmed, proceed to retrieve bill details for the current billing cycle."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC150"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Calculate the total amount due including any late fees or additional charges."}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["outstanding_charges", "late_fees", "additional_charges"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are independent, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify identity for Michael Jones. Once verified, get_bill_details for customer ID C1001 to review recent charges and payments. This will help ensure that Michael Jones is on the most cost-effective plan based on his usage patterns and billing history.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC083"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC083", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are flexible, polite. \"lookup_customer_by_phone with phone number '555-1234' to verify Linda Smith's identity and access her account\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are patient, polite. Verify the identity of James Jones using his email address (james.jones7788@email.com) to access account details. Once verified, suspend line ID L123 due to suspected fraudulent activity, ensuring James is aware of the 30-day reconnection window.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.jones7788@email.com", "user_id": "TC106"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "user_id": "TC106"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are patient, flexible, organized. First, get the bill details for Robert Davis's account to review the outstanding balance and due date. Once you have this information, calculate the total payment required, including any late fees, for Robert Davis's account using the retrieved bill details. This will ensure that Robert has a clear understanding of his financial obligations with our telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are optimistic, patient, polite. Please verify the identity of user Linda Garcia using the email linda.garcia2678@email.com to ensure secure access to her account. Once verified, proceed to lookup customer details by the phone number associated with Linda Garcia to retrieve her account information. Finally, get customer lines for Linda Garcia to identify both active and suspended lines, ensuring accurate account management and support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.garcia2678@email.com", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "linda.garcia2678@email.com", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are patient, organized, confident, flexible. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Jennifer Johnson's identity as she has requested a temporary suspension of her service. Once her identity is confirmed, proceed to get_line_details for line ID L204 to check her current plan and usage details to ensure there are no pending issues that might affect the suspension process. After confirming the details, suspend_line for line ID L204 to temporarily halt the service as per Jennifer's request. Finally, get_customer_lines for customer ID C1023 to confirm the status of all lines after the suspension, ensuring everything is updated correctly in our system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC149"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L204", "user_id": "TC149"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L204", "user_id": "TC149"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC149", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are flexible, direct, confident. Begin by performing a lookup of the customer using the phone number associated with user James Brown. Once you have identified the customer through this phone lookup, proceed to get the customer's lines to review all active services. This will help in providing a comprehensive overview of the customer's current telecom setup and facilitate any necessary follow-up actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "James Brown's phone number", "user_id": "TC116"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC116", "user_id": "TC116"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are independent, flexible, direct, confident. lookup_customer_by_phone with phone_number \"555-123-4567\" to confirm identity for plan upgrade",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are patient, direct, cautious, independent. A customer has contacted you to temporarily suspend their phone line for personal reasons. First, authenticate the user by performing a lookup_customer_by_phone with phone_number=\"555-123-4567\". Once authenticated, proceed to suspend_line for line_id=\"LINE67890\" as per the customer's request for a temporary hold.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE67890", "user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is John Garcia and your email is john.garcia3458@email.com. You are optimistic, organized, patient, flexible. \"lookup_customer_by_phone\" with parameter phone_number set to \"+1234567890\" to retrieve customer details for James Brown.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are organized, patient, optimistic. First, lookup customer by phone number 555-1234 to verify identity for Patricia Smith, ensuring that you have the correct customer account before proceeding. Once verified, get bill details for customer ID C12345 to review current charges and payment status, as Patricia has reported a service disruption and is expecting a credit adjustment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC113"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC113", "user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are optimistic, flexible. suspend_line(line_id=\"LINE67890\", reason=\"Customer request\")",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE67890", "reason": "Customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are direct, logical, organized, optimistic. Use lookup_customer_by_phone with phone number 555-1234 to verify Patricia Brown's identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are direct, logical. Get line details for Linda Smith's primary line to check current plan and usage, then calculate data usage for Linda Smith's primary line to determine if a data refill is needed. This will help ensure that Linda Smith is on the most efficient plan and avoids any potential overage charges, enhancing customer satisfaction and optimizing service delivery.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC041", "phone_number": "primary"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC041"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC041", "line_id": "primary"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "data_usage", "line_id": "primary"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are cautious, patient. First, perform a Lookup_customer_by_phone with phone number 555-1234 to retrieve customer account details. Then, once you have confirmed that the account belongs to Mary Miller, proceed to Get_customer_lines for her account to list all active lines. After identifying the line L001 as the one she wishes to temporarily suspend, proceed to Suspend_line for line L001 with the reason \"customer request\" and note \"temporary suspension requested by Mary Miller.\" This sequence ensures that you have verified the correct account and line before proceeding with the suspension request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_name": "Mary Miller", "user_id": "TC102"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "customer request", "note": "temporary suspension requested by Mary Miller", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are optimistic, independent. First, perform a lookup_customer_by_phone using the phone number 555-123-4567 to verify Patricia Miller's identity. Once her identity is confirmed, proceed to get_customer_lines for user Patricia Miller to retrieve all active lines on her account. This will help ensure that all account details are accurate and up-to-date, providing a seamless experience for Patricia Miller in managing her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC028"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are independent, confident, direct, logical. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify customer identity for Linda Smith. Once her identity is confirmed, proceed to get_bill_details for customer_id \"C001\" to review her current billing statement. This will help ensure that Linda's billing details are accurate and up-to-date, allowing you to address any discrepancies or concerns she might have regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC146"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC146", "user_id": "TC146"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are organized, optimistic, logical, direct. lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity of Jennifer Davis",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are logical, independent. Verify the identity of user James Jones using email james.jones7788@email.com for account access. Once verified, lookup the customer by the phone number associated with James Jones to retrieve the customer ID. Then, get customer lines for the retrieved customer ID to check active lines. This process will ensure that James Jones has the correct access to his telecom account, allowing us to manage his services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.jones7788@email.com", "user_id": "TC106"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC106", "user_id": "TC106"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are cautious, independent, flexible. Verify the identity of Linda Miller using the email linda.miller1663@email.com to ensure secure access to her account. Once verified, lookup the customer by the phone number associated with Linda Miller's account to retrieve her customer ID. Then, use this customer ID to get the customer lines for Linda Miller, allowing you to view both active and suspended lines, which is crucial for managing her telecom services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.miller1663@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are cautious, optimistic, polite. First, lookup the customer by email to verify identity for account access using james.brown7392@email.com. Once the identity is verified, get customer lines for the user ID associated with james.brown7392@email.com to view all active lines. After identifying the relevant line, get line details for line ID L12345 to check the current plan and data usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown7392@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC116"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are direct, confident. First, lookup customer by phone number 555-1234 to verify the identity of Jennifer Smith. Once her identity is confirmed, proceed to get customer lines for user Jennifer Smith (jennifer.smith9988@email.com). After reviewing the customer lines, suspend line L9876 for user Jennifer Smith due to reported issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC023"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "jennifer.smith9988@email.com", "user_id": "TC023"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are cautious, logical, patient, independent. First, lookup customer by phone using John Williams' phone number to retrieve account details. Once you have accessed his account, get customer lines linked to John Williams' account to identify active services. This process will help you verify which services are currently operational and ensure accurate management of his telecom needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "John Williams' phone number", "user_id": "TC031"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are patient, independent, cautious. Use lookup_customer_by_phone with phone number '555-0123' to verify identity of user James Brown.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are organized, confident, logical, cautious. Suspend_line for line ID L001 on Michael Johnson's account due to non-payment",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Johnson"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC134"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC134"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are patient, flexible, polite. Suspend_line for a specific line under Michael Jones' account that is reported lost or stolen, with a note for temporary suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC083"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC083"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC083", "line_id": "line_001"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC083", "line_id": "line_001", "note": "Temporary suspension due to loss or theft"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are confident, optimistic, logical. First, lookup_customer_by_phone with phone number '555-123-4567' to verify identity and access account details. Once the customer's identity is confirmed, get_bill_details for customer ID 'C00123' to review recent payments and outstanding balance. This will help you understand the customer's billing situation before proceeding with any further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC089"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC089", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are optimistic, cautious, direct, organized. \"lookup_customer_by_phone with phone number 123-456-7890 to verify customer identity for Robert Johnson\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are organized, optimistic. Process a plan change request for line ID L001 to a higher data plan, effective next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC104"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC104"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the current plan details and eligibility for upgrade."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Proceed with plan change request for line ID L001 to a higher data plan."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are organized, confident, direct, flexible. First, check the current plan details for Robert Jones's primary line to understand his existing service parameters. Then, calculate the remaining data on Robert Jones's primary line based on current usage to assess if his current plan is meeting his needs effectively. This will help in determining if any adjustments or plan changes are necessary to optimize his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC144", "phone_number": "primary"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC144", "line_id": "primary"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC144", "operation": "remaining_data", "line_id": "primary"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are organized, flexible, direct. First, lookup the customer by phone number associated with Mary Jones to retrieve the customer ID. Once you have the customer ID, use it to get all active phone lines for this customer. Finally, for the line ID L12345 under this customer ID, check the current plan and usage details. This sequence of tasks will help us understand the customer's current telecom setup and identify potential areas for plan optimization.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Jones", "user_id": "TC013"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC013", "user_id": "TC013"}
            ),
            Action(
                name="get_line_details",
                kwargs={"customer_id": "TC013", "line_id": "L12345", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are flexible, patient, organized, optimistic. Verify the identity of user John Garcia using email john.garcia3458@email.com for account access, then retrieve all phone lines associated with John Garcia's account using the customer ID obtained from the identity verification process. This will ensure that we maintain secure access while providing comprehensive service details for telecom account management.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia3458@email.com", "user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC015", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are organized, optimistic. First, verify the identity of Michael Williams using the email michael.williams1902@email.com to ensure secure access to his account details. Once verified, retrieve the bill details for the latest billing cycle to check the payment status and identify any outstanding amounts. Finally, calculate the total amount due for Michael Williams, taking into account any late fees or adjustments, to provide him with accurate information regarding his current financial obligations with the telecom service provider.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to verify the identity of Michael Williams using his email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Since there is no direct tool to verify identity using email, I will transfer this task to human agents."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"reason": "Verify identity of Michael Williams using email michael.williams1902@email.com for secure access."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once identity is verified, I will proceed to retrieve the bill details for the latest billing cycle."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC007"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After retrieving the bill details, I will calculate the total amount due, including any late fees or adjustments."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "total_due = bill_amount + late_fees - adjustments"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are independent, optimistic. Get_line_details for line ID L12345 to check current plan and usage details. Then, think about possible plan upgrades for line ID L12345 based on usage patterns and billing details. This will help you determine if a more cost-effective or feature-rich plan is available, ensuring that the line's needs are met efficiently.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC013"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"line_id": "L12345", "user_id": "TC013"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Based on the current plan and usage details, consider if a more cost-effective or feature-rich plan is available for line ID L12345."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are optimistic, cautious, logical. lookup_customer_by_phone with phone_number: \"555-1234\" to verify Robert Johnson's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are flexible, polite. lookup_customer_by_phone with phone_number \"555-1234\" to verify identity of Mary Miller",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are cautious, optimistic. Verify the identity of John Williams using his email john.williams4633@email.com and check for the associated account. Once his identity is confirmed, retrieve John's phone number using lookup_customer_by_phone with his verified email. This process is essential to ensure we have the correct contact information for John before proceeding with any account modifications or service updates.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.williams4633@email.com", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are confident, direct, cautious, patient. First, lookup_customer_by_phone with phone number '555-1234' to retrieve customer ID for Robert Garcia. Once you have obtained the customer ID, proceed to get_customer_lines for customer ID 'C123' to list all active and suspended lines. This will allow you to review Robert Garcia's account status and provide him with accurate information regarding his service lines, ensuring a seamless customer support experience.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC003"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC003", "user_id": "TC003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are flexible, organized, confident. Lookup customer by phone using phone number 555-123-4567 to verify Jennifer Johnson's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are direct, logical. Suspend_line with line ID L12345 for a temporary suspension request.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC069", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are independent, confident. First, use lookup_customer_by_phone with phone number (555-123-4567) to verify Patricia Brown's account identity. Once her identity is confirmed, retrieve account details for Patricia Brown using get_customer_lines with the customer ID obtained from the previous step. This will help ensure that Patricia's account information is accurate and up-to-date, allowing for better customer service and support in managing her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC094"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC094", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are cautious, polite. First, get bill details for account ID A5678 to review the outstanding balance and billing history. Once you have this information, calculate the total amount due for account ID A5678, including any late fees or charges. This will help you understand the full financial obligation before proceeding with any further actions.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A5678", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are confident, polite, cautious. Verify the identity of user Robert Brown using the email robert.brown5816@email.com to ensure secure account access. Once verified, lookup the customer by the phone number associated with Robert Brown to retrieve the account ID necessary for further actions. Finally, get the bill details for the account ID retrieved from Robert Brown to check his current charges and provide him with an accurate update on his telecom billing status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown5816@email.com", "user_id": "TC120"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are confident, flexible. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Robert Williams' account. Once verified, get_customer_lines for customer ID C1023 to list all active lines associated with the account. After identifying the relevant line, proceed to suspend_line for line ID L9876 with reason \"customer request\" to pause service temporarily, ensuring that Robert Williams' request is handled promptly and efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC067"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "reason": "customer request", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are cautious, polite, patient. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify customer identity for Michael Garcia. Once the identity is confirmed, proceed to get_bill_details for customer_id \"CUST12345\" to check outstanding balance and payment history. This will help determine if there are any overdue payments that need to be addressed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC051"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC051", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are polite, cautious, patient, direct. First, lookup_customer_by_phone with phone_number '555-1234' to verify the identity of Michael Johnson. Once his identity is confirmed, get_bill_details for the customer_id retrieved from the first step to review recent charges and payments. This will help us ensure that all billing information is accurate and up-to-date, and it will provide insight into Michael Johnson's current usage and payment history.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC133"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC133", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are optimistic, patient, logical, polite. Suspend line L67890 temporarily upon request from Mary Jones for vacation purposes.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC147"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC147"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC147", "line_id": "L67890"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC147", "line_id": "L67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are logical, organized, independent, direct. Resume suspended line L67890 for customer ID C12345 within the 30-day window as the customer has requested service restoration. After resuming the line, get line details for line ID L67890 to confirm that the service has been successfully restored and is fully operational.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC041", "user_id": "TC041"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "action": "resume", "user_id": "TC041"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are cautious, optimistic, direct, polite. First, verify the customer identity using the email mary.davis8842@email.com before accessing any account details to ensure security and privacy. Once the identity is confirmed, lookup the customer by the phone number associated with mary.davis8842@email.com to retrieve the customer ID. Finally, with the customer ID in hand, get the bill details to review the current charges and payment status, ensuring that the customer is informed about their financial obligations and any necessary actions they may need to take.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.davis8842@email.com", "user_id": "TC020"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC020", "user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are independent, logical. First, lookup_customer_by_phone with phone number 555-1234 to verify customer identity for Robert Williams. Once verified, proceed to get_line_details for line ID L5623 to check the current plan and usage, ensuring you have all necessary information about the service. Finally, if Robert Williams requests, suspend_line for line ID L5623 with reason \"customer request\" to temporarily suspend service, ensuring all actions are documented for clarity and future reference.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC080"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5623", "user_id": "TC080"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5623", "reason": "customer request", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC024",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are organized, flexible, polite, independent. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Jennifer Davis's identity. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"CUST12345\" to list all active lines associated with Jennifer Davis. This will help ensure that we have an accurate overview of her account for any service updates or troubleshooting needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC024"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC024", "user_id": "TC024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are flexible, patient. First, get bill details for Robert Brown's account to check the outstanding balance, as there has been a notice of overdue payment. Once you have confirmed the outstanding amount, suspend the line with the line ID from Robert Brown's primary line for non-payment, ensuring that he is aware of the suspension due to the unpaid balance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC029"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC029"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC029", "line_id": "primary_line_id", "reason": "Non-payment of outstanding balance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is John Garcia and your email is john.garcia3458@email.com. You are independent, optimistic. Suspend line L001 temporarily for Linda Miller.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC091"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC091", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are optimistic, direct, independent. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify the identity of John Johnson. Once verified, proceed to get_bill_details for account_id \"ACC12345\" to review the current billing status and recent payments. This will ensure you have the most up-to-date information before discussing any billing concerns with the customer.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "ACC12345", "user_id": "TC001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are independent, flexible, patient. Think about the best plan upgrade options for Mary Jones based on her current usage patterns, then transfer_to_human_agents to discuss potential plan changes with Mary Jones after providing available options. As a customer service representative at a telecom company, your goal is to ensure that Mary receives a plan that best suits her needs. First, analyze her data usage, call frequency, and any additional services she frequently uses to determine the most suitable plan upgrades. Once you have identified the best options, connect Mary to a human agent who can further discuss these options with her, ensuring she understands the benefits and any changes in her billing. This approach will help Mary make an informed decision about her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC147"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC147"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC147"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC147"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are organized, logical, direct, cautious. First, use the Lookup_customer_by_phone task with the customer phone number 555-1234 to retrieve Robert Garcia's account information. Once you have the account information, proceed to Retrieve get_customer_lines for Robert Garcia's account to list all active phone lines. This sequence will help you verify the customer's current services and ensure all lines are accounted for before making any further service changes or updates.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC046"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_from_previous_step", "user_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are cautious, logical, patient. Suspend_line L12345 temporarily for Jennifer Williams due to user request",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "user_id": "TC131", "reason": "User request by Jennifer Williams"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are organized, optimistic. suspend_line for line ID L12345 due to customer request for temporary hold",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "Customer request for temporary hold", "user_id": "TC060"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are cautious, direct, independent, patient. check if line ID associated with Linda Smith is currently suspended",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC146", "phone": "Linda Smith"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC146"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC146", "line_id": "line_id_associated_with_Linda_Smith"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are organized, logical, polite, optimistic. First, verify customer identity for Patricia Miller using email patricia.miller3252@email.com before accessing account details. Once her identity is confirmed, proceed to get bill details for Patricia Miller's account to review the latest charges and payment status. This process ensures that we maintain customer privacy and provide accurate billing information. If Patricia Miller expresses any concerns or requests to dispute any charges on the bill, be prepared to transfer her to a human agent for further assistance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.miller3252@email.com", "user_id": "TC028"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "patricia.miller3252@email.com", "user_id": "TC028"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are patient, flexible, polite, direct. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of Robert Johnson. Once verified, proceed to get_bill_details for billing account B1234 to review his current charges and due dates. This will help you understand any billing discrepancies he might be experiencing and provide accurate information before transferring him to a human agent if further assistance is needed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC072"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"billing_account_id": "B1234", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are patient, independent. First, lookup_customer_by_phone with phone number \"555-1234\" to verify identity for account access. Once the customer's identity is confirmed, get_bill_details for the customer ID retrieved earlier to review current charges and due date. This will help ensure the customer is informed about their billing status and any upcoming payments.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC148"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC148", "user_id": "TC148"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are independent, organized. Retrieve details for line L12345 under Linda Davis's account to check current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC150", "customer_name": "Linda Davis"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC150", "customer_name": "Linda Davis"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC150", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are optimistic, direct, independent. First, lookup customer by phone number 555-0123 to verify identity and access account details for Jennifer Jones. Once Jennifer's account is verified, proceed to get customer lines for her using the verified account information to ensure all active lines are accounted for in our system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are independent, cautious, confident, polite. Suspend line L12345 for Robert Garcia due to a reported issue, ensuring it can be resumed within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC003", "phone_number": "L12345"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC003", "customer_id": "TC003"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC003", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC003", "line_id": "L12345", "suspend_reason": "Reported issue", "suspend_duration_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are independent, cautious. First, perform a lookup_customer_by_phone using Robert Brown's registered phone number to verify his identity before proceeding with any account access. Once his identity is confirmed, get_customer_lines for the user ID associated with Robert Brown to list all active lines under his account. This will help ensure that any changes or reviews are done on the correct and authorized lines, providing a seamless and secure customer service experience in the telecom sector.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's registered phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are direct, logical, optimistic, patient. First, lookup_customer_by_phone with phone_number '555-1234' to verify the identity of Robert Jones, ensuring you have the correct customer before proceeding. Once verified, get_bill_details for customer_id 'C6549' to review the latest bill and payment status, providing Robert with accurate and up-to-date information about his account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC119"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC119", "user_id": "TC119"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC139",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are patient, direct, logical. First, lookup customer by phone number 555-123-4567 to retrieve account details. Once you have the account details, get customer lines for user ID U123 to list all active lines associated with the account. After identifying the active lines, get line details for line ID L456 to check the current plan and usage. This will help determine if the customer is on the appropriate plan based on their usage patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC139"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "U123"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC139"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are direct, independent, optimistic. First, use the Lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify Linda Davis's identity. Once verified, proceed with Get_customer_lines for customer_id=\"CUST12345\" to retrieve active lines associated with Linda Davis. After confirming the correct line, use Suspend_line for line_id=\"LINE67890\" due to Linda Davis's request for a temporary hold on her service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC150"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE67890", "user_id": "TC150"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are direct, flexible, polite. First, verify customer identity for user Robert Brown using email robert.brown5816@email.com to ensure secure account access. Once identity verification is complete, proceed to resume the previously suspended line with line ID L1024 for Robert Brown, as he has requested reactivation within the 30-day period. Finally, get line details for line ID L1024 to confirm that the resumption was successful and check for any remaining issues to ensure seamless service continuation.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown5816@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1024"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1024", "action": "resume"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are organized, cautious. First, use the Lookup_customer_by_phone with phone number 555-123-4567 to verify John Miller's identity. Once verified, proceed to Get_bill_details for the account associated with John Miller to review recent charges. Finally, Calculate total outstanding amount from the get_bill_details response to ensure accuracy before any further actions are taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC104"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC104"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "sum(recent_charges)"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are patient, polite, optimistic, cautious. First, lookup_customer_by_phone with phone_number='123-456-7890' to verify customer identity for Jennifer Brown. Once verified, get_customer_lines for customer_id='C3820' to retrieve all active lines on the account. Then, for the specific line with line_id='L5678', get_line_details to check current data usage and plan details. If the current usage exceeds the plan limit, calculate data_overage_fee with current_usage=5GB and plan_limit=3GB to determine additional charges for line L5678.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC026"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678"}
            ),
            Action(
                name="calculate",
                kwargs={"current_usage": "5GB", "plan_limit": "3GB"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are organized, polite. First, lookup customer by phone using the phone number associated with James Brown's account to verify his identity. Once his identity is verified, proceed to get customer lines for James Brown. After obtaining the customer lines, get line details for each active line under James Brown's account to ensure accurate information is available for further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "James Brown's phone number", "user_id": "TC089"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC089", "user_id": "TC089"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Active Line 1 ID", "user_id": "TC089"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Active Line 2 ID", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are cautious, optimistic. Retrieve details for line L001 to check current plan and usage.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC023"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC023", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are polite, flexible. Suspend line L12345 temporarily for Robert Jones due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are independent, flexible. First, get_bill_details for the account to review the latest bill and outstanding balance. Once you have this information, transfer_to_human_agents with context to discuss possible payment plan options for the outstanding balance. This sequence ensures you have all necessary details to have an informed conversation with the telecom representative about managing your account effectively.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC120"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC120", "context": "Discuss possible payment plan options for the outstanding balance."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are organized, flexible. Verify customer identity using email michael.jones4016@email.com before proceeding with account access. Once verified, lookup_customer_by_phone with the phone number associated with Michael Jones to retrieve the customer ID. Then, use this customer ID to get_customer_lines and identify active lines on the account. This sequence ensures secure access and allows you to assist Michael Jones effectively by understanding his current telecom services and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.jones4016@email.com", "user_id": "TC042"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC042", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are independent, optimistic, confident, cautious. First, verify the identity of user Linda Smith using her email linda.smith7771@email.com to ensure the security of her account. Once her identity is confirmed, lookup Linda Smith's account by the phone number associated with her email to access her account details. Finally, retrieve details for the main line under Linda Smith's account to review her current telecom services and ensure everything is functioning correctly.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, verify Linda Smith's identity using her email to ensure account security."}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.smith7771@email.com", "user_id": "TC146"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "associated_phone_number_from_previous_step", "user_id": "TC146"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "main_line_id_from_previous_step", "user_id": "TC146"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are flexible, cautious. First, verify the identity of user Linda Davis using the email linda.davis3121@email.com to ensure you are accessing the correct account. Once verified, proceed to lookup the customer by phone number associated with Linda Davis's account to retrieve her customer ID. With the customer ID in hand, get the bill details to retrieve the latest bill and outstanding balance, ensuring Linda Davis has all the necessary information regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis3121@email.com", "user_id": "TC035"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC035", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are organized, flexible, patient. lookup_customer_by_phone with phone_number \"555-1234\" to verify identity for Jennifer Jones",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are polite, cautious, optimistic. lookup_customer_by_phone(phone_number=\"555-123-4567\")",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are cautious, direct, logical, patient. lookup_customer_by_phone with parameters: phone_number='123-456-7890' to verify Mary Miller's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are optimistic, direct, polite, logical. lookup_customer_by_phone with phone_number \"555-1234\" to verify customer identity for Patricia Smith",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are logical, cautious. lookup_customer_by_phone with phone number 123-456-7890 to verify account access for user Jennifer Williams",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are polite, organized. get_bill_details for user_id=LindaDavis4055 to review outstanding balance and due date.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "LindaDavis4055"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are patient, cautious, confident, organized. lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity for Jennifer Williams before plan change",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are optimistic, logical, independent, confident. First, lookup customer by phone number 555-0123 to retrieve the account ID and associated lines. Then, using the account ID A123, get the bill details to verify the outstanding balance and due date. This will help ensure that the customer is informed about their current billing status and any actions needed to maintain their service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC026"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "A123", "user_id": "TC026"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A123", "user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are logical, confident, organized, patient. First, lookup customer by phone number (555-123-4567) to verify Linda Davis' identity for account access. Once Linda's identity is verified, proceed to get customer lines using the customer ID retrieved from the previous lookup to identify all active lines associated with her account. After identifying the active lines, focus on line ID L102 to get line details, including the current plan and usage, as Linda has requested a temporary suspension of this line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC035"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC035", "user_id": "TC035"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L102", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are optimistic, confident. First, perform a lookup_customer_by_phone with phone_number \"555-0123\" to verify Linda Davis's identity, ensuring you have the correct customer details. Once verified, proceed to get_customer_lines for customer_id \"C3121\" to view all active lines on Linda Davis's account, ensuring you have a comprehensive understanding of her current services. Finally, get_line_details for line_id \"L789\" to check usage and plan details for Linda Davis's primary line, which will help you assess any irregularities and confirm if there is a need to suspend the line due to unauthorized activity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC035"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are optimistic, independent. First, lookup_customer_by_phone with phone number 555-0123 to verify Linda Davis's account. Once verified, proceed to get_customer_lines for customer ID 4055 to retrieve active lines. Finally, use get_line_details for line ID 78901 to check the current plan and usage, and calculate estimated charges for adding a 5GB data refill to this line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC048"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC048", "user_id": "TC048"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "78901", "user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are independent, optimistic, polite. Use the lookup_customer_by_phone tool with the parameter: phone='555-123-4567' to retrieve John Johnson's customer ID. Once you have the customer ID, proceed to get_customer_lines using the retrieved customer ID to list all active lines for John Johnson. After listing the active lines, get_line_details for line ID 'L2345' to check the current plan and data usage. This sequence of actions will help you provide John Johnson with detailed information about his current telecom services, enabling you to assist him effectively with any inquiries or changes he may wish to make.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L2345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are direct, logical, patient, confident. Suspend line L123456 for account ID A987654 due to a customer request received this morning, ensuring that the suspension is processed correctly. Once you have completed the suspension, verify the suspended status of line L123456 to confirm that the suspension was successful, as this is crucial for maintaining accurate service records and customer satisfaction in our telecom operations.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123456", "account_id": "A987654", "user_id": "TC129"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123456", "user_id": "TC129"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are cautious, organized. First, lookup customer by phone number using Michael Jones's phone number to verify identity. Once identity verification is successful, proceed to get customer lines for Michael Jones to ensure his account details are up-to-date and accurate in our telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Jones's phone number", "user_id": "TC083"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC083", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are cautious, confident, optimistic. lookup_customer_by_phone with parameters: phone_number = \"555-1234\", user_email = \"linda.smith7027@email.com\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_email": "linda.smith7027@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are optimistic, patient. Get_bill_details for customer ID to view current billing amount and due date",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC101",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are direct, independent. First, lookup_customer_by_phone with phone number 555-123-4567 to verify customer identity as part of a security check. Once the customer's identity is confirmed, proceed to get_customer_lines for customer ID C12345 to list all active lines associated with the account. After identifying the specific line in question, get_line_details for line ID L98765 to verify current plan and usage details, ensuring that the line matches the customer's report. If everything aligns and the customer confirms a loss of their device, suspend_line for line ID L98765 due to reported loss of device to prevent unauthorized usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC101"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L98765"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L98765", "reason": "reported loss of device", "user_id": "TC101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are organized, independent, optimistic. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity for Linda Garcia. Once her identity is confirmed, get_bill_details for the account associated with linda.garcia2678@email.com to review outstanding charges. After reviewing the outstanding charges, think to determine the next steps to assist Linda Garcia effectively with her billing concerns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC141"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "linda.garcia2678@email.com", "user_id": "TC141"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review the outstanding charges and determine if Linda Garcia needs further assistance or if the issue can be resolved by providing information about the charges."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are independent, patient, cautious. First, lookup_customer_by_phone with phone_number \"+1234567890\" to verify the identity of James Jones. Once verified, proceed to get_customer_lines for customer_id \"C001\" to retrieve all active lines associated with James Jones, ensuring you have a comprehensive view of his account. After obtaining the list of active lines, focus on get_line_details for line_id \"L002\" to check data usage and plan details. This will allow you to think critically and decide if the current plan meets James Jones' usage requirements based on the retrieved details, ensuring he has the most suitable plan for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC106"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC139",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are organized, flexible, independent. First, verify Michael Smith’s account using the email michael.smith4429@email.com to access customer details. Once you have confirmed his account, proceed to calculate the total amount due for Michael Smith’s account using recent billing cycle data. This will ensure that all charges and payments are accurately reflected for the current billing period, which is crucial for maintaining accurate customer billing records in our telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"email": "michael.smith4429@email.com", "user_id": "TC139"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are logical, polite, flexible. First, verify the identity of user Linda Davis using her email linda.davis3121@email.com to ensure secure access to her account. Once her identity is confirmed, retrieve details for line L9876 to check her current plan and usage. After reviewing the plan details, confirm with Linda Davis if she desires to change her plan for line L9876, reminding her that any changes will take effect from the next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis3121@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC035", "line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are patient, logical, confident. Verify customer identity using email michael.jones2722@email.com to access account details. Once verified, get_customer_lines for Michael Jones to list all active lines under the account. Then, get_line_details for the primary line on Michael Jones' account to check current plan and usage. This will help you understand his current usage patterns and enable you to think about the best plan upgrade options for Michael Jones, ensuring he has the most suitable telecom plan for his needs.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"email": "michael.jones2722@email.com", "user_id": "TC083"}
            ),
            Action(
                name="get_line_details",
                kwargs={"email": "michael.jones2722@email.com", "line_id": "primary", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are direct, optimistic. First, lookup_customer_by_phone with phone number '555-1234' to verify the identity of Michael Jones. Once verified, proceed to get_line_details for line ID 'L5678' to review his current plan and usage, ensuring all information is accurate and up-to-date for a comprehensive assessment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC042"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are confident, optimistic, logical. Get_line_details for the primary line on Robert Williams' account to review current plan. Think about the best plan options for Robert Williams based on his usage patterns. Analyze the data to ensure the plan aligns with his needs and offers the best value.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Williams' phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC067"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary_line_id"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are organized, direct, cautious. Verify the identity of user Jennifer Jones using the email jennifer.jones9861@email.com before accessing her account details. Once her identity is confirmed, proceed to get_customer_lines for Jennifer Jones to list all active lines under her account. This will ensure that only authorized personnel can access sensitive information and provide accurate assistance regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.jones9861@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are optimistic, cautious. Lookup_customer_by_phone with phone number 555-1234 to verify identity and retrieve customer account ID.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are flexible, organized, polite. lookup_customer_by_phone with phone number 555-1234 to verify customer identity for Michael Miller",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC024",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are flexible, patient, direct. Verify customer identity using email jennifer.davis7195@email.com for account access. Once verified, get_bill_details for the customer ID to retrieve current billing information and any outstanding payments. After obtaining the billing details, calculate total amount due using current billing information and any additional charges. This process ensures that you provide accurate and up-to-date billing information to the customer, facilitating a seamless experience in the telecom service context.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC024", "email": "jennifer.davis7195@email.com"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["current_billing_amount", "additional_charges"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are cautious, optimistic. First, lookup_customer_by_phone with phone number 555-1234 to verify Mary Johnson's account access. Once her access is confirmed, proceed to get_line_details for line ID L456 to check her current plan and usage details. This will ensure that any subsequent actions, such as plan adjustments or suspensions, are informed by her current service status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC093"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC101",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are flexible, cautious. First, perform a lookup_customer_by_phone with phone_number set to \"123-456-7890\" to verify James Johnson's account. Once verified, proceed to get_customer_lines for customer_id \"C12345\" to retrieve all active lines for James Johnson. This will help ensure that all lines are active and associated with the correct account, providing a comprehensive overview of the customer's current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC101"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC101", "user_id": "TC101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC135",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are confident, direct. First, check the current billing status by using get_bill_details with the customer ID to retrieve the latest billing information. Then, calculate potential charges for a plan upgrade by using calculate with the current plan details and desired new plan parameters, ensuring the customer is aware of any changes in their billing cycle.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC135"}
            ),
            Action(
                name="calculate",
                kwargs={"current_plan": "basic", "new_plan": "premium", "user_id": "TC135"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are logical, direct, patient, polite. Please lookup the customer by phone number 555-123-4567 to verify account access for James Brown. Once you have confirmed access, proceed to get customer lines for the account associated with James Brown to review active services. This will help ensure that all services are correctly aligned with his current needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC145"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC145"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC139",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are cautious, optimistic, independent, organized. First, lookup_customer_by_phone with the customer phone number 555-1234 to verify identity and retrieve account details for Michael Smith. Once you have obtained the customer ID, use it to get_customer_lines to list all active lines on Michael Smith's account. Finally, with the line ID L001, get_line_details to check the current plan and data usage, and then calculate the estimated data overage charges for line L001 based on these details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC139"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC139", "user_id": "TC139"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC139"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "(current_data_usage - plan_data_limit) * overage_rate"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are flexible, organized, confident. lookup_customer_by_phone with phone_number \"+1234567890\" to verify identity of Jennifer Davis",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are patient, optimistic. Suspend line L12345 for John Brown using the line ID and confirm suspension status.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC124"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC124", "line_id": "L12345"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC124", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are logical, patient, flexible. Get_customer_lines for Robert Brown to list all active lines on the account.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Robert Brown", "user_id": "TC129"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are patient, confident, optimistic, independent. First, lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify identity for Linda Davis. Once her identity is confirmed, proceed to suspend_line for line_id=\"L5678\" with reason=\"customer request\" and note=\"temporary suspension for 2 weeks.\" This sequence ensures that Linda Davis's request is securely processed, maintaining the integrity of her service management.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "reason": "customer request", "note": "temporary suspension for 2 weeks", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are optimistic, organized, logical, patient. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of Jennifer Davis, ensuring you are addressing the correct customer. Once her identity is confirmed, proceed to get_customer_lines with customer_id \"C4933\" to retrieve all active lines associated with her account, as this will give you a comprehensive view of her services. After identifying her active lines, focus on get_line_details with line_id \"L12345\" to check the current plan and usage, which will help you understand if her current plan meets her needs or if adjustments are necessary.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC148"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are patient, logical, organized, flexible. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify Robert Jones's account. Once verified, proceed to get_line_details for line_id \"L789\" to check current plan and usage. After reviewing the plan and usage, calculate data usage for line_id \"L789\" to determine if a data refill is needed. If the data usage indicates a potential need for a refill, prepare to advise Robert on his options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "data_usage_for_L789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are flexible, optimistic, patient. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of Jennifer Brown. Once verified, get_customer_lines for account associated with customer ID C1234 to review the lines she has. Then, get_line_details for line ID L5678 to check current plan and usage details, ensuring that her current plan meets her needs and identifying any potential for a plan upgrade.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC062"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC062", "user_id": "TC062"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are cautious, confident, patient, logical. First, lookup customer by phone number 555-123-4567 to verify account identity for Robert Garcia. Once his identity is confirmed, suspend line for line ID L5678 to temporarily pause service at his request, ensuring that the service can be resumed within the 30-day suspension period if needed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC003"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "user_id": "TC003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are logical, organized, independent, cautious. First, lookup customer by phone number 555-0123 to access account details for John Garcia. Once you have accessed the account, get bill details for the account associated with phone number 555-0123 to provide John Garcia with outstanding balance information. If the outstanding balance is not cleared, proceed to suspend the line with line ID L789 due to non-payment, ensuring John Garcia is informed of the 30-day resumption policy.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC015"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"phone_number": "555-0123", "user_id": "TC015"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L789", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are independent, organized. First, lookup customer by phone number 555-1234 to retrieve account details. Then, get bill details for the account associated with phone number 555-1234 to review payment history. This will help us understand the customer's payment patterns and identify any discrepancies in their billing cycle, ensuring accurate and timely resolutions in our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC093"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"phone_number": "555-1234", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are cautious, independent, patient, direct. First, lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify identity for account access. Once verified, proceed to get_customer_lines with customer_id=\"C001\" to retrieve all active lines on the account. After identifying the relevant line, use get_line_details with line_id=\"L123\" to check the current plan and usage details for line L123, ensuring that the service plan aligns with the customer's needs and any potential issues are addressed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC108"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are polite, organized, patient, cautious. \"get_line_details for line ID L001 from Robert Garcia's account to check current plan and usage\"",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC046"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are flexible, confident. lookup_customer_by_phone(phone_number=\"555-123-4567\") to verify Linda Davis's account identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are independent, logical, patient. First, lookup customer by phone number 555-123-4567 to retrieve account ID for Patricia Brown. Once you have the account ID, get customer lines for this account to list all active lines. This will help ensure Patricia has access to all her current telecom services and can manage them effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC094"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC101",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are patient, optimistic, cautious. First, perform a lookup_customer_by_phone with phone_number \"555-0123\" to verify the identity of James Johnson. Once verified, proceed to get_line_details for line_id \"L1234\" to check the current data usage and plan details. This will help determine if James Johnson needs a data refill based on his current usage and plan limits.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC101"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234", "user_id": "TC101"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are optimistic, patient, polite. Please lookup_customer_by_phone for user Linda Davis using the phone number associated with her email linda.davis5049@email.com. Once you have retrieved the customer ID from Linda Davis's account, proceed to get_customer_lines for that customer ID. This will help us ensure that we have the most accurate and up-to-date information on her active lines, which is essential for providing her with the best possible service and support in our telecom operations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis5049@email.com", "user_id": "TC107"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are patient, cautious, confident, independent. lookup_customer_by_phone(phone_number='555-1234')",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are cautious, logical. First, lookup the customer account by phone number using Linda Garcia's phone number for identity verification to ensure you are accessing the correct account. Once the account is verified, get all customer lines for Linda Garcia's account to identify active services and determine which lines are currently in use. Finally, retrieve line details for Linda Garcia's primary line to check the current plan and usage, ensuring that the services align with her needs and to address any potential discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Garcia's phone number", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC141"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary_line_id", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are direct, polite. Please get the customer lines for the account associated with phone number 555-0123 to list active lines. Once you have identified the active lines, proceed to get the line details for line ID L456 to check the current plan and usage. This will help us ensure that the line is correctly documented before any further action is taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC108"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "555-0123", "user_id": "TC108"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC108"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are polite, direct, logical. lookup_customer_by_phone with parameter phone_number as \"555-123-4567\" to verify Mary Brown's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are direct, optimistic, independent, polite. Suspend line L12345 for customer John Smith temporarily",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC016", "phone_number": "John Smith"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC016", "customer_id": "TC016"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC016", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC016", "line_id": "L12345", "suspend_type": "temporary"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are polite, patient. First, lookup_customer_by_phone with phone_number '123-456-7890' to verify the identity of user James Brown. Once verified, proceed to get_customer_lines for customer_id 'CUST123' to retrieve all active lines associated with James Brown. After listing the active lines, if James Brown inquires about his data usage or plan details, use get_line_details for line_id 'LINE456' to provide him with the necessary information regarding his active line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC145"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are confident, optimistic. Get line details for the primary line on Linda Garcia's account to check current plan and usage. Then, think about a suitable plan upgrade for Linda Garcia's primary line based on current usage trends. This will ensure that her plan aligns with her data and call needs, providing her with better value and preventing overage charges.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC127", "phone_number": "primary"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC127", "customer_id": "TC127"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC127", "line_id": "primary"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Based on Linda Garcia's current usage trends, consider a plan upgrade that offers more data and call minutes to prevent overage charges and provide better value."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are flexible, optimistic, cautious. First, lookup_customer_by_phone with phone_number '555-0199' to verify identity for user Jennifer Brown. Once verified, proceed to get_customer_lines for user_id 'jennifer.brown3820@email.com' to list all active lines associated with her account. After identifying the relevant line, get_line_details for line_id 'L123456' to check the current plan and usage, ensuring that everything aligns with the customer's expectations and there are no discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0199"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "jennifer.brown3820@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are confident, patient. First, use Lookup_customer_by_phone with phone number 555-123-4567 to retrieve customer details for John Williams. Once you have confirmed the customer identity, proceed with Get_customer_lines for customer ID C123456 to list all active lines associated with John Williams. After identifying the relevant line, use Suspend_line for line ID L789012 to temporarily halt service as per the customer's request due to an upcoming extended travel period.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC031"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC031", "user_id": "TC031"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L789012", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are organized, patient, logical. First, perform a Lookup_customer_by_phone to find Robert Johnson's account details using his registered phone number. Once you have his account information, proceed to Get_customer_lines for Robert Johnson to retrieve a list of active lines on his account. Finally, use the Get_bill_details for Robert Johnson to review his outstanding balance and past payment history, ensuring you have a comprehensive understanding of his current financial obligations with the telecom company.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Johnson's registered phone number", "user_id": "TC072"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC072", "user_id": "TC072"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC072", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are cautious, direct. Retrieve the current billing details for Linda Davis's account to check the outstanding balance, and then calculate the total amount due for Linda Davis's account, including any late fees. This process is crucial to ensure accurate billing and timely payment processing for our telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are patient, independent, confident. First, perform a Lookup_customer_by_phone with phone number 123-456-7890 to retrieve customer account details for Jennifer Davis. Once you have her account details, proceed to Get_customer_lines for the user ID associated with Jennifer Davis to view all active lines on her account. This will help you understand her current service setup and assist in any inquiries she may have about her account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC148"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are polite, patient, cautious, optimistic. use lookup_customer_by_phone with phone_number '555-0123' to verify Patricia Miller's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are direct, patient, confident, logical. Get_customer_lines for Linda Davis using her customer ID to list all active lines on her account.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are optimistic, polite, confident, organized. First, lookup the customer by phone number using the phone number associated with Robert Williams to verify his identity. After successful identity verification, proceed to get the customer lines for Robert Williams. This process is crucial to ensure we have accurate and up-to-date information on the active lines under his account, which will help us provide better service and support in managing his telecom needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Williams' phone number", "user_id": "TC006"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC006", "user_id": "TC006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are independent, patient. First, lookup_customer_by_phone with phone number 555-1234 to verify identity for Robert Jones. Once identity is confirmed, proceed to get_bill_details for customer ID C6549 to review the current billing status, ensuring all charges are accurate and up-to-date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC119"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC119", "user_id": "TC119"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are flexible, logical, independent. Suspend_line for line ID L12345 with reason \"customer request\" after confirming with Jennifer.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "customer request", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are confident, cautious. Suspend_line for line ID L789 on Jennifer Brown's account due to non-payment",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC062", "phone_number": "not_provided"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC062", "customer_id": "TC062"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC062", "line_id": "L789"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC062", "customer_id": "TC062"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC062", "line_id": "L789", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are flexible, independent. First, verify customer identity for John Garcia using email john.garcia4063@email.com before accessing account details. Once the identity is confirmed, proceed to get the customer lines for John Garcia's account to list all active lines associated with the customer ID. This process ensures that only authorized personnel can view and manage the telecom services linked to the customer's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia4063@email.com", "user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC018", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are confident, cautious, organized, polite. lookup_customer_by_phone with phone number 123-456-7890 to verify identity of John Smith",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are patient, optimistic, flexible, organized. First, lookup customer by phone number to verify account identity for Jennifer Smith using phone number 555-1234. Once her identity is verified, proceed to get customer lines for the account associated with Jennifer Smith. After retrieving the lines, get line details for line ID L9876 on Jennifer Smith's account to check the current plan and usage. This sequence of actions will ensure that you have all necessary information to assist Jennifer Smith effectively in discussing potential plan changes and addressing any billing inquiries she may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC023"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC023"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are direct, confident. Get line details for all active lines under Patricia Smith's account to determine data usage",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC112", "phone_number": "Patricia Smith's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC112", "customer_id": "TC112"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC112", "line_id": "line_id_from_previous_step"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are logical, flexible, optimistic. \"Lookup customer by phone number 555-1234 to verify identity of Linda Garcia for account access\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are patient, independent, flexible, organized. First, lookup_customer_by_phone with phone number 555-0123 to verify customer identity. Once the customer's identity is confirmed, proceed to get_bill_details for customer ID 12345 to review their outstanding balance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC136"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC136", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are confident, organized. lookup_customer_by_phone(customer_email=\"john.garcia4063@email.com\", phone_number=\"555-123-4567\")",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"customer_email": "john.garcia4063@email.com", "phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are optimistic, polite, confident. First, lookup_customer_by_phone with phone number 555-123-4567 to verify the identity of Robert Williams. Once his identity is confirmed, proceed to get_customer_lines for customer ID C789 to gather information on all active lines under his account. After obtaining the list of lines, focus on get_line_details for line ID L456 to check the current plan and usage. This will allow you to think and assess if the current data usage is likely to exceed the plan limits for line ID L456, ensuring Robert Williams is informed and can avoid any potential overage charges.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC006"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC006", "user_id": "TC006"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are direct, cautious. First, lookup_customer_by_phone with phone number 555-1234 to verify identity for user Michael Garcia, ensuring you are addressing the correct account. Next, get_bill_details for user ID 5750 to verify outstanding balance, as this will determine the next steps regarding service status. If an outstanding balance is confirmed and the line has been suspended, proceed to suspend_line for line ID L9876 due to non-payment issue. However, if the customer resolves the payment within the 30-day suspension period, resume_line for line ID L9876 to restore service promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC039"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "5750"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are flexible, organized, cautious, direct. First, perform a lookup for the customer by phone number associated with Jennifer Jones to retrieve the customer ID. Once you have the customer ID, proceed to get all active lines associated with this customer to identify any potential issues. After identifying the active lines, suspend the line with ID L12345 due to a reported lost device, ensuring that the customer is informed about the 30-day resumption policy.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_with_Jennifer_Jones", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC082", "user_id": "TC082"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "Lost device", "notification": "Customer informed about 30-day resumption policy", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are confident, cautious, organized. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Linda Miller's identity. Once her identity is confirmed, proceed to suspend_line for line_id \"L001\" due to her request for temporary suspension. After suspending the line, think about the impact of suspension on the upcoming billing cycle and inform Linda about any changes to her billing to ensure she is fully aware of how this action affects her account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "user_id": "TC019"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Suspending the line may affect Linda's upcoming billing cycle. I should inform her about any changes to her billing due to the suspension."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are direct, cautious. First, use the lookup_customer_by_phone task with phone_number \"555-123-4567\" to verify the customer's identity for account access. Once verified, proceed with the get_customer_lines task for customer_id \"C001\" to list all active lines associated with the account, ensuring that the customer can review their current telecom services accurately.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC026"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC026", "user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are polite, independent, flexible, cautious. First, verify customer identity using email john.smith6987@email.com to access account details. Once verified, get bill details for John Smith's account to identify any outstanding payments. If any issues arise or further assistance is required to process a payment or resolve billing issues, transfer to human agents for support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.smith6987@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC081"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are direct, confident. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Michael Johnson's account. Once verified, proceed to get_customer_lines for customer_id \"CUST-4265\" to retrieve all active lines associated with his account. After obtaining the list of active lines, focus on get_line_details for line_id \"LINE-7890\" to check the current plan and usage. Finally, think to evaluate if the current plan meets Michael Johnson's usage needs and suggest alternatives if necessary.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC134"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE-7890"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Evaluate if the current plan meets Michael Johnson's usage needs and suggest alternatives if necessary."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are organized, patient. Verify the identity of User Michael Williams using email michael.williams1902@email.com. After confirming his identity, lookup the customer using the phone number associated with Michael Williams. Once you have verified his details, proceed to suspend line L001 for temporary disconnection due to Michael's request, ensuring it can be resumed within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.williams1902@email.com", "user_id": "TC007"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "Temporary disconnection requested by customer", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC061",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are confident, patient. First, verify customer identity using Patricia Davis's email (patricia.davis1886@email.com) to ensure secure access to her account. Once her identity is confirmed, get bill details for Patricia Davis's account to identify any outstanding balance and the payment due date, as part of our routine telecom account management process.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.davis1886@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC061"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are polite, confident. Please verify Linda Davis's identity using her email linda.davis8880@email.com to access account details. Once her identity is confirmed, proceed to lookup the customer by phone number 555-0123 to retrieve the customer ID for Linda Davis. This process is essential to ensure that we have accurate and secure access to her account information, which is crucial for maintaining the integrity of our telecom services.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC150", "message": "Please verify Linda Davis's identity using her email linda.davis8880@email.com to access account details."}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC150", "phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are cautious, polite. Use lookup_customer_by_phone with phone number \"555-123-4567\" to verify the identity of Robert Williams.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are patient, confident, cautious. First, verify customer identity for account access using email robert.brown2463@email.com to ensure security protocols are met. Once identity is confirmed, lookup customer by phone number to retrieve the customer ID for Robert Brown, which is essential for accessing his account details. Finally, use the customer ID to get bill details for Robert Brown to understand his recent charges and address any billing inquiries he may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown2463@email.com", "user_id": "TC029"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC029", "user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are confident, patient, logical. Suspend line L002 temporarily due to reported loss or theft.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC096", "line_id": "L002", "reason": "reported loss or theft"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are organized, patient. First, lookup customer by phone number \"555-1234\" to verify identity for account access. Once verified, suspend line ID \"L56789\" for user Michael Miller due to reported loss of device. Finally, transfer to human agents for user Michael Miller to discuss reconnection of line ID \"L56789\" to ensure he receives the necessary support and guidance on restoring his service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L56789", "reason": "Reported loss of device", "user_id": "TC054"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"line_id": "L56789", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are direct, independent, cautious, optimistic. Retrieve detailed information for line L102 to check its current plan and usage.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC081"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC081", "line_id": "L102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are flexible, logical, cautious. lookup_customer_by_phone with phone_number \"555-1234\" for user Michael Garcia to verify account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are logical, patient, flexible. First, verify the identity of Robert Jones using his email robert.jones5323@email.com before accessing account details. Once his identity is confirmed, proceed to lookup Robert Jones's account details using his phone number to obtain his customer ID. Finally, retrieve all active lines associated with Robert Jones's customer ID to ensure comprehensive analysis of his telecom usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones5323@email.com", "user_id": "TC123"}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "realistic_phone_number", "user_id": "TC123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC123", "user_id": "TC123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are polite, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify Michael Jones' account. Once verified, proceed to get_customer_lines for Michael Jones to retrieve all active and suspended lines associated with his account. After identifying the relevant line, use get_line_details for line ID L9876 to check its current status and plan details. If the line is active and matches the customer's request, suspend_line for line ID L9876 with reason \"Customer Request\" to temporarily halt service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC083"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC083", "user_id": "TC083"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC083"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "reason": "Customer Request", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are logical, patient, organized, cautious. Verify the identity of Linda Davis using her email linda.davis4055@email.com to access her account details. Once verified, get the bill details for Linda Davis using her customer ID to review her current charges and payment status. This will ensure that her account information is accurate and up-to-date, facilitating seamless communication and service provision in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis4055@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC048", "user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are organized, cautious, optimistic, independent. First, lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify Patricia Johnson's account. Once her account is verified, proceed to get_customer_lines for customer_id: \"C6047\" to retrieve all active lines under Patricia Johnson's account. This will help ensure that we have the correct information before making any changes or updates to her service plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC096"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC096", "user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are confident, independent. You need to assist a customer who called in with a request to suspend one of their phone lines. First, perform the task Lookup_customer_by_phone with parameters: phone_number='555-123-4567' to retrieve the customer's information. Once you have the customer ID, proceed with the task Get_customer_lines with parameters: customer_id='C12345' to identify all the lines associated with this customer. After confirming the specific line the customer wants to suspend, execute the task Suspend_line with parameters: line_id='L67890', reason='Customer request' to complete the suspension process.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC130"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "reason": "Customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are direct, flexible. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Patricia Smith's account identity. Once her identity is confirmed, get_line_details for line ID L1001 to retrieve current plan and usage details. This will help ensure that Patricia is aware of her current telecom services before any further actions are taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC113"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1001", "user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are organized, independent. First, lookup_customer_by_phone with phone number 555-0123 to verify identity for Michael Jones. Once verified, get_customer_lines for customer ID C4016 to review all active lines on the account. Finally, get_line_details for line ID L7890 to confirm eligibility for plan upgrade, ensuring that Michael Jones can benefit from the latest offers available.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC042"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC042", "user_id": "TC042"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L7890", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are independent, organized, direct. Verify the identity of user James Brown using the provided email (james.brown7392@email.com) to access his account. Once his identity is confirmed, proceed to suspend the line for line ID L1234 if James Brown requests a temporary suspension. This process ensures that the line is securely managed and can be easily resumed upon his request within the allowed 30-day period.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown7392@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC116", "line_id": "L1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are direct, flexible, logical, confident. First, lookup_customer_by_phone with phone_number=555-1234 to verify Linda Davis's account identity. Once verified, proceed to get_customer_lines for customer_id=LD4055 to retrieve all lines associated with Linda Davis. Finally, get_line_details for line_id=LD4055-01 to check current plan and usage details, ensuring Linda's account is on the appropriate plan for her needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC048"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LD4055-01"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are logical, organized, patient, optimistic. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of Jennifer Davis. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C12345\" to list all active lines under her account. Finally, get_bill_details for customer_id \"C12345\" to review her outstanding balance and payment history, ensuring that all financial obligations are up to date and there are no discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC085"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC085", "user_id": "TC085"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC085", "user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are polite, independent, organized, patient. Suspend_line for a specific line ID that Mary wants temporarily suspended",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC063"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC063", "line_id": "line_id_provided_by_mary"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC063", "line_id": "line_id_provided_by_mary"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are direct, independent, polite. lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Linda Garcia",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are flexible, optimistic, independent. Lookup Patricia Smith's account using her email (patricia.smith8398@email.com) to verify customer identity for account access. Once her identity is confirmed, get customer lines for Patricia Smith to identify active lines on the account. After identifying the active lines, suspend line L1234 for Patricia Smith due to the reported loss of her device, ensuring her account security and preventing unauthorized usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.smith8398@email.com", "user_id": "TC112"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "patricia.smith8398@email.com", "user_id": "TC112"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1234", "reason": "Reported loss of device", "user_id": "TC112"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are cautious, optimistic, independent. First, verify Patricia Johnson's identity using her email address patricia.johnson6047@email.com to access her account. Once verified, proceed to get bill details for Patricia Johnson to check her current outstanding balance and payment history. Finally, calculate the total amount due for Patricia Johnson, including any late fees or additional charges, to ensure she has accurate information regarding her telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC096", "email": "patricia.johnson6047@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC096", "email": "patricia.johnson6047@email.com"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC096", "email": "patricia.johnson6047@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are direct, cautious, confident, organized. First, lookup customer by phone using phone number 555-1234 to verify identity for Mary Johnson. Once her identity is confirmed, proceed to get customer lines for Mary Johnson to ensure all her active services are accounted for and up to date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC093"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Mary Johnson", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are direct, organized. First, lookup_customer_by_phone with phone_number \"555-0123\" to verify identity. Once the identity is verified, proceed to get_customer_lines for customer_id \"C456\" to review all active lines under the account. After identifying the relevant line, use get_line_details for line_id \"L789\" to check the current plan and usage. This will help in understanding the customer's current service setup before making any changes. Finally, calculate estimated charges for a plan change for line_id \"L789\" to provide the customer with a clear understanding of potential costs associated with switching plans.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC067"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC067", "line_id": "L789", "action": "estimate_plan_change"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are optimistic, confident, direct. Verify the customer identity using the email michael.jones4016@email.com to ensure secure access to the account. Once the identity is confirmed, use the phone number associated with Michael Jones to retrieve the customer ID. With the customer ID in hand, list all active lines under the account to provide a comprehensive overview of the services currently in use.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.jones4016@email.com", "user_id": "TC042"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC042", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are logical, cautious. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Linda Garcia's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC139",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are direct, independent. First, perform a lookup_customer_by_phone with phone_number: \"555-0123\" to verify identity for Michael Smith, ensuring that you have the correct customer before proceeding. Once verified, get_line_details with line_id: \"L67890\" to check the current plan and usage details, as Michael Smith has expressed concerns about potentially exceeding his data limits.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC139"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are flexible, polite, patient. Verify the identity of user Robert Jones by confirming account details provided in the email robert.jones3449@email.com before accessing account information. Once verified, lookup the customer by phone number associated with Robert Jones to retrieve the customer ID. With the customer ID, get customer lines to identify all active and suspended phone lines. This process ensures that you have accurate information to assist Robert Jones effectively with his account inquiries in a telecom business context.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones3449@email.com", "user_id": "TC109"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC109", "user_id": "TC109"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are optimistic, polite, confident. Please lookup_customer_by_phone with phone number \"555-123-4567\" to retrieve the customer ID for John Williams. Once you have the customer ID, proceed to get_bill_details to verify his outstanding balance and payment history. This will help ensure that we have an accurate understanding of his account status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC098"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC098", "user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are confident, patient, cautious, polite. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity for Mary Johnson. Once verified, proceed to get_customer_lines for user \"Mary Johnson\" to retrieve all associated phone lines. After identifying the relevant line, get_line_details for line ID \"L001\" to check the current plan and usage. This sequence will help ensure that Mary Johnson's account details are accurate and up-to-date, and it will allow us to address any inquiries she may have regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC071", "user_name": "Mary Johnson"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC071", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are cautious, logical, patient, confident. Process data refill for line ID L002 with 5GB additional data for the current billing period.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC143"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC143"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L002"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC143"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "add_data", "line_id": "L002", "data_amount_gb": 5}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are independent, optimistic, polite, logical. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of Mary Brown, ensuring that you are assisting the correct customer. Once identity is confirmed, proceed to get_customer_lines for customer_id \"C4135\" to retrieve all active lines associated with Mary Brown's account. This will help in providing a comprehensive overview of her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC063"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC063", "user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are optimistic, confident, cautious. Get bill details for John Garcia's account to review outstanding balances and payment history.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC015", "phone_number": "John Garcia's phone number"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC015", "customer_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are confident, polite, flexible. First, verify identity for user James Brown using email james.brown3113@email.com before accessing account details. Once verified, lookup customer by phone number 555-1234 to retrieve customer ID for James Brown's account. After obtaining the customer ID, get customer lines for customer ID C1001 to list all active lines under James Brown's account. This sequence ensures that you have the correct customer information and can provide accurate service details, maintaining a high standard of customer service in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC145"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC145", "user_id": "TC145"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are confident, cautious. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify Jennifer Davis's account. Once her account is verified, proceed to get_bill_details for account_id \"CUST1234\" to check for any outstanding balance and confirm the last payment date. These steps will help ensure accurate account handling and decision-making in the context of telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "CUST1234", "user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are confident, polite, patient. Get_bill_details for user John Brown to verify outstanding balance and payment due date.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are direct, independent. First, lookup_customer_by_phone with phone number 555-1234 to verify Michael Garcia's account identity. Once verified, proceed to suspend_line for line ID 5678 due to non-payment. Ensure that the account status is confirmed with Michael Garcia before taking action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC051"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "5678", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are direct, optimistic, patient, cautious. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are organized, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of Mary Jones. Once verified, proceed to get_customer_lines for user Mary Jones to retrieve all active lines associated with her account. Then, focus on line L001 and perform get_line_details to check the current plan and usage details, ensuring that the information aligns with her service expectations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC013"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Mary Jones", "user_id": "TC013"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are organized, polite. First, use the lookup_customer_by_phone with phone_number='555-123-4567' to verify Linda Davis's account identity. Once her identity is confirmed, proceed to get_customer_lines with customer_id='C12345' to retrieve Linda's active phone lines. After identifying her primary line, utilize get_line_details with line_id='L67890' to check the current status and plan details. This will help ensure that all necessary information is reviewed before any further action is taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC150"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are logical, confident, independent. Use lookup_customer_by_phone with Linda Davis's phone number to retrieve her customer ID and associated account information. Then, utilize get_customer_lines with Linda Davis's customer ID to retrieve a list of all active lines on her account. This process will help in understanding the current status and organization of Linda's telecom services, ensuring that her account is managed efficiently and any potential issues are addressed proactively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Davis's phone number", "user_id": "TC035"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC035", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are independent, logical, patient. First, lookup customer by phone number 555-1234 to verify identity for Robert Jones. Once his identity is verified, proceed to get customer lines for the account associated with Robert Jones. This will help ensure that we have the correct account information before making any further inquiries or changes.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Robert Jones", "user_id": "TC123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are cautious, patient, logical. \"lookup_customer_by_phone with phone number 555-1234 to verify identity of Robert Brown\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC073"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are organized, independent, optimistic, direct. Use lookup_customer_by_phone with phone number 555-1234 to retrieve Jennifer Jones's customer ID.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are patient, flexible, cautious, logical. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are confident, optimistic, independent, logical. First, lookup_customer_by_phone with phone_number \"555-123-4567\" for user Robert Brown to verify identity, ensuring that you are reviewing the correct account. Next, get_bill_details for bill_id \"B98765\" to review last month's charges and payment status, confirming all charges are accurate and up to date. Finally, think to assess if any further actions are needed to ensure the account is in good standing, such as advising the customer on payment options or notifying them of any discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC029"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"bill_id": "B98765", "user_id": "TC029"}
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
        user_id="TC020",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are flexible, optimistic, direct. First, use `lookup_customer_by_phone` with phone number \"555-123-4567\" to verify Mary's identity. Once verified, proceed to use `get_customer_lines` with customer ID \"C001\" to retrieve all active lines for Mary Davis. After identifying the active lines, use `get_line_details` with line ID \"L123\" to check the current plan and data allowance to ensure it meets her needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC020"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC020", "user_id": "TC020"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are polite, optimistic, patient, direct. First, verify the customer identity using the email john.smith6987@email.com to access account details. Once verified, proceed to suspend the line for line ID L1234 due to the customer's request for temporary suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.smith6987@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1234", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are cautious, organized. First, get customer lines for Linda Davis to identify active services. Then, get line details for line ID L5678 to check current plan and usage. Based on the information gathered, analyze Linda Davis's current plan and usage patterns to determine if a plan upgrade recommendation is appropriate, ensuring that any suggestions align with her service needs and usage trends.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC048", "customer_name": "Linda Davis"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC048", "line_id": "L5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are organized, flexible, patient, logical. Lookup_customer_by_phone with phone number 555-1234 to verify Jennifer Williams' identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are independent, patient. First, get bill details for user Mary Brown to verify her outstanding balance. Once you have confirmed the outstanding balance, calculate the late fee for Mary Brown's account, which currently has an outstanding balance of $120.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC063"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "120 * 0.05"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are polite, logical. Use lookup_customer_by_phone with the parameter phone_number set to \"123-456-7890\" to verify Michael Garcia's identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are patient, confident, cautious. Get_line_details for line ID L67890 to confirm eligibility for plan upgrade",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC146"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are polite, cautious, confident. First, get line details for line L456 to review options for a plan upgrade for Robert Jones. Once you have reviewed the options and identified suitable plans, transfer Robert Jones to a human agent to discuss the plan upgrade options and immediate activation requirements. This will ensure that Robert Jones receives personalized assistance and can make an informed decision about upgrading his telecom plan.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC144"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC144", "customer_name": "Robert Jones", "reason": "Discuss plan upgrade options and immediate activation requirements"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are polite, confident, patient. lookup_customer_by_phone with phone_number: \"555-1234\" to retrieve customer ID and verify identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are confident, direct, logical. Verify Michael Johnson's identity using email michael.johnson4265@email.com for account access. Once verified, lookup_customer_by_phone using Michael Johnson's phone number to retrieve account information. Finally, get_customer_lines for Michael Johnson's account to list all active lines, ensuring accurate service management and customer satisfaction in our telecom operations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.johnson4265@email.com", "user_id": "TC134"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "retrieved_phone_number", "user_id": "TC134"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are independent, logical, direct. Check the current billing details for Linda Smith using get_bill_details with her account ID.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "LindaSmithAccountID"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are logical, flexible, cautious, patient. To assist in resolving a customer service issue, begin by verifying the identity of customer John Garcia using his email john.garcia4063@email.com to ensure secure access to his account details. Once verified, proceed to look up the customer by the phone number associated with John Garcia to retrieve his unique customer ID. With the customer ID in hand, retrieve all active customer lines associated with this ID to ensure accurate and comprehensive service management.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia4063@email.com", "user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC018", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are polite, logical. Suspend line L12345 for Michael Miller as requested, ensuring the action is reversible within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC054", "email": "linda.garcia4634@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC054"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC054", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC054", "line_id": "L12345", "reason": "Customer request", "reversible_within_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are flexible, cautious, independent, optimistic. First, verify the identity of user James Brown using the email james.brown3113@email.com to ensure secure account access. Once his identity is confirmed, get the bill details for the current billing cycle so James can review his outstanding balance. If the balance remains unpaid, proceed to suspend line L002 for James Brown due to non-payment, ensuring all actions comply with company policy and are completed within the designated timeframe.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown3113@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC145"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC145", "line_id": "L002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are cautious, confident, patient, polite. First, verify the identity of Robert Jones to access his account using the email robert.jones1563@email.com. Once his identity is confirmed, proceed to suspend line L001 for Robert Jones due to his request for a temporary suspension. This sequence ensures that the suspension is authorized and aligns with our protocols for managing customer accounts in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones1563@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC144", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are confident, optimistic, logical. First, perform a lookup_customer_by_phone using phone_number \"555-1234\" to verify the identity of Linda Davis. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C3121\" to retrieve active lines under Linda Davis's account. After identifying the relevant line, use get_line_details for line_id \"L4567\" to check the current plan and usage details. If everything is in order and aligns with Linda Davis's request, proceed to suspend_line for line_id \"L4567\" with the reason \"customer request\" to ensure her service needs are met efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC035"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC035", "user_id": "TC035"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L4567", "user_id": "TC035"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L4567", "reason": "customer request", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are flexible, organized, confident. Suspend line L12345 for user James Jones due to reported issues.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC106"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC106", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC106", "line_id": "L12345", "reason": "Reported issues by user James Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are confident, direct. lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Linda Smith's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are confident, independent. First, perform a lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify Linda Smith's identity. Once her identity is confirmed, proceed to get_customer_lines with customer_id=\"C7027\" to retrieve all lines associated with Linda Smith's account. This sequence will ensure that you have accurate information about her account before addressing any service inquiries or issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC041"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC041", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are polite, flexible, confident. lookup_customer_by_phone using phone_number=555-123-4567 to verify Patricia Smith's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are logical, organized, flexible. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify Patricia Brown's identity. Once her identity is confirmed, proceed to get_bill_details for customer_id \"C9876\" to review the current bill and payment status. If Patricia Brown has any concerns about her payment, calculate outstanding balance for customer_id \"C9876\" to confirm the total amount due and provide her with accurate information.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC094"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC094", "user_id": "TC094"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "outstanding_balance", "customer_id": "TC094", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are independent, patient, confident. First, lookup_customer_by_phone with phone_number '555-0123' to verify identity for John Williams. Once verified, get_customer_lines for customer_id 'C12345' to retrieve all active lines. After identifying the relevant line, get_line_details for line_id 'L67890' to check current plan and data usage, as John is considering upgrading his plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC098"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are flexible, logical. Use lookup_customer_by_phone with the phone number associated with Linda Smith to retrieve her customer ID. Then, use get_customer_lines with Linda Smith's customer ID to list all active lines under her account. This will help us ensure that Linda's account is correctly updated with her current services and to verify any discrepancies in her billing statement.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Smith's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are polite, cautious, optimistic, organized. First, lookup Mary Miller's customer account using her phone number to verify her identity for account access. After successfully verifying her identity, get all active lines associated with Mary Miller's account to ensure comprehensive service management. Once you have the list of active lines, retrieve details for line L001 to check the current plan and usage details, as Mary is interested in understanding her data consumption and plan benefits.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Miller's phone number", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC102", "user_id": "TC102"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are flexible, independent. First, lookup_customer_by_phone with phone number 555-123-4567 to verify the identity of Michael Garcia, ensuring that you are addressing the correct account holder. Once verified, proceed to get_bill_details for customer ID C789 to review the latest billing statement. This will allow you to provide Michael Garcia with accurate and up-to-date information regarding his account status and any outstanding charges.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC039"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC039", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC135",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are flexible, patient, organized. Lookup customer by phone number 555-123-4567 to verify identity for user James Jones.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC135"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are logical, independent. Verify the identity of user Linda Garcia using email linda.garcia4634@email.com to access her account details. Once verified, lookup the customer by phone using Linda Garcia's verified phone number to retrieve her account ID. After obtaining the account ID, get the customer lines associated with Linda Garcia's account to list all active lines.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.garcia4634@email.com", "user_id": "TC127"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_from_previous_step", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are polite, flexible, patient, cautious. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify customer identity for Michael Garcia. Once verified, use the customer_id obtained from the lookup to get_customer_lines and list all active lines under Michael Garcia's account. This will help ensure that all lines are accurately accounted for in our system and assist in managing Michael Garcia's telecom services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC039"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC039", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are polite, logical. Please first lookup_customer_by_phone with phone number 555-1234 to verify the identity of user Robert Jones. Once his identity is confirmed, proceed to get_customer_lines for customer ID C789 to list all active lines associated with Robert Jones. This will help ensure that we have the correct information about his account before making any changes or providing further assistance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC123", "user_id": "TC123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are optimistic, direct. First, lookup_customer_by_phone with phone_number parameter set to Mary Davis's registered phone number to verify her identity. Once her identity is confirmed, proceed to get_bill_details for user Mary Davis to review her current outstanding balance and due date. This will ensure that she has all the necessary information regarding her telecom account and any payments that need to be made.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Davis's registered phone number"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are cautious, optimistic, patient. suspend_line for line_id \"L98765\" to temporarily halt service due to non-payment",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC134", "line_id": "L98765", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are optimistic, independent, organized, confident. Suspend line with line ID L12345 for Linda Smith due to reported lost phone.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "Lost phone", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are cautious, direct, organized. First, lookup_customer_by_phone with phone number associated with user Robert Garcia to verify identity. Once Robert Garcia's identity is confirmed, proceed to get_customer_lines for the customer ID obtained from his verified account. This will allow us to understand the number of active lines under his account, which is crucial for addressing his recent inquiry about potential upgrades and ensuring his account details are up-to-date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Garcia's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are independent, direct, patient. Please lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Robert Johnson. Once identity is confirmed, proceed to suspend_line for line ID L2345 if requested by Robert Johnson for temporary suspension. This process ensures that the customer's request is handled efficiently and securely, maintaining service integrity while accommodating the customer's needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC072"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L2345", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are flexible, independent. First, use lookup_customer_by_phone with phone number 555-123-4567 to verify John Williams' identity. Once his identity is confirmed, get_customer_lines using John Williams' account ID to list all active lines associated with his account. This will help ensure that all services are correctly linked and active for John Williams, providing a comprehensive view of his telecom account status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC031"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_from_previous_step", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are flexible, optimistic, direct, polite. First, get_bill_details for the current billing cycle to review charges and payment status for Robert Garcia's account, ensuring all recent transactions are accurately reflected. Then, transfer_to_human_agents with customer ID to discuss payment options and possible plan change with Robert Garcia, providing him with the most suitable solutions based on the reviewed billing details.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC046"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are cautious, flexible. First, perform a lookup_customer_by_phone with phone_number \"+1-555-0123\" to verify the customer's identity for account access. Once identity is confirmed, proceed to suspend_line for line_id \"L67890\" due to a reported lost phone, ensuring to note the suspension date for record-keeping.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1-555-0123"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are logical, patient. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Linda Johnson's account. Once verified, proceed to suspend_line for line ID L456 with reason 'customer request' and note 'temporary suspension requested by Linda Johnson'. After the suspension, get_customer_lines for customer ID C789 to confirm the status of all lines after suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC060"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "reason": "customer request", "note": "temporary suspension requested by Linda Johnson", "user_id": "TC060"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC060", "user_id": "TC060"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are optimistic, independent, organized, logical. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity for James Brown, as he has contacted customer support regarding his account. Once his identity is confirmed, proceed to get_bill_details for bill_id \"B9876\" to review any outstanding charges on his account, ensuring that you have a clear understanding of his current billing situation.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC116"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"bill_id": "B9876", "user_id": "TC116"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are direct, logical. First, lookup customer by phone number 555-1234 to retrieve account information for Michael Davis. Once you have the customer ID, get customer lines for user Michael Davis to list all active lines. Finally, get line details for line ID 7890 to check the current plan and usage for Michael Davis, ensuring that his telecom needs are being met efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC136"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC136", "user_id": "TC136"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "7890", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are optimistic, logical, independent, flexible. First, get line details for line L5678 to check eligibility for a plan upgrade requested by Robert Jones. Once eligibility is confirmed, calculate the cost difference for upgrading line L5678 to a new plan starting next billing cycle.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are direct, optimistic, organized. First, use lookup_customer_by_phone with phone number 123-456-7890 to verify Patricia Williams' account. Once her account is verified, retrieve all active lines for Patricia Williams using get_customer_lines with customer ID C2585 to ensure her services are correctly listed and active.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC092"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC092", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are logical, direct. \"lookup_customer_by_phone with phone number '555-1234' to verify Michael Garcia's account\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are independent, cautious, flexible. First, lookup_customer_by_phone with phone number 555-1234 to verify identity for account access. Once the customer's identity is confirmed, get_line_details for line ID L98765 to check the current plan and usage. If the customer requests to pause their service, proceed to suspend_line for line ID L98765 to temporarily suspend the service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC015"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L98765", "user_id": "TC015"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L98765", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are patient, flexible, organized. Retrieve all active lines for customer account identified for Jennifer Brown",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC062", "customer_name": "Jennifer Brown"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC062", "customer_name": "Jennifer Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are logical, independent. Begin by using the lookup_customer_by_phone with phone_number \"555-1234\" to verify Michael Miller's account. Once verified, proceed to get_bill_details for customer_id \"C102938\" to review the outstanding balance and payment history. If the account shows non-payment, use the suspend_line with line_id \"L5678\" to initiate suspension, ensuring that suspension eligibility is verified. If there are any complications or if further clarification is needed, transfer_to_human_agents with context \"billing inquiry and line suspension\" for additional assistance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC054"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "billing inquiry and line suspension"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are cautious, organized. lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Linda Smith's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are logical, optimistic, polite, direct. First, lookup_customer_by_phone with phone number '123-456-7890' to verify identity for Robert Brown. Once verified, get_customer_lines for user ID 'RB2463' to list all active lines associated with Robert Brown's account. Then, proceed to get_line_details for line ID 'L98765' to check the current plan and usage, ensuring that Robert Brown's telecom needs are being met efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "RB2463"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L98765"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are logical, flexible, optimistic, independent. Use `lookup_customer_by_phone` with the phone number provided by Linda Smith to verify her identity and access her account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Smith's phone number"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are confident, polite. First, lookup_customer_by_phone with Linda Smith's phone number to retrieve her account information. Once you have her account details, get_customer_lines for Linda Smith's account to list all active lines. After identifying the specific line, get_line_details for line L12345 to check its current plan and usage. This sequence will allow you to assess whether any adjustments are needed for her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Smith's phone number", "user_id": "TC146"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "Linda Smith's account ID", "user_id": "TC146"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC146"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are organized, logical. First, lookup_customer_by_phone for user John Garcia using the phone number associated with email john.garcia3458@email.com to verify identity. After successful identity verification, proceed to get_customer_lines for user John Garcia to retrieve active service lines. This process ensures that John Garcia's account is secure and allows you to manage his telecom services efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia3458@email.com", "user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are cautious, polite, independent, patient. lookup_customer_by_phone(customer_phone=\"123-456-7890\") to verify identity for Mary Johnson's account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"customer_phone": "123-456-7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are direct, logical, polite. Please begin by looking up the customer using the phone number \"555-123-4567\" to retrieve their customer ID. Once you have the customer ID, proceed to get the customer lines associated with it. After identifying the appropriate line, obtain the details of the line with line ID \"L67890\". If the customer has requested a temporary suspension of this line, please suspend the line for the specified reason.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC039"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC039", "user_id": "TC039"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC039"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "reason": "Customer requested temporary suspension", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are flexible, optimistic. First, verify user identity for Jennifer Brown using email jennifer.brown3820@email.com to access account details. Once her identity is confirmed, proceed to suspend line ID L12345 on Jennifer Brown's account due to the reported loss of her device. After 24 hours, get customer lines again to verify the suspension status of line ID L12345, ensuring that the suspension has been successfully implemented.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.brown3820@email.com", "user_id": "TC026"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "user_id": "TC026"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are organized, confident, flexible, patient. First, lookup the customer by the phone number associated with Robert Brown to retrieve his account details. Once you have the account information, get the customer lines for Robert Brown's account to identify active services. Finally, get the line details for line ID L1234 to check the current plan and usage, as this line has reported issues and may require further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number", "user_id": "TC036"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_step", "user_id": "TC036"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are patient, organized, flexible. Lookup customer by phone number '555-123-4567' to verify identity for Jennifer Smith, as she has reported issues with her account. Once her identity is confirmed, get bill details for the customer ID retrieved in the previous step to review her outstanding balance, ensuring that all billing inquiries are addressed accurately and efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC023"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC023", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are flexible, direct, polite. Suspend line L123 for Robert Williams due to non-payment",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC067"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC067"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC067", "line_id": "L123"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC067", "line_id": "L123", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are flexible, polite, patient, confident. lookup_customer_by_phone with phone_number \"555-1234\" to verify customer identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are direct, organized, polite. \"suspend_line with line_id: 'LINE67890' to temporarily suspend service due to suspected fraud activity\"",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC129", "line_id": "LINE67890", "reason": "suspected fraud activity"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are polite, patient. First, verify the identity of Robert Jones using the email robert.jones3449@email.com to access his account details. Once verified, proceed to get the bill details for Robert Jones's account to review his outstanding balance and payment history. After reviewing the bill details, calculate the total outstanding balance for Robert Jones's account, including any applicable late fees. This sequence of actions will help ensure accurate billing information is available for further assistance.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to verify Robert Jones's identity using his email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Unfortunately, there is no direct tool available for verifying identity using email. I will transfer to human agents for this step."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"reason": "Verify identity of Robert Jones using email robert.jones3449@email.com."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once identity is verified by human agents, I will proceed to get the bill details."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC109"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After retrieving the bill details, I will calculate the total outstanding balance including any late fees."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "outstanding_balance + late_fees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC003",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are organized, optimistic, independent, flexible. get_line_details for line ID retrieved from customer lines to check current plan",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC003"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "line_001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are direct, polite, logical, cautious. Please begin by using the lookup_customer_by_phone task with phone_number \"555-1234\" to verify Jennifer Smith's identity. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C12345\" to retrieve all active lines on Jennifer Smith's account. This will help us ensure that we have the correct information on her account before making any changes or providing further assistance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC143"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC143", "user_id": "TC143"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are cautious, patient. First, lookup_customer_by_phone with phone_number '555-1234' to verify the identity of customer James Brown. Once verified, get_bill_details for customer_id 'C12345' to review outstanding balance and recent transactions for James Brown, ensuring you have all necessary information to address potential billing issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC089"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC089", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are optimistic, organized. Get line details for the primary line of Michael Jones to check current plan and usage",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC083", "phone_number": "Michael Jones"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC083"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC083", "line_id": "primary"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are logical, cautious. First, get bill details for the account associated with phone number 555-0198 to review the outstanding balance. Once you have verified the details, calculate the total amount due, including any late fees, for the same account. This will ensure that you have a clear understanding of the financial obligations before proceeding with any further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0198", "user_id": "TC026"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"phone_number": "555-0198", "user_id": "TC026"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "add", "values": ["outstanding_balance", "late_fees"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are direct, flexible, cautious. First, verify customer identity for Jennifer Jones using email jennifer.jones9861@email.com to ensure compliance with our security protocols. Once her identity is confirmed, get bill details for Jennifer Jones to review outstanding balances and due dates, which will help her manage her telecom account effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.jones9861@email.com", "user_id": "TC038"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "jennifer.jones9861@email.com", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are optimistic, patient, independent, direct. Retrieve current plan details for line L12345 to assist Patricia with plan upgrade options. Once you have the necessary information, process the request to change the plan for line L12345 effective from the next billing cycle. Ensure that Patricia is aware of the new plan features and any changes in her billing.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC113", "phone_number": "L12345"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC113", "line_id": "L12345"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC113", "reason": "Plan upgrade assistance for Patricia"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are flexible, independent, polite. First, verify customer identity for Robert Jones using email robert.jones1563@email.com before accessing account details. Once the identity is confirmed, proceed to get bill details for Robert Jones to identify any outstanding payments or discrepancies. This process ensures that we maintain account security while providing accurate billing information.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones1563@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are optimistic, logical. Verify customer identity using email jennifer.davis3568@email.com to access account details. Once verified, get_bill_details for customer ID to review outstanding balance and payment history. This will ensure you have all necessary information to assist the customer effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.davis3568@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are direct, cautious. First, lookup_customer_by_phone with phone_number: \"555-1234\" to verify identity and ensure you are accessing the correct account. Once verified, proceed to get_customer_lines for customer_id: \"C1001\" to retrieve a list of active lines associated with the account. After identifying the specific line of interest, use get_line_details for line_id: \"L2001\" to check the current plan and usage details. If you notice any discrepancies or unauthorized usage, take immediate action by executing suspend_line with line_id: \"L2001\" to temporarily halt service and prevent further issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC060"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L2001"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L2001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are optimistic, direct, confident. \"lookup_customer_by_phone with phone_number '555-0123' to verify identity for account access\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are independent, confident. First, lookup_customer_by_phone with phone_number: \"555-123-4567\" for user Linda Davis to verify identity. Once her identity is confirmed, proceed to get_customer_lines for customer_id: \"C12345\" to list all active lines associated with Linda Davis's account. After identifying the relevant line, get_line_details for line_id: \"L56789\" to check current plan and usage details for Linda Davis.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC048"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L56789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are patient, organized, flexible. First, lookup_customer_by_phone with phone_number '555-1234' to verify customer identity and retrieve account details for Mary Johnson. Once her identity is confirmed, get_bill_details for user_id 'mary.johnson4713' to review the most recent bill and payment status. Finally, calculate total outstanding balance for user_id 'mary.johnson4713' based on recent bill details to provide her with an accurate account summary and assist with any questions she may have regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "mary.johnson4713"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "total_outstanding_balance"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are flexible, optimistic, cautious, independent. \"get_line_details for line_id: 'L987654' to review usage and plan details\"",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L987654"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are optimistic, polite, confident. First, lookup the customer by the phone number associated with James Jones to retrieve his account details. Once you have his account information, proceed to get the customer lines for James Jones to determine the active services on his account. Finally, get the line details for the primary line on James Jones's account to assess the current plan and usage, as this will help in planning a change to a higher data plan, effective from the next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "James Jones's phone number", "user_id": "TC106"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC106", "user_id": "TC106"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary_line_id", "user_id": "TC106"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are logical, patient. Verify the identity of user Mary Jones using her email mary.jones9465@email.com to access account details. Once verified, retrieve the latest bill details for Mary using get_bill_details with her customer ID. Calculate the total amount due on Mary's current bill using calculate with bill details obtained.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC147"}
            ),
            Action(
                name="calculate",
                kwargs={"bill_details": "latest_bill_details"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are cautious, optimistic. Lookup_customer_by_phone with phone_number \"555-1234\" to verify identity for Linda Davis's account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC150"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are optimistic, flexible. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of Jennifer Brown, who has contacted us regarding her account. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C3820\" to retrieve a list of her active lines, as she is interested in reviewing her current services. After obtaining the list, focus on get_line_details for line_id \"L9876\" to check Jennifer's current plan and usage, enabling you to understand her usage patterns and charges. This information will help you think about the best plan options for Jennifer Brown, ensuring she receives the most cost-effective and suitable service for her needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC026", "user_id": "TC026"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are confident, polite, direct, flexible. \"lookup_customer_by_phone using phone number 555-1234 to verify Mary Miller's account\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are flexible, logical, organized. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify identity and access account details for Michael Johnson. Once his identity is verified, proceed to get_customer_lines with customer_id 'CUST-4265' to retrieve all active lines under Michael Johnson's account. This will help in assessing the current services he is subscribed to and identifying opportunities for a potential plan upgrade.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC134"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC134", "user_id": "TC134"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are flexible, polite, direct, logical. First, verify the identity of user James Brown using email james.brown7392@email.com for account access to ensure secure handling of his information. Once his identity is confirmed, proceed to get bill details for James Brown to review the latest billing statement and outstanding balance, ensuring he has all the necessary information to understand his current charges. Finally, calculate the total due amount including any late fees for James Brown's latest bill so he knows the exact amount he needs to pay. If James Brown requests a detailed explanation of his bill discrepancies during this process, be prepared to transfer him to human agents who can provide a thorough clarification.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC116", "email": "james.brown7392@email.com"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC116", "operation": "total_due", "include_late_fees": true}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC116", "reason": "bill_discrepancies"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are cautious, organized. \"get_line_details\" with parameters: line_id=\"LINE5678\" to check the current plan and usage for Mary's primary line",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are independent, polite, flexible, patient. First, use the lookup_customer_by_phone(phone_number=\"555-1234\") to verify the identity of Robert Williams, ensuring you are assisting the correct customer. Once verified, proceed to get_customer_lines(customer_id=\"C789\") to list all active lines associated with Robert Williams, so you can identify the specific line he is inquiring about. After identifying the relevant line, use get_line_details(line_id=\"L456\") to check the current plan and usage for that line, ensuring you provide Robert with accurate and up-to-date information about his plan and remaining data.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC067"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are patient, independent, flexible, confident. Suspend_line for line ID L123 due to non-payment issue",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC124"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
]
