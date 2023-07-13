from helpers import functions
from fastapi import HTTPException, status

def calculate_price_elasticity(initial_price: float, final_price: float, initial_quantity: float, final_quantity: float):
    try:
        percentage_change_price = (final_price - initial_price) / ((final_price + initial_price) / 2)
        percentage_change_quantity = (final_quantity - initial_quantity) / ((final_quantity + initial_quantity) / 2)
        price_elasticity = percentage_change_quantity / percentage_change_price

        return {
            "Tag": "Price Elasticity for demand Calculator",
            "Price Elasticity": price_elasticity,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)