from helpers import functions
from fastapi import HTTPException, status

def leverage_equity_task(debt_payments: int, equity: int):
    try:
        leverage_ratio = functions.leverage_equity(debt_payments, equity)

        return {
            "Tag": "Leverage Ratio By Equity",
            "Debt ": debt_payments,
            "Equity": equity,
            "Leverage Ratio": f"{leverage_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)