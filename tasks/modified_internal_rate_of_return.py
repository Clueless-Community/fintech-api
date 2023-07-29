from helpers import functions
from fastapi import HTTPException, status

def calculate_modified_internal_rate_of_return_task(ending_cash_flow: float,
                                                initial_cash_flow: float,
                                                number_of_periods: int
):
    try:
        mirr = functions.calculate_modified_internal_rate_of_return(
            ending_cash_flow, initial_cash_flow, number_of_periods
        )
        return {
            "Tag": "Modified internal rate of return",
            "Ending cash flow": ending_cash_flow,
            "Initial cash flow": initial_cash_flow,
            "Number of periods": number_of_periods,
            "Modified internal rate of return": f"{mirr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)