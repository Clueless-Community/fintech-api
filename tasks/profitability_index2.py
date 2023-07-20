from helpers import functions
from fastapi import HTTPException, status

def profitability_index2_task(
    initial_investment: float, annual_cash_flows: str, discount_rate: float
):
    try:
        profitability_index = functions.profitability_index2(
            initial_investment, annual_cash_flows, discount_rate
        )
        return {
            "Tag": "profitability_index",
            "initial_investment": initial_investment,
            "annual_cash_flows": annual_cash_flows,
            "discount_rate": discount_rate,
            "profitability index": f"{profitability_index}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)