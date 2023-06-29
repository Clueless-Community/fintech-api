from helpers import functions
from fastapi import HTTPException, status

def salary_calculate_task(
    salary_amount: float,
    payment_frequency: str,
    hours_worked_per_day: int,
    days_worked_per_week: int,
):
    try:
        salary = functions.salary_calculate(
            salary_amount, payment_frequency, hours_worked_per_day, days_worked_per_week
        )

        return {
            "Tag": "Calculate Salary",
            "Salary Amount": salary_amount,
            "Payment frequency": payment_frequency,
            "Salary": salary,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)