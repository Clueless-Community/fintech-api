from helpers import functions
from fastapi import HTTPException, status

def jensens_alpha_task(
    return_from_investment: float,
    return_of_appropriate_market_index: float,
    risk_free_rate: float,
    beta: float,
):
    try:
        alpha = functions.jensens_alpha(
            return_from_investment,
            return_of_appropriate_market_index,
            risk_free_rate,
            beta,
        )
        return {
            "Tag": "Jensen's Alpha",
            "Total return from investment": return_from_investment,
            "Return of appropriate market index": return_of_appropriate_market_index,
            "Risk free rate": risk_free_rate,
            "Beta of the portfolio investment w.r.t chosen market index": beta,
            "Alpha of the return ": f"{alpha}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)