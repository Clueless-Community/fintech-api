from helpers import functions
from fastapi import HTTPException, status

def calculate_gratuity_task(last_salary: float, tenure_years: int, tenure_months: int):
    """
    Gratuity in India refers to the amount payable to an employee who has rendered his / her services
    to the company for a minimum period of five years (continuously)
    Partial years in the tenure are rounded off to 1 if the number of months is greater than 6.
    Last salary  includes the basic salary and the dearness allowanace
    Gratuity is calculated as: (15 * last salary * tenure in years) / 26

    Inputs: last drawn salary, tenure in years, last partial year in months
    """
    try:
        gratuity = functions.calculate_gratuity(
            last_salary, tenure_years, tenure_months
        )
        return {
            "Tag": "Gratuity",
            "Last salary (basic + dearness allowance)": last_salary,
            "Tenure in years (excluding last partial year)": tenure_years,
            "Last partial year in months": tenure_months,
            "Gratuity Amount": f"{gratuity}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)