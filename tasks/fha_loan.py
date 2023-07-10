from helpers import functions
from fastapi import HTTPException, status

async def fha_loan_task(
    home_price: float,
    down_payment_percentage: float,
    loan_term_years: float,
    interest_rate: float,
    fha_annual_mip_percentage: float,
):
    try:
        result = functions.calculate_fha_loan(
            home_price,
            down_payment_percentage,
            loan_term_years,
            interest_rate,
            fha_annual_mip_percentage,
        )
        return {
            "down_payment": result["down_payment"],
            "fha_base_loan_amount": result["fha_base_loan_amount"],
            "fha_upfront_mip": result["fha_upfront_mip"],
            "monthly_mortgage_payment": result["monthly_mortgage_payment"],
            "monthly_mip": result["monthly_mip"],
            "total_fha_loan_amount": result["total_fha_loan_amount"],
            "total_monthly_payment": result["total_monthly_payment"],
            "total_cost_of_loan": result["total_cost_of_loan"],
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)