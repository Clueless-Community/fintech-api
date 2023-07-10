from helpers import functions
from fastapi import HTTPException, status

def cost_of_goods_sold_task(
    beginning_inventory: float, purchases: float, ending_inventory: float
):
    try:
        cogs = functions.cost_of_goods_sold(
            beginning_inventory, purchases, ending_inventory
        )
        return {
            "Tag": "Cost of Goods Sold",
            "Beginning Inventory": beginning_inventory,
            "Purchases during the period": purchases,
            "Ending Inventory": ending_inventory,
            "Cost of Goods Sold(In Rupees)": f"{cogs}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)