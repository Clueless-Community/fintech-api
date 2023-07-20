from helpers import functions
from fastapi import HTTPException, status

def net_worth_calculation_task(assets: float, liabilities: float, loans: float, mortgages: float):
    try:
        total_liabilities = liabilities + loans + mortgages
        net_worth = assets - total_liabilities
        return {
            "Tag": "Net Worth",
            "Assets": assets,
            "Liabilities": total_liabilities,
            "Net Worth": net_worth,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)