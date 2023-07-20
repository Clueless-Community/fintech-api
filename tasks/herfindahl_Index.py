from helpers import functions
from fastapi import HTTPException, status

def herfindahl_Index_task(Firms_market_shares: str):
    try:
        herfindahl_Index = functions.herfindal_Index(Firms_market_shares)
        return {
            "Tag": "Herfindahl Index",
            "Firms market shares": Firms_market_shares,
            "Herfindahl Index": f"{herfindahl_Index}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)