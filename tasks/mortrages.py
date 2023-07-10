from helpers import functions
from fastapi import HTTPException, status

def mortrage_task(princial: int, interest_rate: float, years: int, down_payment: int, property_tax_rate: float, insurance_rate: float):

    try:
        mortrage = functions.calculate_mortgage(
            principal=princial,
            interest_rate=interest_rate,
            years=years,
            down_payment=down_payment,
            property_tax_rate=property_tax_rate,
            insurance_rate=insurance_rate
        )
        return {
            "Monthly Payment": mortrage['monthly_payment'],
            "Total Payment": mortrage['total_payment'],
            "Total Property Tax": mortrage['total_property_tax'],
            "Total insurance cost": mortrage['total_insurance_cost'],
            "Total Cost": mortrage['total_cost'],
            "Loan to value ratio": mortrage["loan_to_value_ratio"]
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)