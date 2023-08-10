from helpers import functions
from fastapi import HTTPException, status

def investment_assest_allocation(
    risk_tolerance: str,
    investment_goals: str,
    age: int,
    market_outlook: str
):
    try:
        if risk_tolerance == "conservative":
                allocation = {"stocks": 30, "bonds": 60, "cash": 10}
        elif risk_tolerance == "moderate":
            allocation = {"stocks": 50, "bonds": 40, "cash": 10}
        else:
            allocation = {"stocks": 70, "bonds": 20, "cash": 10}

        if investment_goals == "retirement":
            expected_return = 0.08
        else:
            expected_return = 0.1
        
        if market_outlook == "bullish":
            expected_return += 0.02
        elif market_outlook == "bearish":
            expected_return -= 0.02

        if age < 30:
            risk_level = "low"
        elif age < 50:
            risk_level = "moderate"
        else:
            risk_level = "high"

        correlation_coefficient = 0.5
        num_unique_holdings = 25

        rebalancing_strategy = "calendar-based"
        return {
            "Tag": "Investment Assest Allocation",
            "asset_allocation": allocation,
            "expected_return": expected_return,
            "risk_level": risk_level,
            "diversification_metrics": {
                "correlation_coefficient": correlation_coefficient,
                "num_unique_holdings": num_unique_holdings,
            },
            "rebalancing_strategy": rebalancing_strategy,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)