from helpers import functions
from fastapi import HTTPException, status

def sharpe_ratio_task(
    portfolio_return: float,
    risk_free_rate: float,
    standard_deviation_of_portfolio: float,
):
    try:
        sharpe_ratio_val = functions.sharpe_ratio(
            portfolio_return, risk_free_rate, standard_deviation_of_portfolio
        )
        return {
            "Tag": "Sharpe Ratio",
            "Portfolio Return": portfolio_return,
            "Risk Free Rate": risk_free_rate,
            "Standard Deviation of Portfolio": standard_deviation_of_portfolio,
            "Sharpe Ratio": f"{sharpe_ratio_val}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)