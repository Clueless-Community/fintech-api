from helpers import functions
from fastapi import HTTPException, status

def inventory_shrinkage_rate_task(recorded_inventory: float, actual_inventory: float):
    try:
        inventory_shrinkage_rate = functions.inventory_shrinkage_rate(
            recorded_inventory, actual_inventory
        )
        return {
            "Tag": "Inventory shrinkage rate",
            "Recorded Inventory": recorded_inventory,
            "Actual Inventory": actual_inventory,
            "Inventory Shrinkage Rate": inventory_shrinkage_rate,
            "Inventory Shrinkage Rate (%)": functions.decimal_to_percent(
                inventory_shrinkage_rate
            ),
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)