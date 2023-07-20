from helpers import functions
from fastapi import HTTPException, status

def accrued_interest_task(
    issue_date: str,
    settlement_date: str,
    rate: float,
    par: float,
    frequency: int = 1,
    basis: int = 0,
):
    try:
        accr_int = functions.accrint(
            issue_date, settlement_date, rate, par, frequency, basis
        )
        return {
            "Tag": "Accrued Interest",
            "Issue Date": issue_date,
            "Settlement Date": settlement_date,
            "Rate": rate,
            "Par": par,
            "Frequency": frequency,
            "Basis": basis,
            "Accrued Interest": accr_int,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)