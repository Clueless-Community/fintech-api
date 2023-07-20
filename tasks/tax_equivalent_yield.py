from helpers import functions
from fastapi import HTTPException, status

def tax_equivalent_yield_task(tax_free_yield: float, tax_rate: float):
    try:
        tax_equivalent_yield = functions.tax_equivalent_yield(
            tax_free_yield, tax_rate)
        return {
            "Tag": "Tax Equivalent Yield",
            "Tax Free Yield": tax_free_yield,
            "Tax Rate": tax_rate,
            "Tax Equivalent Yield": tax_equivalent_yield,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)