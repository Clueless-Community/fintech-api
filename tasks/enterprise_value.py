from helpers import functions
from fastapi import HTTPException, status

def calculate_enterprise_value_task(
    share_price: float,
    fully_diluted_shares_outstanding: int,
    total_debt: float,
    preferred_stock: float,
    non_controlling_interest: float,
    cash_and_cash_equivalents: float,
):
    try:
        enterprise_value = functions.calculate_enterprise_value(
            share_price,
            fully_diluted_shares_outstanding,
            total_debt,
            preferred_stock,
            non_controlling_interest,
            cash_and_cash_equivalents,
        )
        return {
            "Tag": "Enterprise Value",
            "Equity Value": share_price * fully_diluted_shares_outstanding,
            "Total Debt": total_debt,
            "Preferred Stock": preferred_stock,
            "Non-Controlling Interest": non_controlling_interest,
            "Cash & Cash Equivalents": cash_and_cash_equivalents,
            "Enterprise Value": enterprise_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)