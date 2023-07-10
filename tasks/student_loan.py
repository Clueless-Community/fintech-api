from helpers import functions
from fastapi import HTTPException, status

def student_loan_task(principal: int, tenure: int, interest_rate: float):
    try:
        student_loan = functions.student_loan(principal, tenure, interest_rate)
        return {
            "Tag": "Student Loan",
            "Total amount to borrow": principal,
            "total number of years to pay loan": tenure,
            "interest rate percentage annual": interest_rate,
            "total monthly cost": f"{student_loan[0]}",
            "Total Amount of loan": f"{student_loan[1]}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)