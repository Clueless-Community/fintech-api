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

# Endpoints to calculate compound intrest.
@app.get(
    "/compound_interest" ,
    tags=["compound_interest_amount"],
    description="Calculate compound interest amount",
)
def compound_intrest(principal_amount:float, intrest_rate:float, years:int, compounding_period:int):
    try:
        amount = functions.compound_interest(principal_amount, intrest_rate, years, compounding_period)
        return{
            "Tag":"Compound Intrest Amount" ,
            "Principle amount" : principal_amount,
            "Intrest Rate" : intrest_rate,
            "Time in Years": years,
            "Compounding Period": compounding_period,
            "Amount after intrest":f"{amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)