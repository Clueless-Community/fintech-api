from helpers import functions
from fastapi import HTTPException, status

def defensive_interval_ratio_task(cash: float, marketable_securities: float, net_receivables: float, 
annual_operating_expenses: float, non_cash_charges: float):
    try:
        current_assets = cash + marketable_securities + net_receivables	
        daily_operational_expenses = (annual_operating_expenses - non_cash_charges) / 365
        ratio = functions.defensive_interval_ratio(cash, marketable_securities, net_receivables, annual_operating_expenses, non_cash_charges)
        return {
			"Tag": "Defensive Interval Ratio",
			"Cash": cash,
			"Marketable Securites": marketable_securities,
			"Net Receivables": net_receivables,
			"Annual Operating Expenses": annual_operating_expenses,
			"Non Cash Charges": non_cash_charges,
			"Current Assets": current_assets,
			"Daily Operational Expenses": daily_operational_expenses,
			"Defensive Interval Ratio": ratio
		}
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

