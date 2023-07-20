from helpers import functions
from fastapi import HTTPException, status

def future_value_of_annuity_due_task(
    periodic_payment: float, number_of_periods: int, effective_interest_rate: float
):
    try:
        future_value_of_annuity_due = functions.future_value_of_annuity_due(
            periodic_payment, number_of_periods, effective_interest_rate
        )
        return {
            "Tag": "Future value of the ordinary annuity",
            "Periodic payment": periodic_payment,
            "Number of periods": number_of_periods,
            "Effective interest rate": effective_interest_rate,
            "Number of periods": f"{future_value_of_annuity_due}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)