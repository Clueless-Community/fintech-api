from helpers import functions
from fastapi import HTTPException, status

def rule_of_72_task(rate_of_roi: float):
    try:
        time_period = functions.rule_of_72(rate_of_roi)
        return {
            "Tag": "Rule of 72",
            "Rate of ROI": rate_of_roi,
            "Time period in which investment get double(in years)": f"{time_period}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)