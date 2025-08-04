"""
Generated tasks for telecom domain.
Generated at: 2025-08-04T01:21:08.772748
Total tasks: 520
"""

from tau_types import Task, Action

TASKS_TRAIN = [
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are direct, cautious, logical. lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Patricia Williams' account",
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
        user_id="TC016",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are organized, independent. Suspend line L9876 on John Smith’s account due to non-payment, ensuring suspension is reversible within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC016", "phone_number": "John Smith's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC016", "customer_id": "TC016"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC016", "line_id": "L9876"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC016", "customer_id": "TC016"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC016", "line_id": "L9876", "reason": "non-payment", "reversible_within_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are flexible, patient, polite, direct. First, verify customer identity for Patricia Williams using email patricia.williams2585@email.com to access account details. Once her identity is confirmed, get_bill_details for Patricia Williams's account to retrieve the latest bill and payment status. This will help determine the necessary actions to address any outstanding payments and ensure her account remains in good standing.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.williams2585@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are optimistic, direct, polite, cautious. Please begin by looking up the customer by phone to verify account access for user Jennifer Brown, who can be reached at phone number 555-0123. Once you have successfully verified her account, proceed to get customer lines for Jennifer Brown. This process is crucial to ensure that we are providing the correct information and services related to her telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC062"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are optimistic, polite, flexible. First, get the customer lines for Patricia Williams' account to list all active lines. Once you have identified the active lines, proceed to get the line details for line ID L456 to check data usage and remaining data balance. If the remaining data balance is below 1GB, recommend a data refill for line ID L456 to ensure uninterrupted service for the customer.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC092", "customer_name": "Patricia Williams"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC092", "line_id": "L456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are independent, confident. \"lookup_customer_by_phone with phone_number '123-456-7890' to verify identity for John Garcia\"",
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
        user_id="TC092",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are confident, patient, polite, flexible. First, use the lookup_customer_by_phone task with phone number 123-456-7890 to verify the identity of Patricia Williams. Once her identity is confirmed, proceed to get_customer_lines for customer ID C2585 to retrieve all active lines under Patricia Williams' account. This will ensure that we have the correct information to assist her with any inquiries regarding her telecom services.",
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
        user_id="TC065",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are confident, logical. \"Check current plan details for line L001 to determine eligibility for upgrade\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC065", "email": "linda.davis4055@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC065"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC065", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are polite, flexible, independent. Verify the identity of Michael Davis using email michael.davis7894@email.com to access his account. Once verified, get_line_details for the primary line on Michael Davis' account to check the current plan and usage. This information will help in understanding his needs before discussing potential plan upgrades.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.davis7894@email.com", "user_id": "TC069"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "michael.davis7894@email.com", "user_id": "TC069"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary", "user_id": "TC069"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are organized, cautious, patient. suspend_line for line ID L001 due to reported loss by Mary Johnson",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "Reported loss by Mary Johnson", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC024",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are organized, optimistic. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Jennifer Davis's identity, ensuring that you are speaking with the correct account holder. Once her identity is confirmed, proceed to get_bill_details for customer_id \"C789\" to review her outstanding balance and payment due date. This will help you provide Jennifer with accurate information regarding her account status and assist her in resolving any payment issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC024"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC024", "user_id": "TC024"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are flexible, confident. First, lookup_customer_by_phone to verify identity for phone number 555-1234. Once the customer's identity is confirmed, suspend_line for line ID 789012 due to non-payment, and notify the user of the suspension. This process ensures that we maintain accurate records and communicate effectively with our customers regarding their account status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC109"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "789012", "reason": "non-payment", "user_id": "TC109"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are cautious, polite, patient, independent. First, lookup customer by phone number (123-456-7890) to retrieve the account ID for John Brown. Next, get bill details for the account ID associated with John Brown to review any outstanding payments. Finally, calculate the total outstanding balance for the account ID using the bill details retrieved.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC124"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC124"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "sum(outstanding_balances_from_previous_call)"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are polite, cautious, flexible, optimistic. Please lookup the customer by phone number 555-1234 to retrieve account details for John Williams, and then check the bill details for his account to verify any outstanding payments. This is important to ensure that we maintain accurate billing records and provide John with the most up-to-date information regarding his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC031"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC031", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are independent, organized, patient, optimistic. lookup_customer_by_phone with phone_number \"555-0182\" to verify Robert Williams' account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0182", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are direct, optimistic, cautious, flexible. \"lookup_customer_by_phone with phone number 555-0198 to verify account identity for Jennifer Williams\"",
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
        user_id="TC015",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are patient, organized, confident, independent. First, verify the identity of John Garcia by confirming his email john.garcia3458@email.com and any additional required information. Once his identity is confirmed, use lookup_customer_by_phone to retrieve John Garcia's account information using his phone number. Finally, get_customer_lines to list all active lines under John Garcia's account. This sequence will help ensure that John Garcia's account details are accurate and up-to-date, allowing us to provide him with the best possible service and support in managing his telecom needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "John Garcia's phone number", "user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "John Garcia's account ID", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are organized, polite. Get bill details for Jennifer Brown to review the latest billing statement and any outstanding balances.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are optimistic, confident. Verify the identity of User Robert Jones using his email robert.jones6549@email.com to access account details, then get_bill_details for Robert Jones's account to view the latest billing statement and any pending payments. This will ensure you have the necessary information to assist him with any inquiries about his telecom services and facilitate a smooth customer service experience.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC119"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are cautious, organized. suspend_line for line ID 67890 due to reported lost device",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC149", "line_id": "67890", "reason": "reported lost device"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are independent, direct. First, use the lookup_customer_by_phone with phone_number=\"(555) 123-4567\" to verify Linda Garcia's account identity as she reported her device lost. Once her identity is confirmed, proceed to suspend_line with line_id=\"L9876\" to temporarily suspend her service to prevent unauthorized usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "(555) 123-4567"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are optimistic, direct. First, use lookup_customer_by_phone with phone number 555-1234 to verify the identity of Jennifer Miller, ensuring you have the correct customer information. Once her identity is confirmed, retrieve customer lines using get_customer_lines with the customer ID associated with Jennifer Miller to access her account details. This will help in assessing her current telecom services and addressing any inquiries she may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC108"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC108", "user_id": "TC108"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are independent, patient, logical, cautious. First, lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Michael Garcia. Once identity is confirmed, get_customer_lines for customer ID C1023 to list all active lines associated with the account. After identifying the relevant line, proceed to suspend_line for line ID L5678 due to customer request, ensuring suspension is temporary and clearly documenting the reason for future reference.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC051"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC051", "user_id": "TC051"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "reason": "Customer request for temporary suspension", "temporary": true, "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are direct, cautious, logical. First, lookup_customer_by_phone with phone_number \"+1234567890\" to verify identity for user Linda Davis. Once her identity is confirmed, calculate new plan cost with current_usage \"5GB\" and new_plan \"Unlimited\" for Linda Davis. This will help determine if the switch to an unlimited plan is beneficial for her, considering her current usage patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890", "user_id": "TC107"}
            ),
            Action(
                name="calculate",
                kwargs={"current_usage": "5GB", "new_plan": "Unlimited", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are organized, confident. Get details for line L123 to check current plan and usage",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC092"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC092", "line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are confident, cautious, organized. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of Jennifer Davis. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C4933\" to retrieve all active lines associated with her account. After identifying the active lines, get_line_details for line_id \"L7890\" to check the current plan and usage. This will help you understand her account better and provide accurate assistance.",
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
                kwargs={"line_id": "L7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are optimistic, confident. First, lookup_customer_by_phone with phone number 555-123-4567 to verify the identity of Robert Garcia, ensuring that you are interacting with the correct individual. Once verified, proceed to get_customer_lines for the account associated with Robert Garcia to retrieve all active lines, providing a comprehensive view of his telecom services. Finally, get_line_details for line L001 to check the current plan and usage, as Robert Garcia has expressed interest in understanding his service details before making any changes.",
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
                kwargs={"line_id": "L001", "user_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are patient, organized. Get_customer_lines using customer ID obtained to list all active and suspended lines on the account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC145", "email": "linda.johnson5357@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC145", "customer_id": "TC145"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are polite, patient. lookup_customer_by_phone with phone_number \"555-123-4567\"",
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
        user_id="TC061",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are flexible, logical. First, get line details for line L789 to check if it is eligible for a plan upgrade on Patricia Davis's account. Then, think about the best plan options for line L789 based on Patricia Davis's usage patterns and preferences, ensuring that the options align with her current data and call usage trends.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC061", "line_id": "L789"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if line L789 is eligible for a plan upgrade based on current plan details and usage patterns."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are patient, independent. First, verify customer identity using the email robert.johnson9087@email.com to access account details. Once identity verification is successful, lookup customer by phone number associated with Robert Johnson to retrieve account information. Finally, get customer lines for the account identified for Robert Johnson to view active and suspended lines, ensuring all lines are correctly accounted for in the telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC072", "phone_number": "associated_phone_number_for_robert_johnson"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC072", "account_id": "retrieved_account_id_for_robert_johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are cautious, organized, logical, optimistic. Please begin by performing a lookup_customer_by_phone using the phone number \"555-123-4567\" to verify Linda Smith's account. Once you have confirmed her account details, proceed to get_customer_lines for the customer ID retrieved from Linda Smith's account to list all active lines. This process is crucial for ensuring that we have an accurate overview of Linda's current telecom services and can assist her effectively with any inquiries or updates she may require.",
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
        user_id="TC041",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are polite, optimistic, cautious, independent. Get line details for each active line under Linda Smith's account to check plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC041", "phone_number": "Linda Smith's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC041", "customer_id": "TC041"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC041", "line_id": "line1"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC041", "line_id": "line2"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC041", "line_id": "line3"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Mary Miller and your email is mary.miller8461@email.com. You are optimistic, polite, confident. Please begin by verifying customer identity using Jennifer Johnson's email (jennifer.johnson5907@email.com) before proceeding with account access. Once her identity is confirmed, lookup customer by phone number 123-456-7890 to retrieve Jennifer Johnson's account information and verify active lines. This process ensures that we maintain the security and integrity of our telecom services while providing Jennifer with accurate and efficient support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC149"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are confident, organized. First, lookup_customer_by_phone with phone_number \"555-1234\" for user Patricia Smith to verify identity and access account. Once verified, proceed to get_customer_lines for customer_id \"C1001\" to retrieve all active lines on Patricia Smith's account. This will ensure that you have the necessary information to assist Patricia with any inquiries regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC112"}
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
        user_id="TC119",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are direct, optimistic, patient, confident. First, lookup_customer_by_phone with phone number 555-1234 to verify identity and access account details for Robert Jones. Once his identity is confirmed, proceed to get_bill_details for customer ID C6549 to review outstanding charges and payment history. This will help determine if there are any overdue payments that need addressing.",
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
        user_id="TC060",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are cautious, flexible. Lookup customer by phone using phone number 555-123-4567 to verify Linda Johnson's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC060"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are cautious, organized. First, lookup Patricia Smith's account using her phone number to verify her identity, as we need to ensure we are accessing the correct customer information. Once her identity is confirmed, retrieve all active lines associated with Patricia Smith's account to get a comprehensive view of her services. After identifying her active lines, get details for line L001 to check the current plan and data usage. This will help us understand if there are any discrepancies or unusual activities that might indicate fraudulent usage, allowing us to take appropriate action if necessary.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Smith's phone number", "user_id": "TC113"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC113", "user_id": "TC113"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are optimistic, flexible, direct, cautious. First, lookup_customer_by_phone with phone_number '555-1234' to verify identity for user Mary Brown. Once verified, get_customer_lines for customer_id 'C7890' to retrieve all associated phone lines. After identifying the relevant line, get_line_details for line_id 'L123' to check the current plan and features to ensure it aligns with the customer's needs and preferences.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC063"}
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
        user_id="TC146",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are flexible, cautious, independent, direct. First, lookup_customer_by_phone with phone_number=\"555-1234\" for user Linda Smith to identify her customer ID. Once you have retrieved her customer ID, proceed to get_customer_lines for that customer ID to retrieve all active lines associated with Linda Smith. This will help in assessing her current telecom services and ensuring she is on the most suitable plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC146", "user_id": "TC146"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are patient, cautious. First, verify the identity of user Jennifer Jones using email jennifer.jones9861@email.com for account access to ensure the security of her telecom account. Once her identity is confirmed, lookup the customer by phone number associated with Jennifer Jones to retrieve her customer ID, which will be necessary for further account management tasks.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC038", "reason": "Verify identity of Jennifer Jones using email jennifer.jones9861@email.com for account access."}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC038", "phone_number": "phone_number_associated_with_Jennifer_Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are polite, patient, flexible. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Robert Brown's identity, as he has reported an issue with his service. Once verified, proceed to get_customer_lines for customer_id \"CUST123\" to list all active lines under Robert Brown's account. After identifying the specific line in question, get_line_details for line_id \"LINE456\" to check the data usage details and ensure there are no discrepancies. Finally, if Robert Brown confirms the line is indeed lost, suspend_line for line_id \"LINE456\" to prevent unauthorized usage and secure his account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC120"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE456"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE456", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are independent, optimistic, organized. Verify user identity for John Williams using email john.williams8933@email.com and ask for additional security information if needed. Once his identity is confirmed, lookup_customer_by_phone using the phone number provided by John Williams to retrieve account details. This will ensure we have the correct customer information before proceeding with any account-related tasks.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_by_john_williams", "user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are cautious, patient, confident, independent. First, lookup_customer_by_phone with phone_number: \"+1234567890\" to verify Michael Garcia's account, ensuring that the customer information is accurate and up-to-date. Once verified, proceed to get_customer_lines for customer_id: \"C123456\" to list all active lines under Michael Garcia's account, which will help in identifying the specific line that needs attention. Finally, get_line_details for line_id: \"L987654\" to check the current plan and usage details for Michael Garcia's primary line, ensuring that you have the necessary information to address any issues related to his service plan or usage before taking further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC039"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L987654"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are optimistic, cautious. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity and access account details for Jennifer Davis. Once her identity is confirmed, proceed to get_bill_details for customer ID C00123 to view her outstanding balance and payment history. This sequence ensures that you have the necessary information to address any billing concerns Jennifer may have and to discuss potential solutions for her account.",
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
        user_id="TC143",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are optimistic, patient, flexible, confident. Retrieve detailed information for line L12345 to check current plan and status.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC143"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC143", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are optimistic, organized, cautious, logical. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify the identity of Mary Jones. After confirming her identity, proceed to get_bill_details for customer_id \"C12345\" to review her outstanding balance and payment history. If you find that there is a significant overdue amount, get_line_details for line_id \"L67890\" to check her current plan and usage. Should the non-payment issue persist, and after ensuring you have Mary Jones's consent, suspend_line for line_id \"L67890\" to prevent further charges until the balance is settled.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC013"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are polite, flexible, organized. Please lookup customer by phone using Linda Davis's phone number to verify her identity. Once verified, get customer lines for Linda Davis to retrieve all associated phone lines. Finally, get line details for Linda Davis's primary phone line to check her current plan and usage. This sequence will help ensure that we have accurate information about Linda's account and can assist her effectively with any inquiries regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Davis's phone number", "user_id": "TC107"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Linda Davis's primary line ID", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are patient, confident, independent, logical. Verify Jennifer Jones's identity using her email jennifer.jones7047@email.com for account access. Once her identity is confirmed, use her provided phone number to lookup_customer_by_phone and retrieve her account information. This process is essential to ensure secure access and accurate retrieval of her account details in our telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC130", "phone_number": "provided_phone_number"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are polite, patient, direct, logical. First, lookup_customer_by_phone with phone_number as '555-1234' to verify the identity of Jennifer Miller. Once verified, suspend_line for line_id 'L001' due to the reported device loss by Jennifer Miller. After suspending the line, calculate estimated charges for resuming suspended line 'L001' within 30 days to provide Jennifer with an accurate estimate of any potential costs associated with reactivating her service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "Device loss reported", "user_id": "TC108"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"line_id": "L001", "action": "resume", "duration": "30", "user_id": "TC108"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are cautious, patient, logical. First, lookup customer by phone number 555-123-4567 to verify Linda Garcia's account information. Once her account is verified, proceed to get customer lines for account ID A2678 to identify all active lines under Linda Garcia's account. After confirming the active lines, get line details for line ID L3456 to check current plan and usage information for Linda Garcia, ensuring that the line is eligible for the requested temporary suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "A2678", "user_id": "TC141"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L3456", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are independent, flexible, cautious. Verify customer identity using email mary.miller8461@email.com for account access, then use the customer ID obtained to get_customer_lines and list all active lines. This will help ensure that Mary Miller can securely access her account and review her active telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.miller8461@email.com"}
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
        user_id="TC003",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are direct, polite, confident, organized. First, lookup customer by phone number 555-0123 to verify identity and access account details for Robert Garcia. Once the identity is verified, proceed to get customer lines for the account associated with user Robert Garcia to identify active services. This will help us ensure that all active services are correctly listed and up to date, which is crucial for maintaining accurate billing and service management in our telecom operations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC003"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC003"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are polite, flexible, patient. First, use lookup_customer_by_phone with phone number 555-0123 to verify identity for customer John Williams. Once identity is confirmed, proceed to use get_customer_lines with customer ID C001 to retrieve all active lines for John Williams. After obtaining the active lines, use get_line_details with line ID L123 to check plan details and data usage for John Williams' primary line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC031"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC031", "user_id": "TC031"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are cautious, logical, optimistic, confident. First, lookup_customer_by_phone with phone_number: \"123-456-7890\" to verify the identity of Jennifer Brown. Once her identity is confirmed, get_bill_details for user_id: \"jennifer.brown9346@email.com\" to check for any outstanding payments. If you find that there are overdue payments, proceed to suspend_line for line_id: \"LINE123\" and notify Jennifer Brown of the suspension due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "jennifer.brown9346@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are cautious, direct. First, verify the identity of John Williams using the email john.williams8933@email.com to ensure secure access to his account. Once his identity is confirmed, proceed to get the bill details for John Williams' account to review recent charges and the due date, as he has reported discrepancies in his billing statement. This will help in resolving his concerns effectively and maintaining his trust in our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.williams8933@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are independent, confident, flexible, optimistic. Use lookup_customer_by_phone with phone number \"555-0199\" to verify identity for John Smith.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0199", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are confident, cautious, direct, optimistic. lookup_customer_by_phone with phone_number 555-1234 to verify identity for user Jennifer Brown",
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
        user_id="TC081",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are logical, independent. Lookup customer by phone number 555-1234 to verify identity and access account details for John Smith. Once verified, get customer lines for the account associated with John Smith to review active services, ensuring all services are up to date and functioning correctly as part of a routine telecom account audit.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC081"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC081", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are direct, flexible, organized, confident. First, lookup_customer_by_phone(phone_number=\"555-123-4567\", customer_email=\"michael.davis9122@email.com\") to verify the identity and account information of the customer, Michael Davis, who has contacted us regarding his service. Once verified, proceed to get_customer_lines(customer_id=\"CUST12345\") to review all active lines associated with Michael's account, ensuring you have a comprehensive understanding of his current services. Finally, if Michael confirms the need to temporarily halt one of his services, execute suspend_line(line_id=\"LINE67890\", reason=\"Customer Request\") to fulfill his request efficiently, ensuring you document the reason for suspension accurately for future reference.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "customer_email": "michael.davis9122@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC136"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE67890", "reason": "Customer Request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are independent, direct, optimistic, organized. lookup_customer_by_phone with the parameter phone_number as \"555-123-4567\" to verify Robert Brown's identity.",
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
        user_id="TC019",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are flexible, independent. Lookup customer by phone number 555-1234 to retrieve customer ID and account details. Then, get bill details for customer ID to verify outstanding balance and due date. Finally, calculate payment amount including any late fees for customer ID based on bill details to ensure accurate billing and facilitate timely payment processing in the telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC019"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC019", "user_id": "TC019"}
            ),
            Action(
                name="calculate",
                kwargs={"customer_id": "TC019", "user_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are confident, independent. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify Linda Smith's identity, as she has contacted customer support regarding her service issues. Once her identity is confirmed, proceed to get_bill_details for customer_id 'C7027' to review her outstanding balance, ensuring you have all necessary information to discuss her account status and potential service disruptions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC041"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC041", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are flexible, optimistic. First, resume the suspended line ID L987654 for account ID A123456 within the 30-day period to ensure that the customer regains access to their telecom services promptly. After successfully resuming the line, get the line details for line ID L987654 to confirm that the resumption was successful and to review the current plan details, ensuring that the customer is on the correct plan and there are no discrepancies. This process is crucial to maintaining customer satisfaction and ensuring seamless service continuity.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC082", "account_id": "A123456"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC082", "line_id": "L987654"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC082", "line_id": "L987654", "action": "resume"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC082", "line_id": "L987654"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are logical, polite, patient, confident. First, lookup_customer_by_phone with phone_number=555-123-4567 to verify identity for Robert Jones. Once verified, proceed to get_customer_lines for customer_id=CUST123 to list all active lines associated with Robert Jones. After identifying the relevant line, get_line_details for line_id=LINE456 to retrieve the current plan and usage details, ensuring Robert has the most up-to-date information on his account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC144", "user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE456", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are organized, cautious, patient. Verify customer identity using email michael.johnson4265@email.com to access account details. Once verified, get_bill_details for customer ID to review outstanding balance and payment history. This will help in understanding the customer's current financial obligations before proceeding to any further actions.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"email": "michael.johnson4265@email.com", "user_id": "TC134"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are confident, cautious, independent. Lookup customer by phone number 555-1234 to verify Michael Davis's account details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are patient, direct, independent, logical. lookup_customer_by_phone with phone_number 555-1234 to verify Linda Johnson's identity",
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
        user_id="TC016",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are confident, flexible, direct. Lookup customer by phone number 555-0123 to retrieve the customer ID associated with John Smith. Once you have the customer ID, get customer lines for that ID to list all active and suspended lines. This will help us ensure that John Smith's account is up-to-date and that we can address any issues with his service promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC016"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC016", "user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are independent, direct. First, use the Lookup_customer_by_phone with phone number 555-1234 to verify customer identity for John Garcia. Once verified, proceed to Get_customer_lines for the verified customer account to retrieve all active lines. After obtaining the active lines, use Get_line_details for line ID L9876 to review the current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC015"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are patient, cautious, optimistic, direct. Get_bill_details for Mary Smith's account using customer ID to review the latest bill and payment status.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are polite, direct. First, lookup_customer_by_phone(phone_number=\"555-123-4567\") to verify Michael Williams' account identity. Once verified, proceed to get_bill_details(customer_id=\"customer_001\") to retrieve the latest bill for Michael Williams. This will ensure you have the necessary information to assist him with any inquiries about his billing statement.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are independent, organized. First, lookup_customer_by_phone with phone number 555-1234 to verify identity and access account details for Jennifer Smith. Once her identity is confirmed, proceed to get_customer_lines for customer ID 9988 to retrieve all active lines under Jennifer Smith's account. This will help ensure that we have accurate information on her current services and can assist her effectively with any inquiries or changes she may need.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC023"}
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
        user_id="TC096",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are confident, polite, organized. Begin by verifying the identity of Patricia Johnson using her email patricia.johnson6047@email.com before accessing any account details. Once her identity is confirmed, use lookup_customer_by_phone with Patricia's verified phone number to retrieve her customer account information. After obtaining her customer ID, employ get_customer_lines to list all active and suspended lines associated with her account. This process will help ensure that Patricia Johnson's account is accurately managed and that all related services are up-to-date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "verified_phone_number", "user_id": "TC096"}
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
        user_id="TC101",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are confident, optimistic. \"lookup_customer_by_phone with phone_number '555-123-4567' to verify identity for resuming suspended line\"",
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
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are patient, polite, direct, logical. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify Patricia Brown's identity. Once her identity is confirmed, proceed to get_customer_lines for customer_id 'C001' to list all active lines under Patricia Brown's account. Finally, get_line_details for line_id 'L102' to check current plan and usage details, ensuring you have the necessary information to assist Patricia with any inquiries about her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC094"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC094", "user_id": "TC094"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L102", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is James Brown and your email is james.brown7392@email.com. You are organized, independent, optimistic, cautious. First, perform a Lookup_customer_by_phone for Jennifer's phone number to retrieve her account information. Once you have accessed her account, proceed to Get_bill_details for Jennifer's account to review the latest bill and payment status. This will ensure that we have the most up-to-date information on her billing and payment history, which is crucial for maintaining accurate records and providing excellent customer service in our telecom operations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer's phone number", "user_id": "TC038"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "Jennifer's account ID", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are polite, patient. Lookup customer by phone number 555-1234 to verify identity and access account details for Patricia Miller.",
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
        user_id="TC003",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are patient, independent, optimistic, confident. lookup_customer_by_phone(phone_number=\"123-456-7890\") to verify Robert Garcia's account.",
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
        user_id="TC032",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are optimistic, independent, flexible. First, lookup customer by phone number 123-456-7890 to verify customer identity for account access. Once the customer's identity is confirmed, suspend line L67890 for user ID U12345 due to the reported lost device. This ensures the security of the customer's account and prevents unauthorized use of the lost device.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC032"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "user_id": "TC032", "reason": "lost device"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is John Garcia and your email is john.garcia4063@email.com. You are patient, flexible. First, use the lookup_customer_by_phone atomic task with the phone number provided by Linda Garcia to verify her identity. Once her identity is confirmed, proceed to the get_customer_lines atomic task for Linda Garcia’s account to retrieve all active lines. This will help ensure you have the correct information to assist her with any inquiries regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_by_Linda_Garcia", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC141", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are flexible, confident. First, verify the identity of user John Johnson using the email john.johnson9055@email.com to ensure secure account access. Once his identity is confirmed, retrieve all active lines associated with John Johnson's account using get_customer_lines to assess his current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.johnson9055@email.com", "user_id": "TC001"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are optimistic, flexible. Resume suspended line L456 for Jennifer if within 30 days of suspension and upon her request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC038", "phone_number": "Jennifer's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC038", "customer_id": "TC038"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC038", "line_id": "L456"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC038", "line_id": "L456", "action": "resume"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are patient, cautious. Begin by looking up the customer by phone number 555-123-4567 to verify Linda Davis's identity. Once her identity is successfully verified, proceed to get the customer lines for the account associated with Linda Davis. After retrieving the account details, suspend line L789 temporarily due to reported service issues by Linda Davis.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC107"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L789", "reason": "Reported service issues", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are organized, flexible, polite. Suspend line L1234 under Robert Davis's account due to reported issues. Then, get line details to confirm if line L1234 can be resumed within the 30-day suspension period. This will ensure that the service can be reinstated promptly if the issues are resolved within the allowable timeframe, maintaining customer satisfaction and operational efficiency.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC032", "phone_number": "L1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC032", "line_id": "L1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC032", "line_id": "L1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are polite, optimistic, independent, logical. Begin by verifying the identity of user James Brown using the email james.brown6693@email.com to ensure secure access to his account. Once his identity is confirmed, proceed to look up the customer account using the phone number associated with James Brown to access his account details. After retrieving the account information, retrieve all active lines for customer James Brown's account to review his current services and ensure everything is functioning optimally.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown6693@email.com", "user_id": "TC089"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "associated_phone_number", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are flexible, independent. First, verify the identity of user John Williams using the email john.williams4633@email.com for account access. Once his identity is confirmed, get the bill details for John Williams to verify any outstanding balance and the date of his last payment. If there is an outstanding balance, transfer to human agents to assist John Williams with payment processing and discuss potential payment plans.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"email": "john.williams4633@email.com"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are direct, polite. First, lookup_customer_by_phone with phone number '555-0123' to verify customer identity for Patricia Smith. Once verified, proceed to get_customer_lines for the customer ID associated with Patricia Smith to list all active lines. Finally, check the current plan and usage details by using get_line_details for line ID 'L456' to ensure the customer is informed before any further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC112"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC112", "user_id": "TC112"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC112"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are direct, independent. Suspend line L001 temporarily for user John Garcia based on recent request.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC018"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC018", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are polite, flexible. First, lookup_customer_by_phone with phone_number \"555-0123\" to verify identity for Mary Davis. Once verified, proceed to get_customer_lines for customer_id \"C8842\" to retrieve all active lines associated with Mary Davis. After identifying the relevant line, use get_line_details for line_id \"L1234\" to check the current plan and usage details. This sequence will ensure you have all the necessary information to assist Mary Davis effectively in managing her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC020"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC020", "user_id": "TC020"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234", "user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are patient, flexible, polite. \"lookup_customer_by_phone with phone_number='123-456-7890' to verify John Williams' account access\"",
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
        user_id="TC150",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are flexible, independent, logical. First, verify customer identity for user Linda Davis using email linda.davis8880@email.com before accessing account information. Once her identity is confirmed, lookup the customer by the phone number associated with Linda Davis to retrieve her account details. This process ensures that we maintain the security and confidentiality of Linda's account while providing her with accurate and efficient service.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Verify customer identity for Linda Davis using her email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once identity is confirmed, lookup customer by phone number to retrieve account details."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are logical, polite, organized. First, verify the identity of user Michael Davis using email michael.davis7894@email.com to ensure secure account access. Once the identity is confirmed, proceed to get the bill details for Michael Davis's account to review any outstanding charges and payment status. This process will help us provide accurate information regarding his telecom services and ensure that any necessary actions can be taken to maintain his account in good standing.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.davis7894@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC069"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are logical, organized. Lookup customer by phone number '555-1234' to verify identity for account access. Once verified, get customer lines for user John Garcia to review active services and ensure all services are functioning as expected. Then, get line details for line ID 'L789' to check the current plan and usage, and calculate remaining data for line ID 'L789' to determine if there is a need for a data refill, ensuring the customer has sufficient data for their usage patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "John Garcia", "user_id": "TC015"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789", "user_id": "TC015"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "subtract", "value1": "total_data", "value2": "used_data"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are direct, independent, logical, confident. Use lookup_customer_by_phone with phone number \"123-456-7890\" to verify John Garcia's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are direct, organized. First, get bill details for Mary Johnson's account to check the outstanding balance and due date. Once you have this information, inform Mary Johnson about the payment processing time frame and expected service resumption date. This will help her understand the urgency and timeline for resolving her account status with our telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC093"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Inform Mary Johnson about the payment processing time frame and expected service resumption date based on the bill details retrieved."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are polite, direct, independent. Verify customer identity using email jennifer.brown3820@email.com to access account details. Once verified, lookup customer by phone number associated with Jennifer Brown to retrieve the customer ID. With the obtained customer ID, get customer lines to identify active lines. This process is crucial for ensuring that Jennifer Brown's account is secure and up-to-date with her current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.brown3820@email.com", "user_id": "TC026"}
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
        user_id="TC056",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are direct, confident. lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Patricia Brown's account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are cautious, logical, patient, direct. Please begin by using the lookup_customer_by_phone task with phone_number='555-123-4567' to verify the identity of Patricia Johnson, who has reported a loss of her device. Once her identity is confirmed, proceed to suspend_line for line_id='L7890' to prevent unauthorized use of the device. After suspending the line, use the get_customer_lines task for customer_id='C6047' to confirm that the line suspension has been successfully processed. This sequence ensures the customer's account security and maintains accurate service records.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L7890", "user_id": "TC096"}
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
        user_id="TC141",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are patient, direct, confident, logical. lookup_customer_by_phone with phone number \"555-123-4567\" to verify customer identity for Linda Garcia",
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
        user_id="TC023",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are direct, organized, confident, optimistic. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify identity for Jennifer Smith. Once her identity is confirmed, proceed to get_line_details for line_id \"L1001\" to check her current plan and usage. After reviewing the usage details, think to determine if a plan upgrade is beneficial for Jennifer Smith based on her usage patterns and needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review Jennifer Smith's current plan and usage details to determine if a plan upgrade is beneficial based on her usage patterns and needs."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are flexible, independent, confident, logical. Lookup_customer_by_phone for Patricia Smith using the phone number associated with the account to retrieve the customer ID. Once you have the customer ID, proceed to Get_bill_details to review Patricia Smith's outstanding balance and payment history. This will provide you with the necessary information to understand her current billing situation before any further actions are taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number", "user_id": "TC113"}
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
        user_id="TC032",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are patient, organized, polite, cautious. First, lookup_customer_by_phone with \"phone_number\" as \"555-123-4567\" to verify customer identity for Robert Davis. Once the identity is confirmed, use the \"customer_id\" obtained from the previous step to get_customer_lines and list all active lines under Robert Davis's account. This will help ensure that all services are active and accounted for before proceeding with any further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC032"}
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
        user_id="TC056",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are patient, cautious, direct, independent. First, verify Patricia Brown's identity using her email patricia.brown8933@email.com to access her account. Once her identity is confirmed, retrieve her latest bill using her customer ID to get the billing details. After obtaining the billing details, calculate the total amount due for Patricia Brown's latest bill, including any late fees.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "First, I need to verify Patricia Brown's identity using her email to access her account."}
            ),
            Action(
                name="think",
                kwargs={"thought": "However, there is no direct tool available for identity verification using email. I will need to transfer this task to human agents for manual verification."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"reason": "Verify Patricia Brown's identity using her email patricia.brown8933@email.com to access her account."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Once Patricia Brown's identity is confirmed, I can retrieve her latest bill using her customer ID."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC056"}
            ),
            Action(
                name="think",
                kwargs={"thought": "After obtaining the billing details, calculate the total amount due for Patricia Brown's latest bill, including any late fees."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "latest_bill_amount + late_fees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are logical, confident. First, use lookup_customer_by_phone with phone number 555-123-4567 to verify Robert Jones's account identity. Once verified, retrieve customer account details using get_customer_lines for user ID U5323 to ensure all information is up-to-date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "U5323"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are cautious, optimistic, direct. lookup_customer_by_phone with phone_number '555-123-4567' to verify customer identity for Robert Williams",
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
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are patient, flexible. \"update plan for line_id 'L67890' to 'Unlimited Data Plan' effective next billing cycle\"",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC150"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC150", "reason": "Request to update plan to 'Unlimited Data Plan' for line_id 'L67890' effective next billing cycle"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are polite, cautious, flexible, optimistic. First, lookup customer by phone using Linda Smith's phone number to verify her identity. After successfully verifying her identity, proceed to get customer lines for Linda Smith. Once you have the customer lines, get line details for Linda Smith's primary line to check her current plan and usage. This sequence will help ensure that you have accurate information to assist Linda with any inquiries or potential upgrades for her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Smith's phone number", "user_id": "TC041"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC041", "user_id": "TC041"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Linda Smith's primary line ID", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are confident, patient, organized, polite. Verify the identity of user Robert Brown using his email (robert.brown4954@email.com) to ensure secure account access. Once his identity is confirmed, proceed to lookup_customer_by_phone using Robert Brown's phone number to retrieve his customer account information. This process is crucial for maintaining account security and providing personalized service in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number", "user_id": "TC129"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are cautious, patient, organized. Begin by looking up customer by phone number using Jennifer Davis's phone number to verify account access. Once access is confirmed, proceed to get customer lines for Jennifer Davis to identify active service lines associated with the account. This will help ensure that all active lines are accounted for and properly managed within our telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Davis's phone number", "user_id": "TC085"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are flexible, patient, organized, confident. First, lookup customer by email linda.smith7027@email.com to verify identity for account access. Once her identity is confirmed, get bill details for Linda Smith's account to review outstanding balance and payment history. This will help ensure that the information is accurate before proceeding to the next steps in resolving her billing inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.smith7027@email.com", "user_id": "TC041"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "linda.smith7027@email.com", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are optimistic, organized. Verify customer identity for John Johnson using email john.johnson9055@email.com to access account details, and then get_line_details for the primary line associated with John Johnson to view current service plan and usage. This will help ensure that you have the correct information to assist John with any inquiries about his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.johnson9055@email.com", "user_id": "TC001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"email": "john.johnson9055@email.com", "user_id": "TC001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are logical, direct. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Robert Brown's account, ensuring the account details are correct for any further actions. Next, get_bill_details for customer ID C001 to review recent charges and payments, focusing on identifying any patterns of high data usage that might suggest the need for a plan change. After reviewing the billing details and confirming high data usage, think about possible plan upgrades for customer ID C001 based on this usage pattern. If a suitable upgrade is identified or further assistance is needed, transfer_to_human_agents with context 'plan upgrade inquiry' for customer ID C001 to ensure Robert Brown receives personalized service and support.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC129"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC129", "user_id": "TC129"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "plan upgrade inquiry", "customer_id": "TC129", "user_id": "TC129"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are optimistic, confident, cautious. First, use the \"lookup_customer_by_phone\" task with the parameter phone_number=\"123-456-7890\" to verify the customer's identity. Once the customer is verified, proceed with the \"get_bill_details\" task using the parameters customer_id=\"C12345\" and billing_cycle=\"Oct 2023\" to view the current bill status. Finally, apply the \"think\" task to analyze the bill details and identify any overcharges or discrepancies, ensuring the customer is billed accurately for their telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC143", "billing_cycle": "Oct 2023"}
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
        user_id="TC018",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are flexible, direct, optimistic, polite. Retrieve all active phone lines associated with John Garcia's account and then find the current plan and usage details for each line. This information is crucial to ensure that John Garcia's account is optimized for his needs and to identify if any adjustments or upgrades are necessary.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC018", "customer_name": "John Garcia"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC018", "line_id": "line_001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC018", "line_id": "line_002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are flexible, independent, polite. Please begin by performing a lookup_customer_by_phone with phone number \"555-123-4567\" to verify the customer identity for Robert Williams. Once you have confirmed the identity, proceed to get_customer_lines for the customer ID obtained from the previous step to retrieve all active lines associated with Robert Williams. After identifying the active lines, get_bill_details for the same customer ID to review the latest billing statement and payment status. This will help ensure that all lines are accounted for and that Robert Williams is up to date with his payments.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC067"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC067", "user_id": "TC067"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC067", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are patient, polite, independent, confident. Lookup_customer_by_phone with phone number 555-1234 to verify Patricia Brown's account identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are confident, polite, optimistic. First, lookup_customer_by_phone with phone number 555-0123 to verify Michael Johnson's account. Once verified, proceed to get_customer_lines for customer ID C4265 to retrieve all active lines associated with Michael Johnson. After obtaining the active lines, use get_line_details for line ID L9876 to check current plan and usage details, and think to determine if current data usage exceeds 80% of the plan limit.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC134"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC134", "user_id": "TC134"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC134"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if current data usage exceeds 80% of the plan limit."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are cautious, independent, logical. First, lookup_customer_by_phone with phone number \"555-1234\" to verify the identity of Robert Johnson. Once his identity is confirmed, proceed to get_customer_lines for customer ID \"robert.johnson9087\" to list all active lines. This will help ensure that Robert's account is accurately managed and any service inquiries he has can be addressed efficiently.",
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
        user_id="TC080",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are logical, cautious, confident, polite. Begin by using the Lookup_customer_by_phone task to verify the identity and access the account of Robert Williams, ensuring you have the correct customer details. Once verified, proceed with the Get_customer_lines task to review the active lines associated with Robert Williams's account. After identifying the primary line, utilize the Get_line_details task to check the current plan and usage. This information will help you determine if Robert Williams might benefit from a different plan based on his current usage patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Williams's phone number", "user_id": "TC080"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC080", "user_id": "TC080"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Primary line ID", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are independent, logical, optimistic, organized. First, verify the identity of user Mary Brown using the email mary.brown4135@email.com to ensure that she is the authorized account holder. Once her identity is confirmed, proceed to retrieve all active customer lines for user Mary Brown. This will allow us to have a comprehensive understanding of her current services before taking further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.brown4135@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are organized, logical. First, lookup_customer_by_phone with phone_number: \"555-1234\" to verify identity and retrieve account information for user Robert Johnson. Once verified, proceed to get_customer_lines with customer_id: \"C9087\" to list all lines associated with Robert Johnson's account. Finally, if Robert Johnson requests it, suspend_line with line_id: \"L5678\" and reason: \"customer request\" to temporarily suspend service on the specified line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC072"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "reason": "customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are patient, direct. Get_bill_details for the current billing cycle to review charges and payment status for Jennifer Brown's account.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are organized, flexible. First, use lookup_customer_by_phone with phone number \"555-123-4567\" to verify Jennifer Johnson's account details, ensuring her information is up-to-date and accurate. Once verified, proceed to get_customer_lines for the user ID associated with Jennifer Johnson to retrieve a comprehensive list of her active lines, focusing on identifying any potential issues or discrepancies. Finally, for line ID \"L001,\" get_line_details to check the current plan and usage details, ensuring that the plan aligns with Jennifer's needs and usage patterns. This sequence will help in providing Jennifer with a seamless and efficient customer service experience, ensuring her account and service plan are optimized.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC149"}
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
        user_id="TC065",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are polite, patient, confident. First, perform a lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of user James Davis. Once verified, proceed to get_customer_lines with customer_id \"C6038\" to retrieve all active lines under James Davis's account. After identifying the specific line in question, use get_line_details with line_id \"L1023\" to check the current plan and usage details for that line. If the customer requests a temporary suspension of service, execute suspend_line with line_id \"L1023\" and reason \"requested by customer\" to ensure the line is suspended as per the customer's request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC065"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1023"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1023", "reason": "requested by customer"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are logical, flexible, independent. First, use lookup_customer_by_phone with phone number 555-1234 to retrieve customer details for Linda Davis. Once you have confirmed the details, proceed to verify the identity of Linda Davis using customer ID C5049 to ensure account access. This process is crucial for maintaining security and providing seamless service in our telecom operations.",
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
        user_id="TC120",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are confident, direct, optimistic. Verify customer identity for user Robert Brown using email robert.brown5816@email.com to access account details.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"reason": "Identity verification required for accessing account details for Robert Brown using email robert.brown5816@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are direct, logical, flexible. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Patricia Smith's account",
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
        user_id="TC138",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are cautious, organized, direct. First, verify customer identity using email mary.smith4137@email.com for account access to ensure you are working with the correct account. Once verified, lookup customer by phone number associated with Mary Smith to retrieve account details, which will provide you with the necessary information to proceed. Finally, get customer lines for the account associated with Mary Smith to list all active lines, ensuring you have a comprehensive view of the services she is currently using.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.smith4137@email.com", "user_id": "TC138"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "mary.smith4137@email.com", "user_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are independent, patient, organized, optimistic. First, lookup_customer_by_phone with phone number 555-0123 to verify identity for John Garcia. Once verified, proceed to get_customer_lines for customer ID C4063 to retrieve all active lines associated with John Garcia's account. After identifying the relevant line, get_line_details for line ID L7890 to check the current plan and usage. This sequence ensures that you have verified the customer's identity, accessed all necessary account information, and reviewed the specific line details to assist with any inquiries or issues related to their telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC018", "user_id": "TC018"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L7890", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are direct, independent. First, lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify Michael Williams' account access. Once verified, proceed to get_bill_details for customer_id: \"CUST789\" to review the outstanding balance, ensuring that any discrepancies are noted for further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC007"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC007", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are independent, logical, cautious. First, verify customer identity for Robert Brown using email robert.brown6285@email.com to access account details and confirm any recent requests. Next, suspend_line for Line ID L123 to temporarily halt service as requested by the customer, ensuring that all protocols for suspension are followed. Finally, think to determine if a payment is required to resume service for suspended Line ID L123, considering the terms of service and any outstanding balances that may need to be settled before reactivation.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "user_id": "TC036"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Determine if a payment is required to resume service for suspended Line ID L123, considering the terms of service and any outstanding balances."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are optimistic, direct, confident. Verify the identity of Linda Davis by confirming her email and phone number for account access. Once her identity is confirmed, use lookup_customer_by_phone with Linda Davis's phone number to retrieve her customer ID. With the customer ID, retrieve all active lines associated with it using get_customer_lines. This process ensures that Linda's account is secure and allows us to manage her telecom services efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda's phone number", "user_id": "TC048"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC048", "user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are logical, confident, independent, cautious. First, lookup_customer_by_phone with phone_number '555-1234' to verify identity of Michael Williams before accessing account details. Once verified, get_customer_lines for user_id 'MW1902' to retrieve all active lines associated with the account. After identifying the relevant line, get_line_details for line_id 'L5678' to check current plan and usage details, ensuring you have accurate information before proceeding with any plan changes.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "MW1902"}
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
        user_id="TC141",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are optimistic, direct. First, verify Linda Garcia's identity using her email linda.garcia2678@email.com to access her account. Once her identity is confirmed, proceed to get_bill_details for Linda Garcia's account to review the latest bill and payment status. This will ensure that you have accurate information to assist her with any billing inquiries she might have regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.garcia2678@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are confident, logical, cautious. First, lookup_customer_by_phone with phone number \"123-456-7890\" to verify identity for Mary Jones. Once verified, get_bill_details for the customer ID obtained from the previous task to review the current bill and payment status. If the bill is overdue and payment has not been made, proceed to suspend_line with line ID \"L002\" for the customer ID obtained from the previous task due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC147"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC147", "user_id": "TC147"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L002", "customer_id": "TC147", "user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are confident, cautious, organized, polite. lookup_customer_by_phone with phone_number '555-1234' to verify the identity of Robert Brown and retrieve customer ID",
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
        user_id="TC147",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are polite, logical, confident. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity for Mary Jones, ensuring her account details are accessed securely. Once verified, get_bill_details for the customer_id obtained from identity verification to review outstanding charges and payment history, providing a comprehensive overview of her current billing status. Finally, get_bill_details for the same customer_id to verify if her recent payment has been processed, ensuring all transactions are up-to-date and accurate.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC147"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are flexible, organized. First, lookup_customer_by_phone with phone_number \"555-0101\" to verify the identity of Patricia Johnson for account access. Once her identity is confirmed, proceed to get_bill_details for customer_id \"C123456\" to review her outstanding balance and last payment date. If the account shows non-payment issues, suspend_line for line_id \"L78910\" to temporarily suspend service on Patricia Johnson's primary line. This action ensures compliance with company policy while protecting against further service usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0101"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC096"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L78910", "user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are direct, confident, organized. lookup_customer_by_phone with phone_number=\"(555) 123-4567\" to verify Patricia Brown's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "(555) 123-4567", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are logical, organized, cautious, independent. \"lookup_customer_by_phone with phone_number '555-1234' to verify Patricia Brown's identity\"",
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
        user_id="TC001",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are confident, cautious. First, use lookup_customer_by_phone with phone number 555-0123 to retrieve the customer profile for John Johnson. Once you have retrieved the profile, verify the identity of John Johnson using the email john.johnson9055@email.com to proceed with account access. After successfully verifying the identity, use get_customer_lines with the customer ID retrieved from the profile to list all active lines under John Johnson's account. This sequence of actions will ensure you have the necessary information to assist John Johnson effectively with his telecom needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC001"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the identity of John Johnson using the email john.johnson9055@email.com after retrieving the customer profile."}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC001", "user_id": "TC001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are organized, flexible, optimistic, direct. First, lookup_customer_by_phone using the phone number associated with Linda Davis to verify her identity. Once verified, proceed to get_customer_lines for Linda Davis to retrieve all active lines on her account. This will help ensure that you have the correct line information before taking any further action. Then, if Linda confirms that her device is lost, suspend_line for line ID L12345 due to the reported loss. This sequence of actions will help maintain account security and prevent unauthorized use of the lost device.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Davis's phone number", "user_id": "TC107"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107", "user_id": "TC107"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "Lost device", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are optimistic, direct, confident, independent. Please lookup_customer_by_phone with phone_number \"555-0123\" to verify Patricia Smith's identity, ensuring that we are addressing the correct account holder. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"C8398\" to view her active lines. This will help us provide Patricia with accurate information regarding her current telecom services and assist her with any inquiries she may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC112"}
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
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are direct, cautious, flexible. \"get_line_details with line_id=L5678 to check current data plan and usage for Michael Smith\"",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are cautious, polite, logical, optimistic. Get_customer_lines for Michael Davis to list all active and suspended lines on the account",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC069", "customer_name": "Michael Davis"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are flexible, organized. First, lookup_customer_by_phone(phone_number=\"555-1234\") to verify Mary Smith's identity as she has requested assistance with her mobile services. Once her identity is confirmed, proceed to suspend_line(line_id=\"LINE5678\", reason=\"Customer request\") to temporarily suspend her line as per her request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE5678", "reason": "Customer request", "user_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are independent, polite, confident, logical. Verify customer identity using email james.brown6693@email.com for account access to ensure secure handling of his account information. Once verified, proceed to Get_customer_lines for the verified customer account to list all active lines associated with James's account, as this will help in understanding the scope of his services. Finally, Get_line_details for line ID L123 to check current plan and usage, allowing you to assess if the current plan meets James's needs based on his usage details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown6693@email.com", "user_id": "TC089"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "james.brown6693@email.com", "user_id": "TC089"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are organized, independent. Get_line_details for line ID L67890 to confirm eligibility for a plan upgrade requested by the customer.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are optimistic, independent. First, lookup_customer_by_phone using Patricia Johnson's phone number to retrieve her account details. Once you have confirmed her identity by verifying account-specific information such as her billing address or the last four digits of her payment method on file, proceed to get_bill_details for Patricia Johnson to review her current billing statement and past payments. This will ensure that Patricia receives the most accurate and up-to-date information regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Johnson's phone number", "user_id": "TC096"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC096", "user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are optimistic, confident, cautious, organized. Get bill details for account ID C102938 to determine outstanding payment amount",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "C102938", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are organized, direct, patient, logical. First, lookup_customer_by_phone with the phone number associated with Jennifer Davis to verify her identity. Once verified, proceed to get_customer_lines for Jennifer Davis to retrieve all her active lines. After obtaining the active lines, get_bill_details for Jennifer Davis to review her current billing status and any outstanding payments. This sequence ensures that you have a comprehensive understanding of Jennifer Davis's account status, which is crucial for addressing any billing inquiries she may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Davis's phone number", "user_id": "TC148"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC148", "user_id": "TC148"}
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
        user_id="TC104",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are cautious, flexible. First, lookup_customer_by_phone with phone_number '555-0123' to verify John Miller's account access. Once verified, get_bill_details for customer_id 'C12345' to review his outstanding balance. If the outstanding bill exceeds the threshold, proceed to suspend_line for line_id 'L98765' due to non-payment, ensuring compliance with telecom regulations and maintaining customer communication.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC104"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC104", "user_id": "TC104"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L98765", "user_id": "TC104"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are polite, organized, logical. First, verify the identity of user Robert Jones using the email robert.jones1563@email.com to ensure secure account access. Once verified, lookup the customer by the phone number associated with the email robert.jones1563@email.com to retrieve the customer ID. After obtaining the customer ID, get the customer lines for Robert Jones to list all active lines, ensuring you have a comprehensive understanding of the account's current status and services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones1563@email.com", "user_id": "TC144"}
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
        user_id="TC072",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are direct, polite, patient. Lookup_customer_by_phone with phone number 555-0123 to verify identity for Robert Johnson.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are patient, logical, organized. lookup_customer_by_phone(phone_number=\"555-0123\") to verify identity and access account",
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
        user_id="TC120",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are logical, organized, flexible, polite. Verify the identity of Robert Brown using robert.brown5816@email.com for account access. Once his identity is confirmed, get the bill details for Robert Brown to review his outstanding balance and payment history. This will ensure that he is aware of any pending payments and can take necessary actions to maintain his telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"email": "robert.brown5816@email.com", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are polite, logical, patient. \"lookup_customer_by_phone with phone number 555-123-4567 to verify Patricia Brown's identity before accessing account details\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are organized, cautious, optimistic. Get the current bill details for Patricia Johnson's account to review charges and any outstanding balances.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC096", "customer_name": "Patricia Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are optimistic, polite. lookup_customer_by_phone with phone number 555-123-4567 to verify identity for Linda Davis",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are optimistic, independent, direct, patient. Verify the identity of user John Williams using the email john.williams8933@email.com to ensure account security. Once verified, use the phone number associated with John Williams to lookup the customer ID, which is crucial for accessing account details. With the customer ID in hand, retrieve all active lines associated with the account to assess the current telecom services being utilized.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.williams8933@email.com", "user_id": "TC098"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC098", "user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are polite, flexible, patient. First, use the lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Linda Johnson's identity, ensuring that you are assisting the correct customer. Once her identity is confirmed, proceed to get_customer_lines for user \"Linda Johnson\" to identify all active lines on her account. This will help you provide accurate information about her current services and assist with any inquiries she may have about her telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC060", "user": "Linda Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are flexible, cautious, logical. First, lookup customer by phone number 555-1234 to verify identity for Robert Jones. Once verified, get bill details for account ID 12345 to verify current balance and payment history. After confirming the account status and identifying any outstanding amounts, calculate the total amount due for account ID 12345, including any late fees.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC144"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "12345", "user_id": "TC144"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["current_balance", "late_fees"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC094",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are organized, logical, confident. First, verify the identity of Patricia Brown using the email patricia.brown6169@email.com to ensure secure account access. Once her identity is confirmed, proceed to get the bill details for Patricia Brown so she can review her outstanding balance and payment history. This process is crucial in assisting her with any potential billing discrepancies or questions regarding her telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"email": "patricia.brown6169@email.com", "user_id": "TC094"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are optimistic, confident, direct. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify customer identity for Jennifer Williams",
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
        user_id="TC069",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are logical, direct, confident, optimistic. lookup_customer_by_phone with phone_number = \"+18005551234\" to verify identity for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+18005551234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are organized, confident, patient, direct. Suspend line L123 if there is a reported issue and confirm suspension status.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC016", "line_id": "L123"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC016", "line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are patient, independent. First, lookup_customer_by_phone with phone number associated with Robert Jones to verify identity. Once verified, get_customer_lines for the account associated with Robert Jones to list all active lines. Then, for one of the active lines, specifically line ID L1234, suggest plan upgrade options to Robert Jones, highlighting benefits and cost differences, to ensure he is aware of potential improvements to his current service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated with Robert Jones", "user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC144", "user_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are organized, independent, polite, optimistic. First, lookup_customer_by_phone using phone number 555-1234 to verify identity for John Davis. Once verified, get_bill_details for customer ID 12345 to review outstanding balance and payment history. If there is an outstanding balance, suspend_line for line ID 67890 due to non-payment, ensuring customer is aware of the 30-day resumption policy.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC074"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC074", "user_id": "TC074"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "67890", "user_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are direct, patient, logical, polite. First, verify customer identity for Robert Brown using email robert.brown6285@email.com to access account details. Once verified, get bill details for Robert Brown's account to verify outstanding balance and payment status. Finally, process payment for the outstanding balance using the payment method on file for Robert Brown.",
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
                name="transfer_to_human_agents",
                kwargs={"reason": "Process payment for outstanding balance", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are independent, direct, cautious. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Robert Jones' identity. Once verified, proceed to get_customer_lines for customer_id \"C12345\" to retrieve all active lines for Robert Jones. After identifying the primary line, use get_line_details for line_id \"L67890\" to check current plan and usage details. If everything matches and Robert confirms a reported loss, proceed to suspend_line for line_id \"L67890\" to temporarily suspend service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC144"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are cautious, flexible, logical. Suspend_line for line L001 on Patricia Johnson's account due to request for temporary suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC096", "email": "linda.johnson5357@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC096"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC096", "line_id": "L001"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC096", "line_id": "L001", "reason": "Temporary suspension requested"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are patient, direct, confident, cautious. First, verify customer identity for Jennifer Davis using email jennifer.davis4933@email.com before accessing account details. Once her identity is confirmed, proceed to lookup_customer_by_phone using Jennifer Davis's verified phone number to retrieve her customer account information. After obtaining the account details, get_customer_lines for Jennifer Davis to list all active and suspended lines associated with her account. This process ensures that you have a comprehensive view of her telecom services, allowing you to manage her account effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.davis4933@email.com", "user_id": "TC148"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "verified_phone_number", "user_id": "TC148"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are direct, confident, organized. First, lookup_customer_by_phone with phone_number = \"Michael Davis's verified phone number\" to retrieve the customer ID. Next, use the retrieved customer ID to get_customer_lines and list all active lines associated with Michael. Then, for each line, get_line_details with line_id = \"specific line ID from customer lines\" to check the current plan and usage. Finally, think to determine if the current plan meets Michael's usage needs, ensuring he has the most suitable plan for his telecom requirements.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Davis's verified phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC069"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "specific_line_id_from_customer_lines"}
            ),
            Action(
                name="think",
                kwargs={"task": "Determine if the current plan meets Michael's usage needs"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are organized, direct. Calculate the cost of upgrading Jennifer Smith's plan to include unlimited data for line ID L234",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC023", "phone_number": "L234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC023"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC023", "line_id": "L234"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC023", "line_id": "L234", "plan_change": "unlimited_data"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are flexible, optimistic, direct. Lookup_customer_by_phone with phone number 555-123-4567 to verify Linda Davis's identity and access her account information.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are optimistic, flexible, direct, polite. First, lookup_customer_by_phone with phone number 555-123-4567 to verify identity and retrieve account information for Mary Miller. Once her identity is confirmed, proceed to get_customer_lines for user Mary Miller to list all active lines associated with her account. This will help ensure that we have the correct information to assist her with any inquiries she may have about her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Mary Miller", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Mary Miller and your email is mary.miller8461@email.com. You are cautious, organized. lookup_customer_by_phone with phone_number '555-123-4567' to verify identity of Robert Brown",
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
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are optimistic, logical. Suspend line with Line ID L456 for temporary deactivation, ensuring suspension rules are followed.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC016", "line_id": "L456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are flexible, cautious, polite, optimistic. lookup_customer_by_phone with parameter: phone_number=123-456-7890 to verify customer identity for Robert Johnson",
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
        user_id="TC150",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are cautious, patient, confident, polite. First, verify the identity of user Linda Davis using her email linda.davis8880@email.com before accessing her account details. Once her identity is confirmed, use her verified phone number to retrieve her customer ID by executing the lookup_customer_by_phone task. With Linda's customer ID in hand, proceed to execute the get_customer_lines task to list all active lines on her account. This sequence ensures that Linda's information is handled securely and efficiently, allowing you to assist her with any inquiries regarding her telecom services.",
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
        user_id="TC091",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are confident, patient, flexible. First, verify customer identity for Linda Miller using email linda.miller7970@email.com to access account information. Once her identity is confirmed, calculate potential costs for upgrading line L001 to a premium plan starting next billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.miller7970@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC091"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC091"}
            ),
            Action(
                name="calculate",
                kwargs={"line_id": "L001", "plan_type": "premium", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are independent, logical, polite. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify identity of user Linda Davis",
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
        user_id="TC028",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are cautious, flexible. First, verify identity for customer Patricia Miller using email patricia.miller3252@email.com to access account details, ensuring that all security protocols are followed strictly. Once her identity is confirmed, get_bill_details for Patricia Miller to review her current billing statement and outstanding balance, identifying any overdue amounts. If there is an outstanding balance that has not been paid, proceed to suspend_line for line ID L12345 due to non-payment, making sure to inform Patricia Miller of the 30-day resumption policy, so she is aware of the steps needed to resume service.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"email": "patricia.miller3252@email.com", "user_id": "TC028"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "non-payment", "user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are flexible, independent, logical. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of John Davis, ensuring you are addressing the correct account holder. Once verified, proceed to get_line_details for line_id \"L123\" to check the current plan and usage, providing a comprehensive understanding of the customer's service status. Finally, if the customer requests, suspend_line for line_id \"L123\" with reason \"customer request\" to pause their service temporarily, ensuring all actions align with the customer's needs and company policies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "reason": "customer request", "user_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are polite, direct. First, use lookup_customer_by_phone with phone number 555-123-4567 to verify Linda Davis's account. Once the account is verified, retrieve account details for Linda Davis using get_customer_lines with the verified account information. This will help ensure that we have the correct details before proceeding with any changes or updates to her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC035"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_info": "Linda Davis", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are patient, organized, polite, confident. get_bill_details for customer \"Jennifer Jones\" to review outstanding balance and payment history",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_name": "Jennifer Jones", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are direct, cautious, patient. First, lookup_customer_by_phone with phone number 555-123-4567 to verify Robert Williams' account identity, ensuring that we are addressing the correct account. Once verified, proceed to get_bill_details for customer ID C3951 to review the outstanding balance and payment history, which will provide insight into any missed payments or discrepancies. Finally, calculate total amount due including late fees for customer ID C3951 to determine the exact amount Robert Williams needs to settle, ensuring all fees are accounted for before proceeding to further action.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC080"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC080", "user_id": "TC080"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "total_amount_due", "customer_id": "TC080", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are independent, confident. Verify the identity of Patricia Smith using her email patricia.smith8398@email.com to access her account details. Once verified, get the bill details for the current billing period on Patricia Smith's account using her customer ID to ensure accurate billing information for our telecom services.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"email": "patricia.smith8398@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC112"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are optimistic, organized, direct, flexible. lookup_customer_by_phone with phone_number=555-1234 to verify identity of John Garcia",
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
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are direct, polite, patient. \"lookup_customer_by_phone with phone_number '555-1234' to verify identity for Mary Miller\"",
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
        user_id="TC139",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are flexible, logical. First, lookup_customer_by_phone with phone_number '123-456-7890' to verify Michael Smith's identity. Once verified, get_line_details for line_id 'LINE123' to check the current plan and data usage. Based on this information, calculate estimated charges for a plan change on line_id 'LINE123' for the next billing cycle to assist Michael Smith in making an informed decision about upgrading his plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE123"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "estimate_plan_change_charges", "line_id": "LINE123", "user_id": "TC139"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are confident, cautious, independent, polite. First, verify customer identity for user John Garcia using email john.garcia4063@email.com to ensure secure account access. Once identity verification is complete, proceed to suspend line ID L12345 for John Garcia due to the reported loss of his device. This sequence ensures that the customer's account is protected before taking action on the reported issue.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia4063@email.com", "user_id": "TC018"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are direct, polite. \"lookup_customer_by_phone\" with parameter phone_number: \"555-123-4567\" to verify user identity for Robert Williams.",
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
        user_id="TC085",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are cautious, optimistic, direct, polite. Verify identity for user Jennifer Davis using email jennifer.davis3568@email.com to access account details. Once her identity is confirmed, get bill details for customer ID to review recent charges and payments. This will help ensure that Jennifer's account is secure and that she is informed about her current financial obligations with our telecom service.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC085"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are optimistic, cautious, confident. First, lookup customer by phone using phone number 123-456-7890 to verify identity for Robert Jones. Once verified, get customer lines for user ID U3449 to view all active lines. After identifying the relevant line, get line details for line ID L5678 to check the current plan and usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC109"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "U3449"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC109"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are direct, flexible, organized. Use lookup_customer_by_phone to retrieve customer ID for Linda Garcia using phone number 555-1234, then get_customer_lines using Linda Garcia's customer ID to retrieve all active lines on her account. This will help us ensure that all her active lines are correctly set up and identify any discrepancies in her account for a seamless telecom service experience.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC141", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are confident, logical. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of Linda Davis. Once verified, get_bill_details for account ID A3121 to review the latest billing statement, ensuring all charges are accurate and there are no discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC035"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A3121", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are polite, patient, confident, cautious. Suspend line L9876 for Robert Brown due to a request for temporary hold",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC073", "line_id": "L9876", "reason": "Temporary hold request by Robert Brown"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are confident, logical, direct, patient. Resume suspended line L456 for customer ID C789 within 30-day window by confirming payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC108", "phone": "customer_phone_number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC108", "customer_id": "TC108"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC108", "line_id": "L456"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC108", "customer_id": "TC108"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC108", "line_id": "L456", "action": "resume"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are independent, cautious. First, lookup_customer_by_phone with phone number 555-0123 to verify identity for Robert Brown. Once verified, proceed to get_customer_lines for customer ID C987 to retrieve all active lines associated with Robert Brown. Finally, get_line_details for line ID L456 to check the current plan and usage for Robert Brown, ensuring you have the necessary information to assess if the current plan meets his usage needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC036"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC036", "user_id": "TC036"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are optimistic, confident, independent. Please suspend the line with line_id L9876 for the reason \"customer request.\" After suspending the line, get the line details for line_id L9876 to confirm the suspension status. This sequence ensures that the customer's request is fulfilled accurately and that the line is successfully suspended in the system.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "reason": "customer request", "user_id": "TC133"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are independent, cautious. suspend_line with line_id \"L98765\" and suspension_reason \"customer_request\" to pause services temporarily",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC015", "line_id": "L98765", "suspension_reason": "customer_request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are confident, logical, optimistic. lookup_customer_by_phone with phone_number \"555-0123\" to verify identity of Mary Brown",
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
        user_id="TC062",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are cautious, polite, confident, direct. Suspend_line for line ID L12345 on Jennifer Brown's account due to a customer request for temporary suspension.",
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
                kwargs={"user_id": "TC062", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC062", "line_id": "L12345", "reason": "Customer request for temporary suspension"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are independent, cautious, confident. lookup_customer_by_phone(phone_number='123-456-7890') to verify the identity of James Brown",
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
        user_id="TC035",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are direct, flexible, polite, logical. First, verify the identity of user Linda Davis using her email linda.davis3121@email.com to ensure secure account access. Once her identity is confirmed, lookup Linda Davis by the phone number associated with her account to retrieve her customer ID. Finally, use this customer ID to get customer lines for Linda Davis and list all active lines associated with her account. This sequence ensures that Linda Davis's account information is accessed securely and efficiently, allowing for accurate management of her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis3121@email.com", "user_id": "TC035"}
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
        user_id="TC092",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are organized, flexible. First, perform a lookup_customer_by_phone using the phone number associated with Patricia Williams to verify her identity. Once her identity is confirmed, use the customer ID obtained to get_customer_lines and list all active lines under her account. This will help in managing her services efficiently and ensure that Patricia's request is handled accurately.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Williams' phone number", "user_id": "TC092"}
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
        user_id="TC106",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are confident, direct, flexible. Lookup_customer_by_phone for James Jones to obtain associated customer ID and account information.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC106", "customer_name": "James Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are polite, cautious. First, lookup_customer_by_phone with phone_number: \"555-0123\" to verify Michael Jones' account. Once verified, proceed to get_bill_details for customer_id: \"CUST-2722\" to review any outstanding payments. If you find that there are overdue payments, prepare to take appropriate action by suspending the line with line_id: \"LINE-12345\" due to non-payment, ensuring you follow company policy and notify the customer of the suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC083"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC083", "user_id": "TC083"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE-12345", "reason": "Non-payment", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are logical, direct, organized. First, lookup_customer_by_phone with phone number \"123-456-7890\" to verify identity and retrieve customer ID for Jennifer Jones. Once you have the customer ID, proceed to get_customer_lines with the retrieved customer ID to list all active lines under Jennifer Jones's account. This will help ensure that all lines are correctly associated with her account before any further account management or billing inquiries.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC130"}
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
        user_id="TC018",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are confident, polite, direct, independent. First, verify customer identity for John Garcia using email john.garcia4063@email.com to access account details. Once verified, retrieve customer account information for John Garcia by looking up the phone number associated with the email john.garcia4063@email.com. Then, get all active lines for John Garcia's account using the retrieved customer phone number. This sequence ensures that you have the correct and complete account information needed to assist John Garcia effectively with his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia4063@email.com", "user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "retrieved_phone_number", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are logical, patient, independent, confident. Begin by verifying if Mary Jones is eligible for a plan upgrade by reviewing her current plan details and usage. Once eligibility is confirmed, proceed to process the plan change request for Mary Jones to upgrade to plan P1234, effective next billing cycle. Ensure all steps are completed in sequence to maintain a smooth transition for the customer in the telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC013", "phone_number": "unknown"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC013"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC013", "line_id": "line_id_for_mary_jones"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC013", "line_id": "line_id_for_mary_jones"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if Mary Jones is eligible for a plan upgrade based on current plan details and usage."}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "eligibility_criteria_expression"}
            ),
            Action(
                name="think",
                kwargs={"thought": "If eligible, proceed to process the plan change request for Mary Jones to upgrade to plan P1234."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC013", "line_id": "line_id_for_mary_jones", "new_plan_id": "P1234", "effective_date": "next_billing_cycle"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are logical, patient, direct. First, lookup_customer_by_phone with phone number 555-0123 to verify James Davis's account. Once verified, proceed to suspend_line for line ID L001 due to a request from James Davis. After suspending the line, get_line_details for line ID L001 to confirm the suspension status. This sequence ensures that James Davis's request is accurately processed and documented in the system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC065"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "user_id": "TC065"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are organized, optimistic, flexible, logical. Begin by verifying the customer identity using the email linda.davis5049@email.com. Once the email is verified, proceed to lookup the customer account using the verified email to retrieve the customer ID. With the customer ID obtained, get the customer lines to list all active phone lines associated with the account. This process will help ensure that we have accurate and up-to-date information on the customer's active services, which is crucial for providing effective support and service management in the telecom industry.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are cautious, logical. Get_customer_lines for John Johnson’s account to list all active lines",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC001", "customer_name": "John Johnson"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC001", "customer_name": "John Johnson"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are patient, direct. lookup_customer_by_phone with phone number 555-0123 to verify account access for Robert Brown",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are independent, polite, flexible. First, verify customer identity for Michael Jones using email michael.jones4016@email.com to access account information. Once verified, proceed to get_customer_lines for Michael Jones to retrieve all active lines on the account. This will ensure you have the necessary information to assist him with any inquiries related to his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.jones4016@email.com", "user_id": "TC042"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "michael.jones4016@email.com", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are independent, logical, flexible. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of user James Jones, who has reported a lost phone. After confirming his identity, get_line_details for line ID L123 to check the current plan and usage, ensuring that there are no outstanding issues or overages. Finally, suspend_line for line ID L123 due to the reported lost phone to prevent unauthorized usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC106"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC106"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "reason": "lost phone", "user_id": "TC106"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are organized, confident, flexible, polite. First, verify the identity of user Robert Williams by confirming his email robert.williams3479@email.com before granting him account access. Once his identity is confirmed, proceed to lookup the customer by phone using the phone number associated with Robert Williams to retrieve his customer account information. After accessing the account, get the customer lines for Robert Williams to list all active telecom lines under his account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC006", "email": "robert.williams3479@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC006", "phone_number": "associated_phone_number"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are cautious, organized, optimistic, confident. First, verify the identity of user Robert Brown using the email robert.brown4015@email.com to ensure you are accessing the correct account. Once his identity is confirmed, proceed to get the bill details for Robert Brown's account to check the outstanding balance. This sequence ensures that you have the necessary information to address any billing issues effectively and maintain proper communication with the customer.",
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
        user_id="TC148",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are logical, cautious, flexible, independent. First, lookup_customer_by_phone with phone_number 555-123-4567 to verify Jennifer Davis's identity as part of a routine security check. Once her identity is confirmed, proceed to get_customer_lines for customer_id C4933 to retrieve all active lines associated with her account. This will ensure that all her account details are up-to-date and help in managing her telecom services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC148"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC148", "user_id": "TC148"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are logical, flexible, independent, polite. First, verify customer identity using email james.brown3113@email.com for account access to ensure the correct account is being managed. Once verified, suspend line ID L789 due to non-payment and notify the customer via email about the suspension and the steps needed to resolve the issue. After receiving payment confirmation within 30 days, resume line ID L789 promptly to restore the customer's service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown3113@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC145", "line_id": "L789"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC145", "message": "Notify customer via email about the suspension of line ID L789 due to non-payment and provide steps to resolve the issue."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are cautious, patient. First, lookup_customer_by_phone with phone_number \"555-0123\" to verify the identity of Jennifer Davis. Once her identity is confirmed, proceed to get_customer_lines for user_id \"jennifer.davis4933@email.com\" to retrieve all active lines associated with her account. After identifying her primary line, use get_line_details for line_id \"L789\" to check the current plan details. This will allow you to assist Jennifer in understanding her current plan and explore potential upgrades or changes.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "jennifer.davis4933@email.com"}
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
        user_id="TC141",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are logical, direct, polite. Suspend_line for line ID L5678 temporarily due to reported loss of device.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC141", "line_id": "L5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC040",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are independent, flexible. Begin by verifying Patricia Brown's identity by confirming her email patricia.brown2967@email.com and any additional required security questions. Once her identity is verified, proceed to lookup Patricia Brown's customer account using her verified phone number. After accessing her account, get the billing details for Patricia Brown's account to review outstanding balances and payment history. This information will help ensure Patricia is informed about her current financial obligations and assist in any further discussions regarding her account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "verified_phone_number", "user_id": "TC040"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC040", "user_id": "TC040"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is James Brown and your email is james.brown6693@email.com. You are confident, independent, patient, flexible. First, verify customer identity for Linda Miller using her email linda.miller1663@email.com before accessing account details. Once her identity is confirmed, lookup_customer_by_phone using Linda Miller's registered phone number to retrieve her customer ID. With the customer ID obtained, get_customer_lines for Linda Miller's account to list all active lines. This sequence ensures secure and efficient handling of customer information in the telecom sector.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.miller1663@email.com", "user_id": "TC019"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC019", "user_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are optimistic, cautious, direct. Use lookup_customer_by_phone with parameter phone=\"Robert Jones's registered phone number\" to verify customer identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "Robert Jones's registered phone number"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are cautious, independent, optimistic, patient. Please begin by performing a lookup_customer_by_phone with phone_number \"555-0123\" to verify the identity of Jennifer Davis. Once her identity is confirmed, proceed to get_bill_details for the customer_id retrieved from the lookup to review any outstanding balance she may have. This process is essential to ensure that Jennifer's account is accurately assessed for any overdue payments, which is crucial for maintaining her service with our telecom company.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC148"}
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
        user_id="TC148",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are confident, patient, optimistic, logical. First, lookup the customer by phone using the phone number provided by Jennifer Davis, such as 555-123-4567, to verify their identity. Once the customer's identity is confirmed, proceed to get customer lines for Jennifer Davis to list all active lines. After identifying the active lines, focus on line ID L98765 to check its current plan and usage details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC148"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC148", "user_id": "TC148"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L98765", "user_id": "TC148"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are cautious, patient. lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity of Robert Williams",
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
        user_id="TC123",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are confident, optimistic. First, use the get_bill_details for customer ID to retrieve the latest billing information and outstanding balance. Once you have confirmed the outstanding balance, proceed to transfer_to_human_agents for payment arrangement setup for the same customer ID to ensure the balance is managed effectively.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC123"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC123", "reason": "Payment arrangement setup"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Jennifer Johnson and your email is jennifer.johnson5907@email.com. You are confident, patient, flexible. First, get_line_details for line_id='L456' to check the current plan and usage. Then, think to determine if the current plan meets the user's needs based on their usage. This will help you provide a tailored recommendation to the customer regarding their telecom plan.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Review the current plan and usage details to determine if it meets Jennifer Johnson's needs based on her confidence, patience, and flexibility."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are optimistic, patient, polite. First, lookup the customer by email (jennifer.smith8259@email.com) to retrieve the customer ID and verify her identity. Once you have confirmed her identity, proceed to get the customer lines for the user ID retrieved from the previous lookup to understand her current services. Finally, get the line details for the line ID retrieved from the customer lines to check her current plan and usage. This will allow you to assess her needs accurately and suggest an upgrade if her current usage indicates that she would benefit from a different plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.smith8259@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC143"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "line_id_retrieved_from_previous_call"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are logical, independent, cautious, direct. get_line_details for line ID L1001 to check the current plan and usage",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1001", "user_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are logical, cautious, independent, patient. Lookup customer by phone number to retrieve customer ID and associated account details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are direct, flexible, patient, confident. First, check the billing details for Robert Brown's account to identify any outstanding payments. Once you have verified the billing details, process a payment of $100 for Robert Brown's account, noting that it may take 1-2 business days to reflect. This process is crucial for maintaining Robert's telecom services without interruption.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC029", "customer_name": "Robert Brown"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Check if there are any outstanding payments for Robert Brown's account."}
            ),
            Action(
                name="calculate",
                kwargs={"amount_due": 100, "payment_amount": 100}
            ),
            Action(
                name="think",
                kwargs={"thought": "Process a payment of $100 for Robert Brown's account."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are logical, optimistic. First, get the bill details for Patricia Miller's account to review the latest bill and outstanding balance. Then, calculate the total amount due, including any late fees or additional charges for Patricia Miller's account, to ensure accurate billing information is available for her telecom services.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC028"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are organized, direct. Process a plan change request for line ID L7890, effective the next billing cycle, ensuring Robert Williams is aware of changes.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC006"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC006", "line_id": "L7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are independent, organized, patient, confident. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify identity of Michael Davis. Once verified, get_customer_lines for customer_id 'C9122' to list all active lines associated with your account. After identifying the specific line you wish to manage, get_line_details for line_id 'L7890' to check the current plan and usage details. If you decide to temporarily pause the service for this line, proceed to suspend_line for line_id 'L7890' with reason 'customer request' to ensure the service is paused as per your needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC136"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L7890"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L7890", "reason": "customer request", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are patient, optimistic, cautious, independent. Get_bill_details for Patricia Miller's account to review the latest billing statement and payment status.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are confident, logical. First, lookup_customer_by_phone with phone_number '555-0123' to verify Robert Jones's account. Once verified, proceed to get_bill_details for customer_id 'C6549' to check the outstanding balance and billing history. This will help ensure that Robert Jones's account is up-to-date and any discrepancies can be addressed promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC119"}
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
        user_id="TC065",
        instruction="Your name is Michael Jones and your email is michael.jones2722@email.com. You are independent, organized, optimistic. First, lookup_customer_by_phone for phone number 555-1234 to verify identity. Once the customer's identity is verified, proceed to get_customer_lines for customer ID C001 to review their current active lines and ensure all details are up-to-date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC065"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC065", "user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are confident, cautious, flexible. Suspend_line for line ID L12345 to temporarily deactivate service due to customer request",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC106", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are organized, logical. First, lookup the customer by phone using the parameters: phone_number=\"555-123-4567\" and user_email=\"linda.davis8880@email.com\". Once you have confirmed the customer details, proceed to suspend the specific line with the parameters: line_id=\"LINE67890\" and reason=\"User Request\". This sequence ensures that the correct customer is identified before taking action to suspend the line as per their request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_email": "linda.davis8880@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE67890", "reason": "User Request", "user_id": "TC150"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is Mary Miller and your email is mary.miller8461@email.com. You are flexible, confident, direct, organized. First, lookup_customer_by_phone with phone number 555-0123 to verify identity for Robert Garcia. Once his identity is confirmed, proceed to suspend_line for line ID L102 due to reported loss or theft. After suspending the line, lookup_customer_by_phone with phone number 555-0123 to confirm the suspended line status. These steps ensure that the customer's account is secure and that the suspension has been successfully processed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC046"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L102", "user_id": "TC046"}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC046"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are optimistic, independent, cautious. First, lookup_customer_by_phone using phone number 555-0123 to verify Patricia Brown's account. Once Patricia's account is successfully verified, proceed to get_customer_lines for customer ID C001 to identify all active lines under her account. After identifying the lines, focus on get_line_details for line ID L123 to check the current plan and usage. This sequence will help ensure that Patricia's account details are accurate and up-to-date, allowing for efficient management of her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC056"}
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
        user_id="TC065",
        instruction="Your name is Mary Miller and your email is mary.miller8461@email.com. You are direct, confident. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify customer identity for user James Davis",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Robert Williams and your email is robert.williams3951@email.com. You are confident, cautious. lookup_customer_by_phone with phone_number \"123-456-7890\" to verify identity for Linda Garcia",
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
        user_id="TC048",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are optimistic, patient, polite, confident. A customer has reported an issue with their phone line and needs assistance. First, use the lookup_customer_by_phone(phone_number=\"123-456-7890\") to find the customer's ID. Once you have the customer ID, proceed to get_customer_lines(customer_id=\"C1234\") to identify all active lines associated with the account. After identifying the specific line in question, use get_line_details(line_id=\"L5678\", customer_id=\"C1234\") to gather detailed information about the line's status and recent activity. If the line needs to be temporarily suspended due to the issue, execute suspend_line(line_id=\"L5678\", customer_id=\"C1234\") to pause service while the problem is being resolved.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC048"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "customer_id": "TC048"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "customer_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are optimistic, independent, organized. lookup_customer_by_phone with phone number 555-1234 to verify identity for account access",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are flexible, polite. First, lookup_customer_by_phone with phone number 555-1234 to verify customer identity for Linda Miller. Once her identity is confirmed, get_bill_details for customer ID C102 to review her current billing statement, ensuring you have all necessary information before proceeding to assist her further.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC019"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC019", "user_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are independent, polite, logical. First, lookup_customer_by_phone with phone_number 123-456-7890 to verify identity for Robert Brown. Once identity is confirmed, get_line_details for line_id L12345 to check current plan and usage. This will help determine if Robert Brown's current plan meets his needs or if adjustments are necessary to optimize his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC029"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC067",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are cautious, independent, polite, optimistic. Begin by verifying the identity of user Robert Williams using his email robert.williams8770@email.com to ensure secure access to his account. Once his identity is confirmed, proceed to look up the customer by the phone number associated with Robert Williams to gather relevant account information. Finally, retrieve all customer lines for Robert Williams' account to provide a comprehensive overview of his telecom services and ensure all lines are accounted for and correctly linked to his profile.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.williams8770@email.com", "user_id": "TC067"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "robert.williams8770@email.com", "user_id": "TC067"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are logical, optimistic. suspend_line for line ID 5678 to temporarily halt service upon customer request",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC069", "line_id": "5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are optimistic, cautious, organized. First, verify customer identity using email robert.jones6549@email.com for account access to ensure secure handling of sensitive information. Once verified, proceed to lookup_customer_by_phone to retrieve account details for Robert Jones using the phone number associated with his account, as this will provide a comprehensive view of his account status. Finally, get_customer_lines for Robert Jones to list all active lines on the account, allowing you to assess the current services he is utilizing and address any potential issues or upgrades.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC119", "email": "robert.jones6549@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC119", "phone_number": "associated_phone_number"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are flexible, patient, optimistic, polite. Lookup customer by phone using phone number 555-123-4567 to verify identity. Once the identity is verified, get line details for line ID L67890 to check the current plan and usage. This will help ensure that the customer's plan aligns with their usage patterns, providing an opportunity to suggest a more suitable plan if necessary.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567", "user_id": "TC051"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are polite, organized. First, lookup_customer_by_phone with the phone number associated with Linda Garcia to verify her account identity. Once verified, proceed to get_customer_lines for Linda Garcia to retrieve all active lines under her account. After identifying the necessary line, get_line_details for line ID L001 to verify its current plan and usage details, as Linda Garcia has requested to review this information before making any changes to her service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Garcia's phone number", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC141", "user_id": "TC141"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are flexible, independent, logical, polite. First, lookup_customer_by_phone with phone_number \"555-0134\" to retrieve the customer ID for Mary Miller. Then, use this customer ID to get_line_details with line_id \"L67890\" to check the current plan and usage for Mary Miller's primary line. This will help determine if her data usage exceeds 80% of her plan limit, ensuring she stays informed about her telecom usage and avoids potential overage charges.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0134", "user_id": "TC102"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are polite, flexible, patient. Verify identity of user Jennifer Jones using email jennifer.jones7047@email.com to access account information.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC130", "reason": "Verify identity of user Jennifer Jones using email jennifer.jones7047@email.com for account access."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are independent, patient, confident, organized. First, verify the identity of Linda Miller using her email address (linda.miller7970@email.com) to access her account. Once her identity is confirmed, retrieve her billing details to assess any outstanding balance and review her payment history. If there is an outstanding balance, initiate payment processing using Linda Miller's preferred payment method. Upon successful payment confirmation, resume service for the suspended line L12345, ensuring this is completed within the 30-day period to maintain continuity of service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.miller7970@email.com", "user_id": "TC091"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "linda.miller7970@email.com", "user_id": "TC091"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "action": "resume", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are patient, organized. First, verify the identity of user John Garcia using the email john.garcia3458@email.com to ensure he has the authority to request account changes. Once his identity is confirmed, proceed to suspend the line with line ID L123456 for maintenance as per the customer's instruction.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia3458@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123456", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are organized, confident. Get bill details for account ID A12345 to verify outstanding balance and payment history.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A12345", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are organized, flexible. First, lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify Jennifer Miller's account identity. Once her identity is confirmed, proceed to get_customer_lines for customer_id: \"C001\" to list all active lines under Jennifer Miller's account. Finally, use get_bill_details for customer_id: \"C001\" to view recent billing statements and payment history, ensuring that all charges are correctly applied to the active lines.",
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
                name="get_bill_details",
                kwargs={"customer_id": "TC108"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are flexible, polite. First, use the Lookup_customer_by_phone task to retrieve John Smith's account details using his phone number. Once you have the account information, proceed to Get_customer_lines for John Smith to view all active lines on his account. This will help ensure that you have a comprehensive understanding of the services he is currently using, allowing you to assist him effectively with any inquiries or changes he may wish to make.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "John Smith's phone number", "user_id": "TC081"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "John Smith's account ID", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are flexible, polite. \"suspend_line for line ID L2345678 upon Linda Davis' request due to temporary non-use\"",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC150", "line_id": "L2345678", "reason": "Temporary non-use upon Linda Davis' request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are cautious, direct. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of Linda Smith",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are patient, independent, flexible. First, verify the identity of user Michael Miller using the email michael.miller4797@email.com before accessing account details. Once verified, lookup the customer by the phone number associated with Michael Miller's account to retrieve the account ID. Then, use this account ID to get customer lines and identify active telecom lines.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.miller4797@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are optimistic, direct. First, use the \"lookup_customer_by_phone\" atomic task with the phone number \"555-123-4567\" to verify your identity as Robert Williams. Once verified, proceed with the \"get_customer_lines\" task using the customer_id \"C9876\" to retrieve all lines associated with your account. Finally, utilize the \"get_line_details\" task for line_id \"L54321\" to check your current plan and data usage. This will help you determine if your current plan meets your needs based on your usage patterns.",
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
                kwargs={"line_id": "L54321", "user_id": "TC006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are cautious, logical. First, perform a Lookup_customer_by_phone with Michael Miller's phone number to retrieve his customer account details. Once you have the account details, proceed to Get_customer_lines using Michael Miller's account information to list all active lines associated with his account. After identifying the active lines, focus on Get_line_details for line L789 to check its current plan and usage details. This information will help you understand if a plan change is necessary and beneficial for Michael Miller.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Miller's phone number", "user_id": "TC054"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC054"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are patient, flexible, independent, logical. First, lookup_customer_by_phone with phone number 555-1234 to verify identity and access Michael Miller's account. Once his identity is confirmed, proceed to get_bill_details for user Michael Miller to review his current billing statement and due payment. This will ensure that you have all the necessary information to assist Michael with any billing inquiries he may have regarding his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC054"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are polite, cautious, logical. First, verify the customer identity for Michael Davis using his email michael.davis9122@email.com to ensure we are addressing the correct account holder. Once verified, proceed to get_customer_lines for Michael Davis to list all active lines on his account. This will allow us to identify the specific line ID that needs attention. After confirming the active lines, suspend_line for line ID L12345 due to the requested temporary suspension by Michael Davis. This sequential approach ensures that all actions are verified and executed accurately, maintaining a high standard of customer service in our telecom operations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.davis9122@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "michael.davis9122@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are cautious, flexible, patient, organized. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify identity for Jennifer Jones, ensuring you have the correct customer details. Once verified, proceed to get_line_details for line_id \"L123\" to check the current plan and usage for Jennifer's primary line, which will help assess the situation accurately. If the line is confirmed to be the one reported lost, suspend_line for line_id \"L123\" due to the reported loss of the device, ensuring it's within the 30-day resume period. This sequence of actions will help manage Jennifer's account effectively and maintain service integrity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "user_id": "TC130"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are patient, cautious, direct. First, perform a lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of user Mary Jones. Once her identity is confirmed, proceed to get_customer_lines for the customer_id retrieved from the verification task to list all active lines associated with her account. This process is essential to ensure that Mary Jones has access to the correct services and to address any inquiries she may have regarding her active lines.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC147"}
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
        user_id="TC038",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are direct, flexible, confident, optimistic. Suspend line L002 for Jennifer Jones due to a reported issue, ensuring to note the suspension date.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Jones"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC038"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L002"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L002", "suspension_date": "2023-10-05"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are cautious, direct. First, lookup the customer by the phone number associated with Jennifer Brown to retrieve the account ID. Once you have the account ID, get the customer lines for that account to ensure all services are active and correctly linked. This process is crucial for maintaining accurate and efficient telecom service management.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number_of_jennifer_brown", "user_id": "TC026"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "retrieved_account_id", "user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are organized, patient, optimistic, polite. \"lookup_customer_by_phone with phone_number 555-1234 to verify customer identity for Robert Williams\"",
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
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are optimistic, cautious, flexible, polite. First, verify customer identity for user Jennifer Smith using email jennifer.smith8259@email.com to ensure you are accessing the correct account. Once verified, proceed to lookup_customer_by_phone using the phone number associated with Jennifer Smith to retrieve her customer ID. Finally, use the obtained customer ID to get_customer_lines, allowing you to review the lines associated with her account for any potential service updates or issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.smith8259@email.com", "user_id": "TC143"}
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
        user_id="TC144",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are optimistic, confident, patient. First, access the bill details for customer Robert Jones for the current billing cycle to review charges and payments. Then, calculate the total outstanding balance for Robert Jones using the bill details retrieved. This will help ensure that all charges are accurate and up-to-date before proceeding to the next steps in the billing process.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC144", "customer_name": "Robert Jones"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["charges", "payments"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC029",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are confident, patient, polite. lookup_customer_by_phone with phone number 555-123-4567 to verify Robert Brown's identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC029"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are cautious, confident, organized, patient. First, lookup_customer_by_phone to verify account for phone number 555-123-4567. Once the account is verified, proceed to suspend_line for line ID L456 due to reported loss of device. This ensures that the customer's account is secure and prevents any unauthorized use of the lost device.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC092"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "reason": "Reported loss of device", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are direct, patient, independent. First, verify customer identity for Robert Williams using email robert.williams3479@email.com to access his account. Once verified, get the bill details for Robert Williams using his customer ID to check the outstanding balance and due date. This will help ensure that all information is accurate and up-to-date for billing inquiries at the telecom company.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.williams3479@email.com", "user_id": "TC006"}
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
        user_id="TC147",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are confident, organized, logical. Suspend line L12345 temporarily for Mary Jones as requested due to lost device.",
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
                kwargs={"user_id": "TC147", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC147", "line_id": "L12345", "reason": "Lost device"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Michael Johnson and your email is michael.johnson4664@email.com. You are logical, organized, flexible, confident. Begin by performing a lookup_customer_by_phone with phone_number \"123-456-7890\" to verify the identity of Jennifer Brown. Once verified, proceed to get_customer_lines for the user ID obtained from the verification process to list all active lines associated with Jennifer. After identifying the active lines, focus on get_line_details for line ID \"L001\" to check the current plan and usage. This will allow you to think about the best plan recommendations for line ID \"L001\" based on Jennifer's usage patterns, ensuring she has the most suitable and cost-effective plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC062"}
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
        user_id="TC031",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are patient, flexible. First, lookup John Williams' account by his phone number 555-0123 to retrieve customer information. Once you have the account information, get the customer lines associated with John Williams' account. This will help us ensure that all lines are correctly linked to his account for accurate billing and service management.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC031"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are organized, optimistic, polite. First, lookup_customer_by_phone with phone number '555-123-4567' to verify the identity of John Williams. Once verified, get_line_details for line ID 'L9876' to check the current plan and usage. This will help ensure that John Williams is on the appropriate plan and allow us to provide him with accurate information about his account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC031"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9876", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are patient, optimistic, flexible. First, verify customer identity using email john.brown8493@email.com for account access to ensure secure handling of their information. Once verified, proceed to get_bill_details for customer ID to review outstanding balance and payment history, as the customer has reported a potential discrepancy in their recent bill. If any issues are identified, transfer_to_human_agents with the customer ID and issue details for further assistance on billing discrepancies, ensuring the customer receives the necessary support to resolve their concerns.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC124"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC124", "issue_details": "Billing discrepancy reported by customer"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are independent, direct. Get_line_details for line ID L001 to check current plan and usage details. Think about possible plan upgrades for line ID L001 to accommodate increased data usage. As a telecom consultant, you need to ensure that the current plan for line ID L001 meets the user's needs. Start by reviewing the current plan and usage details to identify any discrepancies or limitations. Then, consider potential plan upgrades that would better suit the user's increased data usage. This will help you provide a comprehensive recommendation to the client, ensuring their telecom services align with their usage patterns.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are flexible, logical, patient. First, lookup_customer_by_phone with phone_number \"555-0123\" to verify Linda Davis's account access. Once verified, proceed to get_customer_lines for customer_id \"C3121\" to list all active lines associated with Linda Davis. This will help ensure that Linda's account is secure and that all her active lines are correctly accounted for in our system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC035"}
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
        user_id="TC082",
        instruction="Your name is Mary Johnson and your email is mary.johnson8773@email.com. You are cautious, independent, patient. First, verify Jennifer Jones’s identity using her email (jennifer.jones5314@email.com) to access her account. Once her identity is confirmed, proceed to get_customer_lines for Jennifer Jones's account to list all active lines. This will help ensure that all her active lines are correctly accounted for and managed within the telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.jones5314@email.com", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "jennifer.jones5314@email.com", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are independent, direct. First, lookup customer by phone number 555-1234 to retrieve account details, as we need to verify the user ID associated with this number. Once confirmed, proceed to suspend line L789 for the user ID associated with phone number 555-1234, as the customer has requested a temporary suspension due to an extended overseas trip.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC007", "line_id": "L789"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are confident, polite. Please verify the identity of user Robert Brown using the email robert.brown6285@email.com. Once his identity is confirmed, proceed to lookup his account details using his registered phone number. After retrieving the account information, get the active line IDs associated with Robert Brown's account to ensure all lines are correctly listed and active.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC036", "phone_number": "registered_phone_number"}
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
        user_id="TC013",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are logical, independent, patient, flexible. Use lookup_customer_by_phone with phone number \"555-123-4567\" to verify Mary Jones's identity. Once her identity is confirmed, get_bill_details for user Mary Jones to review the latest billing statement and any outstanding balances. After reviewing the billing details, calculate the total amount due including any late fees for Mary Jones's account to ensure she has the most accurate information for her payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC013"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "latest_bill_amount + late_fees"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are confident, direct, flexible, logical. First, verify the identity of user Mary Miller through her email mary.miller8461@email.com to ensure secure account access. Once verified, lookup customer by phone number 555-0123 to retrieve Mary's account details, ensuring you have the correct account information. Finally, get customer lines associated with Mary Miller's account to check active services, confirming that all services are functioning as expected and identifying any discrepancies that may require attention.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are logical, direct, optimistic. Suspend_line for line ID L12345 due to reported loss, ensuring the customer is aware of the 30-day resumption policy.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "reported loss", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are direct, independent, organized, flexible. Verify the identity of Patricia Miller using her email patricia.miller3252@email.com to access her account details. Once verified, use the phone number associated with Patricia Miller to retrieve her customer account ID. With the account ID, get the bill details to review her current billing information and payment status, ensuring there are no discrepancies or pending issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.miller3252@email.com", "user_id": "TC028"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "account_id_from_previous_step", "user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are logical, direct, patient. A customer has reported a lost device and wishes to suspend their service temporarily. First, lookup_customer_by_phone(phone_number=\"555-1234\") to retrieve the customer's details. Once you have the customer ID, proceed to get_customer_lines(customer_id=\"CUST001\") to identify all active lines associated with the account. After identifying the specific line that needs suspension, execute suspend_line(line_id=\"LINE12345\", reason=\"Customer request due to lost device\") to ensure the customer's line is suspended promptly and securely.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC042"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE12345", "reason": "Customer request due to lost device", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are confident, optimistic. Get line details for line ID L5678 to check current plan and data usage.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC073", "line_id": "L5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are polite, confident. Suspend line with line ID L9876 due to customer request for temporary disconnection.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC001", "line_id": "L9876", "reason": "Customer request for temporary disconnection"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are flexible, logical, patient. First, lookup the customer by phone number 555-0123 to retrieve their account information. Then, retrieve the bill details for this account to verify the current charges and due dates, ensuring that all information is accurate and up-to-date to assist the customer effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC048"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are optimistic, organized, cautious, patient. First, verify the identity of the user Michael Davis (michael.davis9122@email.com) by confirming their account password or security question. Once his identity is confirmed, proceed to get the bill details for the current billing cycle for Michael Davis to review any outstanding payments or charges. This process will ensure that Michael Davis has accurate and up-to-date information regarding his telecom account, allowing him to address any pending issues promptly.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={"reason": "Verify identity of Michael Davis by confirming their account password or security question."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are optimistic, patient, logical. First, retrieve billing details for Robert Brown's account to assess outstanding amounts. Once you have identified any outstanding balances, proceed to process payment for the outstanding amount on Robert Brown's account. This sequence ensures that Robert Brown's telecom services remain uninterrupted and up-to-date with payments.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC120"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "assess_outstanding_amount"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC040",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are logical, polite, patient, direct. lookup_customer_by_phone with phone_number: \"123-456-7890\" to verify Patricia Brown's account",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC040"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are polite, patient, optimistic. First, verify customer identity for Michael Jones using the email address michael.jones2722@email.com to access his account details. Once his identity is confirmed, proceed to get customer lines for Michael Jones to identify all active and suspended lines. This will help us ensure that we have accurate information about his account status and can assist him effectively with any inquiries about his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.jones2722@email.com", "user_id": "TC083"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "michael.jones2722@email.com", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are independent, flexible, confident. Begin by performing a lookup_customer_by_phone with phone number 555-1234 to verify identity and retrieve the customer ID. Once you have confirmed the customer ID, proceed to get_bill_details for customer ID 98765 to review the outstanding balance and recent transactions. This sequence will help you gather the necessary information to assist the customer effectively in a telecom business context.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC065"}
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
        user_id="TC051",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are direct, confident. Verify customer identity using email michael.garcia8786@email.com before accessing account details. Once verified, lookup the customer by phone number associated with Michael Garcia to retrieve the account ID. With the account ID, get customer lines to list all active lines. This process ensures that you can accurately manage and review the customer's telecom services, focusing on identifying data usage and plan type for each active line.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.garcia8786@email.com", "user_id": "TC051"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_from_previous_step", "user_id": "TC051"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are organized, confident. \"get_bill_details for account ID A789456 to review outstanding balance\"",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A789456", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are logical, organized, patient. Suspend line for Michael Davis' secondary line using the line ID and reason \"temporary hold requested by customer\".",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC136"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC136", "line_id": "secondary_line_id", "reason": "temporary hold requested by customer"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC038",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are cautious, flexible, polite. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify the identity of Jennifer Jones. Once verified, proceed to get_bill_details for customer_id \"C00123\" to review her outstanding balance and payment history. After reviewing the details, calculate total amount due for customer_id \"C00123\" including late fees and current charges to ensure Jennifer has the most accurate information before discussing any payment options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC038"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC038", "user_id": "TC038"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "outstanding_balance + late_fees + current_charges", "variables": {"outstanding_balance": "value_from_get_bill_details", "late_fees": "value_from_get_bill_details", "current_charges": "value_from_get_bill_details"}}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are patient, flexible, polite. First, perform a lookup_customer_by_phone with phone number \"555-123-4567\" to verify the identity of Jennifer Jones. Once her identity is confirmed, proceed to get_customer_lines for the customer ID retrieved from the previous task to list all active lines under her account. Finally, use the same customer ID to get_bill_details and review Jennifer's current billing status, ensuring that all information is up-to-date and accurate.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC082", "user_id": "TC082"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC082", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Patricia Davis and your email is patricia.davis1886@email.com. You are patient, organized, confident, direct. lookup_customer_by_phone with phone_number \"555-123-4567\" to verify customer identity for Michael Johnson",
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
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are cautious, patient. Retrieve all active lines for Patricia Brown’s account to ensure you have the correct line information. Once you have confirmed the details, get details of line L12345 to assess its current plan and usage. This will allow you to evaluate whether the current plan meets the customer's needs or if an upgrade might be beneficial.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC094", "customer_name": "Patricia Brown"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC094", "line_id": "L12345"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are optimistic, logical. Get all active lines associated with James Brown's customer ID.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "James Brown's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC145"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are cautious, patient, independent. First, lookup_customer_by_phone with phone_number '555-1234' to verify Linda Davis's account access, ensuring you have the correct customer information. Next, get_line_details for line_id 'L789' to retrieve current plan details, so you can understand what services Linda is currently using. Finally, think to decide if Linda wants to change her current plan based on line details, considering the benefits or limitations of her current plan and any recent usage patterns or feedback she may have provided.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC107"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L789", "user_id": "TC107"}
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
        user_id="TC129",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are logical, confident, flexible. Get details of Robert Brown's current plan and data usage for all active lines.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC129", "email": "michael.miller4797@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC129"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC129", "line_id": "line_001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC129", "line_id": "line_002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC028",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are confident, cautious, independent. Get customer lines for Patricia Miller using her customer ID to identify all active lines.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC028", "user_id": "TC028"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are polite, logical. Get_bill_details for Patricia Smith's account ID to review the latest billing statement.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "Patricia_Smith_Account_ID", "user_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are flexible, cautious. First, verify customer identity using email john.brown8493@email.com and any available security questions to ensure secure access to the account. Once verified, proceed to get_customer_lines for the customer with email john.brown8493@email.com to identify all active lines associated with the account. Finally, get_bill_details for the same customer to review any outstanding payments, ensuring all active lines are accounted for in the billing details.",
        actions=[
            Action(
                name="get_customer_lines",
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
        user_id="TC092",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are polite, confident, patient. First, lookup_customer_by_phone with phone number '555-1234' to verify Patricia Williams' identity. Once her identity is confirmed, get_bill_details for customer_id 'C2585' to review the latest charges and due date, ensuring you have all necessary information to assist with any billing inquiries Patricia may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC092"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC092", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are logical, polite, patient, confident. First, lookup_customer_by_phone with the phone number associated with Patricia Williams to verify account access. Once the account is verified, proceed to get_customer_lines for the verified account to list all active lines. This will help ensure that Patricia Williams has access to the correct services and can manage her telecommunications needs effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number_for_Patricia_Williams", "user_id": "TC092"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are direct, organized. \"lookup_customer_by_phone with phone number 555-1234 to verify Mary's account access\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are flexible, optimistic. Initiate a plan change for line ID L103 to a higher data plan, effective next billing cycle.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC089"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L103"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify if line L103 is eligible for a plan change and determine the available higher data plans."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"reason": "Initiate a plan change for line ID L103 to a higher data plan, effective next billing cycle. Customer is flexible and optimistic."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are independent, direct. lookup_customer_by_phone with phone number '555-1234' to verify identity and access account details",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC006"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC041",
        instruction="Your name is John Garcia and your email is john.garcia3458@email.com. You are polite, confident. First, verify the identity of Linda Smith using her email linda.smith7027@email.com to ensure secure account access. Once her identity is confirmed, proceed to retrieve all active lines associated with Linda Smith's account. This process is crucial to ensure that Linda has uninterrupted access to her telecom services and to address any potential issues with her account efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.smith7027@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC041"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC071",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are patient, logical. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify Mary Johnson's identity, ensuring that you are speaking with the correct account holder. Once her identity is confirmed, proceed to suspend_line for line ID \"L001\" due to non-payment with customer consent, as Mary has agreed to this action until she can settle the outstanding balance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC071"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "user_id": "TC071"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC109",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are independent, polite. First, lookup_customer_by_phone with the phone_number \"555-123-4567\" to verify the identity of Robert Jones. Once verified, proceed to get_customer_lines for user_id \"U3449\" to retrieve all active telecom lines under Robert Jones' account. Finally, use get_line_details for line_id \"L9823\" to check the current plan and usage details, ensuring that the line is eligible for temporary suspension due to Robert Jones' upcoming travel plans.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "U3449"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L9823"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC051",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are logical, polite. Verify the identity of the user Michael Garcia using email michael.garcia8786@email.com to access account details. Once verified, get_customer_lines using the account ID to list all active lines associated with Michael Garcia's account. Then, for each line, get_line_details to determine current usage, plan details, and line status. This sequence of actions will help ensure that we have a comprehensive understanding of the account's current status and usage, which is essential for providing accurate customer support and service recommendations.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC051", "account_id": "michael.garcia8786@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC051", "line_id": "line_001"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC051", "line_id": "line_002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are cautious, direct, independent, patient. First, verify the identity of user John Smith using the email john.smith6383@email.com to ensure secure access to his account details. Once verified, lookup the customer by the phone number associated with John Smith to retrieve his customer ID. After obtaining the customer ID, get the customer lines for this ID to list all active lines under John Smith’s account, ensuring that we have a comprehensive view of his current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.smith6383@email.com", "user_id": "TC016"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC016", "user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are flexible, polite. First, lookup_customer_by_phone with phone number 123-456-7890 to verify identity for John Davis, as he has called in regarding his telecom account. Once the identity is confirmed, get_bill_details for customer ID C001 to review outstanding balance, as John Davis has expressed concerns about his recent bill and needs clarification on the charges.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC074"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC074", "user_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are patient, direct, organized. Suspend line L789 for temporary hold as requested by Michael Jones.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC042", "line_id": "L789", "reason": "Temporary hold as requested by Michael Jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is John Davis and your email is john.davis8441@email.com. You are organized, optimistic, confident, patient. Retrieve the latest bill details for Patricia Smith's account to ensure accuracy in her billing information. Once you have verified the details, calculate the total amount due on Patricia Smith's current bill. This will help provide her with precise information and assist in any further inquiries she may have regarding her telecom services.",
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
        user_id="TC120",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are cautious, polite, organized. First, verify customer identity for account access using email robert.brown5816@email.com to ensure secure handling of account information. Once the identity is confirmed, proceed to lookup_customer_by_phone with the phone number associated with Robert Brown's account to retrieve the customer ID. This will allow us to efficiently manage and review the customer's account details in our telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "associated_phone_number", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown3820@email.com. You are organized, cautious. First, verify customer identity for James Davis using email james.davis6038@email.com to ensure all account actions are authorized. After confirming his identity, get bill details for the latest billing cycle to review outstanding payments for James Davis. This will help determine if further action is needed to address any non-payment issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.davis6038@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC145",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are independent, optimistic, polite, flexible. lookup_customer_by_phone with phone_number \"555-1234\" to verify identity for account access",
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
        user_id="TC060",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are logical, patient, cautious, flexible. First, lookup_customer_by_phone with phone_number '555-0134' to verify the identity of Linda Johnson. Once her identity is confirmed, proceed to get_customer_lines for customer_id 'C123456' to list her active lines. After identifying her active lines, use get_line_details for line_id 'L987654' to check the current plan and usage. This will help in assessing her current service status and any potential issues with her plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0134"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC060"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L987654"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are cautious, optimistic, direct. First, use lookup_customer_by_phone with the phone number associated with Mary Davis to verify her identity and retrieve her customer ID. Once you have confirmed her identity, proceed to Get_customer_lines using Mary Davis's customer ID to list all active lines under her account. Finally, for each line retrieved, use Get_line_details to check the current plan and usage, ensuring that all active lines are up to date with their respective plans and usage limits.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Davis's phone number", "user_id": "TC020"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC020", "user_id": "TC020"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Line ID 1", "user_id": "TC020"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "Line ID 2", "user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are direct, cautious. First, lookup_customer_by_phone with phone number '555-1234' to verify identity for user John Brown, ensuring you have the correct account details. Once verified, get_customer_lines for user ID retrieved from 'lookup_customer_by_phone' to list all active lines associated with John Brown's account. Finally, get_line_details for line ID 'L002' to verify eligibility for plan upgrade, as John Brown has expressed interest in enhancing his current service plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC124"}
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
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are independent, organized. First, lookup_customer_by_phone with phone_number '123-456-7890' to verify identity for Michael Smith. Once identity is confirmed, get_bill_details for account ID 'A123456' to verify outstanding balance. If there is an outstanding balance, transfer_to_human_agents with account ID 'A123456' for payment arrangement discussion.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A123456"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"account_id": "A123456"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are organized, polite, direct. First, verify the identity of Robert Jones using his email robert.jones6549@email.com to ensure secure account access. Once his identity is confirmed, proceed to get the line details for the primary line on Robert Jones's account to check the current plan and usage. This will help us provide accurate information and recommendations for any potential plan changes.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones6549@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC119"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary", "user_id": "TC119"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC040",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are independent, direct, confident. Suspend line L001 on Patricia Brown's account due to non-payment.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC040", "email": "linda.miller7970@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC040"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC040", "line_id": "L001", "reason": "non-payment"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are patient, confident. First, lookup_customer_by_phone with phone number (555-123-4567) to verify identity and retrieve customer ID for Mary Jones (mary.jones9465@email.com). Once you have the customer ID, get_customer_lines for the retrieved customer ID to list all active lines on Mary Jones's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC147"}
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
        user_id="TC127",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are independent, confident, optimistic. lookup_customer_by_phone with phone number 555-0143 to retrieve customer account details for Linda Garcia",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0143", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are direct, logical. lookup_customer_by_phone with phone_number \"555-0123\" for user Patricia Williams",
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
        user_id="TC123",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are flexible, polite, cautious. Verify customer identity using Robert Jones's email (robert.jones5323@email.com) to access account details. Once verified, check bill details for Robert Jones to verify any outstanding payments or recent transactions. Ensure that all information is accurate and up-to-date to assist in resolving any potential billing issues efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones5323@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Linda Miller and your email is linda.miller1663@email.com. You are logical, optimistic. First, use lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Mary's identity. Once verified, proceed to use get_customer_lines with customer_id \"C123456\" to retrieve all active lines for Mary. After identifying her primary line, use get_line_details with line_id \"L987654\" to check the current plan details.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC102"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L987654"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC112",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are organized, independent, confident. First, lookup_customer_by_phone with phone number (123-456-7890) to confirm Patricia Smith's identity for a plan upgrade. Once her identity is confirmed, proceed to get_line_details for line ID (L1234) to determine eligibility for a plan upgrade. This will ensure that Patricia's line is eligible for the upgrade she desires, streamlining the process and maintaining customer satisfaction.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC112"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234", "user_id": "TC112"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC116",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are optimistic, confident, direct, independent. lookup_customer_by_phone with parameters: phone_number=\"555-1234\", user_email=\"james.brown7392@email.com\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_email": "james.brown7392@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are confident, logical, independent, direct. \"Lookup customer by phone with phone number 555-1234 to verify user identity for John Miller (john.miller2529@email.com)\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC104"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are direct, flexible, polite, confident. First, use lookup_customer_by_phone with phone number 555-1234 to verify Linda Miller's identity. Once verified, retrieve customer lines for verified customer ID C001 to list active lines on the account. This will help ensure that all active lines are accurately accounted for and managed within the telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC091"}
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
        user_id="TC144",
        instruction="Your name is Robert Williams and your email is robert.williams8770@email.com. You are optimistic, cautious. Use lookup_customer_by_phone with phone number \"555-123-4567\" to verify Robert Jones's identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are polite, organized, optimistic, direct. Lookup_customer_by_phone with phone_number '123-456-7890' to verify identity for Robert Davis.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC143",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are cautious, patient, confident. First, perform a lookup_customer_by_phone with phone_number=\"555-123-4567\" to verify identity for Jennifer Smith. Once her identity is confirmed, proceed to get_bill_details with customer_id=\"CUST8259\" to review her outstanding balance and due dates. This will ensure you have all necessary information before discussing any payment arrangements.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC143"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC143", "user_id": "TC143"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are organized, independent. First, verify the identity of customer Michael Garcia using his email michael.garcia5750@email.com to access account details. Once verified, retrieve all active lines under Michael Garcia's account using the get_customer_lines tool with the customer ID obtained. After retrieving the active lines, get details of the primary line from Michael Garcia's account using the get_line_details tool with the specific line ID. This sequence will ensure you have accurate and up-to-date information about the customer's primary line, which is crucial for providing effective telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.garcia5750@email.com", "user_id": "TC039"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC039", "user_id": "TC039"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary_line_id_obtained", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are logical, confident, direct, patient. First, lookup_customer_by_phone with the phone number associated with Mary Johnson to verify her account identity. Once verified, proceed to get_customer_lines for user Mary Johnson to view her active lines. This will help ensure that all lines associated with her account are accounted for and up-to-date, which is crucial for providing accurate customer service and addressing any potential issues with her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Johnson's phone number", "user_id": "TC093"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC135",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are flexible, direct, independent, polite. Retrieve bill details for the current billing cycle for James Jones's account and calculate the total amount due, including any late fees if applicable. This information is needed to ensure that all charges are accurate before proceeding with the payment process. As part of our telecom service, we aim to provide a seamless experience for our customers, so please ensure all details are verified and up-to-date.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC135"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are optimistic, confident, logical, cautious. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify the identity of Patricia Brown. Once her identity is confirmed, proceed to get_bill_details for customer_id 'CUST12345' to review her outstanding balance and payment history. This will help in providing Patricia with accurate information about her account status before discussing further options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC056"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC056", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Linda Davis and your email is linda.davis4055@email.com. You are patient, flexible. First, get bill details for the account associated with Jennifer Brown to check for outstanding payments. Then, calculate the total outstanding amount due for Jennifer Brown's account from the bill details. This will help us understand her current financial obligations and assist in planning her payment options.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are organized, cautious. lookup_customer_by_phone with phone number 555-1234 to verify identity for user Michael Jones",
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
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are confident, organized, cautious, logical. First, lookup_customer_by_phone with phone=555-123-4567 to verify identity for Robert Brown (robert.brown4015@email.com). Once verified, proceed to get_customer_lines for user_id=U4015 to list all active lines on the account. Then, for each active line, get_line_details for line_id=L1234 to check current plan and usage, ensuring that Robert Brown's telecom needs are being met effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "U4015"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC113",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are logical, independent, polite. Retrieve billing details for Patricia Smith's account to check for outstanding balances.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC113", "phone_number": "Patricia Smith's phone number"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC113", "customer_id": "TC113"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC101",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are logical, organized, independent. First, verify customer identity for James Johnson using email james.johnson2916@email.com to ensure you are accessing the correct account. Once verified, proceed to lookup_customer_by_phone with the phone number associated with James Johnson to retrieve the customer ID. Finally, use the customer ID to get_customer_lines and list all active lines for James Johnson, which will help in managing his account effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.johnson2916@email.com", "user_id": "TC101"}
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
        user_id="TC146",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are cautious, polite, direct. Suspend line L12345 under Linda Smith's account temporarily due to customer request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC146", "phone_number": "L12345"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC146", "customer_id": "TC146"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC146", "line_id": "L12345"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC146", "line_id": "L12345", "reason": "Customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are organized, optimistic. First, lookup_customer_by_phone with phone_number: \"555-1234\" to verify Jennifer Brown's account. Once her account is verified, proceed to get_customer_lines for customer_id: \"C3820\" to list all active lines on Jennifer Brown's account. This will help ensure that all her active services are correctly documented and up to date in our system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC026"}
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
        user_id="TC143",
        instruction="Your name is Robert Jones and your email is robert.jones3449@email.com. You are patient, optimistic, independent. First, use the Lookup_customer_by_phone task with phone_number \"555-123-4567\" to verify Jennifer Smith's identity. Once her identity is confirmed, proceed to Get_customer_lines for customer_id \"C8259\" to retrieve all active lines on Jennifer Smith's account. This will help us ensure that we have the correct information before discussing any changes or upgrades to her service plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC143"}
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
        user_id="TC003",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are direct, flexible, polite, patient. \"get_line_details using line ID from Robert Garcia's account to check current plan and usage\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC003", "phone_number": "Robert Garcia's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC003"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC003", "line_id": "line_id_from_previous_step"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are logical, flexible. Verify customer identity using email linda.garcia4634@email.com for account access. Once verified, lookup customer by phone number associated with this email to retrieve account details. This process ensures secure access and accurate retrieval of customer information, which is crucial for maintaining high standards of service in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.garcia4634@email.com", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC032",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are cautious, confident, logical, direct. First, verify customer identity for user Robert Davis using email robert.davis2812@email.com to ensure you are discussing account details with the correct individual. Once verified, get_bill_details for the account of Robert Davis to check outstanding payments and understand the current financial status. If there are outstanding payments, proceed to suspend_line for line ID L123 due to non-payment, ensuring Robert Davis is informed of the suspension and the reason behind it.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.davis2812@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC032"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "reason": "Non-payment", "user_id": "TC032"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are logical, confident, organized, patient. First, perform a lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Linda Miller's identity as she has contacted customer service regarding her account. Once her identity is confirmed, proceed to get_customer_lines for customer_id \"CUST1663\" to retrieve all active lines associated with her account, as she mentioned issues with one of her lines. Finally, use get_line_details for line_id \"LINE7890\" to check the current plan and data usage, as Linda is concerned about unexpected data charges on her latest bill.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC019"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC019", "user_id": "TC019"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE7890", "user_id": "TC019"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are confident, logical. First, get bill details for Robert Brown's account to verify the outstanding balance and payment due date. Once you have confirmed these details, calculate the total amount due for Robert Brown's account, including any late fees or surcharges. This will ensure that you have an accurate understanding of his financial obligations before proceeding with further actions.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC073"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "outstanding_balance + late_fees + surcharges"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are patient, optimistic, cautious. First, lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify identity for Mary Jones. Once verified, proceed to get_customer_lines for customer_id: \"C123456\" to list all active lines associated with Mary Jones. After identifying the primary line, use get_line_details for line_id: \"L987654\" to check the current plan details. If a plan upgrade is desired, transfer_to_human_agents with context: \"plan change request\" to assist Mary Jones in selecting a new plan that better suits her needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC147"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L987654"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "plan change request", "user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are confident, organized, cautious. First, verify customer identity for Linda Garcia using email linda.garcia4634@email.com to access account details. Once her identity is confirmed, proceed to lookup_customer_by_phone using Linda Garcia's verified phone number to retrieve her customer account information. After obtaining the account details, get_customer_lines for Linda Garcia's account to list all active lines associated with her account. This will help us ensure that we have the correct line information before proceeding with any further actions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.garcia4634@email.com", "user_id": "TC127"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "verified_phone_number_from_previous_step", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are polite, confident, organized, optimistic. First, lookup_customer_by_phone with phone_number=\"555-1234\" to verify customer identity for Michael Davis. Once the identity is confirmed, proceed to get_bill_details for user_id=\"michael.davis9122\" to review the latest billing statement and outstanding balance. This will help assess the situation before taking further action regarding any service issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "michael.davis9122"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are polite, direct, organized. First, verify the identity of John Johnson using his email john.johnson9055@email.com before proceeding with account access to ensure security compliance. Once verified, lookup John's account using his phone number to gather account details, which will provide a comprehensive overview of his services. Finally, retrieve all active lines associated with John's account to review current services, ensuring all lines are accounted for and functioning properly. This sequential process is crucial for maintaining the integrity and quality of service in our telecom operations.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.johnson9055@email.com", "user_id": "TC001"}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "john's_phone_number", "user_id": "TC001"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "john's_phone_number", "user_id": "TC001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC046",
        instruction="Your name is John Brown and your email is john.brown8493@email.com. You are direct, polite, confident, cautious. Suspend_line for line ID L5678 under Robert Garcia's account if usage exceeds the plan limit and customer requests suspension.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC046"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC046", "line_id": "L5678"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC046", "line_id": "L5678"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are cautious, polite, flexible, logical. Suspend_line for line ID L12345 due to a temporary request from user Jennifer Jones.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "user_id": "TC130"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC026",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are organized, flexible. First, get bill details for Jennifer Brown's account to review outstanding balance and recent transactions. Then, transfer to human agents to discuss payment plan options with Jennifer Brown for settling the outstanding balance. This will ensure that Jennifer is aware of her current financial obligations and can explore feasible solutions for her telecom account.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC026"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC026"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are cautious, independent, polite. Begin by performing a lookup_customer_by_phone with phone number 555-1234 for user Robert Brown to verify identity as part of a routine customer service check. Once Robert Brown's identity is confirmed, proceed to get_bill_details for customer ID C1234 to review his current billing status and ensure there are no discrepancies or overdue amounts. After reviewing the bill details, think to assess if payment is needed based on the information provided. If you detect any payment issues or discrepancies that require further assistance, transfer_to_human_agents with context of billing inquiry for customer ID C1234 to ensure Robert Brown receives the necessary support to resolve his billing concerns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC036"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC036", "user_id": "TC036"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Assess if payment is needed based on the bill details provided."}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "billing inquiry for customer ID C1234", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Robert Williams and your email is robert.williams3479@email.com. You are patient, organized, confident, flexible. First, lookup_customer_by_phone with phone number 555-1234 to verify Linda Miller's account identity. Once her identity is confirmed, proceed to get_customer_lines for customer ID C001 to retrieve active lines associated with Linda Miller. After identifying the active lines, get_line_details for line ID L123 to check the current plan and usage details for Linda Miller, ensuring that you have all necessary information to assist with her request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC091"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC091", "user_id": "TC091"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are optimistic, confident, patient. First, verify customer identity using email john.garcia4063@email.com to access the account. Once verified, process the payment for the total amount due on John Garcia's account and confirm the expected reflection time. After confirming the payment has been processed successfully, ensure that the suspended line ID L1234 is resumed within the 30-day window, as this will restore the customer's service promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.garcia4063@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC018"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L1234", "action": "resume", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC135",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are flexible, patient, optimistic. Suspend_line for line ID L12345 due to requested temporary suspension by James Jones.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L12345", "reason": "Requested temporary suspension by James Jones", "user_id": "TC135"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are polite, direct. First, lookup_customer_by_phone with phone number \"123-456-7890\" to verify Mary Brown's identity. Once her identity is confirmed, proceed to get_customer_lines for the customer ID retrieved from the previous step to list her active lines. This will help us ensure that we have the correct information about her account status and services.",
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
        user_id="TC145",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are independent, polite, confident, flexible. Verify the identity of user James Brown using email james.brown3113@email.com to access the account. Once verified, get the bill details for the current billing cycle for James Brown's account to review charges and due dates. Calculate the total amount due for James Brown by summing up all charges in the get_bill_details response.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC145"}
            ),
            Action(
                name="calculate",
                kwargs={"expression": "sum(charges)"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are direct, organized, cautious, patient. First, verify your identity by confirming your email, patricia.brown8933@email.com, to access your account. Once verified, lookup your account using your phone number, 555-0123, through the lookup_customer_by_phone method. After retrieving your customer ID, proceed to retrieve all active lines associated with your account using the get_customer_lines method. This sequence of actions will help ensure that you have a comprehensive overview of your telecom services, allowing you to manage them effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC056"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are logical, confident. Get_bill_details for billing account linked to customer ID to review recent charges and payment status",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Robert Garcia and your email is robert.garcia1279@email.com. You are flexible, confident, patient, independent. First, get_customer_lines for user 'john.williams8933@email.com' to retrieve active lines to ensure we are working with the correct account information. Next, get_line_details for line_id 'L002' to verify eligibility for plan upgrade, ensuring that the line qualifies for the new service plan. Finally, calculate new monthly cost for line_id 'L002' if upgraded to 'Premium Plan' to provide the customer with accurate pricing information before proceeding with any changes.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC098", "email": "john.williams8933@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC098", "line_id": "L002"}
            ),
            Action(
                name="calculate",
                kwargs={"user_id": "TC098", "line_id": "L002", "new_plan": "Premium Plan"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is John Williams and your email is john.williams8933@email.com. You are polite, patient, flexible. Get_bill_details for account linked to Robert Jones to review outstanding balance and due date.",
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
        user_id="TC013",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are logical, optimistic, polite. \"get_line_details with line_id='L56789' to check current plan and usage details\"",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L56789", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC144",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are polite, organized, logical, confident. First, lookup_customer_by_phone with phone_number: '555-123-4567' to verify identity for Robert Jones, ensuring that you have the correct customer information before proceeding. Once verified, think about plan upgrade options for Robert Jones based on his current usage and available promotions, so you can offer him a more suitable plan that meets his needs and potentially saves him money.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify the identity of Robert Jones using the phone number provided. Once verified, review his current plan and usage to determine suitable upgrade options."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are independent, patient. Lookup customer by phone number 555-1234 for Jennifer Williams to access her account details. After verifying her identity, get customer lines for Jennifer Williams to view active and suspended lines, ensuring you have the necessary information to assist with any service adjustments she may require.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC131"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Jennifer Williams", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC127",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are cautious, independent. First, lookup_customer_by_phone with phone_number: '555-123-4567' to verify identity for Linda Garcia. Once her identity is confirmed, proceed to get_customer_lines for customer_id: 'C4634' to retrieve all active lines associated with her account. This will ensure you have the correct information before discussing any changes or updates to her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC127"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC127", "user_id": "TC127"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC101",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are direct, polite, confident, independent. First, lookup_customer_by_phone with phone '555-123-4567' to verify James Johnson's identity, as he has reported an issue with his service. Once his identity is confirmed, proceed to get_customer_lines for customer ID 'C1001' to retrieve all active lines under his account. This will help us identify which line is experiencing the issue and ensure we address his concerns accurately.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567", "user_id": "TC101"}
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
        user_id="TC056",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are direct, logical. First, use lookup_customer_by_phone with phone number 555-123-4567 to verify Patricia Brown's account access. Once verified, proceed to use get_customer_lines with Patricia Brown's customer ID to retrieve all active lines under her account. Finally, use calculate tool to estimate the cost difference for Patricia Brown if she upgrades to a premium plan, ensuring she is informed of the potential financial impact of this change.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC056"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC056", "user_id": "TC056"}
            ),
            Action(
                name="calculate",
                kwargs={"current_plan_cost": "Current Plan Cost", "premium_plan_cost": "Premium Plan Cost"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are optimistic, direct, cautious. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify Michael Miller's account. Once verified, proceed to get_bill_details for account_id \"A456\" to view the latest bill and payment status, ensuring that all recent transactions are accurately reflected. If there are any discrepancies or if Michael has reported issues with his payment not reflecting, transfer_to_human_agents for account_id \"A456\" to assist with resolving these payment issues promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A456"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"account_id": "A456", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are patient, optimistic. lookup_customer_by_phone with phone_number \"555-1234\" to verify Michael Johnson's identity",
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
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are flexible, polite, cautious. lookup_customer_by_phone with phone_number=1234567890 to verify John Williams' identity",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "1234567890", "user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC031",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are direct, optimistic, polite. First, verify the customer identity using the email john.williams4633@email.com to ensure secure access to account details. Once the identity is confirmed, proceed to get the customer lines for the user ID associated with john.williams4633@email.com. This will allow you to review all active services and ensure the customer is receiving the appropriate telecom services they have subscribed to.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.williams4633@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC031"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are direct, logical. First, use `lookup_customer_by_phone` with Patricia Williams' phone number to verify her identity. Once verified, use `get_customer_lines` with Patricia Williams' account ID to retrieve all active lines associated with her account. This will help ensure that we have accurate information about her services for any potential plan upgrades or troubleshooting.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Williams' phone number", "user_id": "TC092"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "Patricia Williams' account ID", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are cautious, polite, flexible. First, lookup_customer_by_phone with phone number 555-1234 to verify identity for account access. Once the customer's identity is confirmed, proceed to calculate estimated charges for plan upgrade on line L1234 effective next billing cycle, ensuring the customer is informed about potential cost changes and benefits associated with the upgrade.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC083"}
            ),
            Action(
                name="calculate",
                kwargs={"line_id": "L1234", "change_type": "plan_upgrade", "effective_date": "next_billing_cycle", "user_id": "TC083"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC129",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are polite, cautious, independent. get_bill_details for account_id \"ACC54321\" to review outstanding balance and due date for Robert Brown's account",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "ACC54321", "user_id": "TC129"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC054",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are independent, flexible, cautious. First, lookup_customer_by_phone with phone number 555-1234 to verify customer identity for Michael Miller. Once verified, proceed to get_customer_lines for user Michael Miller to retrieve all active lines on the account. This will ensure you have accurate information about the customer's current telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC054"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Michael Miller", "user_id": "TC054"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are flexible, optimistic, confident. Get bill details for John Garcia's account to review the current outstanding balance and due date.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are flexible, logical, patient. Suspend_line for line ID L102 due to reported lost phone, ensuring it's within the 30-day resumption period. After completing the suspension, get_customer_lines to confirm the successful suspension of line ID L102 as requested by John Garcia. This will ensure that the line is properly deactivated and ready for resumption within the specified period, maintaining account integrity and customer satisfaction.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC018", "line_id": "L102", "reason": "Lost phone"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC119",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are confident, direct. Verify customer identity for Robert Jones using email robert.jones6549@email.com to access account details. Once verified, proceed to get_customer_lines for Robert Jones to list all active lines under his account. After obtaining the list, focus on line ID L12345 to get_line_details and check its current plan and usage details. This will allow you to think about possible plan upgrades or changes for line ID L12345 to offer Robert Jones better options, ensuring he receives the most suitable telecom services for his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.jones6549@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC119"}
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
        user_id="TC069",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are direct, polite, flexible. Verify the identity of user Michael Davis using email michael.davis7894@email.com to access account. Once verified, suspend line L7890 for Michael Davis due to reported issues, ensuring suspension is reversible within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "michael.davis7894@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC069", "line_id": "L7890", "suspension_reason": "Reported issues", "reversible_within_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC124",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis3568@email.com. You are confident, logical, direct, independent. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify customer identity for John Brown. Once verified, proceed to get_customer_lines for customer_id \"C8493\" to retrieve all active lines associated with John Brown's account. After identifying the relevant line, use get_line_details for line_id \"L5678\" to check current plan and usage details. If everything is in order, move forward to suspend_line with line_id \"L5678\" for a maintenance request initiated by John Brown.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC124"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L5678", "user_id": "TC124"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are flexible, confident. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Linda Davis's identity. Once her identity is confirmed, proceed to get_bill_details for customer_id \"C5049\" to review the latest bill and payment status to understand the reason for any outstanding balance. If the bill shows non-payment, suspend_line for line_id \"L7890\" due to non-payment, ensuring Linda Davis is aware of the 30-day resumption policy and confirming that other lines are unaffected by the suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC107"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L7890", "reason": "non-payment", "user_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are polite, independent. First, lookup_customer_by_phone with phone number 123-456-7890 to verify account access for John Garcia. Once access is confirmed, proceed to get_customer_lines for customer ID 4063 to retrieve all active lines associated with the account. Finally, get_line_details for line ID L102 to check current plan and usage details, ensuring that John Garcia's current plan meets his usage needs effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC018", "user_id": "TC018"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L102", "user_id": "TC018"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones7047@email.com. You are polite, organized. First, retrieve customer information for Robert Brown using email robert.brown6285@email.com to verify account access. Once access is confirmed, get all active lines associated with Robert Brown’s customer account to review current services. Finally, check the billing status for Robert Brown’s account to verify any pending payments or recent transactions. This sequence will ensure that we have a comprehensive understanding of Robert Brown's current telecom services and account status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "robert.brown6285@email.com", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are direct, cautious, optimistic. First, lookup_customer_by_phone with phone number 123-456-7890 to verify identity for Jennifer Williams. Once her identity is confirmed, get_bill_details for customer ID C12345 to review her outstanding balance and due date. If there is an overdue amount, transfer_to_human_agents for assistance with payment arrangement for customer ID C12345 to ensure her service continues smoothly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC131"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC131", "user_id": "TC131"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC131", "user_id": "TC131"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are confident, direct, flexible. First, use the Lookup_customer_by_phone task with Linda Davis's phone number to retrieve her account information. Once you have her account details, proceed with the Get_customer_lines task for Linda Davis to list all active lines on her account. This will help us ensure all her lines are correctly configured and up to date with the latest plans and services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Davis's phone number", "user_id": "TC150"}
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
        user_id="TC038",
        instruction="Your name is Mary Davis and your email is mary.davis8842@email.com. You are cautious, polite, patient. get_bill_details for account_id 'A123' to retrieve current outstanding balance for Jennifer Jones",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A123", "user_id": "TC038"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC083",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are organized, polite, cautious. Suspend_line for a line ID if user requests temporary suspension due to non-usage",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC083", "reason": "Temporary suspension due to non-usage"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are logical, flexible. First, perform a Lookup_customer_by_phone using the phone number 123-456-7890 to verify Jennifer Davis's identity for account access. Once her identity is confirmed, proceed to Get_customer_lines for the customer ID retrieved to list all active lines under Jennifer Davis's account. This process ensures that Jennifer's account is secure and allows us to manage her telecom services effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC148"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC148", "user_id": "TC148"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC123",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are independent, organized, polite. Suspend_line for the line ID that Robert Jones has specified for temporary suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC123"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC123"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC123", "line_id": "line_id_specified_by_robert_jones"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Robert Johnson and your email is robert.johnson9087@email.com. You are cautious, direct, flexible. lookup_customer_by_phone with phone_number=\"123-456-7890\" to verify Robert Brown's identity",
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
        user_id="TC124",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are logical, optimistic, organized. \"suspend_line for line_id 'L5678' with reason 'customer request' to temporarily disable service\"",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC124", "line_id": "L5678", "reason": "customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are flexible, optimistic, polite, confident. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify Patricia Williams' identity. Once her identity is confirmed, proceed to get_customer_lines for the account associated with user Patricia Williams using her verified phone number. This will help us ensure we have the correct account details before addressing any service inquiries or changes she may have regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC092"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is John Smith and your email is john.smith6383@email.com. You are optimistic, cautious, direct. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify identity for account access. Once identity is confirmed, transfer_to_human_agents with context 'customer request for assistance with overcharges' and user_id 'mary.johnson8773@email.com' to ensure the customer receives the necessary support in resolving billing discrepancies.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"context": "customer request for assistance with overcharges", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC136",
        instruction="Your name is James Jones and your email is james.jones6884@email.com. You are organized, direct. First, verify the identity of Michael Davis using the email michael.davis9122@email.com to ensure secure access to his account information. Once his identity is confirmed, proceed to lookup_customer_by_phone using Michael Davis's registered phone number to retrieve his customer ID. This process ensures that you have the correct details to manage his account effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "registered_phone_number_of_michael_davis", "user_id": "TC136"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are polite, direct. First, perform a Lookup_customer_by_phone to retrieve the customer record using Robert Brown’s phone number. Then, proceed to Get_customer_lines for Robert Brown to list all active lines on his account. Finally, use Get_line_details for line L12345 to check its current status and plan details, as there have been concerns about its usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number", "user_id": "TC120"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC120", "user_id": "TC120"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L12345", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are patient, flexible, confident. First, lookup the customer by phone number \"555-1234\" to verify identity and retrieve account details for John Johnson. Once his identity is confirmed, proceed to get the bill details for the account associated with John Johnson to review the current balance and due date. If you find that the account is overdue, suspend the line with line ID \"L456\" for John Johnson due to non-payment, ensuring the action is reversible within 30 days.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC001"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_name": "John Johnson", "user_id": "TC001"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "reason": "non-payment", "user_id": "TC001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is John Miller and your email is john.miller2529@email.com. You are independent, direct, logical, organized. First, perform a lookup_customer_by_phone with phone number 555-1234 to verify the identity of Robert Johnson. Once his identity is confirmed, proceed to get_bill_details for customer ID C9087 to review his latest bill and payment status. This sequence is crucial to ensure accuracy before taking further action regarding any outstanding issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC072"}
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
        user_id="TC071",
        instruction="Your name is Robert Jones and your email is robert.jones6549@email.com. You are cautious, patient. First, lookup_customer_by_phone using the phone number associated with user Mary Johnson to verify her identity. Once her identity is confirmed, proceed to get_customer_lines for Mary Johnson to list her active phone lines. This process ensures that we have the correct customer information before accessing her account details, maintaining security and accuracy in managing her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Mary Johnson's phone number", "user_id": "TC071"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Mary Johnson", "user_id": "TC071"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are polite, confident. First, lookup customer by phone using Jennifer Brown's phone number to verify her identity. Once her identity is verified, proceed to get customer lines for Jennifer Brown's account. This sequence ensures that you are accessing the correct account information and maintaining data privacy, which is crucial in a telecom business setting.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Brown's phone number", "user_id": "TC062"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC062", "user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC092",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are patient, organized, confident, logical. First, verify customer identity for Patricia Williams using the email patricia.williams2585@email.com to ensure secure access to her account. Once verified, proceed to get bill details for the current billing cycle for Patricia Williams to review recent charges. This will help her understand any discrepancies before deciding if further assistance is needed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "patricia.williams2585@email.com", "user_id": "TC092"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "patricia.williams2585@email.com", "user_id": "TC092"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are confident, logical. First, lookup_customer_by_phone with phone_number: \"555-0123\" to verify the identity of Michael Jones. Once verified, proceed to get_customer_lines for customer_id: \"C4016\" to retrieve all active lines associated with Michael Jones. After identifying the relevant line, use get_line_details for line_id: \"L7890\" to check the current plan and usage details, ensuring that the customer is on the appropriate plan and determine if any adjustments are necessary.",
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
        user_id="TC091",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are polite, independent. First, lookup_customer_by_phone with phone_number \"800-555-0199\" to verify Linda Miller's account. Once her account is verified, proceed to get_customer_lines for customer_id \"C1001\" to retrieve all active lines associated with Linda Miller, ensuring you have a comprehensive view of her services. Finally, use get_line_details for line_id \"L2002\" to check the current status and plan details for Linda Miller's primary line, allowing you to provide her with accurate and up-to-date information about her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "800-555-0199"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC091"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L2002"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are independent, polite, direct. Verify the identity of user James Jones using his email address james.jones7788@email.com before granting account access. Once verified, retrieve the bill details for the customer ID associated with James Jones to review any outstanding balance. Calculate the total amount due for James Jones's account, including any pending charges or late fees, to provide a comprehensive overview of his financial obligations.",
        actions=[
            Action(
                name="think",
                kwargs={"thought": "Verify the identity of James Jones using his email address before accessing account details."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Retrieve the bill details for the customer ID associated with James Jones to review any outstanding balance."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC106"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Calculate the total amount due for James Jones's account, including any pending charges or late fees."}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["outstanding_balance", "pending_charges", "late_fees"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are organized, patient. First, lookup customer by phone number 555-1234 to retrieve customer account details to ensure you have the correct account information. Once you have confirmed the account, get customer lines for the account associated with Robert Johnson to list all active lines and identify the specific line you need to focus on. Then, calculate data usage for line ID L001 to determine if additional data is needed, ensuring the customer is on the most suitable plan for their usage.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC072"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Robert Johnson", "user_id": "TC072"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L001", "user_id": "TC072"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "data_usage", "line_id": "L001", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC108",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are patient, direct, flexible, optimistic. Suspend_line for line ID L123456 due to reported lost phone",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC108", "line_id": "L123456", "reason": "reported lost phone"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are flexible, direct, cautious. First, verify the identity of user Jennifer Davis using her email jennifer.davis3568@email.com to ensure you are accessing the correct account. Once her identity is confirmed, proceed to get_customer_lines for Jennifer Davis to retrieve all active lines on her account. After identifying the specific line, get_line_details for line ID L001 to check its current status and plan details. If everything is in order and there is a valid request from Jennifer, suspend_line for line ID L001 with the reason \"customer request\" and document the action taken for future reference.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC085", "email": "jennifer.davis3568@email.com"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC085", "line_id": "L001"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC085", "line_id": "L001", "reason": "customer request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC006",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are patient, optimistic. Check if line L1234 is currently active or suspended using get_line_details tool.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC006", "line_id": "L1234"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC048",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are cautious, organized. Lookup customer by phone number 123-456-7890 to retrieve account ID for Linda Davis, then get customer lines associated with the retrieved account ID to view active services. This will help ensure that all active services are correctly accounted for and managed effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC048"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_placeholder", "user_id": "TC048"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are flexible, organized, optimistic. Check the billing status for Linda Miller's account with customer ID to view recent payments and outstanding balance.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC091", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC035",
        instruction="Your name is Michael Garcia and your email is michael.garcia8786@email.com. You are polite, cautious, confident. Get_bill_details for Linda Davis using her customer ID to review the last bill and outstanding balance.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC035"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC001",
        instruction="Your name is Linda Smith and your email is linda.smith7771@email.com. You are polite, independent, logical. lookup_customer_by_phone with phone_number \"555-1234\" to verify customer identity for John Johnson",
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
        user_id="TC145",
        instruction="Your name is Jennifer Miller and your email is jennifer.miller7721@email.com. You are independent, confident, logical, cautious. Verify customer identity using email james.brown3113@email.com for account access. Once verified, lookup_customer_by_phone using the phone number associated with James Brown to retrieve the customer ID. With the obtained customer ID, get_customer_lines to list all active lines associated with the account. This process ensures secure access and provides a comprehensive view of the customer's active services, crucial for managing account queries or updates in a telecom setting.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "james.brown3113@email.com", "user_id": "TC145"}
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
        user_id="TC141",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are optimistic, organized. First, verify the identity of Linda Garcia using her email address (linda.garcia2678@email.com) to ensure secure access to her account details. Once her identity is confirmed, retrieve Linda Garcia's current bill details using get_bill_details with her account ID to review and understand her current charges as part of the monthly billing cycle for our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.garcia2678@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "account_id_from_previous_step", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are logical, organized, patient, cautious. request plan change for line ID L7890 to \"Unlimited Data Plan\" effective next billing cycle",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC096"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC096", "line_id": "L7890"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC096", "reason": "Request plan change for line ID L7890 to 'Unlimited Data Plan' effective next billing cycle"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC072",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are direct, optimistic. First, lookup_customer_by_phone with phone_number \"555-1234\" to retrieve customer account details for Robert Johnson. Once you have the account details, use the customer_id \"C9087\" to get_customer_lines and list all active lines associated with Robert Johnson's account. Finally, focus on Robert Johnson's primary line by using get_line_details with line_id \"L7890\" to check the current plan and usage, and calculate remaining data allowance for line_id \"L7890\" based on current usage and plan limits. This will help Robert understand his current data usage and manage his plan effectively.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC072"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC072", "user_id": "TC072"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L7890", "user_id": "TC072"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC130",
        instruction="Your name is Patricia Miller and your email is patricia.miller3252@email.com. You are organized, patient, optimistic. First, retrieve the customer lines for customer ID C123 to list all active lines and ensure you have the correct line information. Next, check the line details for line ID L456 to verify the current plan and usage details, confirming if the line is active and in use. If the line is reported lost or stolen, proceed to suspend the line L456, ensuring that the customer is informed about the suspension and the steps to resume the line if it is found within 30 days to avoid disconnection.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC130", "user_id": "TC130"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC130"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "user_id": "TC130", "reason": "Reported lost or stolen"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Mary Jones and your email is mary.jones9465@email.com. You are polite, optimistic, flexible. First, lookup the customer by phone number 555-1234 to retrieve the account ID and associated information. Next, get the bill details for the account ID from the lookup to review outstanding charges and payment history. Finally, calculate the total amount due, including any late fees, for the account ID from the previous lookup. This process will help ensure that the customer is informed of their current financial obligations with our telecom service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC082"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "account_id_from_lookup", "user_id": "TC082"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "total_due", "account_id": "account_id_from_lookup", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are patient, cautious, confident, direct. First, lookup customer by phone number 555-1234 to verify John Davis's account identity. Once his identity is confirmed, retrieve the customer lines for John Davis's account using the customer ID obtained from the identity verification process. After obtaining the line details, proceed to suspend the line with line ID L001 associated with John Davis's account due to reported issues, ensuring minimal disruption to his service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC074"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC074", "user_id": "TC074"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L001", "reason": "Reported issues", "user_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC104",
        instruction="Your name is Michael Miller and your email is michael.miller4797@email.com. You are polite, independent, logical, optimistic. Begin by verifying the identity of user John Miller using the email john.miller2529@email.com to ensure you are accessing the correct account. Once verified, proceed to look up the customer by phone to retrieve John Miller's account details, which will provide you with an overview of his account status and associated information. After obtaining the account details, get the customer lines for John Miller's account to list all active services, allowing you to understand the services currently in use. This sequential approach will help ensure that John Miller's account is accurately reviewed and managed within the telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "john.miller2529@email.com", "user_id": "TC104"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"email": "john.miller2529@email.com", "user_id": "TC104"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC063",
        instruction="Your name is Michael Davis and your email is michael.davis7894@email.com. You are organized, cautious, direct, patient. Lookup_customer_by_phone with phone number 555-1234 to verify Mary's identity and retrieve account information. Once you have the account information, use the retrieved account ID to Get_customer_lines and list all active lines under Mary's account. After identifying the active lines, focus on line ID 9876 and Get_line_details to check the current plan and data usage details. This sequence will help ensure that Mary's account information is accurate and up-to-date, and allows you to assess whether a data refill is needed based on the current usage of line ID 9876.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC063"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC063"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "9876", "user_id": "TC063"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC106",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are organized, direct. Get_line_details for line ID L123 associated with James Jones to check current plan and usage details.",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC106", "line_id": "L123"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are confident, polite, organized. First, lookup_customer_by_phone using Michael Williams' phone number to retrieve his account details. Once you have the account details, proceed to get_customer_lines for Michael Williams' account to list all active lines. This will help you verify the number of active lines associated with his account and ensure that all services are correctly provisioned.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Williams' phone number", "user_id": "TC007"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "account_id_retrieved_from_previous_call", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC147",
        instruction="Your name is James Jones and your email is james.jones7788@email.com. You are logical, organized, patient, independent. First, lookup_customer_by_phone with phone number '555-123-4567' for user Mary Jones to verify identity, ensuring that you have the correct customer before proceeding. Once verified, get_bill_details for the account associated with Mary Jones to review her recent billing history, which will help in understanding any discrepancies or patterns in her billing cycle.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC147"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Patricia Brown and your email is patricia.brown2967@email.com. You are cautious, confident, optimistic. First, lookup customer by phone using Michael Garcia's phone number to verify identity, ensuring that you have the correct account details. Once verified, get customer lines for Michael Garcia to list all associated mobile numbers, which will help in identifying the primary line. Finally, get line details for the primary line associated with Michael Garcia to review current plan and usage, allowing you to provide accurate information about his service and address any potential concerns he may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Garcia's phone number", "user_id": "TC039"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC039", "user_id": "TC039"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "primary_line_id", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC146",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are logical, optimistic, polite. Please lookup_customer_by_phone with phone_number: '555-1234' to verify the identity of Linda Smith. Once verified, proceed to get_customer_lines for the account associated with the customer ID retrieved from the previous step. This will help us ensure that the correct lines are being managed and billed accurately, supporting our goal of providing excellent customer service in the telecom industry.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC146"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC146", "user_id": "TC146"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is Robert Garcia and your email is robert.garcia8578@email.com. You are optimistic, polite. First, verify the identity of user Jennifer Jones using her email jennifer.jones5314@email.com to access her account. Once her identity is confirmed, use lookup_customer_by_phone with the phone number associated with Jennifer Jones to retrieve her customer ID. After obtaining the customer ID, proceed to get_customer_lines for the retrieved customer ID to list all active lines on Jennifer Jones' account. This process will help ensure that we have accurate information about her account and can assist her effectively with any telecom-related inquiries or updates she may need.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.jones5314@email.com", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC082", "user_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC089",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are flexible, optimistic, polite. First, lookup_customer_by_phone with phone number 555-1234 to verify the identity of James Brown, ensuring that you have the correct customer details. Once verified, proceed to get_bill_details for the user ID obtained from the identity verification to review recent charges. This will help you provide James with accurate billing information and assist him with any questions he may have regarding his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC089"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC131",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are organized, logical, direct, patient. First, lookup_customer_by_phone with phone number '555-1234' to verify account access for Jennifer Williams. Once her account access is confirmed, proceed to get_bill_details for user ID 'U6918' to review recent charges and payments. This will ensure that Jennifer Williams has the correct information regarding her billing and any recent transactions with our telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "U6918"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC073",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are direct, independent, logical, confident. \"lookup_customer_by_phone with phone number 555-1234 to verify identity of Robert Brown\"",
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
        user_id="TC144",
        instruction="Your name is Patricia Smith and your email is patricia.smith7071@email.com. You are cautious, direct, flexible, organized. First, lookup customer by phone number to retrieve Robert Jones' account ID. Once you have the account ID, get customer lines using this ID to list all active lines associated with Robert Jones. Finally, get bill details for the current billing cycle to review charges and payment status for Robert Jones. This process will help ensure that Robert Jones' account is up-to-date and that all active lines are correctly billed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "customer_phone_number", "user_id": "TC144"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "retrieved_account_id", "user_id": "TC144"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "retrieved_account_id", "billing_cycle": "current", "user_id": "TC144"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC061",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are patient, polite, organized. Please suspend the secondary line on Patricia Davis's account for non-payment. After completing the suspension, get customer lines again to verify the suspension status of the secondary line. This ensures that the suspension process has been executed correctly and Patricia is informed of the status, maintaining accurate account records and customer satisfaction.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC061", "phone_number": "Patricia Davis"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC061", "line_id": "secondary_line_id"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC061"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Linda Johnson and your email is linda.johnson5357@email.com. You are direct, flexible. suspend_line for line_id \"L7890\" to temporarily suspend service due to non-payment",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC096", "line_id": "L7890"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Linda Miller and your email is linda.miller7970@email.com. You are independent, optimistic, polite. lookup_customer_by_phone with phone_number \"555-1234\" to verify Linda Garcia's account.",
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
        user_id="TC096",
        instruction="Your name is John Johnson and your email is john.johnson9055@email.com. You are optimistic, confident. First, lookup_customer_by_phone(phone_number=\"555-123-4567\") to identify the customer associated with this number. Once you have the customer details, proceed to get_customer_lines(customer_id=\"CUST12345\") to review all active lines under their account. After identifying the specific line that requires action, get_line_details(line_id=\"LINE6789\") to verify its current status and usage. If the customer has requested to temporarily halt services, suspend_line(line_id=\"LINE6789\", reason=\"Customer Request\") to ensure their needs are met promptly and efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC096"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE6789"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "LINE6789", "reason": "Customer Request"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC074",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are direct, flexible, organized. Lookup customer by phone number 555-1234 to verify John Davis's identity.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC074"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC019",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are logical, patient, independent. First, use the lookup_customer_by_phone task with phone_number \"555-1234\" to verify Linda Miller's account. Once her account is verified, proceed with the get_customer_lines task using customer_id \"C10234\" to retrieve all active lines associated with Linda Miller. After identifying the active lines, use the get_line_details task with line_id \"L98765\" to check the current plan and usage for Linda Miller's primary line. These steps will help ensure that we have accurate and up-to-date information regarding Linda Miller's account and usage, which is crucial for providing excellent customer service and addressing any potential issues with her telecom services.",
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
                kwargs={"line_id": "L98765"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC018",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are direct, confident. First, lookup_customer_by_phone with the phone_number provided by John Garcia during verification to identify the customer. Once you have retrieved the customer_id from this initial lookup, proceed to get_customer_lines using the customer_id to review the active lines associated with this customer. Finally, get_bill_details with the same customer_id to access the billing information and think with the context to determine if any overdue amounts exist based on the bill details. This process will help ensure that any outstanding issues are identified and addressed promptly in our telecom system.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "provided_by_John_Garcia", "user_id": "TC018"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC018", "user_id": "TC018"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC018", "user_id": "TC018"}
            ),
            Action(
                name="think",
                kwargs={"context": "Review the bill details to determine if there are any overdue amounts."}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is James Brown and your email is james.brown3113@email.com. You are logical, confident, optimistic, direct. get_bill_details for Patricia Johnson to review outstanding balance and due date",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC096"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC015",
        instruction="Your name is Michael Davis and your email is michael.davis9122@email.com. You are cautious, optimistic. First, lookup customer by phone number 555-1234 to retrieve John Garcia's account information. Once you have accessed his account, proceed to get customer lines for John Garcia's account to list all active lines. This will help ensure that you have a comprehensive view of his services before making any further assessments or decisions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC015"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "John Garcia's Account ID", "user_id": "TC015"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC102",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are optimistic, confident. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Mary Miller's identity. Once verified, proceed to get_customer_lines for customer_id \"C001\" to retrieve her active lines. Then, get_line_details with line_id \"L123\" to check the current plan and usage details, ensuring that Mary Miller's data needs are being adequately met.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC102"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC102", "user_id": "TC102"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L123", "user_id": "TC102"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are patient, direct, optimistic. First, lookup customer by phone number 555-0123 to retrieve account information. Once you have the account details, proceed to get customer lines for the account associated with phone number 555-0123. If you find that the customer has requested a temporary hold on one of their lines, suspend the line with line ID L456. This action is in response to the customer's request for a temporary hold, ensuring their service can be paused without penalty.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC062"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"phone_number": "555-0123", "user_id": "TC062"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L456", "user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are organized, flexible. First, use lookup_customer_by_phone with phone number \"555-1234\" to verify the identity of John Smith. Once his identity is confirmed, get_bill_details for the user ID associated with John Smith to review recent charges and payment status. This will ensure that you have all the necessary information to assist him effectively with any billing inquiries he may have.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC148",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are organized, direct, confident, independent. First, verify customer identity for Jennifer Davis using email jennifer.davis4933@email.com to ensure compliance with security protocols. Once identity verification is successful, lookup customer by phone number to retrieve account details for Jennifer Davis to understand her service plan and account status. Finally, get customer lines associated with Jennifer Davis's account to review active services and assess any potential issues or opportunities for service upgrades.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.davis4933@email.com", "user_id": "TC148"}
            ),
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890", "user_id": "TC148"}
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
        user_id="TC141",
        instruction="Your name is Robert Brown and your email is robert.brown5816@email.com. You are logical, confident, flexible, patient. First, use the lookup_customer_by_phone task with the parameter phone='555-123-4567' to verify the identity of Linda Garcia. Once her identity is confirmed, proceed with the get_customer_lines task using the parameter customer_id='C001' to retrieve all active lines associated with her account. After identifying her active lines, utilize the get_bill_details task with parameters customer_id='C001' and billing_cycle='2023-10' to review her current charges for the specified billing cycle. This sequence will ensure you have verified Linda's identity, understood her active services, and can discuss her billing details accurately.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC141"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC141", "billing_cycle": "2023-10"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Linda Garcia and your email is linda.garcia2678@email.com. You are polite, confident. \"lookup_customer_by_phone with phone number '555-1234' to verify identity of Jennifer Smith\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC023"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are independent, polite, organized, flexible. First, verify the identity of user Robert Brown using email robert.brown6285@email.com before granting any account access. Once his identity is confirmed, proceed to check the current billing details for Robert Brown’s account using the get_bill_details tool to ensure all information is accurate and up-to-date. This process is crucial to maintain the integrity of our telecom services and to provide Robert with the best possible customer experience.",
        actions=[
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC150",
        instruction="Your name is Mary Smith and your email is mary.smith4137@email.com. You are optimistic, organized. First, verify the identity of user Linda Davis using email linda.davis8880@email.com to ensure you are accessing the correct account. Once her identity is confirmed, retrieve all active lines for Linda Davis's account to get an overview of her current services. Then, get details for line L9876 on Linda Davis's account to check data usage, as this will help determine if a data refill is needed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis8880@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC150"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC150", "line_id": "L9876"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Jennifer Brown and your email is jennifer.brown9346@email.com. You are independent, organized, cautious, confident. First, perform a lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify Michael Davis's identity. Once his identity is confirmed, proceed to get_line_details for line_id: \"L5678\" to check his current plan and usage. This will help us understand if an upgrade is necessary based on his usage patterns.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L5678", "user_id": "TC069"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC134",
        instruction="Your name is Patricia Brown and your email is patricia.brown6169@email.com. You are organized, direct. Get_customer_lines using the retrieved customer ID to list all active and suspended lines under Michael Johnson's account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Johnson's phone number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC134"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC091",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are polite, cautious, logical, independent. First, lookup_customer_by_phone with phone number 555-123-4567 to verify identity for linda.miller7970@email.com, as she has reported a lost phone. Once her identity is verified, proceed to get_customer_lines for customer ID C001 to identify all active lines under her account. After identifying the specific line in question, get_line_details for line ID L101 to check the current plan and usage. Finally, suspend_line for line ID L101 due to the reported lost phone, ensuring that Linda Miller is aware of the 30-day resume policy and any implications on her service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC091"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L101"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L101", "user_id": "TC091"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC082",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are logical, optimistic, independent. First, perform a lookup_customer_by_phone with phone_number \"555-1234\" to verify the customer's identity for account access. Once identity is confirmed, proceed to suspend_line for line_id \"L204\" with reason \"customer request\" due to a lost phone. After the suspension, conduct a get_customer_lines for customer_id \"C102\" to verify if there are any suspended lines that need resumption, ensuring all customer needs are addressed efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L204", "reason": "customer request", "user_id": "TC082"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC082"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is Patricia Smith and your email is patricia.smith8398@email.com. You are independent, optimistic, logical. First, verify Mary Johnson's identity using the email mary.johnson8773@email.com to access her account details. Once her identity is confirmed, proceed to get_bill_details for the current billing cycle to inform Mary Johnson about her outstanding balance. This process ensures that Mary is aware of her current financial obligations with our telecom services and can make timely payments.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "mary.johnson8773@email.com", "user_id": "TC093"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"email": "mary.johnson8773@email.com", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC036",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are independent, confident. First, lookup the customer by phone using the phone number associated with Robert Brown's account to retrieve his account details. Once you have located the account, verify Robert Brown's identity using his email robert.brown6285@email.com to ensure secure access. After successful identity verification, proceed to get customer lines for Robert Brown's account to review the active lines he currently holds.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number", "user_id": "TC036"}
            ),
            Action(
                name="think",
                kwargs={"thought": "Verify Robert Brown's identity using his email."}
            ),
            Action(
                name="think",
                kwargs={"thought": "Ensure the email matches: robert.brown6285@email.com."}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"account_id": "Robert Brown's account ID", "user_id": "TC036"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are logical, independent, polite. lookup_customer_by_phone with phone_number \"+1234567890\" to verify customer identity for Michael Jones",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "+1234567890", "user_id": "TC042"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are logical, patient. Lookup_customer_by_phone using phone number associated with Michael Johnson to verify identity for account access. Once verified, proceed to Get_customer_lines for Michael Johnson's account to review active lines. This will help ensure that all active lines are correctly accounted for and assist in resolving any customer inquiries regarding their telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Michael Johnson's phone number", "user_id": "TC133"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC133", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC020",
        instruction="Your name is James Johnson and your email is james.johnson2916@email.com. You are independent, organized. Lookup customer by phone number 555-0123 to verify identity for Mary Davis. After verifying her identity, get customer lines for Mary Davis to list active services, ensuring she receives accurate information about her current telecom subscriptions.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC020"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Mary Davis", "user_id": "TC020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are organized, independent, flexible. First, use the lookup_customer_by_phone with phone number '555-123-4567' to verify the customer's identity. Once verified, proceed to get_customer_lines for customer ID 'C12345' to list all active lines associated with the customer. This process ensures that you have the correct customer and can accurately manage their telecom services.",
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
        user_id="TC147",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are independent, organized, direct, logical. First, lookup_customer_by_phone with phone number \"555-123-4567\" to verify the identity of Mary Jones. Once her identity is confirmed, get_customer_lines for the customer ID retrieved to list all active lines under her account. After identifying the active lines, suspend_line for line ID \"L98765\" due to a reported loss by Mary Jones.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC147"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L98765", "reason": "Reported loss", "user_id": "TC147"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC065",
        instruction="Your name is Michael Williams and your email is michael.williams1902@email.com. You are independent, polite, optimistic, flexible. First, perform a lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of the customer requesting account access. Once the identity is confirmed, proceed to get_customer_lines for customer_id \"C1001\" to retrieve all active lines on the account. After identifying the specific line in question, execute suspend_line for line_id \"L2002\" with reason \"Customer Request\" and note \"Temporary suspension requested by James Davis\" to fulfill the customer's request for a temporary suspension of service.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC065"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L2002", "reason": "Customer Request", "note": "Temporary suspension requested by James Davis", "user_id": "TC065"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis7195@email.com. You are organized, independent. First, lookup_customer_by_phone using phone_number '555-0123' to verify Michael Garcia's identity, ensuring you are assisting the correct customer. Once verified, get_bill_details for billing_period '2023-09' to review charges and payments, providing Michael with a clear understanding of his current billing status.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC039"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"billing_period": "2023-09", "user_id": "TC039"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is Mary Brown and your email is mary.brown4135@email.com. You are logical, polite, flexible. First, perform a lookup_customer_by_phone with phone_number \"555-123-4567\" to verify the identity of John Williams, a valued customer who has contacted us regarding his account. Once his identity is confirmed, proceed to get_customer_lines for customer_id \"CUST-8933\" to retrieve all active lines associated with him. This will help us ensure that we have the correct information on his account and can assist him effectively with any inquiries about his telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC098"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC098", "user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC039",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are organized, cautious. Use lookup_customer_by_phone with phone_number: \"555-123-4567\" to verify user identity.",
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
        instruction="Your name is Linda Davis and your email is linda.davis3121@email.com. You are independent, cautious, optimistic. First, verify customer identity for user Linda Davis using email linda.davis4055@email.com to ensure the correct account is being accessed. Once identity verification is complete, suspend line L001 for Linda Davis due to the reported loss of the device. This will prevent unauthorized use of the line. If there are any further questions or concerns regarding the suspension or related billing inquiries, transfer to human agents to provide personalized assistance.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "linda.davis4055@email.com"}
            ),
            Action(
                name="suspend_line",
                kwargs={"user_id": "TC048", "line_id": "L001"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"user_id": "TC048", "issue": "suspension and billing inquiries"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC141",
        instruction="Your name is Jennifer Williams and your email is jennifer.williams6918@email.com. You are confident, cautious, independent, patient. First, perform a lookup_customer_by_phone using the phone number associated with Linda Garcia's account to verify her identity. Once her identity is verified, proceed to get_customer_lines for Linda Garcia's account to retrieve all active lines. This will help ensure that you have the most accurate and up-to-date information about her account before any further actions are taken.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Garcia's phone number", "user_id": "TC141"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC141", "user_id": "TC141"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC080",
        instruction="Your name is Patricia Brown and your email is patricia.brown8933@email.com. You are confident, organized, polite, direct. lookup_customer_by_phone with phone_number \"555-0123\" for user Robert Williams",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC080"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC098",
        instruction="Your name is John Smith and your email is john.smith6987@email.com. You are direct, cautious. First, lookup_customer_by_phone with phone_number '555-0123' to verify John Williams' account access. Once verified, calculate data usage for line_id 'L2001' to determine the remaining data balance. This will help ensure that John Williams has accurate information before discussing any potential plan upgrade options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC098"}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "data_usage", "line_id": "L2001", "user_id": "TC098"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC085",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are optimistic, organized. Retrieve detailed information for line L001 on Jennifer Davis's account to check the current plan and usage. Then, calculate the total data usage for line L001 for the current billing cycle. This will help ensure that Jennifer Davis is on the most suitable plan and identify if she might benefit from any available data refill options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC085", "email": "robert.brown4015@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC085"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC085", "line_id": "L001"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC085", "line_id": "L001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC093",
        instruction="Your name is Robert Brown and your email is robert.brown4015@email.com. You are logical, polite, flexible. Get_customer_lines for Mary Johnson's account to list all active lines.",
        actions=[
            Action(
                name="get_customer_lines",
                kwargs={"customer_name": "Mary Johnson", "user_id": "TC093"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Robert Brown and your email is robert.brown4954@email.com. You are cautious, logical, confident, independent. \"lookup_customer_by_phone with phone number '555-0123' to verify identity for Patricia Brown\"",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC056"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC042",
        instruction="Your name is Robert Brown and your email is robert.brown6285@email.com. You are cautious, flexible, patient. First, verify the identity of the user Michael Jones using email michael.jones4016@email.com to access account details. Once verified, retrieve bill details for the current billing cycle for Michael Jones to review charges and payment status. After reviewing the charges, calculate the total outstanding balance on Michael Jones's account to assist with payment processing.",
        actions=[
            Action(
                name="think",
                kwargs={"message": "Verify the identity of Michael Jones using his email."}
            ),
            Action(
                name="think",
                kwargs={"message": "Once verified, retrieve bill details for the current billing cycle."}
            ),
            Action(
                name="get_bill_details",
                kwargs={"user_id": "TC042"}
            ),
            Action(
                name="think",
                kwargs={"message": "Calculate the total outstanding balance on Michael Jones's account."}
            ),
            Action(
                name="calculate",
                kwargs={"operation": "sum", "values": ["charges", "fees", "taxes"]}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC101",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith8259@email.com. You are direct, confident, flexible, independent. First, lookup_customer_by_phone with phone_number '555-123-4567' to verify James Johnson's account. Once verified, proceed to get_customer_lines for customer_id 'C2916' to retrieve active lines on James Johnson's account. Finally, use get_line_details for line_id 'L1001' to check the current plan and data usage, ensuring James is on the most suitable plan for his needs.",
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
                kwargs={"line_id": "L1001"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are confident, optimistic, polite, organized. First, lookup_customer_by_phone with the phone number associated with Linda Davis to verify account access. Once access is confirmed, proceed to get_customer_lines for Linda Davis using her customer ID to list all active lines on the account. Finally, get_bill_details for Linda Davis using her customer ID to review recent billing information and payment status, ensuring her account is up to date and there are no outstanding issues.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Linda Davis's phone number", "user_id": "TC107"}
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
        user_id="TC071",
        instruction="Your name is Jennifer Smith and your email is jennifer.smith9988@email.com. You are patient, confident, logical, cautious. lookup_customer_by_phone with phone_number \"123-456-7890\" to verify identity of user Mary Johnson",
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
        user_id="TC019",
        instruction="Your name is Mary Johnson and your email is mary.johnson4713@email.com. You are direct, confident. First, lookup_customer_by_phone with phone_number='555-0163' to verify Linda Miller's identity. Once her identity is confirmed, proceed to get_customer_lines for user_id='linda.miller1663@email.com' to retrieve all active lines associated with her account. This will help ensure that we have the correct information to assist her with any inquiries or issues regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0163"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "linda.miller1663@email.com"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC062",
        instruction="Your name is John Garcia and your email is john.garcia3458@email.com. You are flexible, optimistic, direct. First, perform a lookup_customer_by_phone with the phone number associated with Jennifer Brown to verify her identity. Once verified, proceed to get_customer_lines for the customer ID retrieved during verification to list all active lines under her account. After identifying the active lines, use the get_bill_details task for the same customer ID to review her outstanding balance and recent payments. If you find that there is a non-payment issue, you may need to suspend_line for line ID L002, but only after confirming the non-payment status with Jennifer Brown.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Jennifer Brown's Phone Number", "user_id": "TC062"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC062", "user_id": "TC062"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC062", "user_id": "TC062"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC069",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones9861@email.com. You are optimistic, independent. First, lookup_customer_by_phone with phone number '555-1234-5678' to verify customer identity. Once the customer's identity is confirmed, proceed to suspend_line for line ID 'L4567' with reason 'customer request' to temporarily suspend service. This sequence ensures that the suspension is authorized and aligns with the customer's needs, maintaining service integrity and customer satisfaction.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234-5678"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L4567", "reason": "customer request", "user_id": "TC069"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC138",
        instruction="Your name is Jennifer Davis and your email is jennifer.davis4933@email.com. You are confident, flexible, cautious, independent. First, lookup customer by phone number 555-1234 to retrieve account ID for Mary Smith. Once you have the account ID, get bill details for account ID C7890 to check the outstanding balance and due date. This will help you assist Mary Smith effectively in understanding her current billing status and prepare for any further actions needed.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC138"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "C7890", "user_id": "TC138"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC096",
        instruction="Your name is Jennifer Jones and your email is jennifer.jones5314@email.com. You are confident, polite, logical, organized. First, lookup_customer_by_phone using Patricia Johnson's phone number to verify her identity as part of a routine security check. Once her identity is confirmed, proceed to get_customer_lines for Patricia Johnson to retrieve all active lines under her account. This process ensures that we have accurate information before discussing any account-specific details with her.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Patricia Johnson's phone number", "user_id": "TC096"}
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
        user_id="TC067",
        instruction="Your name is Michael Jones and your email is michael.jones4016@email.com. You are flexible, confident, polite. First, verify customer identity using email robert.williams8770@email.com to access account details. Once verified, get_bill_details for billing account B98765 to check outstanding balance and payment history. Then, calculate total amount due using the outstanding balance and any applicable late fees for billing account B98765.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "robert.williams8770@email.com"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"billing_account": "B98765", "user_id": "TC067"}
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
        user_id="TC069",
        instruction="Your name is James Davis and your email is james.davis6038@email.com. You are logical, organized. First, lookup_customer_by_phone with phone_number \"555-0123\" to verify identity for account access. Once the identity is confirmed, get_bill_details for customer_id \"C7894\" to review the outstanding balance and payment history. This sequence ensures that you have the necessary customer information and context before proceeding with any further actions related to their telecom account.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-0123", "user_id": "TC069"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC069", "user_id": "TC069"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC060",
        instruction="Your name is Michael Smith and your email is michael.smith4429@email.com. You are logical, confident. Lookup_customer_by_phone(phone_number=\"555-123-4567\") to verify Linda Johnson's identity and access her account.",
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
        user_id="TC108",
        instruction="Your name is John Williams and your email is john.williams4633@email.com. You are logical, organized, independent, polite. Suspend the line with line ID L2023 due to a payment issue and notify Jennifer Miller, the account holder, about this suspension. Once the payment is confirmed within the 30-day suspension period, promptly resume the line with line ID L2023. Ensure that Jennifer Miller is informed of the successful line resumption and updated account status via email to maintain transparency and customer satisfaction.",
        actions=[
            Action(
                name="suspend_line",
                kwargs={"line_id": "L2023", "reason": "payment issue", "user_id": "TC108"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"message": "Notify Jennifer Miller about the suspension of line ID L2023 due to a payment issue. Email: john.williams4633@email.com", "user_id": "TC108"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC023",
        instruction="Your name is Patricia Williams and your email is patricia.williams2585@email.com. You are optimistic, logical, organized, patient. Please lookup_customer_by_phone with phone number 555-123-4567 to verify Jennifer Smith's account access as she has reported an issue with her service. Once her account access is confirmed, proceed to get_customer_lines for customer ID C102 to retrieve all active lines associated with Jennifer Smith. This will help us ensure that all her services are functioning correctly and address any discrepancies she may be experiencing.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567", "user_id": "TC023"}
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
        user_id="TC060",
        instruction="Your name is Michael Johnson and your email is michael.johnson4265@email.com. You are logical, organized, polite, direct. get_line_details for line_id \"L67890\" to verify eligibility for plan upgrade",
        actions=[
            Action(
                name="get_line_details",
                kwargs={"line_id": "L67890", "user_id": "TC060"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Patricia Johnson and your email is patricia.johnson6047@email.com. You are direct, logical. First, lookup_customer_by_phone with phone_number \"555-123-4567\" to verify Mary's account details. Once verification is complete and it's confirmed that Mary has an outstanding balance, proceed to suspend_line for line_id \"L67890\" due to non-payment, ensuring that Mary is informed of the suspension and any necessary steps she needs to take to resolve the issue.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-123-4567"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "reason": "Non-payment", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC040",
        instruction="Your name is Linda Davis and your email is linda.davis5049@email.com. You are cautious, patient, polite. Get details of Patricia Brown's current plan to compare available upgrade options.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"user_id": "TC040", "phone_number": "Patricia's Phone Number"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC040"}
            ),
            Action(
                name="get_line_details",
                kwargs={"user_id": "TC040", "line_id": "Line ID from previous step"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC013",
        instruction="Your name is Robert Jones and your email is robert.jones5323@email.com. You are confident, optimistic, polite. lookup_customer_by_phone with phone number \"555-123-4567\" to verify identity for Mary Jones",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone": "555-123-4567", "user_id": "TC013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC149",
        instruction="Your name is Linda Smith and your email is linda.smith7027@email.com. You are cautious, organized, independent, direct. Verify customer identity using Jennifer Johnson's email (jennifer.johnson5907@email.com) to access account details. If Jennifer Johnson requests a temporary suspension of one of her active lines, suspend line L123 and notify her via email about the suspension.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"email": "jennifer.johnson5907@email.com"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "TC149"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L123", "user_id": "TC149"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC107",
        instruction="Your name is Robert Davis and your email is robert.davis2812@email.com. You are flexible, cautious, patient, polite. First, lookup_customer_by_phone with phone_number \"123-456-7890\" to verify Linda Davis's account and ensure all details are correct. Next, get_bill_details for customer_id \"C5049\" to review the outstanding balance and assess the situation. If there is a significant overdue amount, proceed to suspend_line for line_id \"L9876\" due to non-payment with reason \"Overdue Bill.\" Finally, transfer_to_human_agents for customer_id \"C5049\" to discuss payment options, ensuring Linda has the opportunity to resolve the issue and restore her service promptly.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"customer_id": "TC107"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L9876", "reason": "Overdue Bill"}
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={"customer_id": "TC107"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC081",
        instruction="Your name is Mary Jones and your email is mary.jones5285@email.com. You are logical, polite, independent, patient. First, lookup_customer_by_phone with phone_number \"555-1234\" to verify the identity of John Smith. Once his identity is confirmed, proceed to get_customer_lines for customer_id \"C12345\" to retrieve all active lines under John Smith's account. If John Smith requests to temporarily suspend one of his lines, suspend_line for line_id \"L67890\" with reason \"customer request\" to ensure the line is suspended as per his request.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234", "user_id": "TC081"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC081", "user_id": "TC081"}
            ),
            Action(
                name="suspend_line",
                kwargs={"line_id": "L67890", "reason": "customer request", "user_id": "TC081"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC007",
        instruction="Your name is Michael Garcia and your email is michael.garcia5750@email.com. You are optimistic, cautious, confident. First, use the lookup_customer_by_phone task with the parameter phone_number as \"555-1234\" to verify Michael Williams' identity, ensuring that you are assisting the correct customer. Once verified, proceed with the get_line_details task for line_id \"LINE456\" to check the current plan and usage, as Michael Williams has expressed concerns about high data usage and potential overage charges. This will allow you to provide accurate information and recommend any necessary adjustments to his plan.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "LINE456", "user_id": "TC007"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC133",
        instruction="Your name is Linda Davis and your email is linda.davis8880@email.com. You are patient, polite, logical, cautious. First, perform a lookup_customer_by_phone with phone_number '555-1234' to verify the identity of Michael Johnson. Once his identity is confirmed, proceed to get_line_details for line_id 'L456' to check Michael's current plan and usage. This will help you understand his current data consumption and ensure that any potential plan upgrades meet his needs.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_line_details",
                kwargs={"line_id": "L456", "user_id": "TC133"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC056",
        instruction="Your name is Robert Jones and your email is robert.jones1563@email.com. You are direct, independent. First, lookup_customer_by_phone with phone number \"555-1234\" to verify Patricia Brown's account identity. Once her identity is confirmed, proceed to get_customer_lines for user ID \"PatriciaB8933\" to retrieve all active lines associated with Patricia Brown's account. This will ensure you have the correct information to assist her with any inquiries regarding her telecom services.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "555-1234"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"user_id": "PatriciaB8933"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC016",
        instruction="Your name is Robert Brown and your email is robert.brown2463@email.com. You are cautious, logical, flexible, confident. First, lookup_customer_by_phone with phone_number='123-456-7890' to verify the identity of John Smith, who has reported an issue with his billing. Once his identity is confirmed, proceed to get_bill_details for account_id='A001' to review outstanding charges and due dates, ensuring that all information is accurate and up-to-date before discussing payment options with the customer.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "123-456-7890"}
            ),
            Action(
                name="get_bill_details",
                kwargs={"account_id": "A001", "user_id": "TC016"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="gpt-4o",
        user_id="TC120",
        instruction="Your name is Linda Garcia and your email is linda.garcia4634@email.com. You are confident, cautious, independent. First, lookup_customer_by_phone with the phone number associated with Robert Brown's account to verify his identity. Once the account is verified, proceed to get_customer_lines for the verified customer account to list all active lines. This will help ensure that Robert Brown's account details are up-to-date and allow us to address any potential issues with his telecom services efficiently.",
        actions=[
            Action(
                name="lookup_customer_by_phone",
                kwargs={"phone_number": "Robert Brown's phone number", "user_id": "TC120"}
            ),
            Action(
                name="get_customer_lines",
                kwargs={"customer_id": "TC120", "user_id": "TC120"}
            ),
        ],
        outputs=[]
    ),
]
