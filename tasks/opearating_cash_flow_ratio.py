from helpers import functions
from fastapi import HTTPException, status

def opearating_cash_flow_ratio(operating_cash_flow: int, current_liabilities: int):
    try:
        opearating_cash_flow_ratio_value = functions.opearating_cash_flow_ratio(operating_cash_flow, current_liabilities)
        return {
            "Tag": "Operating Cash Flow Ratio",
            "Operating Cash Flow": operating_cash_flow,
            "Current Liabilities": current_liabilities,
            "Opearating Cash Flow Ratio": opearating_cash_flow_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

