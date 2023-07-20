from helpers import functions
from fastapi import HTTPException, status

def free_cash_flow_to_firm_task(
    sales: float,
    operating_cost: float,
    depreciation: float,
    interest: float,
    tax_rate: float,
    fcInv: float,
    wcInv: float,
):
    try:
        ebitda = sales - operating_cost
        ebit = ebitda - depreciation
        ebt = ebit - interest

        eat = ebt - ebt * (tax_rate * 0.01)
        fcff = functions.free_cash_flow_to_firm(
            sales, operating_cost, depreciation, interest, tax_rate, fcInv, wcInv
        )
        return {
            "Tag": "Free Cash Flow to Firm (FCFF)",
            "Earnings before interest, taxes, depreciation and amortization": f"{ebitda}",
            "Earnings before interest and taxes : ": f"{ebit}",
            "Net Income": f"{eat}",
            "Free Cash Flow to Firm": f"{fcff}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)