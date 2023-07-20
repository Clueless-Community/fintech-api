from helpers import functions
from fastapi import HTTPException, status

def effective_annual_rate_task(annual_interest_rate: float, compounding_period: int):
    try:
        eff_annual_rate = functions.effective_annual_rate(
            annual_interest_rate, compounding_period
        )
        eff_annual_rate_percentage = functions.decimal_to_percent(
            eff_annual_rate)
        return {
            "Tag": "Effective Annual Rate",
            "Annual Intrest Rate": annual_interest_rate,
            "Compounding Period": compounding_period,
            "Effective Annual Rate (in percentage)": f"{eff_annual_rate_percentage}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)