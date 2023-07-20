from helpers import functions
from fastapi import HTTPException, status

def treynor_ratio_task(
    returns: list[float], risk_free_rate: float, beta: float
):
    try:
        ratio = functions.calculate_treynor_ratio(
            returns, risk_free_rate, beta)
        return {
            "Tag": "Treynor Ratio",
            "Returns": returns,
            "Risk-free Rate": risk_free_rate,
            "Beta": beta,
            "Treynor Ratio": ratio,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))