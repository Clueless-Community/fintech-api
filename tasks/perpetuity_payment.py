from helpers import functions
from fastapi import HTTPException, status

def perpetuity_payment_task(present_value: float, rate: float):
    try:
        payment = functions.perpetuity_payment(present_value, rate)
        return {
            "Tag": "Perpetuity Payment",
            "Present Value": present_value,
            "Perpetuity Payment": f"{payment}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)