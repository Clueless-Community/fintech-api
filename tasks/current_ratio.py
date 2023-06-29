from helpers import functions
from fastapi import HTTPException, status

def current_ratio_task(total_current_assets: float, total_liabilities: float):
    try:
        ratio = functions.current_ratio(
            total_current_assets, total_liabilities)
        return {
            "Tag": "Current Ratio",
            "Total Current Assets": total_current_assets,
            "Total Liabilities": total_liabilities,
            "Current Ratio": f"{ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)