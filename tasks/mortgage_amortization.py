from helpers import functions
from fastapi import HTTPException, status

def mortgage_amortization_task(
    mortgage_amount: float,
    mortgage_deposit: float,
    annual_interest_rate: float,
    loan_term: int,
):
    try:
        annual_payment = functions.calculate_mortgage_interest(
            mortgage_amount, mortgage_deposit, annual_interest_rate, loan_term
        )
        return {
            "TAG": "Mortgage monthly payments",
            "mortgage_amount": mortgage_amount,
            "mortgage_deposit": mortgage_deposit,
            "annual_interest_rate": annual_interest_rate,
            "loan_term": loan_term,
            "monthly_payment": round(annual_payment / 12, 3),
            "annual_payment": round(annual_payment, 3),
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)