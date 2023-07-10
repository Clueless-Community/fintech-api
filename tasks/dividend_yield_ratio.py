from helpers import functions
from fastapi import HTTPException, status

def dividend_yield_ratio_task(dividend_per_share: float, share_price: float):
    try:
        dividend_yield = functions.dividend_yield_ratio(
            dividend_per_share, share_price)
        return {
            "Tag": "Dividend yield ratio",
            "Dividend per share": dividend_per_share,
            "Share price": share_price,
            "Dividend yield ratio": f"{dividend_yield}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)