from helpers import functions
from fastapi import HTTPException, status

def certificate_of_deposit_task(
    principal_amount: float, interest_rate: float, yrs: int, compounding_per_yr: int
):
    try:
        cd = functions.certificate_of_deposit(
            principal_amount, interest_rate, yrs, compounding_per_yr
        )
        return {
            "Tag": "Certificate of Deposit (CD)",
            "Principal amount": principal_amount,
            "Interest Rate": interest_rate,
            "Time in Years": yrs,
            "Number of Compounding per Year": compounding_per_yr,
            "Certificate of Deposit (CD)": f"{cd}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)