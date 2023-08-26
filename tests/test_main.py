import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(current_dir, '..'))

from main import app
from fastapi import status
from fastapi.testclient import TestClient
import json


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_certificate_of_deposit():
    response = client.get(
        "/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3&compounding_per_yr=1"
    )
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Certificate of Deposit (CD)",
        "Principal amount": 5000.0,
        "Interest Rate": 5.0,
        "Time in Years": 3,
        "Number of Compounding per Year": 1,
        "Certificate of Deposit (CD)": "5788.125000000001",
    }


# Compounding per year cannot be 0, as it is division by 0 error
def test_certificate_of_deposit_invalid_value():
    response = client.get(
        "/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3&compounding_per_yr=0"
    )
    assert response.json()["status_code"] == 500


# Years cannot be a float, as it is a type error
def test_certificate_of_deposit_invalid_type():
    response = client.get(
        "/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3.5&compounding_per_yr=1"
    )
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "yrs"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            }
        ]
    }


def test_simple_interest_rate_main():
    response = client.get(
        "http://127.0.0.1:8000/simple_interest_rate?amount_paid=4500&principle_amount=453&months=3"
    )
    assert response.status_code == 200

    assert response.json() == {
  "Tag": "Simple Interest Rate",
  "Total amount paid": 4500,
  "Principle amount": 453,
  "Interest Paid": 4047,
  "Interest Rate": "3573.5099337748343%"
}

#
# def test_roi_main():
#     response = client.get("/roi/?current_value_of_investment=100&cost_of_investment=80")
#     assert response.status_code == 200
#
#     assert response.json() == {
#         "Tag": "Return on Investment",
#         "Current Value of Investment": 100,
#         "Cost of Investment": 80,
#         "Return on Investment": f"25.0%",
#     }
#
#
# def test_calculate_enterprise_value_main():
#     response = client.get(
#         "/enterprise-value/?share_price=10.00&fully_diluted_shares_outstanding=100&total_debt=500.00&preferred_stock=500.00&non_controlling_interest=1000.00&cash_and_cash_equivalents=1000.00"
#     )
#     assert response.status_code == 200
#
#     assert response.json() == {
#         "Tag": "Enterprise Value",
#         "Equity Value": 1000,
#         "Total Debt": 500,
#         "Preferred Stock": 500,
#         "Non-Controlling Interest": 1000,
#         "Cash & Cash Equivalents": 1000,
#         "Enterprise Value": 2000,
#     }
#
#
# # def test_calculate_treynor_ratio():
# #     response = client.get("/calculate_treynor_ratio/?returns=0.1,0.05,0.08,0.12,0.09&risk_free_rate=0.03")
# #     assert response.status_code == 200
# #
# #     assert response.json() == {
# #         "Tag": "Treynor Ratio",
# #         "returns": [0.1, 0.05, 0.08, 0.12, 0.09],
# #         "risk_free_rate": 0.03,
# #         "treynor_ratio": 1.6
# #     }
#
#
#
def test_future_sip():
    response = client.get(
        "http://127.0.0.1:8000/future_sip?interval_investment=1257&rate_of_return=3&number_of_payments=7"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Future Value of SIP",
  "Investment at every Interval": 1257,
  "Interest": 0.0025,
  "Number of Payments": 7,
  "Future Value": "8887.431327596654"
}


def test_calculate_pension():
    response = client.get(
        "http://127.0.0.1:8000/calculate_pension?monthly_investment_amount=1239&no_of_years=5&annuity_rates=3&annuity_purchased=5&yearly_interest_rates=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "status_code": 500,
  "detail": "Internal Server Error",
  "headers": None
}


def test_payback_period_years():
    response = client.get(
        "http://127.0.0.1:8000/payback_period?years_before_recovery=2&unrecovered_cost=2456&cash_flow=21"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Payback period",
  "Years before full recovery": 2,
  "Unrecovered cost at start of the year": 2456,
  "Cash flow during the year": 21,
  "Payback period": "118.95238095238095"
}


def test_compound_interest_amount():
    response = client.get(
        "http://127.0.0.1:8000/compound_interest?principal_amount=6464&interest_rate=6&years=4&compounding_period=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() =={
  "Tag": "Compound Interest Amount",
  "Principle amount": 6464,
  "Intrest Rate": 6,
  "Time in Years": 4,
  "Compounding Period": 4,
  "Amount after interest": "15050172805.786133"
}

def test_certificate_of_deposit():
    response = client.get(
        "http://127.0.0.1:8000/certificate_of_deposit?principal_amount=4555&interest_rate=5&yrs=3&compounding_per_yr=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Certificate of Deposit (CD)",
  "Principal amount": 4555,
  "Interest Rate": 5,
  "Time in Years": 3,
  "Number of Compounding per Year": 5,
  "Certificate of Deposit (CD)": "5288.213591710344"
}

def test_inflated():
    response = client.get(
        "http://127.0.0.1:8000/inflation?present_amount=332&inflation_rate=4&years=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Inflated Amount",
  "Present Amount": 332,
  "Inflation Rate": 4,
  "Time in Years": 3,
  "Future Amount": "373.454848"
}

def test_effective_annual_rate():
    response = client.get(
        "http://127.0.0.1:8000/effective_annual_rate?annual_interest_rate=5&compounding_period=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Effective Annual Rate",
  "Annual Intrest Rate": 5,
  "Compounding Period": 4,
  "Effective Annual Rate (in percentage)": "2462.890625%"
}

def test_return_on_investment():
    response = client.get(
        "http://127.0.0.1:8000/roi?current_value_of_investment=677&cost_of_investment=34"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Return on Investment",
  "Current Value of Investment": 677,
  "Cost of Investment": 34,
  "Return on Investment": "1891.1764705882351%"
}

def test_jensens_alpha():
    response = client.get(
        "http://127.0.0.1:8000/jensens_alpha?return_from_investment=4566&return_of_appropriate_market_index=32&risk_free_rate=3&beta=45"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Jensen's Alpha",
  "Total return from investment": 4566,
  "Return of appropriate market index": 32,
  "Risk free rate": 3,
  "Beta of the portfolio investment w.r.t chosen market index": 45,
  "Alpha of the return ": "3258.0%"
}

def test_wacc():
    response = client.get(
        "http://127.0.0.1:8000/wacc?firm_equity=4553&firm_debt=3&cost_of_equity=55&cost_of_debt=33&corporate_tax_rate=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "status_code": 500,
  "detail": "Internal Server Error",
  "headers": None
}

def test_load_emi():
    response = client.get(
        "http://127.0.0.1:8000/loan_emi?principle_amount=5345&annual_rate=3&months=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Loan Emi",
  "Principal amount borrowed": 5345,
  "Annual Rate of interest": 3,
  "Total number of monthly payments": 3,
  "EMI": "1790.582",
  "Total Amount Payble": "5371.747",
  "Interest amount": "26.747"
}

def test_asset_portfolio():
    response = client.get(
        "http://127.0.0.1:8000/asset_portfolio?price_A=234&price_B=555&return_A=3232&return_B=4322&standard_dev_A=21&standard_dev_B=21&correlation=12"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Portfolio Variance",
  "Expected Returns": "399873.0038022814%",
  "Portfolio Variance": "2465.026081047868"
}
def test_put_call_parity():
    response = client.get(
        "http://127.0.0.1:8000/put_call_parity?call_price=344&put_price=433&strike_price=221"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Pull Call Parity",
  "Future Price": "132.0",
  "Call Price": "344.0",
  "Put Price": "433.0",
  "Strike Price": "221.0"
}

def test_dividend_payout_ratio():
    response = client.get(
        "http://127.0.0.1:8000/dividend_payout_ratio?dividend_per_share=3535&earnings_per_share=533"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Dividend payout ratio",
  "Dividend per share": 3535,
  "Share price": 533,
  "Dividend yield ratio": "6.0%"
}

def test_bep():
    response = client.get(
        "http://127.0.0.1:8000/bep?fixed_cost=434&selling_price=567&variable_cost=65"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Break Even Point (BEP)",
  "Fixed costs": 434,
  "Selling price per unit": 567,
  "Variable cost per unit": 65,
  "Break Even Point in units": "0.0",
  "Break Even Point in Rupees": "490.0"
}

def test_fcff():
    response = client.get(
        "http://127.0.0.1:8000/fcff?sales=444&operating_cost=334&depreciation=44&interest=4&tax_rate=4&fcInv=2&wcInv=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Free Cash Flow to Firm (FCFF)",
  "Earnings before interest, taxes, depreciation and amortization": "110.0",
  "Earnings before interest and taxes : ": "66.0",
  "Net Income": "59.52",
  "Free Cash Flow to Firm": "103.36"
}

def test_dividend_yield_ratio():
    response = client.get(
        "http://127.0.0.1:8000/dividend_yield_ratio?dividend_per_share=456&share_price=443"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Dividend yield ratio",
  "Dividend per share": 456,
  "Share price": 443,
  "Dividend yield ratio": "1.0%"
}


def test_debt_to_income_ratio():
    response = client.get(
        "http://127.0.0.1:8000/debt_to_income_ratio?annual_income=455&total_debt_per_month=6"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Debt to income ratio",
  "Annual income": 455,
  "Total debt per month": 6,
  "Debt to income ratio per month": "15.0%"
}

def test_fixed_charges_coverage_ratio():
    response = client.get(
        "http://127.0.0.1:8000/fixed_charges_coverage_ratio?earnings_before_interest_taxes=6446&fixed_charge_before_tax=444&interest=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "fixed charges coverage ratio",
  "Earnings before interest taxes": 6446,
  "Fixed charge before tax": 444,
  "Interest": 4,
  "Fixed charge coverage ratio": "15.0%"
}

def test_inventory_shrinkage_rate():
    response = client.get(
        "http://127.0.0.1:8000/inventory_shrinkage_rate?recorded_inventory=544&actual_inventory=434"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Inventory shrinkage rate",
  "Recorded Inventory": 544,
  "Actual Inventory": 434,
  "Inventory Shrinkage Rate": 0.20220588235294118,
  "Inventory Shrinkage Rate (%)": 20.22058823529412
}

def test_markup_percentage():
    response = client.get(
        "http://127.0.0.1:8000/markup_percentage?price=455&cost=33"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Markup Percentage",
  "Price": 455,
  "Cost": 33,
  "Markup Percentage": 1278.7878787878788
}

def test_purchasing_power():
    response = client.get(
        "http://127.0.0.1:8000/purchasing_power?initial_amount=554&annual_inflation_rate=3&time=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Purchasing Power",
  "Initial Amount": 554,
  "Annual Inflation Rate": 3,
  "Time in years": 3,
  "Purchasing Power": "506.9884792816504"
}


def test_monthly_emi():
    response = client.get(
        "http://127.0.0.1:8000/monthly_emi?loan_amt=466&interest_rate=6&number_of_installments=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Monthly EMI",
  "Loan Amount": 466,
  "Interest Rate": 6,
  "Number of Installments": 5,
  "Total EMI": "2796.166369153874"
}

def test_doubling_time():
    response = client.get(
        "http://127.0.0.1:8000/doubling_time?r=56"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Doubling Time",
  "Rate of Interest": 56,
  "Time in years to double the money": "1.5587346108623077"
}

def test_capital_Asset_Pricing_Model():
    response = client.get(
        "http://127.0.0.1:8000/capital_Asset_Pricing_Model?risk_free_interest_rate=4&beta_of_security=2&expected_market_return=44"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Capital Asset Pricing Model",
  "Risk free interest rate": 4,
  "Beta of security": 2,
  "Expected market return": 44,
  "Capital asset expected return": "84.0"
}

def test_cost_of_equity():
    response = client.get(
        "http://127.0.0.1:8000/cost_of_equity?risk_free_rate_of_return=455&Beta=4&market_rate_of_return=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Cost of Equity",
  "Risk free rate of return": 455,
  "Beta": 4,
  "Market rate of return ": 3,
  "Cost of equity": "-1353.0%"
}

def test_cogs():
    response = client.get(
        "http://127.0.0.1:8000/cogs?beginning_inventory=4566&purchases=5&ending_inventory=8755"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Cost of Goods Sold",
  "Beginning Inventory": 4566,
  "Purchases during the period": 5,
  "Ending Inventory": 8755,
  "Cost of Goods Sold(In Rupees)": "-4184.0"
}

def test_ruleof72():
    response = client.get(
        "http://127.0.0.1:8000/ruleof72?rate_of_roi=56"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Rule of 72",
  "Rate of ROI": 56,
  "Time period in which investment get double(in years)": "1.2857142857142858"
}

def test_acid_test_ratio():
    response = client.get(
        "http://127.0.0.1:8000/acid_test_ratio?cash=555&marketable_securities=43&accounts_receivable=32&current_liabilities=34"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Acid Test Ratio",
  "Cash and Cash Equivalents": 555,
  "Marketable Securities": 43,
  "Accounts Receivable": 32,
  "Current Liabilities": 34,
  "Acid Test Ratio (Quick Ratio)": "18.53"
}

def test_cogr():
    response = client.get(
        "http://127.0.0.1:8000/cogr?beginning_value=4445&ending_value=6785&years=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Compound Annual Growth Rate",
  "Beginning Value": 4445,
  "Ending Value": 6785,
  "Compound Annual Growth Rate": "-10.0%"
}

def test_current_liability_coverage_ratio():
    response = client.get(
        "http://127.0.0.1:8000/current_liability_coverage_ratio?net_cash_from_operating_activities=4556&total_current_liabilities=55&number_of_liabilities=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "current liability coverage ratio",
  "net cash from operating activities": 4556,
  "total current liabilities": 55,
  "number of liabilities": 3,
  "current liability coverage ratio": "248.50909090909093"
}

def test_levered_beta():
    response = client.get(
        "http://127.0.0.1:8000/levered_beta?unlevered_beta=5587&tax_rate=4&debt=56&equity=33"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() =={
  "Tag": "Levered Beta",
  "Unlevered Beta": 5587,
  "Tax rate": 4,
  "debt": 56,
  "Equity": 33,
  "Levered Beta": "-11174.0%"
}

def test_monthly_payment():
    response = client.get(
        "http://127.0.0.1:8000/monthly_payment?principal=5555&interest_rate=4&number_of_periods=4&payments_per_period=6"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "status_code": 500,
  "detail": "Internal Server Error",
  "headers": None
}

def test_current_ratio():
    response = client.get(
        "http://127.0.0.1:8000/current_ratio?total_current_assets=455&total_liabilities=54"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Current Ratio",
  "Total Current Assets": 455,
  "Total Liabilities": 54,
  "Current Ratio": "8.426"
}

def test_inventory_turnover_ratio():
    response = client.get(
        "http://127.0.0.1:8000/inventory_turnover_ratio?cost_of_goods_sold=4455&beginning_inventory=2233&ending_inventory=23345"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Inventory Turnover Ratio",
  "Cost of Goods Sold": 4455,
  "Inventory Turnover Ratio": "0.35"
}

def test_herfindahl_Indexn_rate():
    response = client.get(
        "http://127.0.0.1:8000/herfindahl_Index?Firms_market_shares=455"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Herfindahl Index",
  "Firms market shares": "455",
  "Herfindahl Index": "3025"
}


def test_discount_opex():
    response = client.get(
        "http://127.0.0.1:8000/discount_opex?annual_opex=33&wacc=3&project_lifetime=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Discount OPEX",
  "Annual OPEX": 33,
  "WACC": 3,
  "project lifetime": 2,
  "Discount opex": "11.0%"
}


def test_project_efficiency():
    response = client.get(
        "http://127.0.0.1:8000/project_efficiency?annual_production=335&collector_surface=33&dni=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Project efficiency",
  "Annual production": 335,
  "collector surface": 33,
  "dni": 4,
  "Discount opex": "2.0%"
}

def test_real_gdp():
    response = client.get(
        "http://127.0.0.1:8000/real_gdp?nominal_gdp=456&gdp_deflator=44"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Real GDP",
  "Nominal GDP": 456,
  "GDP Deflator": 44,
  "Real GDP": 1036.3636363636363
}


def test_excess_reserves():
    response = client.get(
        "http://127.0.0.1:8000/excess_reserves?deposits=456&reserve_requirement=44"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Excess Reserves",
  "Deposits": 456,
  "Reserve Requirement": 44,
  "Excess Reserves": -19608
}

def test_discounted_cash_flow():
    response = client.get(
        "http://127.0.0.1:8000/discounted_cash_flow?real_feed_in_tariff=43&annual_production=533&wacc=4&project_lifetime=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Discounted cash flow",
  "Real feed in teriff": 43,
  "annual production": 533,
  "wacc": 4,
  "project lifetime": 3,
  "discounted cash flow": "5729.0%"
}

def test_gdp_growth_rate():
    response = client.get(
        "http://127.0.0.1:8000/gdp_growth_rate?current_year_gdp=34&last_year_gdp=33"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "GDP Growth Rate",
  "Current Year GDP": 34,
  "Last Year GDP": 33,
  "GDP Growth Rate": 3.0303030303030303
}

def test_credit_card_equation():
    response = client.get(
        "http://127.0.0.1:8000/credit_card_equation?balance=2334&monthly_payment=33&daily_interest_rate=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Credit card equation",
  "Balance": 2334,
  "Monthly Payment": 33,
  "daily interest rate": 3,
  "credit card equation": "nan%"
}

def test_future_value_of_ordinary_due():
    response = client.get(
        "http://127.0.0.1:8000/future_value_of_ordinary_due?periodic_payment=455&number_of_periods=23&effective_interest_rate=23"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Future value of the ordinary annuity",
  "Periodic payment": 455,
  "Number of periods": "1.0993655407008683e+33",
  "Effective interest rate": 23
}

def test_future_value_of_annuity_due():
    response = client.get(
        "http://127.0.0.1:8000/future_value_of_annuity_due?periodic_payment=3455&number_of_periods=3&effective_interest_rate=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Future value of the ordinary annuity",
  "Periodic payment": 3455,
  "Number of periods": "134745.0",
  "Effective interest rate": 2
}

def test_present_value_of_annuity_due():
    response = client.get(
        "http://127.0.0.1:8000/present_value_of_annuity_due?periodic_payment=4566&number_of_periods=9&rate_per_period=6"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Present value of annuity due",
  "Periodic payment": 4566,
  "Number of periods": 9,
  "Rate Per Period": 6,
  "PV of Annuity Due": "5326.999867991974"
}

def test_compound_annual_growth_rate():
    response = client.get(
        "http://127.0.0.1:8000/compound_annual_growth_rate?ending_value=345&beginning_value=223&number_of_periods=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "compound annual growth rate 1",
  "ending_value": 345,
  "beginning value": 223,
  "Number of periods": 3,
  "compound annual growth rate": "0.0%"
}

def test_loan_to_value():
    response = client.get(
        "http://127.0.0.1:8000/loan_to_value?mortgage_value=444&appraised_value=334"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Loan to Value (LTV) ratio",
  "Mortgage Value": 444,
  "Appraised Property Value": 334,
  "Loan to Value ratio": "132.93413173652695%"
}

def test_retention_ratio():
    response = client.get(
        "http://127.0.0.1:8000/retention_ratio?net_income=445&dividends=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Retention Ratio",
  "Net Income": 445,
  "Dividends": 2,
  "Retention Ratio": 0.9955056179775281
}

def test_tax_equivalent_yield():
    response = client.get(
        "http://127.0.0.1:8000/tax_equivalent_yield?tax_free_yield=55663&tax_rate=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Tax Equivalent Yield",
  "Tax Free Yield": 55663,
  "Tax Rate": 3,
  "Tax Equivalent Yield": -27831.5
}

def test_perpetuity_payment():
    response = client.get(
        "http://127.0.0.1:8000/perpetuity_payment?present_value=34&rate=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Perpetuity Payment",
  "Present Value": 34,
  "Perpetuity Payment": "0.68"
}

def test_year_to_year():
    response = client.get(
        "http://127.0.0.1:8000/year_to_year?later_period_value=455&earlier_period_value=332"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Year to Year Growth",
  "Year to Year growth": "37.04819277108434%"
}

def test_future_value_of_annuity():
    response = client.get(
        "http://127.0.0.1:8000/future_value_of_annuity?payments_per_period=345&interest_rate=44&number_of_periods=4 "
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Future value of annuity",
  "Payments per periods": 345,
  "interest rate": 44,
  "number of periods": 4,
  "future value of annuity": "32152620.0%"
}

def test_yield_to_maturity():
    response = client.get(
        "http://127.0.0.1:8000/yield_to_maturity?bond_price=345&face_value=2233&coupon_rate=2&years_to_maturity=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Yield To Maturity",
  "Face Value": 2233,
  "Years to maturity": 4,
  "Yield to Maturity": "40.08%"
}

def test_balloon_balance():
    response = client.get(
        "http://127.0.0.1:8000/balloon_balance?present_value=4553&payment=3344&rate_per_payment=32&number_of_payments=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Balloon Balance of a Loan",
  "Present Value (Original Balance)": 4553,
  "Payment": 3344,
  "Rate per Payment": 32,
  "Number of Payments": 3,
  "Future Value (Balloon Balance)": 159865849
}

def test_periodic_lease_payment():
    response = client.get(
        "http://127.0.0.1:8000/periodic_lease_payment?Asset_value=3554&monthly_lease_interest_rate=3&number_of_lease_payments=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Periodic Lease Payment",
  "Asset value": 3554,
  "Monthly lease interest rate": 3,
  "Number of lease payments": 2,
  "Periodic Lease Payment": "11372.8"
}
def test_zero_coupon_bond_value():
    response = client.get(
        "http://127.0.0.1:8000/zero_coupon_bond_value?face_value=4456&rate_of_yield=3&time_of_maturity=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() ==  {
  "Tag": "Zero Coupon Bond Value",
  "Face Value": 4456,
  "Rate of yield": "3.0%",
  "Zero Coupon Bond Value": 3959.1
}


def test_zero_coupon_bond_yield():
    response = client.get(
        "http://127.0.0.1:8000/zero_coupon_bond_yield?face_value=444&present_value=3333&time_of_maturity=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Zero Coupon Bond Effective Yield",
  "Face Value": 444,
  "Present Value": 3333,
  "Time to maturity": 4,
  "Zero Coupon Bond Effective Yield": "-39.6%"
}


def test_profitability_index():
    response = client.get(
        "http://127.0.0.1:8000/profitability_index?initial_investment=3445&pv_of_future_cash_flows=33"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Profitability Index",
  "Initial Investment": 3445,
  "PV of Future Cash Flows": 33,
  "Profitability Index": 0.009579100145137881
}


def test_receivables_turnover_ratio():
    response = client.get(
        "http://127.0.0.1:8000/receivables_turnover_ratio?sales_revenue=4656&avg_accounts_receivable=33"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Receivables Turnover Ratio",
  "Sales Revenue": 4656,
  "Avg Accounts Receivables": 33,
  "Receivables Turnover Ratio": 141.0909090909091
}


def test_remaining_balance():
    response = client.get(
        "http://127.0.0.1:8000/remaining_balance?regular_payment=456&interest_rate_per_period=3&number_of_payments=23&number_of_payments_done=21"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Remaining balance",
  "regular_payment": 456,
  "interest rate per period": 3,
  "number of payments": 23,
  "number of payments done": 21,
  "remaining balance": 0
}


def test_net_present_value():
    response = client.get(
        "http://127.0.0.1:8000/net_present_value?cash_flows=5445&discount_rate=44&initial_investment=555"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Net present value",
  "cash flows": "5445",
  "discount rate": 44,
  "initial investment": 555,
  "Net present value": 3226.25
}

def test_leverage_ratio_income():
    response = client.get(
        "http://127.0.0.1:8000/leverage_ratio_income?debt_payments=456&income=32"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Leverage Ratio By Income",
  "Debt ": 456,
  "Income": 32,
  "Leverage Ratio": "14.25"
}


def test_leverage_ratio_equity():
    response = client.get(
        "http://127.0.0.1:8000/leverage_ratio_equity?debt_payments=334&equity=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Leverage Ratio By Equity",
  "Debt ": 334,
  "Equity": 3,
  "Leverage Ratio": "111.33333333333333"
}


def test_time_period_required_for_growth():
    response = client.get(
        "http://127.0.0.1:8000/time_period_required_for_growth?interest_rate=12&growth_factor=33"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Time period required for exponential growth",
  "interest rate": 12,
  "growth factor": 33
}


def test_preferred_stock_value():
    response = client.get(
        "http://127.0.0.1:8000/preferred-stock-value?dividend=64&discount_rate=24"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Preferred stock value",
  "Dividend": 64,
  "Discount Rate": 24,
  "Preferred Stock Value": 2.6666666666666665
}


def test_asset_turnover_ratio():
    response = client.get(
        "http://127.0.0.1:8000/asset_turnover_ratio?net_sales=4556&total_asset_beginning=343&total_asset_ending=234"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Asset Turnover Ratio",
  "Net Sales": 4556,
  "Total beginning asset": 343,
  "Total ending asset": 234,
  "Total average asset": 288.5,
  "Asset Turnover Ratio": "15.792027729636049"
}


def test_bid_ask_spread():
    response = client.get(
        "http://127.0.0.1:8000/bid-ask-spread?ask_price=445&bid_price=1234"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Bid Ask Spread",
  "Ask Price": 445,
  "Bid Price": 1234,
  "Bid Ask Spread": -789
}


def test_calculate_period_FV_PV_rate():
    response = client.get(
        "http://127.0.0.1:8000/calculate-period-FV-PV-rate?present_val=4255&future_val=6345&rate=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Period in years ",
  "Present Value": 4255,
  "Future Value": 6345,
  "Periods": 10.187788722235
}


def test_Balloon_loan_payment():
    response = client.get(
        "http://127.0.0.1:8000/balloon-loan-payment?principal=345&interest_rate=2&term_years=1&balloon_payment_year=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Balloon Loan Payment",
  "Principal": 345,
  "Interest Rate": 2,
  "Term Years": 1,
  "Balloon Payment Year": 3,
  "Balloon Loan Payment": -711.0313639642766
}


def test_monthly_lease_payment():
    response = client.get(
        "http://127.0.0.1:8000/monthly_lease_payment?Asset_value=424&monthly_lease_interest_rate=4&number_of_lease_payments=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Monthly Lease Payment",
  "Asset value": 424,
  "Monthly lease interest rate": 4,
  "Number of lease payments": 4,
  "Monthly Lease Payment": "424.6794871794872"
}


def test_401k():
    response = client.get(
        "http://127.0.0.1:8000/401k?income=4563&contribution_percentage=23&current_age=23&age_at_retirement=36&rate_of_return=3&salary_increase_rate=2&withdraw_tax_rate=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Estimated 401(k)",
  "income": 4563,
  "contribution_percentage": 23,
  "current_age": 23,
  "age_at_retirement": 36,
  "rate_of_return": 3,
  "withdraw_tax_rate": 3,
  "estimated_401k": 18909.175,
  "annual_withdraw_amount": 567.275
}


def test_roth_ira():
    response = client.get(
        "http://127.0.0.1:8000/roth-ira?principal=4355&interest_rate=3&years=3&tax_rate=2&annual_contribution=32"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Roth-IRA",
  "Principal": 4355,
  "Interest Rate": 3,
  "Years": 3,
  "Tax Rates": 2,
  "Annual Contributions": 32,
  "Roth Ira Balance": 4861,
  "Taxable saving Balance": 4853
}


def test_mortgage_amortization():
    response = client.get(
        "http://127.0.0.1:8000/mortgage-amortization?mortgage_amount=4556&mortgage_deposit=3232&annual_interest_rate=4&loan_term=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "TAG": "Mortgage monthly payments",
  "mortgage_amount": 4556,
  "mortgage_deposit": 3232,
  "annual_interest_rate": 4,
  "loan_term": 5,
  "monthly_payment": -2671.077,
  "annual_payment": -32052.923
}


def test_enterprise_value():
    response = client.get(
        "http://127.0.0.1:8000/enterprise-value?share_price=345&fully_diluted_shares_outstanding=33&total_debt=43&preferred_stock=3&non_controlling_interest=2&cash_and_cash_equivalents=43"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Enterprise Value",
  "Equity Value": 11385,
  "Total Debt": 43,
  "Preferred Stock": 3,
  "Non-Controlling Interest": 2,
  "Cash & Cash Equivalents": 43,
  "Enterprise Value": 11390
}


def test_refinance_calculator():
    response = client.get(
        "http://127.0.0.1:8000/refinance?current_loan_amount=4453&current_interest_rate=3&current_loan_term_years=3&time_remaining_years=2&new_interest_rate=2&new_loan_term_years=6&cash_out_amount=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Refinance",
  "Current loan amount": 4453,
  "Balance left on loan": 3012.91,
  "New loan amount": 3010.91,
  "Current monthly payment": 129.5,
  "New monthly payment": 44.41,
  "Monthly savings": 85.09,
  "Current interest paid left": 95.05,
  "New total interest paid": 186.77,
  "Total interest saving": -91.72,
  "Current total cost left": 3107.97,
  "New total cost loan": 3197.68,
  "Total cost saving": -89.72
}


def test_salary_calculate():
    response = client.get(
        "http://127.0.0.1:8000/salary-calculate?salary_amount=3554&payment_frequency=3&hours_worked_per_day=2&days_worked_per_week=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Calculate Salary",
  "Salary Amount": 3554,
  "Payment frequency": "3",
  "Salary": {
    "error": "Invalid payment frequency."
  }
}


def test_commission_calc():
    response = client.get(
        "http://127.0.0.1:8000/commission_calc?sales_price=3555&commission_rate=3&commission=224"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "status_code": 500,
  "detail": "Internal Server Error",
  "headers": None
}


def test_college_cost():
    response = client.get(
        "http://127.0.0.1:8000/college_cost?book_cost=4566&college_tuition=34&Devices=33&travel_expenses=44&hostel_charges=55&mess_fee=33&miscellaneous=45"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "College Cost",
  "Books cost of one year": 4566,
  "College tuition fee per year": 34,
  "Electronic devices cost": 33,
  "Monthly Travel expenses": 44,
  "Monthly Hostel charges": 55,
  "Monthly mess fee": 33,
  "monthly miscellaneous expenses": 45,
  "Total cost of one year": 6757
}


def test_diluted_earnings_per_share():
    response = client.get(
        "http://127.0.0.1:8000/diluted-earnings-per-share?net_income=4455&weighted_avg_shares=23&dilutive_securities=22"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Diluted Earnings Per Share (EPS)",
  "Net Income": 4455,
  "Weighted Average Shares Outstanding": 23,
  "Number of Dilutive Securities": 22,
  "Diluted EPS": "99.0"
}


def test_roi_equity_funds():
    response = client.get(
        "http://127.0.0.1:8000/roi_equity_funds?amount_invested=4563&amount_returned=32&tenure=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Calculate return of investments on equity funds",
  "Amount Invested": 4563,
  "Amount Returned": 32,
  "Duration of investment": 3,
  "Return of Investment": "-99.29870699101468%",
  "Annualized Return": "0.23321999781458214%"
}


def test_student_loan():
    response = client.get(
        "http://127.0.0.1:8000/student_loan?principal=5663&tenure=33&interest_rate=3"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Student Loan",
  "Total amount to borrow": 5663,
  "total number of years to pay loan": 33,
  "interest rate percentage annual": 3,
  "total monthly cost": "22",
  "Total Amount of loan": "8927"
}


def test_calculate_gst():
    response = client.get(
        "http://127.0.0.1:8000/calculate_gst?price=545&gst_rate=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "status_code": 500,
  "detail": "Internal Server Error",
  "headers": None
}


def test_calculate_retirement_goals():
    response = client.get(
        "http://127.0.0.1:8000/calculate_retirement_goals?retirement_age=34&annual_retirement_expenses=344&inflation_rate=5&annual_retirement_income=45567&current_age=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() ==  {
  "Tag": "Retirement Goals",
  "Retirement age": 34,
  "Annual retirement expenses": 344,
  "inflation rate": 5,
  "Annual Retirement Income": 45567,
  "Current Age": 5,
  "Retirement Goals": "-1.666270978588454e+27"
}


def test_calculate_market_cap():
    response = client.get(
        "http://127.0.0.1:8000/calculate_market_cap?current_market_share_price=5545&total_number_of_shares_outstanding=434"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Market capitalization value",
  "Current market share price": 5545,
  "Total number of shares outstanding": 434,
  "Marketcap value": "2406530"
}


def test_annual_debt_service_coverage_ratio():
    response = client.get(
        "http://127.0.0.1:8000/asdcr?net_operating_cost=322&depreciation=3&non_cash_expenses=33&annual_debt_service=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Annual Debt Service Coverage Ratio",
  "Annual Debt Ratio": 89.5,
  "Net Operating Income": 322,
  "Depreciation": 3,
  "Non Cash Expenses": 33,
  "Annual Debt": 4
}


def test_calculate_vat():
    response = client.get(
        "http://127.0.0.1:8000/calculate_vat?price=4343&vat_rate=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Price (excluding VAT)": 4136.190476190476,
  "Price (including VAT)": 4343,
  "VAT Amount": 206.80952380952385
}


def test_bond_equivalent_yield():
    response = client.get(
        "http://127.0.0.1:8000/bond_equivalent_yield?face_value=5353&purchase_price=5&days_to_maturity=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Bond Equivalent Yield",
  "Face value": 5353,
  "Purchase Price": 5,
  "Days to maturity": 5,
  "Bond Equivalent Yield (BEY)": "7808079.999999999%"
}


def test_calculate_gratuity():
    response = client.get(
        "http://127.0.0.1:8000/calculate_gratuity?last_salary=3535&tenure_years=5&tenure_months=4"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Gratuity",
  "Last salary (basic + dearness allowance)": 3535,
  "Tenure in years (excluding last partial year)": 5,
  "Last partial year in months": 4,
  "Gratuity Amount": "10197"
}


def test_mortrage():
    response = client.get(
        "http://127.0.0.1:8000/mortrages?princial=4344&interest_rate=4&years=4&down_payment=223&property_tax_rate=2&insurance_rate=2"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Monthly Payment": 93.04828417840245,
  "Total Payment": 4466.317640563318,
  "Total Property Tax": 347.52,
  "Total insurance cost": 347.52,
  "Total Cost": 5161.357640563318,
  "Loan to value ratio": 94.86648250460405
}


def test_post_tax_return_percentage():
    response = client.get(
        "http://127.0.0.1:8000/calculate_post_tax_return_percentage?tax_rate_percentage=3537&annual_net_income=2244&initial_cost_of_investment=444"    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Calculate post tax return percentage",
  "Tax Rate Percentage": 3537,
  "Annual net income": 2244,
  "Initial cost of investment": 444,
  "Post tax return percentage": -17370.783783783783
}


def test_loan_to_value_ratio():
    response = client.get(
        "http://127.0.0.1:8000/loan_to_value_ratio?loan_amount=5464&value_of_collateral=6"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
  "Tag": "Loan to Value Ratio",
  "Loan Amount": 5464,
  "Value Of Collateral": 6,
  "Loan to Value Ratio": "91066.66666666666%"
}


def test_modified_internal_rate_of_return():
    response = client.get(
        "http://127.0.0.1:8000/modified_internal_rate_of_return?initial_cash_flow=-300000&ending_cash_flow=500000&number_of_periods=5"
    )
    assert response.status_code == status.HTTP_200_OK

    assert response.json() ==  {
      "Tag": "Modified internal rate",
      "Ending cash flow": 500000,
      "Initial cash flow": -300000,
      "Number of periods": 5,
      "Modified internal rate of return": "12.04%",
      }



