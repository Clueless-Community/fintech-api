from helpers import functions
from fastapi import HTTPException, status
def gross_margin_ratio(gross_profit:int,net_sales: int):
    try:
        gross_margin_ratio_value = functions.gross_margin_ratio(gross_profit,net_sales)
        return {
            "Tag": "Gross Margin Ratio",
            "Gross Profit": gross_profit ,
            "Net Sales": net_sales ,
            "Gross Margin Ratio": gross_margin_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

