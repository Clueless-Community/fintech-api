# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate

# Function to Calculate Certificate of Deposit (CD)
def certificate_of_deposit(principal_amount:float, interest_rate:float, yrs:int, compounding_per_yr:float):
    cd = principal_amount * (1 + interest_rate / (100 * compounding_per_yr) ) ** (compounding_per_yr * yrs)
    return cd
