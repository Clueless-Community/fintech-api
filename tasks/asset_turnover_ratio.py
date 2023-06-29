from helpers import functions
from fastapi import HTTPException, status

def asset_turnover_ratio_task(
    net_sales: float, total_asset_beginning: float, total_asset_ending: float
):
    try:
        asset_turnover_ratio = functions.asset_turnover_ratio(
            net_sales, total_asset_beginning, total_asset_ending
        )
        return {
            "Tag": "Asset Turnover Ratio",
            "Net Sales": net_sales,
            "Total beginning asset": total_asset_beginning,
            "Total ending asset": total_asset_ending,
            "Total average asset": (total_asset_beginning + total_asset_ending) / 2,
            "Asset Turnover Ratio": f"{asset_turnover_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)