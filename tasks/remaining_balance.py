from helpers import functions
from fastapi import HTTPException, status

def remaining_balance_task(
    regular_payment: float,
    interest_rate_per_period: float,
    number_of_payments: float,
    number_of_payments_done: float,
):
    try:
        B = functions.remaining_balance(
            regular_payment,
            interest_rate_per_period,
            number_of_payments,
            number_of_payments_done,
        )
        return {
            "Tag": "Remaining balance",
            "regular_payment": regular_payment,
            "interest rate per period": interest_rate_per_period,
            "number of payments": number_of_payments,
            "number of payments done": number_of_payments_done,
            "remaining balance": B,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)