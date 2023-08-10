from helpers import functions
from fastapi import HTTPException, status

def financial_goal_palnner(initial_savings_amount: int, monthly_savings_amount: int, target_savings_amount: int, 
timeframe: int):
    try:
       total_savings_goal = target_savings_amount - initial_savings_amount
       months = timeframe if isinstance(timeframe, int) else timeframe * 12
       monthly_savings_goal = total_savings_goal / months

       savings_schedule = []
       current_savings = initial_savings_amount

       for month in range(1, months + 1):
            current_savings += monthly_savings_amount
            savings_schedule.append((month, current_savings))
       return {
            "Tag": "financial goal planner",
             "monthly_savings_goal": monthly_savings_goal,
            "total_savings_goal": total_savings_goal,
            "savings_schedule": savings_schedule
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) 