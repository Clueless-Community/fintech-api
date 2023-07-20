from helpers import functions
from fastapi import HTTPException, status
def calculate_lumpsum_task(principal: float, interest_rate: float, years: int):

    try:
        total_amount = principal * (
            (1 + functions.percent_to_decimal(interest_rate)) ** years
        )
        interest_earned = total_amount - principal
        return {
            "total_amount": round(total_amount, 2),
            "interest_earned": round(interest_earned, 2),
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)