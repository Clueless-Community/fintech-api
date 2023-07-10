from helpers import functions
from fastapi import HTTPException, status

def roth_ira_task(
    principal: float,
    interest_rate: float,
    years: int,
    tax_rate: float,
    annual_contribution: float,
):
    try:
        roth_ira_balance, taxable_saving_balance = functions.roth_ira(
            principal, interest_rate, years, tax_rate, annual_contribution
        )
        return {
            "Tag": "Roth-IRA",
            "Principal": principal,
            "Interest Rate": interest_rate,
            "Years": years,
            "Tax Rates": tax_rate,
            "Annual Contributions": annual_contribution,
            "Roth Ira Balance": roth_ira_balance,
            "Taxable saving Balance": taxable_saving_balance,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)