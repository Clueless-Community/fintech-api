from helpers import functions
from fastapi import HTTPException, status

def inflation_task(present_amount: float, inflation_rate: float, years: float):
    try:
        future_amount = functions.inflation(
            present_amount, inflation_rate, years)
        return {
            "Tag": "Inflated Amount",
            "Present Amount": present_amount,
            "Inflation Rate": inflation_rate,
            "Time in Years": years,
            "Future Amount": f"{future_amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)