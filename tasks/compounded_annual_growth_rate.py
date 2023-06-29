from helpers import functions
from fastapi import HTTPException, status

def compounded_annual_growth_rate_task(
    end_investment_value: float, initial_investment_value: float, years: int
):
    try:
        cagr = functions.compounded_annual_growth_rate(
            end_investment_value, initial_investment_value, years
        )

        return {
            "Tag": "Compounded Annual Growth Rate",
            "End investment value": end_investment_value,
            "Initial investment value": initial_investment_value,
            "Years": years,
            "Compounded Annual Growth Rate": f"{cagr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)