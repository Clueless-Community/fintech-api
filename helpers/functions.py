# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate
    
# Function to Calculate Loan Emi
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    monthly_rate=annual_rate/1200
    emi= (principle_amount*monthly_rate*(1+monthly_rate)**months)/(((1+monthly_rate)**months -1))
    return emi
    
def future_sip(interval_investment:float, rate_of_return:float, number_of_payments:int):
    interest= (rate_of_return/100)/12
    value = interval_investment*((1+ interest)**number_of_payments - 1)*(1+interest)/interest
    return value


def payback_period(years_before_recovery:int, unrecovered_cost:float, cash_flow:float):
    period=years_before_recovery+(unrecovered_cost/cash_flow)
    return period

# Function to Calculate Compound Intrest 
def compound_interest(principal_amount:float, intrest_rate:float, years:int, compounding_period:int):
    amount = principal_amount * (pow((1 + (intrest_rate / compounding_period)), (compounding_period*years)))
    print(amount)
    return amount

# Function to Calculate Inflation
def inflation(present_amount:float , inflation_rate:float ,years:int):
    future_amount = present_amount*(pow((1+inflation_rate),years))
    return future_amount

# Function to Calculate Effective Annual Rate
def effective_annual_rate(annual_interest_rate:float , compounding_period:int):
    EAR = pow((1+(annual_interest_rate/compounding_period)),compounding_period) -1
    return EAR

# Function to Calculate Certificate of Deposit (CD)
def certificate_of_deposit(principal_amount:float, interest_rate:float, yrs:int, compounding_per_yr:int):
    cd = principal_amount * (1 + interest_rate / (100 * compounding_per_yr) ) ** (compounding_per_yr * yrs)
    return float(cd)


# Function to Calculate Return on Investment
def return_on_investment(gain_from_investment:float, cost_of_investment:float):
    roi = (gain_from_investment - cost_of_investment)/cost_of_investment
    return roi

# Function to calculate Compounded Annual Growth Rate (CAGR)
def compounded_annual_growth_rate(end_investment_value:float, initial_investment_value:float, years:int):
    n=1/years
    cagr=(end_investment_value/initial_investment_value)**n -1
    return cagr

#Function to calculate Jensens Alpha
def jensens_alpha(return_from_investment:float,return_of_appropriate_market_index:float,risk_free_rate:float,beta:float):
    alpha=return_from_investment-(risk_free_rate+beta*(return_of_appropriate_market_index-risk_free_rate))
    return alpha 

#Function to calculate Weighted Average Cost of Capital (WACC) 
def weighted_average_cost_of_capital(firm_equity:float,firm_debt:float,cost_of_equity:float,cost_of_debt:float,corporate_tax_rate:float):
    v=firm_debt+firm_equity
    wacc=(firm_equity*cost_of_equity/v)+(firm_debt*cost_of_debt*(1-corporate_tax_rate)/v)
    return wacc
    
# Function to calculate variance of a two asset portfolio
def asset_portfolio(price_A:float, price_B:float, retrun1:float, return2:float, standard_dev_A:float, standard_dev_B:float, stock_correlation:float):
    weight_A = price_A/(price_A + price_B)
    weight_B = price_B/(price_A + price_B)
    cov = stock_correlation*standard_dev_A*standard_dev_B
    portfolio_variance = weight_A*weight_A*standard_dev_A*standard_dev_A + weight_B*weight_B*standard_dev_B*standard_dev_B + 2*weight_A*weight_B*cov
    return portfolio_variance
