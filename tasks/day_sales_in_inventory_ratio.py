from helpers import functions
from fastapi import HTTPException, status

def day_sales_in_inventory_ratio(avg_inventory: int, cost_of_goods_sold: int, no_of_days: int):
    try:
        day_sales_in_inventory_ratio_value = functions.day_sales_in_inventory_ratio(avg_inventory,cost_of_goods_sold,no_of_days)
        return {
            "Tag": "Day Sales in Inventory Ratio",
            "Average Inventory": avg_inventory,
            "Cost Of Goods Sold": cost_of_goods_sold,
            "Number Of Days":no_of_days ,
            "Day Sales in Inventory Ratio": day_sales_in_inventory_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
