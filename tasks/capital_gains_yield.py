from helpers import functions
from fastapi import HTTPException, status

def capital_gains_yield_task(inital_price: float, price_after_first_period: float):
    try:
        gains_yield = functions.capital_gains_yield(inital_price, price_after_first_period)
        return {
            "Tag": "Capital Gains Yield",
		    "Inital Price of Stock": inital_price,
    	    "Price of Stock After First Period": price_after_first_period,
    	    "Capital Gains Yield": f"{gains_yield}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)