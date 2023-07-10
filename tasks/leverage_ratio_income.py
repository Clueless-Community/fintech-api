from helpers import functions
from fastapi import HTTPException, status

def leverage_income_task(debt_payments: int, income: int):
    try:
        leverage_ratio = functions.leverage_income(debt_payments, income)

        return {
            "Tag": "Leverage Ratio By Income",
            "Debt ": debt_payments,
            "Income": income,
            "Leverage Ratio": f"{leverage_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)