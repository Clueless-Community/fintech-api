 
def risk_assessment(age: int, financial_goals: str, investment_knowledge: str, time_horizon: str):
   
        # Calculate risk score based on the provided factors
    risk_score = calculate_risk_score(age, financial_goals, investment_knowledge, time_horizon)

    return {
            "Tag": "Risk Assessment",
            "Age": age,
            "Financial Goals": financial_goals,
            "Investment Knowledge": investment_knowledge,
            "Time Horizon": time_horizon,
            "Risk Score": risk_score,
        }
    

def calculate_risk_score(age: int, financial_goals: str, investment_knowledge: str, time_horizon: str) -> int:
    # Perform calculations and return a risk score
    # You can define your own logic based on the provided factors
    risk_score = 0

    # Example risk assessment logic
    if age < 30:
        risk_score += 2
    elif age >= 30 and age < 50:
        risk_score += 4
    else:
        risk_score += 6

    if financial_goals == "short-term":
        risk_score += 2
    elif financial_goals == "mid-term":
        risk_score += 4
    elif financial_goals == "long-term":
        risk_score += 6

    if investment_knowledge == "low":
        risk_score += 2
    elif investment_knowledge == "medium":
        risk_score += 4
    elif investment_knowledge == "high":
        risk_score += 6

    if time_horizon == "short-term":
        risk_score += 2
    elif time_horizon == "medium-term":
        risk_score += 4
    elif time_horizon == "long-term":
        risk_score += 6

    return risk_score

