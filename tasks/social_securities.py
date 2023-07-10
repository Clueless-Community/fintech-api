from helpers import functions
from fastapi import HTTPException, status

def ss_task(birth_date: str, earnings: int, retirement_age: int):

    try:
        monthly_benefits, future_benefits = functions.calculate_social_security(
            birth_date=birth_date,
            earnings=earnings,
            retirement_age=retirement_age
        )
        return {
            f"The monthly benefits are {monthly_benefits} and future benefits are {future_benefits}"
        }

    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)