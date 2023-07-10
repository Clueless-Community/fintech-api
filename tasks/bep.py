from helpers import functions
from fastapi import HTTPException, status

def break_even_point_task(fixed_cost: float, selling_price: float, variable_cost: float):
    try:

        bep = functions.break_even_point(
            fixed_cost, selling_price, variable_cost)
        return {
            "Tag": "Break Even Point (BEP)",
            "Fixed costs": fixed_cost,
            "Selling price per unit": selling_price,
            "Variable cost per unit": variable_cost,
            "Break Even Point in units": f"{bep[0]}",
            "Break Even Point in Rupees": f"{bep[1]}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)