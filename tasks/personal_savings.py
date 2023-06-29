from helpers import functions
from fastapi import HTTPException, status

def personal_savings_task(init: int,
                     monthly: int,
                     tenure: float):
    try:
        personal_savings = functions.personal_savings(init, monthly, tenure)
        return {
            "Tag": "Simple Personal Savings",
            "Initial Deposit": init,
            "total number of years": tenure,
            "Monthly Contribution": monthly,
            "Total Amount Saved": f"{total_amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)