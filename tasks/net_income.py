from helpers import functions
from fastapi import HTTPException, status
def net_income(revenue: float, expenses: int):
    try:
        net_income_value = functions.net_income(revenue,expenses)
        return {
             "Tag": "Net Income",
             "Revenue": revenue,
             "Expenses": expenses,
             "Net Income": net_income_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)