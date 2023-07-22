from helpers import functions
from fastapi import HTTPException, status
def break_even_point(fixed_costs: int, sales_price_per_unit: float, variable_price_per_unit: float):
    try:
        break_even_point_value = functions.break_even_point(fixed_costs,sales_price_per_unit,variable_price_per_unit)
        return {
            "Tag": "Break-even Point",
            "Fixed Costs": fixed_costs,
            "Sales Price Per Unit": sales_price_per_unit,
            "Variable Price Per Unit":variable_price_per_unit ,
            "Break-even Point": break_even_point_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)