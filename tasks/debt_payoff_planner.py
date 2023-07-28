from fastapi import HTTPException, status
from helpers import functions

def debt_payoff_planner(debt_amount: float, interest_rate: float, monthly_payment: float):
    try:
        result = functions.debt_payoff_planner(debt_amount, interest_rate, monthly_payment)
        return {
            "Tag": "Debt Payoff Planner",
            "Debt Amount": debt_amount,
            "Interest Rate": interest_rate,
            "Monthly Payment": monthly_payment,
            "Months to Pay Off": result["Months to Pay Off"],
            "Total Interest Paid": result["Total Interest Paid"],
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
