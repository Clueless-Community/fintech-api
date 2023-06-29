from helpers import functions
from fastapi import HTTPException, status

def year_over_year_task(later_period_value: float, earlier_period_value: float):
    try:
        growth = functions.year_over_year(
            later_period_value, earlier_period_value)
        return {
            "Tag": "Year to Year Growth",
            "Year to Year growth": f"{growth}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)