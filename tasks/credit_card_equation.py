from helpers import functions
from fastapi import HTTPException, status

def credit_card_equation_task(
    balance: float, monthly_payment: float, daily_interest_rate: float
):
    try:
        N = functions.credit_card_equation(
            balance, monthly_payment, daily_interest_rate
        )
        return {
            "Tag": "Credit card equation",
            "Balance": balance,
            "Monthly Payment": monthly_payment,
            "daily interest rate": daily_interest_rate,
            "credit card equation": f"{N}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)