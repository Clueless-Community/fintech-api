from helpers import functions
from fastapi import HTTPException, status

def cost_of_equity_task(
    risk_free_rate_of_return: float, Beta: float, market_rate_of_return: float
):
    try:
        costOfEquity = functions.cost_of_equity(
            risk_free_rate_of_return, Beta, market_rate_of_return
        )
        return {
            "Tag": "Cost of Equity",
            "Risk free rate of return": risk_free_rate_of_return,
            "Beta": Beta,
            "Market rate of return ": market_rate_of_return,
            "Cost of equity": f"{costOfEquity}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)