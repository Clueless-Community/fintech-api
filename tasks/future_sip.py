from helpers import functions
from fastapi import HTTPException, status

def future_sip_task(
    interval_investment: float, rate_of_return: float, number_of_payments: int
):
    try:
        value = functions.future_sip(
            interval_investment, rate_of_return, number_of_payments
        )
        return {
            "Tag": "Future Value of SIP",
            "Investment at every Interval": interval_investment,
            "Interest": functions.percent_to_decimal(rate_of_return) / 12,
            "Number of Payments": number_of_payments,
            "Future Value": f"{value}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)