from helpers import functions
from fastapi import HTTPException, status

def debt_to_income_ratio_task(annual_income: float, total_debt_per_month: float):
    try:
        DTI = functions.debt_to_income_ratio(
            annual_income, total_debt_per_month)
        return {
            "Tag": "Debt to income ratio",
            "Annual income": annual_income,
            "Total debt per month": total_debt_per_month,
            "Debt to income ratio per month": f"{DTI}%",
        }
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)