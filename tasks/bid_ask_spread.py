from helpers import functions
from fastapi import HTTPException, status

def bid_ask_spread_task(ask_price: float, bid_price: float):
    try:
        bid_ask_spread = functions.bid_ask_spread(ask_price, bid_price)
        return {
            "Tag": "Bid Ask Spread",
            "Ask Price": ask_price,
            "Bid Price": bid_price,
            "Bid Ask Spread": bid_ask_spread,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)