
from helpers import functions
from fastapi import HTTPException, status


def margin_of_safety_task(current_sales:float, break_even_point: float):
	try:
		margin = functions.margin_of_safety (current_sales, break_even_point)
		return{
			"Tag": "Margin Of Safety",
			"Current Sales": current_sales,
			"Break Even Point": break_even_point,
			"Margin Of Safety": f"{margin}%",
		}
	except:
		return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
