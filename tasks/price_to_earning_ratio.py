from helpers import functions
from fastapi import HTTPException, status

def price_to_earning_ratio_task(share_price: float, earnings_per_share: float):
    try:
        p_e_ratio = functions.price_to_earning_ratio(share_price, earnings_per_share)
        return {
            "Tag": "Price to Earning ratio",
            "Share price": share_price,
            "Earning per share": earnings_per_share,
            "Price to Earning ratio": f"{p_e_ratio}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)