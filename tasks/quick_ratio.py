from helpers import functions
from fastapi import HTTPException, status

def quick_ratio(cash: float, accounts_receivable: float, marketable_security: float, current_liabilities: float):
    try:
        QR=functions.quick_ratio(cash, accounts_receivable, marketable_security, current_liabilities)
        return{
            "Tag": "quick_ratio",
            "Total cash as asset": cash,
            "Total recievable cash": accounts_receivable,
            "Total marketable security": marketable_security,
            "Total current liabilities": current_liabilities,
            "quick ratio":f"{QR}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
