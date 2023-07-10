from helpers import functions
from fastapi import HTTPException, status

def present_value_of_annuity_due_task(
    periodic_payment: float, number_of_periods: int, rate_per_period: float
):
    try:
        present_value_of_annuity_due = functions.present_value_of_annuity_due(
            periodic_payment, number_of_periods, rate_per_period
        )
        return {
            "Tag": "Present value of annuity due",
            "Periodic payment": periodic_payment,
            "Number of periods": number_of_periods,
            "Rate Per Period": rate_per_period,
            "PV of Annuity Due": f"{present_value_of_annuity_due}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)