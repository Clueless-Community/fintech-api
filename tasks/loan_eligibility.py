from fastapi import HTTPException, status

def loan_eligibility_check(credit_score: float, monthly_income: float,  loan_amount:float):

    try:
        max_debt_to_income_ratio = 0.4
        max_loan_amount = monthly_income * max_debt_to_income_ratio

        if loan_amount > max_loan_amount:
            loan_eligibility = -1
            loan_terms = ""
            interest_rate = 0
            monthly_payment = 0
            loan_agreement = ""
        else:
            loan_eligibility = loan_amount / 1000  
            loan_terms = "5 years" 
            interest_rate = 5.5  
            monthly_payment = (loan_amount * (1 + interest_rate / 100)) / (5 * 12)  
            loan_agreement = "Loan agreement details"
        return {
            "loan_eligibility": loan_eligibility,
            "loan_terms": loan_terms,
            "loan_amount": loan_amount,
            "interest_rate": interest_rate,
            "monthly_payment": monthly_payment,
            "loan_agreement": loan_agreement
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
