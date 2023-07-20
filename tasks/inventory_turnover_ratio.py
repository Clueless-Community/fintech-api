from helpers import functions
from fastapi import HTTPException, status

def inventory_turnover_ratio_task(
    cost_of_goods_sold: float, beginning_inventory: float, ending_inventory: float
):
    try:
        ratio = functions.inventory_turnover_ratio(
            cost_of_goods_sold, beginning_inventory, ending_inventory
        )
        return {
            "Tag": "Inventory Turnover Ratio",
            "Cost of Goods Sold": cost_of_goods_sold,
            "Inventory Turnover Ratio": f"{ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)