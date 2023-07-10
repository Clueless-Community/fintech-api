from helpers import functions
from fastapi import HTTPException, status

def calculate_bvps_task(stockholders_equity, preferred_stock, average_outstanding_shares):
    try:
        book_value = functions.calulate_bvps(
            stockholders_equity, preferred_stock, average_outstanding_shares
        )
        return {
            "Tag": "Calculate Book value per share",
            "Stockholders Equity": stockholders_equity,
            "Preferred Stock value": preferred_stock,
            "Average outstanding shares": average_outstanding_shares,
            "Book value per share": f"{book_value}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)