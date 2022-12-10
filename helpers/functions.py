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

# Function to calculate the future price in a put - call parity
def put_call_parity(call_price:float, put_price:float, strike_price:float):
    future_price = call_price + strike_price - put_price
    return future_price

#Function to calculate break even point 
def break_even_point(fixed_cost:float, selling_price:float, variable_cost:float):
    contribution_margin = selling_price - variable_cost
    units = fixed_cost//contribution_margin
    rupees = fixed_cost//(contribution_margin/selling_price)
    return units,rupees

#Function to calculate the Price-to-Earning ratio (P/E ratio):
def price_to_earning_ratio(share_price:float, earnings_per_share:float):
    p_e_ratio = share_price//earnings_per_share
    return p_e_ratio  

#Function to calculate the Dividend yield ratio:
def dividend_yield_ratio(dividend_per_share:float,share_price:float):
    dividend_yield = dividend_per_share//share_price
    return dividend_yield


# Function to calculate the dividend payout ratio 
def dividend_payout_ratio(dividend_per_share:float,earnings_per_share:float):
    dividend_payout = dividend_per_share//earnings_per_share
    return dividend_payout
    
#Function to calculate the Fixed-charge coverage ratio :
def fixed_charge_coverage_ratio(earnings_before_interest_taxes:float,fixed_charge_before_tax:float,interest:float):
    a = earnings_before_interest_taxes + fixed_charge_before_tax
    b = interest + fixed_charge_before_tax
    fccr = a//b
    return fccr    

