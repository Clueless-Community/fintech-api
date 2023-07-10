from helpers import functions
from fastapi import HTTPException, status

def future_value_of_annuity_task(
    payments_per_period: float, interest_rate: float, number_of_periods: float
):
    try:
        fva = functions.future_value_of_annuity(
            payments_per_period, interest_rate, number_of_periods
        )
        return {
            "Tag": "Future value of annuity",
            "Payments per periods": payments_per_period,
            "interest rate": interest_rate,
            "number of periods": number_of_periods,
            "future value of annuity": f"{fva}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)