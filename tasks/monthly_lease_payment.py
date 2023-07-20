from helpers import functions
from fastapi import HTTPException, status

def monthly_lease_payment_task(
    Asset_value: float,
    monthly_lease_interest_rate: float,
    number_of_lease_payments: float,
):
    try:
        pmt = functions.monthly_lease_payment(
            Asset_value, monthly_lease_interest_rate, number_of_lease_payments
        )
        return {
            "Tag": "Monthly Lease Payment",
            "Asset value": Asset_value,
            "Monthly lease interest rate": monthly_lease_interest_rate,
            "Number of lease payments": number_of_lease_payments,
            "Monthly Lease Payment": f"{pmt}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)