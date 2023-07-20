from helpers import functions
from fastapi import HTTPException, status

def discounted_payback_period_task(outflow: float, rate: float, periodic_cash_flow: float):
    try:
        discounted_payback_period = functions.discounted_payback_period(
            outflow, rate, periodic_cash_flow
        )
        return {
            "Tag": "Discounted Payback Period",
            "Initial Investment (Outflow)": outflow,
            "Rate": rate,
            "Periodic Cash Flow": periodic_cash_flow,
            "Discounted Payback Period": discounted_payback_period,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)