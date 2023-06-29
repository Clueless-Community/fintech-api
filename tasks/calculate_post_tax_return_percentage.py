from helpers import functions
from fastapi import HTTPException, status

def calculate_post_tax_return_percentage_task(tax_rate_percentage: float,
                                         annual_net_income: float,
                                         initial_cost_of_investment: float):
    try:
        post_tax_return_percentage = functions.calculate_post_tax_return_percentage(
            tax_rate_percentage, annual_net_income, initial_cost_of_investment)
        return {
            "Tag": "Calculate post tax return percentage",
            "Tax Rate Percentage": tax_rate_percentage,
            "Annual net income": annual_net_income,
            "Initial cost of investment": initial_cost_of_investment,
            "Post tax return percentage": post_tax_return_percentage
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)