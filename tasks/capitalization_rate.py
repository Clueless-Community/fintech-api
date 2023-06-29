from helpers import functions
from fastapi import HTTPException, status

def capitalization_rate_task(
        rental_income: float,
        amenities: float,
        propertyManagement: float,
        propertyTaxes:float,
        insurance: float,
        current_market_value: float):
    try:
        rate = functions.capitalization_rate(rental_income, amenities, propertyManagement, 
            propertyTaxes, insurance, current_market_value
        )
        annual_income = rental_income + amenities, 
        expenses = propertyManagement + propertyTaxes + insurance,
        net_operating_income = annual_income - expenses,
 
        return {
            "Tag": "Capitalization Rate",
            "Rental Income": rental_income,
            "Amenities": amenities,
            "Property Management": propertyManagement,
            "Property Taxes": propertyTaxes,
            "Insurance": insurance,
  	        "Annual Income": annual_income,
  	        "Expenses": expenses,
  	        "Net Operating Income": net_operating_income,
  	        "Current Market Value": current_market_value,
  	        "Capitalization Rate": f"{rate}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)