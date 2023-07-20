from helpers import functions
from fastapi import HTTPException, status

def real_gdp_task(nominal_gdp: float, gdp_deflator: float):
    try:
        real_gdp = functions.real_gdp(nominal_gdp, gdp_deflator)
        return {
            "Tag": "Real GDP",
            "Nominal GDP": nominal_gdp,
            "GDP Deflator": gdp_deflator,
            "Real GDP": real_gdp,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)