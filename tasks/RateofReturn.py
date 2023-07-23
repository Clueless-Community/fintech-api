from helpers import functions
from fastapi import HTTPException, status

def calculate_rate_of_return(initial_investment: float, final_value: float, cash_flows: float, 
time_period: float, holding_period: float):
    try:
        net_cash_flows = sum(cash_flows)
        final_value += net_cash_flows
    
        if holding_period > 0:
            rate_of_return = ((final_value - initial_investment) / (initial_investment + net_cash_flows)) * 100
            holding_period_return = ((final_value - initial_investment) / initial_investment) * 100
        else:
            rate_of_return = ((final_value - initial_investment) / initial_investment) * 100
            holding_period_return = rate_of_return
        
        annualized_return = rate_of_return / time_period
        return {
            "Tag": "Rate of return",
            "rate_of_return": rate_of_return,
            "annualized_return": annualized_return,
            "holding_period_return": holding_period_return
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) 