# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate

# Function to Calculate Return on Investment
def return_on_investment(gain_from_investment:float, cost_of_investment:float):
    roi = (gain_from_investment - cost_of_investment)/cost_of_investment
    return roi

# Function to calculate Compounded Annual Growth Rate (CAGR)
def compounded_annual_growth_rate(end_investment_value:float, initial_investment_value:float, years:int):
    n=1/years
    cagr=(end_investment_value/initial_investment_value)**n -1
    return cagr
