from helpers import functions
from fastapi import HTTPException, status

def credit_card_payoff_task(
    debts: list, interest_rates: list, minimum_payments: list, monthly_payment: int
):
    try:
        result = functions.credit_card_payoff(
            debts, interest_rates, minimum_payments, monthly_payment
        )
        return {
            "Tag": "Credit card payoff",
            "debts": debts,
            "interest rates": interest_rates,
            "minimum payments": minimum_payments,
            "Monthly payment": monthly_payment,
            "Months": [r["month"] for r in result],
            "Interest paid": [r["interest_paid"] for r in result],
            "Total Payment": [r["total_payment"] for r in result],
        }
    except: 
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)