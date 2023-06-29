from helpers import functions
from fastapi import HTTPException, status

def simple_interest_rate_task(amount_paid: float, principle_amount: float, months: int):
    try:
        rate = functions.simple_interest_rate(
            amount_paid, principle_amount, months)
        return {
            "Tag": "Simple Interest Rate",
            "Total amount paid": amount_paid,
            "Principle amount": principle_amount,
            "Interest Paid": amount_paid - principle_amount,
            "Interest Rate": f"{rate}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)