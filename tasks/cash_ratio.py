from helpers import functions
from fastapi import HTTPException, status

def cash_ratio(cash: float, cash_equivalents: float, current_liabilities: float):
    try:
        cash_ratio_value = functions.cash_ratio(cash,cash_equivalents,current_liabilities)
        return {
            "Tag": "Cash Ratio",
            "Cash": cash,
            "Cash Equivalents": cash_equivalents,
            "Current Liabilities":current_liabilities ,
            "Cash Ratio": cash_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
