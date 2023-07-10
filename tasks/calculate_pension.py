from helpers import functions
from fastapi import HTTPException, status

def calculate_pension_task(
    monthly_investment_amount,
    no_of_years,
    annuity_rates,
    annuity_purchased,
    yearly_interest_rates,
):
    try:
        (total_corpus, lump_sum_pension, monthly_pension) = functions.calculate_pension(
            monthly_investment_amount,
            no_of_years,
            annuity_rates,
            annuity_purchased,
            yearly_interest_rates,
        )
        return {
            "Tag": "Calculate pension",
            "Total Corpus": total_corpus,
            "Lump sum pension": lump_sum_pension,
            "Monthly pension": monthly_pension,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)