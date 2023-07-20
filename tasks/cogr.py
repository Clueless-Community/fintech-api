from helpers import functions
from fastapi import HTTPException, status

def compound_annual_growth_rate_task(
    beginning_value: float, ending_value: float, years: int
):
    try:
        rate = functions.compound_annual_growth_rate(
            beginning_value, ending_value, years
        )
        return {
            "Tag": "Compound Annual Growth Rate",
            "Beginning Value": beginning_value,
            "Ending Value": ending_value,
            "Compound Annual Growth Rate": f"{rate}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)