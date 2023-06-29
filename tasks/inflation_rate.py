from helpers import functions
from fastapi import HTTPException, status

def inflation_rate_task(bigger_year: int, smaller_year: int, base_year: int):
    try:
        inflation_rate = functions.inflation_rate(
            bigger_year, smaller_year, base_year)
        return {
            "Tag": "Inflation Rate",
            "Bigger Year": bigger_year,
            "Smaller Year": smaller_year,
            "Base Year": base_year,
            "Inflation Rate": inflation_rate,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)