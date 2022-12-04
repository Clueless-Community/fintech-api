# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate

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