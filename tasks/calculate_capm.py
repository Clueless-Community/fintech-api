from helpers import functions
from fastapi import HTTPException, status


def calculate_capm(risk_free_return:float, sensitivity:float, expected_market_return:float):
    try:
        expected_asset_return = functions.capm_calculation(risk_free_return, sensitivity, expected_market_return)
        return {
            "Tag": "Capital Asset Pricing Model (CAPM)",
            "Risk-free rate of return":risk_free_return,
            "Asset's sensitivity": sensitivity,
            "Expected return of the market": expected_market_return,
            "expected return on the asset": f"{expected_asset_return}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)