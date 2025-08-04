# Copyright Sierra

from .calculate import Calculate
from .think import Think
from .transfer_to_human_agents import TransferToHumanAgents
from .lookup_customer_by_phone import LookupCustomerByPhone
from .get_customer_lines import GetCustomerLines
from .get_line_details import GetLineDetails
from .suspend_line import SuspendLine
from .get_bill_details import GetBillDetails


ALL_TOOLS = [
    Calculate,
    Think,
    TransferToHumanAgents,
    LookupCustomerByPhone,
    GetCustomerLines,
    GetLineDetails,
    SuspendLine,
    GetBillDetails,
]