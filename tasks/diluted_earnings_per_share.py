from helpers import functions
from fastapi import HTTPException, status

def calculate_diluted_eps_task(
    net_income: float,
    weighted_avg_shares: float,
    dilutive_securities: float,
):
    try:
        result = functions.diluted_eps(
            net_income, weighted_avg_shares, dilutive_securities
        )
        return {
            "Tag": "Diluted Earnings Per Share (EPS)",
            "Net Income": net_income,
            "Weighted Average Shares Outstanding": weighted_avg_shares,
            "Number of Dilutive Securities": dilutive_securities,
            "Diluted EPS": f"{result}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)