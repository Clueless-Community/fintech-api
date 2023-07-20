from helpers import functions
from fastapi import HTTPException, status

def acid_test_ratio_task(
    cash: float,
    marketable_securities: float,
    accounts_receivable: float,
    current_liabilities: float,
):
    try:
        ratio = functions.acid_test_ratio(
            cash, marketable_securities, accounts_receivable, current_liabilities
        )
        return {
            "Tag": "Acid Test Ratio",
            "Cash and Cash Equivalents": cash,
            "Marketable Securities": marketable_securities,
            "Accounts Receivable": accounts_receivable,
            "Current Liabilities": current_liabilities,
            "Acid Test Ratio (Quick Ratio)": f"{ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)