from helpers import functions
from fastapi import HTTPException, status

def profit_percentage_task(profit: float, cost_price: float):
    try:
        profit_percent = functions.profit_percentage(profit, cost_price)
        return {
            "Tag": "Profit Percentage",
            "Total Profit": profit,
            "Cost Price": cost_price,
            "Profit Percent": f"{profit_percent}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)