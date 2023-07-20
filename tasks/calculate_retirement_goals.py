from helpers import functions
from fastapi import HTTPException, status

def calculate_retirement_goals_task(
    retirement_age: int,
    annual_retirement_expenses: int,
    inflation_rate: float,
    annual_retirement_income: int,
    current_age: int,
):
    try:
        amount = functions.calculate_retirement_goals(
            retirement_age,
            annual_retirement_expenses,
            inflation_rate,
            annual_retirement_income,
            current_age,
        )
        return {
            "Tag": "Retirement Goals",
            "Retirement age": retirement_age,
            "Annual retirement expenses": annual_retirement_expenses,
            "inflation rate": inflation_rate,
            "Annual Retirement Income": annual_retirement_income,
            "Current Age": current_age,
            "Retirement Goals": f"{amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)