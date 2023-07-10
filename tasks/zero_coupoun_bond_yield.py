from helpers import functions
from fastapi import HTTPException, status

def zero_coupon_bond_yield_task(
    face_value: float, present_value: float, time_of_maturity: float
):
    try:
        zcby = functions.zero_coupon_bond_yield(
            face_value, present_value, time_of_maturity
        )
        return {
            "Tag": "Zero Coupon Bond Effective Yield",
            "Face Value": face_value,
            "Present Value": present_value,
            "Time to maturity": time_of_maturity,
            "Zero Coupon Bond Effective Yield": f"{zcby}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)