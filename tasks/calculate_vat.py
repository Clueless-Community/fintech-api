from helpers import functions
from fastapi import HTTPException, status

async def calculate_vat_task(price: float, vat_rate: float):
    try:
        excluding_vat = price / (1 + functions.percent_to_decimal(vat_rate))
        including_vat = price
        vat_amount = price - excluding_vat

        return {
            "Price (excluding VAT)": excluding_vat,
            "Price (including VAT)": including_vat,
            "VAT Amount": vat_amount,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during VAT calculation",
        )
