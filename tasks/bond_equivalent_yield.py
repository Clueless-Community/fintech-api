from helpers import functions
from fastapi import HTTPException, status

def bond_equivalent_yield_task(
    face_value: float, purchase_price: float, days_to_maturity: int
):
    try:
        bey = functions.calculate_bond_equivalent_yield(
            face_value, purchase_price, days_to_maturity
        )
        return {
            "Tag": "Bond Equivalent Yield",
            "Face value": face_value,
            "Purchase Price": purchase_price,
            "Days to maturity": days_to_maturity,
            "Bond Equivalent Yield (BEY)": f"{functions.decimal_to_percent(bey)}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)