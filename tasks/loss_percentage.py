from helpers import functions
from fastapi import HTTPException, status

def loss_percentage_task(loss: float, cost_price: float):
    try:
        loss_percent = functions.loss_percentage(loss, cost_price)
        return {
            "Tag": "Loss Percentage",
            "Total loss": loss,
            "Cost Price": cost_price,
            "Interest Rate": f"{loss_percent}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)