from helpers import functions
from fastapi import HTTPException, status

def compound_annual_growth_rate_1_task(
    ending_value: float, beginning_value: float, number_of_periods: float
):
    try:
        cagr = functions.compound_annual_growth_rate_1(
            ending_value, beginning_value, number_of_periods
        )
        return {
            "Tag": "compound annual growth rate 1",
            "ending_value": ending_value,
            "beginning value": beginning_value,
            "Number of periods": number_of_periods,
            "compound annual growth rate": f"{cagr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)