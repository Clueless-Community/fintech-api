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

