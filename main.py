from fastapi import FastAPI, HTTPException, status
from helpers import functions


app = FastAPI()


@app.get('/')
def index():
    return {"details": ""}

@app.get('/rate',tags=["simple_interest"], description="Calculate simple interest rates")
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    try:
        rate = functions.simple_interest_rate(amount_paid, principle_amount,months)
        return {
            "Tag":"Simple Interest Rate",
            "Total amount paid":amount_paid,
            "Principle amount":principle_amount,
            "Interest Paid":amount_paid-principle_amount,
            "Interest Rate":f"{rate}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get('/payback_period',tags=["payback_period"], description="Calculate payback period")
def payback_period(years_before_recovery:int, unrecovered_cost:float, cash_flow:float):
    try:
        period = functions.payback_period(years_before_recovery, unrecovered_cost, cash_flow)
        return {
            "Tag":"Payback period",
            "Years before full recovery":years_before_recovery,
            "Unrecovered cost at start of the year":unrecovered_cost,
            "Cash flow during the year":cash_flow,
            "Payback period":f"{period}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    