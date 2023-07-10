from helpers import functions
from fastapi import HTTPException, status

def retention_ratio_task(net_income: float, dividends: float):
    try:
        retention_ratio = functions.retention_ratio(net_income, dividends)
        return {
            "Tag": "Retention Ratio",
            "Net Income": net_income,
            "Dividends": dividends,
            "Retention Ratio": retention_ratio,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)