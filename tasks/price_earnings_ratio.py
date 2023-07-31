from helpers import functions
from fastapi import HTTPException, status

def price_earnings_ratio(share_price:int,earnings_per_share: int):
    try:
        price_earnings_ratio_value = functions.price_earnings_ratio(share_price,earnings_per_share)
        return {
            "Tag": "Price Earnings Ratio",
            "Share Price": share_price ,
            "Earnings Per Shares": earnings_per_share ,
            "Price Earnings Ratio": price_earnings_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)