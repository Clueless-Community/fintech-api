from helpers import functions
from fastapi import HTTPException, status

def commission_calc_task(
    sales_price: float = None, commission_rate: float = None, commission: float = None
):
    try:
        output = functions.commission_calc(
            sales_price, commission_rate, commission)

        if sales_price == None and commission_rate != None and commission != None:
            return {
                "Tag": "Sales Price",
                "Sales Price": output,
                "Commission Rate": f"{commission_rate}%",
                "Commission": commission,
            }
        elif sales_price != None and commission_rate == None and commission != None:
            return {
                "Tag": "Commission Rate",
                "Sales Price": sales_price,
                "Commission Rate": f"{output}%",
                "Commission": commission,
            }
        elif sales_price != None and commission_rate != None and commission == None:
            return {
                "Tag": "Commission",
                "Sales Price": sales_price,
                "Commission Rate": f"{commission_rate}%",
                "Commission": output,
            }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)