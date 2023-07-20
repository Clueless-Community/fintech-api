from helpers import functions
from fastapi import HTTPException, status

def time_period_required_for_growth_task(interest_rate: float, growth_factor: int):
    try:
        time_period_required_for_growth = functions.time_period_required_for_growth(
            interest_rate, growth_factor
        )
        return {
            "Tag": "Time period required for exponential growth",
            "interest rate": interest_rate,
            "growth factor": growth_factor,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)