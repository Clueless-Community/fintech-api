from helpers import functions
from fastapi import HTTPException, status

def calculate_roi_equity_funds_task(
    amount_invested: float,
    amount_returned: float,
    tenure: float,
):
    try:
        roi, annualized_roi = functions.calculate_roi_equity_funds(
            amount_invested, amount_returned, tenure
        )
        return {
            "Tag": "Calculate return of investments on equity funds",
            "Amount Invested": amount_invested,
            "Amount Returned": amount_returned,
            "Duration of investment": tenure,
            "Return of Investment": f"{roi}%",
            "Annualized Return": f"{annualized_roi}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)