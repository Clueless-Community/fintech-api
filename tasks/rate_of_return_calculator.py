from fastapi import HTTPException, status

def calcualate_rate_of_return(initial_investment: int, final_value: int, additional_investments: int, 
additional_withdrawals: int):
    try:
        total_invested = initial_investment + sum(additional_investments)
        final_value = final_value - sum(additional_withdrawals)

        rate_of_return = (final_value - total_invested) / total_invested
        percentage_return = rate_of_return * 100

        return {
            "Tag": "Rate of return Calculator",
            "Initial Investement": initial_investment,
            "Final Value": final_value,
            "Additional Investments": additional_investments,
            "Additional Withdrawals": additional_withdrawals,
            "Total Invested": total_invested,
            "Percentage Return": percentage_return,
            "Rate of Return": rate_of_return
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)