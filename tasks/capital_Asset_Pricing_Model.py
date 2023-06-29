from helpers import functions
from fastapi import HTTPException, status

def Capital_Asset_Pricing_Model_task(
    risk_free_interest_rate: float,
    beta_of_security: float,
    expected_market_return: float,
):
    try:
        Capital_Asset_Pricing_Model = functions.Capital_Asset_Pricing_Model(
            risk_free_interest_rate, beta_of_security, expected_market_return
        )
        return {
            "Tag": "Capital Asset Pricing Model",
            "Risk free interest rate": risk_free_interest_rate,
            "Beta of security": beta_of_security,
            "Expected market return": expected_market_return,
            "Capital asset expected return": f"{Capital_Asset_Pricing_Model}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)