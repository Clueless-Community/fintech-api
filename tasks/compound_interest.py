from helpers import functions
from fastapi import HTTPException, status

def compound_interest_task(
    principal_amount: float, interest_rate: float, years: int, compounding_period: int
):
    try:
        amount = functions.compound_interest(
            principal_amount, interest_rate, years, compounding_period
        )
        return {
            "Tag": "Compound Interest Amount",
            "Principle amount": principal_amount,
            "Intrest Rate": interest_rate,
            "Time in Years": years,
            "Compounding Period": compounding_period,
            "Amount after interest": f"{amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
