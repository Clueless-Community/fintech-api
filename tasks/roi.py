from helpers import functions
from fastapi import HTTPException, status

def return_on_investment_task(current_value_of_investment: float, cost_of_investment: float):
    try:
        roi = functions.return_on_investment(
            current_value_of_investment, cost_of_investment
        )

        return {
            "Tag": "Return on Investment",
            "Current Value of Investment": current_value_of_investment,
            "Cost of Investment": cost_of_investment,
            "Return on Investment": f"{roi}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)