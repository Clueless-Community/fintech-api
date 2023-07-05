from helpers import functions
from fastapi import HTTPException, status

def debt_service_coverage_ratio_task(revenue: float, operating_expenses: float, interest: float, 
tax_rate: float, principal: float):
    try:
        net_operating_income = revenue - operating_expenses
        total_debt_service = (interest * (1 - tax_rate)) + principal
        ratio =  functions.debt_service_coverage_ratio(revenue,
        operating_expenses,
        interest,
        tax_rate,
        principal)
        return {
            "Tag": "Debt Service Coverage Ratio",
            "Revenue": revenue,
            "Operating Expenses": operating_expenses,
            "Interest": interest,
            "Tax Rate": tax_rate,
            "Principal": principal,
            "Net Operating Income": net_operating_income,
            "Total Debt Service": total_debt_service,
            "Debt Service Coverage Ratio": ratio
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) 