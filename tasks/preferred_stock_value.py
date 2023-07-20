from helpers import functions
from fastapi import HTTPException, status

def preferred_stock_value_task(dividend: float, discount_rate: float):
    try:
        preferred_stock_value = functions.preferred_stock_value(
            dividend, discount_rate)
        return {
            "Tag": "Preferred stock value",
            "Dividend": dividend,
            "Discount Rate": discount_rate,
            "Preferred Stock Value": preferred_stock_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)