from helpers import functions
from fastapi import HTTPException, status

def asdcr_task(
    net_operating_cost: float,
    depreciation: float,
    non_cash_expenses: float,
    annual_debt_service: float,
):
    try:
        asdcr_debt = functions.annual_debt_service_coverage_ratio(
            net_operating_cost, depreciation, non_cash_expenses, annual_debt_service
        )
        return {
            "Tag": "Annual Debt Service Coverage Ratio",
            "Annual Debt Ratio": asdcr_debt,
            "Net Operating Income": net_operating_cost,
            "Depreciation": depreciation,
            "Non Cash Expenses": non_cash_expenses,
            "Annual Debt": annual_debt_service,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)