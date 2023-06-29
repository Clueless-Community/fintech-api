from helpers import functions
from fastapi import HTTPException, status

def duration_task(rate, coupon_rate, frequency, face_value, settlement_date, maturity_date):
    try:
        duration = functions.duration(
            rate, coupon_rate, frequency, face_value, settlement_date, maturity_date
        )
        return {
            "Tag": "Convexity Adjusted Duration",
            "Market Rate": rate,
            "Coupon rate": coupon_rate,
            "Frequency": frequency,
            "Face Value": face_value,
            "Settlement Date": settlement_date,
            "Maturity Date": maturity_date,
            "Convexity Adjusted Duration": f"{duration}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)