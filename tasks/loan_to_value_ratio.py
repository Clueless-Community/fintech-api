from helpers import functions
from fastapi import HTTPException, status

def loan_to_value_ratio_task(loan_amount: float, value_of_collateral: float):
    try:
        ratio = functions.loan_to_value_ratio(loan_amount, value_of_collateral)
        return {
            "Tag": "Loan to Value Ratio",
            "Loan Amount": loan_amount,
            "Value Of Collateral": value_of_collateral,
            "Loan to Value Ratio": f"{ratio}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)