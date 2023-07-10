from helpers import functions
from fastapi import HTTPException, status

def balloon_loan_payment_task(
    principal: float,
    interest_rate: float,
    term_years: float,
    balloon_payment_year: float,
):
    try:
        balloon_loan_payment = functions.balloon_loan_payment(
            principal, interest_rate, term_years, balloon_payment_year
        )
        return {
            "Tag": "Balloon Loan Payment",
            "Principal": principal,
            "Interest Rate": interest_rate,
            "Term Years": term_years,
            "Balloon Payment Year": balloon_payment_year,
            "Balloon Loan Payment": balloon_loan_payment,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)