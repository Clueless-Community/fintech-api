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
            "Interest Rate": f"{rate}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get(
    "/future_sip",
    tags=["future_sip"],
    description="Calculate Future Value of SIP",
)
def future_sip(interval_investment:float, rate_of_return:float, number_of_payments:int):
    try:
        value = functions.future_sip(interval_investment, rate_of_return, number_of_payments)
        return {
            "Tag": "Future Value of SIP",
            "Investment at every Interval": interval_investment,
            "Interest": (rate_of_return/100)/12,
            "Number of Payments": number_of_payments,
            "Future Value": f"{value}%"
        }         
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
#endpoint for payback period
@app.get('/payback_period',
tags=["payback_period_years"], 
description="Calculate payback period",
)
def payback_period(years_before_recovery:int, unrecovered_cost:float, cash_flow:float):
    try:
        period = functions.payback_period(years_before_recovery, unrecovered_cost, cash_flow)
        return {
            "Tag":"Payback period",
            "Years before full recovery":years_before_recovery,
            "Unrecovered cost at start of the year":unrecovered_cost,
            "Cash flow during the year":cash_flow,
            "Payback period":f"{period}"
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
            "Amount after intrest":f"{amount}"
       }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Endpoints to calculate certificate of deposit (CD)
@app.get(
    "/certificate_of_deposit",
    tags=["certificate_of_deposit"],
    description="Calculate certificate of deposit (CD)",
)
def certificate_of_deposit(principal_amount:float, interest_rate:float, yrs:int, compounding_per_yr:int):
    try:
        cd = functions.certificate_of_deposit(principal_amount, interest_rate, yrs, compounding_per_yr)
        return {
            "Tag": "Certificate of Deposit (CD)",
            "Principal amount": principal_amount,
            "Interest Rate": interest_rate,
            "Time in Years": yrs,
            "Number of Compounding per Year": compounding_per_yr,
            "Certificate of Deposit (CD)": f"{cd}"
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

# Endpoint to calculate Compounded Annual Growth Rate.
@app.get(
    "/compounded_annual_growth_rate",
    tags=["compounded_annual_growth_rate"],
    description="Calculate compounded annual growth rate",
)
def compounded_annual_growth_rate(end_investment_value:float, initial_investment_value:float, years:int):
    try:
        cagr = functions.compounded_annual_growth_rate(end_investment_value, initial_investment_value, years)

        return {
            "Tag":"Compounded Annual Growth Rate",
            "End investment value":end_investment_value,
            "Initial investment value":initial_investment_value,
            "Years":years,
            "Compounded Annual Growth Rate":f"{cagr}%"
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
#Endpoint to calculate Jensen's Alpha
@app.get(
    "/jensens_alpha",
    tags=["jensens_alpha"],
    description="Calculate Jensen's Alpha of a market return",
)
def jensens_alpha(return_from_investment:float,return_of_appropriate_market_index:float,risk_free_rate:float,beta:float):
    try:
        alpha = functions.jensens_alpha(return_from_investment,return_of_appropriate_market_index,risk_free_rate,beta)
        return {
            "Tag": "Jensen's Alpha",
            "Total return from investment": return_from_investment,
            "Return of appropriate market index": return_of_appropriate_market_index,
            "Risk free rate": risk_free_rate,
            "Beta of the portfolio investment w.r.t chosen market index":beta,
            "Alpha of the return ":f'{alpha}%'
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)            



#Endpoint to calculate WACC 
@app.get(
    "/wacc",
    tags=["wacc"],
    description="Calculate Weighted Average Cost of Capital (WACC)",
)
def weighted_average_cost_of_capital(firm_equity,firm_debt,cost_of_equity,cost_of_debt,corporate_tax_rate):
    try:
        wacc = functions.wacc(firm_equity,firm_debt,cost_of_equity,cost_of_debt,corporate_tax_rate)
        return {
            "Tag": "Weighted Average Cost of Capital (WACC)",
            "Market value of firm's equity": firm_equity,
            "Market value of firm's debt": firm_debt,
            "Cost of equity": cost_of_equity,
            "Cost of debt":cost_of_debt,
            "Corporate tax rate":corporate_tax_rate,
            "WACC":f'{wacc}%'
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
            "EMI": f"{round(emi,3)}",
            "Total Amount Payble": f"{round(emi*months,3)}",
            "Interest amount": f"{round(emi*months-principle_amount,3)}"
        }
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Endpoint to calculate Variance of a Two Asset Portfolio
@app.get(
    "/asset_portfolio",
    tags=["asset_portfolio"],
    description="Calculate Variance of a Two Asset Portfolio",
)
def asset_portfolio(price_A:float, price_B:float, return_A:float, return_B:float, standard_dev_A:float, standard_dev_B:float, correlation:float):
    try:
        weight_A = price_A/(price_A + price_B)
        weight_B = price_B/(price_A + price_B)
        cov = correlation*standard_dev_A*standard_dev_B
        portfolio_variance = weight_A*weight_A*standard_dev_A*standard_dev_A + weight_B*weight_B*standard_dev_B*standard_dev_B + 2*weight_A*weight_B*cov
        expected_return = 100*(weight_A*return_A + weight_B*return_B)
        return {
            "Tag": "Portfolio Variance",
            "Expected Returns": f"{expected_return}%",
            "Portfolio Variance": f"{portfolio_variance}", 
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#Endpoint to calculate break even point 
@app.get(
    "/bep",
    tags=["bep"],
    description="Calculate Break Even Point",
)
def break_even_point(fixed_cost:float,selling_price:float,variable_cost:float):
    try:
        bep = functions.bep(fixed_cost,selling_price,variable_cost)
        return{
            "Tag" : "Break Even Point (BEP)",
            "Fixed costs" : fixed_cost,
            "Selling price per unit" : selling_price,
            "Variable cost per unit" : variable_cost,
            "Break Even Point in units" : f"{bep[0]}",
            "Break Even Point in Rupees" : f"{bep[1]}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
