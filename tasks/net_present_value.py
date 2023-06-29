from helpers import functions
from fastapi import HTTPException, status

def net_present_value_task(cash_flows: str, discount_rate: float, initial_investment: float):
    try:
        net_present_value = functions.net_present_value(
            cash_flows, discount_rate, initial_investment
        )
        return {
            "Tag": "Net present value",
            "cash flows": cash_flows,
            "discount rate": discount_rate,
            "initial investment": initial_investment,
            "Net present value": net_present_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)