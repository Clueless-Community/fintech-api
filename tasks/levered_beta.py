from helpers import functions
from fastapi import HTTPException, status

def levered_beta_task(unlevered_beta: float, tax_rate: float, debt: float, equity: float):
    try:
        l_beta = functions.levered_beta(unlevered_beta, tax_rate, debt, equity)
        return {
            "Tag": "Levered Beta",
            "Unlevered Beta": unlevered_beta,
            "Tax rate": tax_rate,
            "debt": debt,
            "Equity": equity,
            "Levered Beta": f"{l_beta}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)