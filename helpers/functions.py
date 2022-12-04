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


