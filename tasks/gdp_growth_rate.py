from helpers import functions
from fastapi import HTTPException, status

def gdp_growth_rate_task(current_year_gdp: float, last_year_gdp: float):
    try:
        gdp_growth_rate = functions.gdp_growth_rate(
            current_year_gdp, last_year_gdp)
        return {
            "Tag": "GDP Growth Rate",
            "Current Year GDP": current_year_gdp,
            "Last Year GDP": last_year_gdp,
            "GDP Growth Rate": gdp_growth_rate,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)