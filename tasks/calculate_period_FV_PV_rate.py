from helpers import functions
from fastapi import HTTPException, status

def CalculatePeriods_task(present_val: float, future_val: float, rate: float):
    try:
        period = functions.CalculatePeriods(present_val, future_val, rate)
        return {
            "Tag": "Period in years ",
            "Present Value": present_val,
            "Future Value": future_val,
            "Periods": period,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)