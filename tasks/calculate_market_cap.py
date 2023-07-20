from helpers import functions
from fastapi import HTTPException, status

def calculate_market_cap_task(
    current_market_share_price: int, total_number_of_shares_outstanding: int
):
    try:
        calculate = functions.calculate_market_cap(
            current_market_share_price, total_number_of_shares_outstanding
        )
        return {
            "Tag": "Market capitalization value",
            "Current market share price": current_market_share_price,
            "Total number of shares outstanding": total_number_of_shares_outstanding,
            "Marketcap value": f"{calculate}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)