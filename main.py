from fastapi import FastAPI, HTTPException, status
from helpers import functions


app = FastAPI(
    title="FinTech API",
    description="An API that helps you to deal with your financial calculations.",
    version="1",
    contact={
        "name": "Clueless Community",
        "url": "https://www.clueless.tech/",
        "email": "https://www.clueless.tech/contact-us",
    },
    license_info={
        "name": " MIT license",
        "url": "https://github.com/Clueless-Community/fintech-api/blob/main/LICENSE.md",
    },
)


@app.get("/")
def index():
    return {
        "title": "FinTech API",
        "description": "An API that helps you to deal with your financial calculations.",
        "version": "1",
        "contact": {
            "name": "Clueless Community",
            "url": "https://www.clueless.tech/",
            "email": "https://www.clueless.tech/contact-us",
        },
        "license_info": {
            "name": " MIT license",
            "url": "https://github.com/Clueless-Community/fintech-api/blob/main/LICENSE.md",
        },
        "endpoints":{
            "/simple_interest":"Calculate simple interest rates"
        }
    }

# Endpoints to calculate simple interest.
@app.get(
    "/simple_interest_rate",
    tags=["simple_interest_rate"],
    description="Calculate simple interest rates",
)
def simple_interest_rate(amount_paid: float, principle_amount: float, months: int):
    try:
        rate = functions.simple_interest_rate(amount_paid, principle_amount, months)
        return {
            "Tag": "Simple Interest Rate",
            "Total amount paid": amount_paid,
            "Principle amount": principle_amount,
            "Interest Paid": amount_paid - principle_amount,
            "Interest Rate": f"{rate}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get(
    "/loan_emi",
    tags=["load_emi"],
    description="Calculate Loan EMI",
)
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    try:
        emi = functions.loan_emi(principle_amount, annual_rate, months)
        return {
            "Tag": "Loan Emi",
            "Princiapl amount borrowed": principle_amount,
            "Annual Rate of interest": annual_rate,
            "Total number of monthly payments": months,
            "EMI": f"{emi}%",
            "Total Amount Payble": f"{emi*months}%",
            "Interest amount": f"{emi*months-principle_amount}%"
        }
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
