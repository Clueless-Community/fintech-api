from helpers import functions
from fastapi import HTTPException, status

def earnings_per_share_ratio(net_earnings:int,total_share_outstanding: int):
    try:
        earnings_per_share_ratio_value = functions.earnings_per_share_ratio(net_earnings,total_share_outstanding)
        return {
            "Tag": "Earnings Per Share Ratio",
            "Net Earnings": net_earnings ,
            "Total Share Outstanding": total_share_outstanding ,
            "Earnings Per Share Ratio": earnings_per_share_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)