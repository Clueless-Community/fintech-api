from helpers import functions
from fastapi import HTTPException, status

def personal_loan_task(
    loan_amount: float, interest_rate: float, loan_term_years: int, loan_start_date: str
):
    try:
        result = functions.personal_loan(
            loan_amount, interest_rate, loan_term_years, loan_start_date
        )
        return {
            "Tag": "Personal Loan",
            "Loan amount": loan_amount,
            "Monthly payment": round(result["Monthly payment"], 2),
            "Total interest paid": round(result["Total interest paid"], 2),
            "Total cost loan": round(result["Total cost loan"], 2),
            "Schedule": result["Schedule"],
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)