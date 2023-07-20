from helpers import functions
from fastapi import HTTPException, status

def zero_coupon_bond_value_task(
    face_value: float, rate_of_yield: float, time_of_maturity: float
):
    try:
        zcbv = functions.zero_coupon_bond_value(
            face_value, rate_of_yield, time_of_maturity
        )
        return {
            "Tag": "Zero Coupon Bond Value",
            "Face Value": face_value,
            "Rate of yield": f"{rate_of_yield}%",
            "Zero Coupon Bond Value": zcbv,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)