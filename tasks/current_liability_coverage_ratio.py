from helpers import functions
from fastapi import HTTPException, status

def current_liability_coverage_ratio_task(
    net_cash_from_operating_activities: float,
    total_current_liabilities: float,
    number_of_liabilities: int,
):
    try:
        current_liability_coverage_ratio = functions.current_liability_coverage_ratio(
            net_cash_from_operating_activities,
            total_current_liabilities,
            number_of_liabilities,
        )
        return {
            "Tag": "current liability coverage ratio",
            "net cash from operating activities": net_cash_from_operating_activities,
            "total current liabilities": total_current_liabilities,
            "number of liabilities": number_of_liabilities,
            "current liability coverage ratio": f"{current_liability_coverage_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)