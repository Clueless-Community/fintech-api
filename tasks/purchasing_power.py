from helpers import functions
from fastapi import HTTPException, status

def purchasing_power_task(initial_amount: float, annual_inflation_rate: float, time: float):
    try:
        purchasing_power = functions.purchasing_power(
            initial_amount, annual_inflation_rate, time
        )
        return {
            "Tag": "Purchasing Power",
            "Initial Amount": initial_amount,
            "Annual Inflation Rate": annual_inflation_rate,
            "Time in years": time,
            "Purchasing Power": f"{purchasing_power}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)