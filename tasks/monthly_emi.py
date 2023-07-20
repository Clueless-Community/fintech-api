from helpers import functions
from fastapi import HTTPException, status

def monthly_emi_task(loan_amt: float, interest_rate: float, number_of_installments: float):
    try:
        monthly_emi = functions.monthly_emi(
            loan_amt, interest_rate, number_of_installments
        )
        return {
            "Tag": "Monthly EMI",
            "Loan Amount": loan_amt,
            "Interest Rate": interest_rate,
            "Number of Installments": number_of_installments,
            "Total EMI": f"{monthly_emi}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)