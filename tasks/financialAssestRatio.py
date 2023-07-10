from helpers import functions
from fastapi import HTTPException, status

def financial_assest_ratio(current_assets: float, current_liabilities: float, total_debt: float, 
total_equity: float, net_income: float, total_assets:float, total_revenue: float, gross_profit: float, stock_price: float, earnings_per_share:float):
    try:
        current_ratio = current_assets / current_liabilities
        debt_to_equity_ratio = total_debt / total_equity
        return_on_assets = net_income / total_assets
        return_on_equity = net_income / total_equity
        asset_turnover_ratio = total_revenue / total_assets
        gross_profit_margin = gross_profit / total_revenue
        net_profit_margin = net_income / total_revenue
        price_to_earnings_ratio = stock_price / earnings_per_share
        return {
            "Tag": "financial assest ratio",
            "current_ratio": current_ratio,
            "debt_to_equity_ratio": debt_to_equity_ratio,
            "return_on_assets": return_on_assets,
            "return_on_equity": return_on_equity,
            "asset_turnover_ratio": asset_turnover_ratio,
            "gross_profit_margin": gross_profit_margin,
            "net_profit_margin": net_profit_margin,
            "price_to_earnings_ratio": price_to_earnings_ratio,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) 