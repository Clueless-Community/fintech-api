from helpers import functions
from fastapi import HTTPException, status

def doubling_time_task(r: float):
    try:
        doubling_time = functions.doubling_time(r)
        return {
            "Tag": "Doubling Time",
            "Rate of Interest": r,
            "Time in years to double the money": f"{doubling_time}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)