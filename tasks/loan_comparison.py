from fastapi import HTTPException, status
from helpers import functions

def loan_comparison(loan_amount: float, loan_term: int):
    try:
        if loan_amount <= 0 or loan_term <= 0:
            raise HTTPException(status_code=400, detail="Loan amount and loan term must be positive.")

        class LoanOffer:
            def __init__(self, name, interest_rate, loan_term, processing_fee):
                self.name = name
                self.interest_rate = interest_rate
                self.loan_term = loan_term
                self.processing_fee = processing_fee

        # Sample loan offers data (You can fetch this from a database or API)
        loan_offers = [
            LoanOffer("Loan Offer A", 8.5, 12, 200),
            LoanOffer("Loan Offer B", 7.9, 24, 150),
            LoanOffer("Loan Offer C", 9.2, 18, 250),
            LoanOffer("Loan Offer D", 6.5, 36, 100),
        ]

        # Calculate the total repayment amount for each loan offer
        loan_offers_with_total_repayment = [
            {
                "name": offer.name,
                "interest_rate": offer.interest_rate,
                "loan_term": offer.loan_term,
                "processing_fee": offer.processing_fee,
                "total_repayment": loan_amount + (loan_amount * (offer.interest_rate / 100)) + offer.processing_fee
            }
            for offer in loan_offers
        ]

        # Sort the loan offers based on total repayment amounts (lowest to highest)
        sorted_loan_offers = sorted(loan_offers_with_total_repayment, key=lambda x: x["total_repayment"])

        return sorted_loan_offers

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
