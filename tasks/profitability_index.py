from helpers import functions
from fastapi import HTTPException, status

def profitability_index_task(initial_investment: float, pv_of_future_cash_flows: float):
    try:
        profitability_index = functions.profitability_index(
            initial_investment, pv_of_future_cash_flows
        )
        return {
            "Tag": "Profitability Index",
            "Initial Investment": initial_investment,
            "PV of Future Cash Flows": pv_of_future_cash_flows,
            "Profitability Index": profitability_index,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)