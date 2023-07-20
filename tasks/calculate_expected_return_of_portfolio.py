from helpers import functions
from fastapi import HTTPException, status

def calculate_expected_return_of_portfolio_task(no_of_investments: int,
                                           investment_amount: list,
                                           rate_of_return: list):
    try:
        expected_return_of_portfolio = functions.calculate_expected_return_of_portfolio(
            no_of_investments, investment_amount, rate_of_return)
        return {
            "Tag": "Calculate expected return of portfolio",
            "No of investments": no_of_investments,
            "Investment Amount": investment_amount,
            "Rate of Return": rate_of_return

        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)