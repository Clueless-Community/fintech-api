from helpers import functions
from fastapi import HTTPException, status

def book_value_per_share_ratio(shareholders_equity:int,preferred_equity:int,total_common_share_outstanding:int):
    try:
        book_value_per_share_ratio_value = functions.book_value_per_share_ratio(shareholders_equity,preferred_equity,total_common_share_outstanding)
        return {
            "Tag": "Book Value Per Share Ratio",
            "Shareholders Equity": shareholders_equity ,
            "Preferred Equity":preferred_equity,
            "Total Common Share Outstanding": total_common_share_outstanding ,
            "Book Value Per Share Ratio": book_value_per_share_ratio_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)