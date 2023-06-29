from helpers import functions
from fastapi import HTTPException, status

def balloon_balance_task(
    present_value: float,
    payment: float,
    rate_per_payment: float,
    number_of_payments: float,
):
    try:
        balloon_balance = functions.balloon_balance_of_loan(
            present_value, payment, rate_per_payment, number_of_payments
        )
        return {
            "Tag": "Balloon Balance of a Loan",
            "Present Value (Original Balance)": present_value,
            "Payment": payment,
            "Rate per Payment": rate_per_payment,
            "Number of Payments": number_of_payments,
            "Future Value (Balloon Balance)": balloon_balance,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)