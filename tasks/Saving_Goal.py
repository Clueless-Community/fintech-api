from fastapi import HTTPException, status

def saving_goal(current_savings: float, monthly_contributions: float, interest_rate: float, goal_amount: float):
    try:
        while current_savings < goal_amount:
         months_required += 1
        total_contributions += monthly_contributions
        current_savings += monthly_contributions
        interest_earned += (current_savings * interest_rate / 100) / 12

        if current_savings >= goal_amount:

         return {
             "months_required": months_required,
            "total_contributions": total_contributions,
            "interest_earned": interest_earned,

        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) 