from helpers import functions
from fastapi import HTTPException, status

def receivables_turnover_ratio_task(sales_revenue: float, avg_accounts_receivable: float):
    try:
        receivables_turnover_ratio = functions.receivables_turnover_ratio(
            sales_revenue, avg_accounts_receivable
        )
        return {
            "Tag": "Receivables Turnover Ratio",
            "Sales Revenue": sales_revenue,
            "Avg Accounts Receivables": avg_accounts_receivable,
            "Receivables Turnover Ratio": receivables_turnover_ratio,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)