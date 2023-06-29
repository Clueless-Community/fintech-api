from helpers import functions
from fastapi import HTTPException, status

def fixed_charge_coverage_ratio_task(
    earnings_before_interest_taxes: float,
    fixed_charge_before_tax: float,
    interest: float,
):
    try:
        fccr = functions.fixed_charge_coverage_ratio(
            earnings_before_interest_taxes, fixed_charge_before_tax, interest
        )
        return {
            "Tag": "fixed charges coverage ratio",
            "Earnings before interest taxes": earnings_before_interest_taxes,
            "Fixed charge before tax": fixed_charge_before_tax,
            "Interest": interest,
            "Fixed charge coverage ratio": f"{fccr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)