from helpers import functions
from fastapi import HTTPException, status

def put_call_parity_task(call_price: float, put_price: float, strike_price: float):
    try:
        future_amount = functions.put_call_parity(
            call_price, put_price, strike_price)
        return {
            "Tag": "Pull Call Parity",
            "Future Price": f"{future_amount}",
            "Call Price": f"{call_price}",
            "Put Price": f"{put_price}",
            "Strike Price": f"{strike_price}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)