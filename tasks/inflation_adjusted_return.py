from helpers import functions
from fastapi import HTTPException, status

def inflation_adjusted_return_task(
    beginning_price: float,
    ending_price: float,
    dividends: float,
    beginning_cpi_level: float,
    ending_cpi__level: float,
):
    try:
        stock_return = (ending_price - beginning_price +
                        dividends) / beginning_price
        inflation = (ending_cpi__level - beginning_cpi_level) / \
            beginning_cpi_level
        inflation_adj_return = functions.inflation_adjusted_return(
            beginning_price,
            ending_price,
            dividends,
            beginning_cpi_level,
            ending_cpi__level,
        )
        return {
            "Tag": "Inflation Adjusted Return",
            "Stock Return": f"{stock_return}%",
            "Inflation Rate": f"{inflation}%",
            "Inflation Adjusted Return": f"{inflation_adj_return}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)