from helpers import functions
from fastapi import HTTPException, status

def estimate_401k_task(
    income: float,
    contribution_percentage: float,
    current_age: int,
    age_at_retirement: int,
    rate_of_return: float,
    salary_increase_rate: float,
    withdraw_tax_rate: float,
):
    try:
        estimated_401k = functions.calculate_401k(
            income,
            contribution_percentage,
            current_age,
            age_at_retirement,
            rate_of_return,
            salary_increase_rate,
        )
        return {
            "Tag": "Estimated 401(k)",
            "income": income,
            "contribution_percentage": contribution_percentage,
            "current_age": current_age,
            "age_at_retirement": age_at_retirement,
            "rate_of_return": rate_of_return,
            "withdraw_tax_rate": withdraw_tax_rate,
            "estimated_401k": estimated_401k,
            "annual_withdraw_amount": round(
                functions.percent_to_decimal(
                    withdraw_tax_rate) * estimated_401k, 3
            ),
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)