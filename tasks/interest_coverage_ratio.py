from helpers import functions
from fastapi import HTTPException, status
def interest_coverage_ratio(operating_income: int, interest_expenses: int):
    try:
        interest_coverage_ratio_value = functions.interest_coverage_ratio(operating_income,interest_expenses)
        return {
             "Tag": "Interest Coverage Ratio",
             "Operating Income": operating_income,
             "Interest Expenses": interest_expenses,
             "Interest Coverage Ratio": interest_coverage_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

