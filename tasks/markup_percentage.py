from helpers import functions
from fastapi import HTTPException, status

def markup_percentage_task(price: float, cost: float):
    try:
        markup_percentage = functions.markup_percentage(price, cost)
        return {
            "Tag": "Markup Percentage",
            "Price": price,
            "Cost": cost,
            "Markup Percentage": markup_percentage,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)