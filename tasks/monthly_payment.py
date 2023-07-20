from helpers import functions
from fastapi import HTTPException, status

def monthly_payment_task(
    principal: float,
    interest_rate: float,
    number_of_periods: float,
    payments_per_period: float,
):
    try:
        monthly_pay = functions.monthly_payment(
            principal, interest_rate, number_of_periods, payments_per_period
        )
        return {
            "Tag": "Monthly Payment",
            "Principal": principal,
            "Interest Rate": interest_rate,
            "Number of Periods": number_of_periods,
            "Payments per period": payments_per_period,
            "Levered Beta": f"{monthly_pay}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)