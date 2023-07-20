from helpers import functions
from fastapi import HTTPException, status

def calculate_policy_premium(policy_type: str, age: int, coverage_amount: int, deductible: int, num_claims: int, num_accidents: int):
    try:
        policy_factors = {
        "auto": {
            "age": {
                "18-25": 1.5,
                "26-40": 1.2,
                "41-60": 1.0,
                "61+": 1.3
            },
            "claims": {
                "0": 1.0,
                "1-3": 1.2,
                "4+": 1.5
            },
            "accidents": {
                "0": 1.0,
                "1-2": 1.2,
                "3+": 1.5
            }
        },
    }

        if policy_type not in policy_factors:
            return None  

        factors = policy_factors[policy_type]

        base_premium = coverage_amount * 0.01  
        age_multiplier = factors["age"].get(age, 1.0)
        claims_multiplier = factors["claims"].get(num_claims, 1.0)
        accidents_multiplier = factors["accidents"].get(num_accidents, 1.0)
        deductible_factor = 1 - (deductible / coverage_amount)  
           
        premium_amount = base_premium * age_multiplier * claims_multiplier * accidents_multiplier * deductible_factor

        return {
            "Tag": "Debt Service Coverage Ratio",
            "Premium Amount": premium_amount,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) 