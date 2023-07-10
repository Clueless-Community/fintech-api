from helpers import functions
from fastapi import HTTPException, status

def calculate_loan_affordability_task(
    income: float,  # annual Income
    expenses: float,  # annual expenses
    loan_term: int,  # loan term period
    interest_rate: float,  # annual interest rate
):
    """
    This endpoint is use to check your ability to take any particular Loan on the Basis on
    your income,expenses,loan_term,intrest_rate, This is basically loan affordability function

    eg url :- http://127.0.0.1:8000/loan-affordability?income=5000&expenses=2000&loan_term=12&interest_rate=5

    explanation for calculating max_loan_amount :-
        (1 + utils.percent_to_decimal(interest_rate)): This calculates the factor by which the loan amount increases due to the interest rate. For example, if the interest rate is 5%, this factor would be 1.05.
        ** -loan_term: This raises the above factor to the power of negative loan_term. It represents the compounding effect of interest over the loan term. For example, if the loan term is 12 months, this factor would be (1.05) ** -12
        (1 - (1 + utils.percent_to_decimal(interest_rate)) ** -loan_term): This calculates the ratio of the remaining loan balance after making monthly payments to the initial loan amount. It represents the discounted value of the loan.
        (monthly_income - monthly_expenses): This calculates the disposable income available for loan repayment each month.
        (monthly_income - monthly_expenses) * (1 - (1 + utils.percent_to_decimal(interest_rate)) ** -loan_term): This calculates the discounted monthly loan payment amount based on the available disposable income.

    """
    try:
        # monthly_income = income / 12
        # monthly_expenses = expenses / 12

        max_loan_amount = functions.calculate_max_loan_amount(
            income, expenses, loan_term, interest_rate
        )

        return {
            "income": income,
            "expenses": expenses,
            "loan_term": loan_term,
            "interest_rate": interest_rate,
            "max_loan_amount": max_loan_amount,
        }
    except:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some Error occured",
        )