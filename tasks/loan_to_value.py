from helpers import functions
from fastapi import HTTPException, status

def loan_to_value_task(mortgage_value: float, appraised_value: float):
    try:
        ratio = functions.loan_to_value(mortgage_value, appraised_value)
        return {
            "Tag": "Loan to Value (LTV) ratio",
            "Mortgage Value": mortgage_value,
            "Appraised Property Value": appraised_value,
            "Loan to Value ratio": f"{ratio}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)