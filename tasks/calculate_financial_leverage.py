from helpers import functions
from fastapi import HTTPException, status

def calculate_financial_leverage_task(total_assets : float,
                                 total_liabilities : float,
                                 short_term_debt : float,
                                 long_term_debt : float
                                 ):
    try:
        financial_leverage = functions.calculate_financial_leverage(
            total_assets, total_liabilities, short_term_debt, long_term_debt)
        return {
            "Tag": "Calculate financial leverage",
            "Total Assets": total_assets,
            "Total Liabilities": total_liabilities,
            "Short term debt": short_term_debt,
            "Long term debt": long_term_debt,
            "Financial Leverage": financial_leverage,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)