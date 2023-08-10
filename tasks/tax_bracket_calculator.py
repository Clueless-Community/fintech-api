from helpers import functions
from fastapi import HTTPException, status

def tax_bracket_calculator(income: float, filing_status: str,):
  try:
        """
        Calculate the applicable tax bracket and tax liability based on a user's income and tax filing status (United States, 2021 tax brackets for single filers).

        Parameters:
            income (float): The user's total income.
            filing_status (str): The user's tax filing status ('single', 'married_joint', 'married_separate', 'head_of_household').

        Returns:
            dict: A dictionary containing the applicable tax bracket and tax liability.
                - 'Tax Bracket': The user's applicable tax bracket as a percentage.
                - 'Tax Liability': The calculated tax liability amount.
        """
        # Tax brackets and their corresponding tax rates (United States, 2021 tax brackets for single filers)
        tax_brackets = {
            0: 0.10,
            9875: 0.12,
            40125: 0.22,
            85525: 0.24,
            163300: 0.32,
            207350: 0.35,
            518400: 0.37,
        }

        # Find the applicable tax bracket and calculate the tax liability
        tax_liability = 0
        remaining_income = income

        for bracket, tax_rate in tax_brackets.items():
            if remaining_income <= bracket:
                tax_liability += remaining_income * tax_rate
                break
            else:
                taxable_income_in_bracket = bracket - max(0, income - remaining_income)
                tax_liability += taxable_income_in_bracket * tax_rate
                remaining_income -= taxable_income_in_bracket
        
        return {
            "Tag": "Accrued Interest",
            'Tax Bracket': "{:.2%}".format(tax_rate),
            'Tax Liability': tax_liability,
        }
     except:
         return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)