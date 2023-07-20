from helpers import functions
from fastapi import HTTPException, status

def yield_to_maturity_task(
    bond_price: float, face_value: float, coupon_rate: float, years_to_maturity: float
):
    try:
        yield_cal = functions.yield_to_maturity(
            bond_price, face_value, coupon_rate, years_to_maturity
        )
        return {
            "Tag": "Yield To Maturity",
            "Face Value": face_value,
            "Years to maturity": years_to_maturity,
            "Yield to Maturity": f"{yield_cal}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)