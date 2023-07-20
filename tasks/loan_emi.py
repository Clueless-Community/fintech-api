from helpers import functions
from fastapi import HTTPException, status

def loan_emi_task(principle_amount: float, annual_rate: float, months: int):
    try:
        emi = functions.loan_emi(principle_amount, annual_rate, months)
        return {
            "Tag": "Loan Emi",
            "Principal amount borrowed": principle_amount,
            "Annual Rate of interest": annual_rate,
            "Total number of monthly payments": months,
            "EMI": f"{round(emi,3)}",
            "Total Amount Payble": f"{round(emi*months,3)}",
            "Interest amount": f"{round(emi*months-principle_amount,3)}",
        }
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)