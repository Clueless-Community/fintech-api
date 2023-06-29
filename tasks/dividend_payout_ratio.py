from helpers import functions
from fastapi import HTTPException, status

def dividend_payout_ratio_task(dividend_per_share: float, earnings_per_share: float):
    try:
        dividend_payout = functions.dividend_payout_ratio(
            dividend_per_share, earnings_per_share
        )
        return {
            "Tag": "Dividend payout ratio",
            "Dividend per share": dividend_per_share,
            "Share price": earnings_per_share,
            "Dividend yield ratio": f"{dividend_payout}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)