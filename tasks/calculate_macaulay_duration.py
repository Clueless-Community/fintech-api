from helpers import functions
from fastapi import HTTPException, status

def calculate_macaulay_duration_task(
    face_value : float, coupon_rate : float, dt : int, month : int, year : int, coupon_frequency : int, discount_rate : float
):
    '''
    Macaulay duration is the weighted average term to maturity of the cash flows from a bond. 
    Inputs:  face value of bond, coupon rate, dt, month, year of maturity, coupon frequency, discount rate
    Ouput: Macaulay duration in years 
    '''
    try:
        duration = functions.calculate_gratuity(
            face_value, coupon_rate, dt, month, year, coupon_frequency, discount_rate
        )
        return {
            "Tag": "Macaulay_duration",
            "Face-value of bond": face_value,
            "Coupon Rate (in decimal)": coupon_rate,
            "Date of maturity(DD)": dt,
            "Month of maturity(MM)": month,
            "Year of maturity(YY)": year,
            "Coupon frequency": coupon_frequency,
            "Discount frequency (int decimal)": discount_rate,
            "Macaulay duration": f"{duration}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)