# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate
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
