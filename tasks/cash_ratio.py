from helpers import functions
from fastapi import HTTPException, status

def cash_ratio(cash: float, marketable_securities: float, current_liabilities: float):
    try:
        ratio=functions.cash_ratio(cash, marketable_securities, current_liabilities)
        return {
            "Tag": "cash ratio ~higher than 1 means better debt paying capacity",
            "Total cash as asset": cash,
            "marketable securities": marketable_securities,
            "Total current liabilities": current_liabilities,
            "cash ratio": "f{ratio}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

                