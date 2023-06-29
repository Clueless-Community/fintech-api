from helpers import functions
from fastapi import HTTPException, status

def portfolio_return_monte_carlo_task(principal: float, 
                                 expected_return_range_start: float, 
                                 expected_return_range_end: float,
                                 volatility_range_start: float,
                                 volatility_range_end: float,
                                 num_simulations: float):
    try:
        portfolio_returns = functions.portfolio_return_monte_carlo(principal, expected_return_range_start,expected_return_range_end, volatility_range_start,volatility_range_end, num_simulations)

        return {
            "Tag": "Portfolio Return Monte Carlo",
            "Principal": principal,
            "Number of Simulations": num_simulations,
            "Portfolio Returns": f"{portfolio_returns}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)