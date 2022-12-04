# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate

def payback_period(years_before_recovery:int, unrecovered_cost:float, cash_flow:float):
    period=years_before_recovery+(unrecovered_cost/cash_flow)
    return period
