from helpers import functions
from fastapi import HTTPException, status

def payback_period_task(
    years_before_recovery: int, unrecovered_cost: float, cash_flow: float
):
    try:
        period = functions.payback_period(
            years_before_recovery, unrecovered_cost, cash_flow
        )
        return {
            "Tag": "Payback period",
            "Years before full recovery": years_before_recovery,
            "Unrecovered cost at start of the year": unrecovered_cost,
            "Cash flow during the year": cash_flow,
            "Payback period": f"{period}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)