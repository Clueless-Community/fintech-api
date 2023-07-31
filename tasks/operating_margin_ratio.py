from helpers import functions
from fastapi import HTTPException, status

def operating_margin_ratio(operating_income:int,net_sales:int):
    try:
        operating_margin_ratio_value = functions.operating_margin_ratio(operating_income,net_sales)
        return {
            "Tag": "Operating Margin Ratio",
            "Operating Income": operating_income ,
            "Net Sales": net_sales ,
            "Operating Margin Ratio": operating_margin_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)