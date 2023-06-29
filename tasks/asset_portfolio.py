from helpers import functions
from fastapi import HTTPException, status

def asset_portfolio_task(
    price_A: float,
    price_B: float,
    return_A: float,
    return_B: float,
    standard_dev_A: float,
    standard_dev_B: float,
    correlation: float,
):
    try:
        weight_A = price_A / (price_A + price_B)
        weight_B = price_B / (price_A + price_B)
        cov = correlation * standard_dev_A * standard_dev_B
        portfolio_variance = (
            weight_A * weight_A * standard_dev_A * standard_dev_A
            + weight_B * weight_B * standard_dev_B * standard_dev_B
            + 2 * weight_A * weight_B * cov
        )
        expected_return = functions.decimal_to_percent(
            weight_A * return_A + weight_B * return_B
        )
        return {
            "Tag": "Portfolio Variance",
            "Expected Returns": f"{expected_return}%",
            "Portfolio Variance": f"{portfolio_variance}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)