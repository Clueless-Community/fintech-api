from helpers import functions
from fastapi import HTTPException, status

def weighted_average_cost_of_capital_task(
    firm_equity, firm_debt, cost_of_equity, cost_of_debt, corporate_tax_rate
):
    try:
        wacc = functions.wacc(
            firm_equity, firm_debt, cost_of_equity, cost_of_debt, corporate_tax_rate
        )
        return {
            "Tag": "Weighted Average Cost of Capital (WACC)",
            "Market value of firm's equity": firm_equity,
            "Market value of firm's debt": firm_debt,
            "Cost of equity": cost_of_equity,
            "Cost of debt": cost_of_debt,
            "Corporate tax rate": corporate_tax_rate,
            "WACC": f"{wacc}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)