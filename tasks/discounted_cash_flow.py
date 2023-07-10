from helpers import functions
from fastapi import HTTPException, status

def discounted_cash_flow_task(
    real_feed_in_tariff: float,
    annual_production: float,
    wacc: float,
    project_lifetime: float,
):
    try:
        d_cash_flow = functions.discounted_cash_flow(
            real_feed_in_tariff, annual_production, wacc, project_lifetime
        )
        return {
            "Tag": "Discounted cash flow",
            "Real feed in teriff": real_feed_in_tariff,
            "annual production": annual_production,
            "wacc": wacc,
            "project lifetime": project_lifetime,
            "discounted cash flow": f"{d_cash_flow}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)