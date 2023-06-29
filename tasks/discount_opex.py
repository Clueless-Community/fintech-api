from helpers import functions
from fastapi import HTTPException, status

def discount_opex_task(annual_opex: float, wacc: float, project_lifetime: float):
    try:
        dis_opex = functions.discount_opex(annual_opex, wacc, project_lifetime)
        return {
            "Tag": "Discount OPEX",
            "Annual OPEX": annual_opex,
            "WACC": wacc,
            "project lifetime": project_lifetime,
            "Discount opex": f"{dis_opex}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)