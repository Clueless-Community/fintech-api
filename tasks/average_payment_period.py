from helpers import functions
from fastapi import HTTPException, status


def average_payment_period_task(beginning_accounts_payable: float, ending_accounts_payable: float,
total_credit_purchases: float):
    try:
        average_accounts_payable = (beginning_accounts_payable + ending_accounts_payable) / 2
        app = functions.average_payment_period(beginning_accounts_payable, ending_accounts_payable, total_credit_purchases)
        return {
		    "Tag": "Average Payment Period",
            "Beginning Accounts Payable": beginning_accounts_payable,
            "Ending Accounts Payable": ending_accounts_payable,
		    "Total Credit Purchases": total_credit_purchases,
            "Average Accounts Payable": average_accounts_payable,
            "Average Payment Period": f"{app} days",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

