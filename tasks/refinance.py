from helpers import functions
from fastapi import HTTPException, status

def refinance_task(
    current_loan_amount: float,
    current_interest_rate: float,
    current_loan_term_years: int,
    time_remaining_years: int,
    new_interest_rate: float,
    new_loan_term_years: int,
    cash_out_amount: float,
):
    try:
        result = functions.refinance_calculator(
            current_loan_amount,
            current_interest_rate,
            current_loan_term_years,
            time_remaining_years,
            new_interest_rate,
            new_loan_term_years,
            cash_out_amount,
        )
        return {
            "Tag": "Refinance",
            "Current loan amount": current_loan_amount,
            "Balance left on loan": round(result["Balance left on loan"], 2),
            "New loan amount": round(result["New loan amount"], 2),
            "Current monthly payment": round(result["Current monthly payment"], 2),
            "New monthly payment": round(result["New monthly payment"], 2),
            "Monthly savings": round(result["Monthly savings"], 2),
            "Current interest paid left": round(
                result["Current left interest paid"], 2
            ),
            "New total interest paid": round(result["New total interest paid"], 2),
            "Total interest saving": round(result["Total interest saving"], 2),
            "Current total cost left": round(result["Current total cost left"], 2),
            "New total cost loan": round(result["New total cost loan"], 2),
            "Total cost saving": round(result["Total cost saving"], 2),
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)