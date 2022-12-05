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


# Endpoints to calculate Compound Intrest.
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

# EndPoint to calculate Inflation 
@app.get(
    "/inflation" ,
    tags=["inflated"],
    description="Calculate Inflated amount"
)
def inflation(present_amount:float , inflation_rate:float , years:float):
    try:
        future_amount = functions.inflation(present_amount , inflation_rate ,years)
        return{
            "Tag":"Inflated Amount" ,
            "Present Amount" : present_amount,
            "Inflation Rate" : inflation_rate,
            "Time in Years": years,
            "Future Amount":f"{future_amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to Calculate Effective Annual Rate
@app.get(
    "/effective_annual_rate" ,
    tags=["Effective Annual Rate"],
    description="Calculate Effective Annual Rate"
)
def inflation(annual_interest_rate:float , compounding_period:int):
    try:
        Eff_annual_rate = functions.effective_annual_rate(annual_interest_rate, compounding_period)
        Eff_annual_rate_percentage = Eff_annual_rate * 100
        return{
            "Tag":"Effective Annual Rate" ,
            "Annual Intrest Rate" : annual_interest_rate,
            "Compounding Period" : compounding_period,
            "Effective Annual Rate (in percentage)":f"{Eff_annual_rate_percentage}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



@app.get('/roi',tags=["return_on_investment"], description="Calculate return on investment")
def return_on_investment(gain_from_investment:float, cost_of_investment:float):
    try:
        roi = functions.return_on_investment(gain_from_investment, cost_of_investment)

        return {
            "Tag":"Return on Investment",
            "Gain from Investment":gain_from_investment,
            "Cost of Investment":cost_of_investment,
            "Return on Investment":f"{roi}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


