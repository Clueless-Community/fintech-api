from helpers import functions
from fastapi import HTTPException, status

def bond_valuation_task(face_value: int, coupon_rate: float, years_to_maturity: int, discount_rate : float):
    try:
        result = functions.calculate_bond_value(
            face_value, coupon_rate, years_to_maturity, discount_rate
        )
        return {
            "Tag": "Bond Valuation",
            "Face Value": face_value,
            "Coupon Rate": coupon_rate,
            "Years to Maturity": years_to_maturity,
            "Discount Rate": discount_rate,
            "Bond Valuation": f"{result}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)