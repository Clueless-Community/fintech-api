from helpers import functions
from fastapi import HTTPException, status

def calculate_gst_task(price, gst_rate):
    try:
        gst_amount, total_price = functions.calulate_gst(price, gst_rate)
        return {
            "Tag": "Calculate GST and Total Price",
            "Original Price": price,
            "GST rate": gst_rate,
            "Amount of GST": f"{gst_amount}",
            "Total price after GST": f"{total_price}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)