from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
import jwt

# Importing all the tasks
from tasks.simple_interest_rate import simple_interest_rate_task
from tasks.future_sip import future_sip_task
from tasks.calculate_pension import calculate_pension_task
from tasks.payback_period import payback_period_task
from tasks.compound_interest import compound_interest_task
from tasks.certificate_of_deposit import certificate_of_deposit_task
from tasks.inflation import inflation_task
from tasks.roi import return_on_investment_task
from tasks.jensens_alpha import jensens_alpha_task
from tasks.social_securities import ss_task
from tasks.tax_equivalent_yield import tax_equivalent_yield_task
from tasks.time_period_required_for_growth import time_period_required_for_growth_task
from tasks.treynor_ratio import treynor_ratio_task
from tasks.wacc import weighted_average_cost_of_capital_task
from tasks.loan_emi import loan_emi_task
from tasks.asset_portfolio import asset_portfolio_task
from tasks.put_call_parity import put_call_parity_task
from tasks.bep import break_even_point_task
from tasks.fcff import free_cash_flow_to_firm_task
from tasks.price_to_earning_ratio import price_to_earning_ratio_task
from tasks.dividend_yield_ratio import dividend_yield_ratio_task
from tasks.dividend_payout_ratio import dividend_payout_ratio_task
from tasks.debt_to_income_ratio import debt_to_income_ratio_task
from tasks.fixed_charges_coverage_ratio import fixed_charge_coverage_ratio_task
from tasks.inventory_shrinkage_rate import inventory_shrinkage_rate_task
from tasks.markup_percentage import markup_percentage_task
from tasks.sharpe_ratio import sharpe_ratio_task
from tasks.purchasing_power import purchasing_power_task
from tasks.monthly_emi import monthly_emi_task
from tasks.doubling_time import doubling_time_task
from tasks.weighted_average import weighted_average_task
from tasks.capital_Asset_Pricing_Model import Capital_Asset_Pricing_Model_task
from tasks.cost_of_equity import cost_of_equity_task
from tasks.cogs import cost_of_goods_sold_task
from tasks.ruleof72 import rule_of_72_task
from tasks.acid_test_ratio import acid_test_ratio_task
from tasks.inflation_adjusted_return import inflation_adjusted_return_task
from tasks.cogr import compound_annual_growth_rate_task
from tasks.current_liability_coverage_ratio import current_liability_coverage_ratio_task
from tasks.levered_beta import levered_beta_task
from tasks.monthly_payment import monthly_payment_task
from tasks.convexity_duration import duration_task
from tasks.current_ratio import current_ratio_task
from tasks.credit_card_equation import credit_card_equation_task
from tasks.credit_card_payoff import credit_card_payoff_task
from tasks.discount_opex import discount_opex_task
from tasks.discounted_cash_flow import discounted_cash_flow_task
from tasks.effective_annual_rate import effective_annual_rate_task
from tasks.excess_reserves import excess_reserves_task
from tasks.future_value_of_annuity_due import future_value_of_annuity_due_task
from tasks.future_value_of_ordinary_due import future_value_of_ordinary_due_task
from tasks.gdp_growth_rate import gdp_growth_rate_task
from tasks.herfindahl_Index import herfindahl_Index_task
from tasks.inflation_rate import inflation_rate_task
from tasks.inventory_turnover_ratio import inventory_turnover_ratio_task
from tasks.loan_to_value import loan_to_value_task
from tasks.present_value_of_annuity_due import present_value_of_annuity_due_task
from tasks.project_efficiency import project_efficiency_task
from tasks.real_gdp import real_gdp_task
from tasks.weighted_average_of_values import weighted_average_of_values_task
from tasks.year_to_year import year_over_year_task
from tasks.yield_to_maturity import yield_to_maturity_task
from tasks.zero_coupoun_bond_value import zero_coupon_bond_value_task
from tasks.zero_coupoun_bond_yield import zero_coupon_bond_yield_task
from tasks.balloon_balance import balloon_balance_task
from tasks.discounted_payback_period import discounted_payback_period_task
from tasks.future_value_of_annuity import future_value_of_annuity_task
from tasks.leverage_ratio_equity import leverage_equity_task
from tasks.leverage_ratio_income import leverage_income_task
from tasks.net_present_value import net_present_value_task
from tasks.periodic_lease_payment import periodic_lease_payment_task
from tasks.perpetuity_payment import perpetuity_payment_task
from tasks.profitability_index import profitability_index_task
from tasks.profitability_index2 import profitability_index2_task
from tasks.receivables_turnover_ratio import receivables_turnover_ratio_task
from tasks.remaining_balance import remaining_balance_task
from tasks.retention_ratio import retention_ratio_task
from tasks.roi_equity_funds import calculate_roi_equity_funds_task
from tasks.student_loan import student_loan_task
from tasks.commission_calc import commission_calc_task
from tasks.lumpsum import calculate_lumpsum_task
from tasks.personal_loan import personal_loan_task
from tasks.refinance import refinance_task
from tasks.asdcr import asdcr_task
from tasks.calculate_gst import calculate_gst_task
from tasks.calculate_market_cap import calculate_market_cap_task
from tasks.calculate_retirement_goals import calculate_retirement_goals_task
from tasks.college_cost import college_cost_task
from tasks.diluted_earnings_per_share import calculate_diluted_eps_task
from tasks.salary_calculate import salary_calculate_task
from tasks.enterprise_value import calculate_enterprise_value_task
from tasks.fha_loan import fha_loan_task
from tasks.mortgage_amortization import mortgage_amortization_task
from tasks.roth_ira import roth_ira_task
from tasks.k401 import estimate_401k_task
from tasks.monthly_lease_payment import monthly_lease_payment_task
from tasks.calculate_period_FV_PV_rate import CalculatePeriods_task
from tasks.bid_ask_spread import bid_ask_spread_task
from tasks.asset_turnover_ratio import asset_turnover_ratio_task
from tasks.preferred_stock_value import preferred_stock_value_task
from tasks.accounts_payable_turnover_ratio import accounts_payable_turnover_ratio_task
from tasks.accrint import accrued_interest_task
from tasks.balloon_loan_payment import balloon_loan_payment_task
from tasks.calculate_bvps import calculate_bvps_task
from tasks.calculate_expected_return_of_portfolio import calculate_expected_return_of_portfolio_task
from tasks.calculate_financial_leverage import calculate_financial_leverage_task
from tasks.calculate_gratuity import calculate_gratuity_task
from tasks.calculate_macaulay_duration import calculate_macaulay_duration_task
from tasks.calculate_net_profit_margin import calculate_net_profit_margin_task
from tasks.calculate_post_tax_return_percentage import calculate_post_tax_return_percentage_task
from tasks.calculate_salary import calculate_salary_task
from tasks.capital_gains_yield import capital_gains_yield_task
from tasks.capitalization_rate import capitalization_rate_task
from tasks.free_cash_flow_to_equity import free_cash_flow_to_equity_task
from tasks.loan_affordability import calculate_loan_affordability_task
from tasks.bond_equivalent_yield import bond_equivalent_yield_task
from tasks.calculate_vat import calculate_vat_task
from tasks.loan_to_value_ratio import loan_to_value_ratio_task
from tasks.mortrages import mortrage_task
from tasks.net_worth import net_worth_calculation_task
from tasks.personal_savings import personal_savings_task
from tasks.portfolio_return_monte_carlo import portfolio_return_monte_carlo_task
from tasks.calculate_capm import calculate_capm
from tasks.debt_service_coverage_ratio import debt_service_coverage_ratio_task
from tasks.profit_percentage import profit_percentage_task
from tasks.loss_percentage import loss_percentage_task
from tasks.defensive_interval_ratio import defensive_interval_ratio_task
from tasks.RateofReturn import calculate_rate_of_return
from tasks.cash_conversion_cycle import cash_conversion_cycle_task
from tasks.financialAssestRatio import financial_assest_ratio
from tasks.PolicyPremium import calculate_policy_premium
from validators.request_validators import SimpleInterestRateRequest, calculatePension, compoundInterest, futureSip, paybackPeriod, capmRequest, DebtServiceCoverageRatio, futureValueOfAnnuity, futureValueOfAnnuityDue, ProfitPercentage, LossPercentage, DefensiveIntervalRatio, CashConversionCycle, RateofReturn, financialAssestRatio, PriceElasticity, PolicyPremium, AveragePaymentPeriod, ModifiedInternalRateOfReturn, SavingGoal, InterestCoverageRatio, MarginOfSafety, TaxBracketCalculator
from tasks.financialAssestRatio import financial_assest_ratio
from tasks.PriceElasticity import calculate_price_elasticity
from tasks.average_payment_period import average_payment_period_task
from tasks.Saving_Goal import saving_goal
from tasks.modified_internal_rate_of_return import calculate_modified_internal_rate_of_return_task
from tasks.interest_coverage_ratio import interest_coverage_ratio_task
from tasks.tax_bracket_calculator import tax_bracket_calculator
from tasks.margin_of_safety import margin_of_safety_task

# Creating the app
app = FastAPI(
    title="FinTech API",
    description="An API that helps you to deal with your financial calculations.",
    version="2",
    contact={
        "name": "Clueless Community",
        "url": "https://www.clueless.tech/",
    },
    license_info={
        "name": " MIT license",
        "url": "https://github.com/Clueless-Community/fintech-api/blob/main/LICENSE.md",
    },
)

# Adding the routes

@app.get("/")
def index():
    return {
        "title": "FinTech API",
        "description": "An API that helps you to deal with your financial calculations.",
        "version": "1",
        "contact": {
            "name": "Clueless Community",
            "url": "https://www.clueless.tech/",
        },
        "license_info": {
            "name": " MIT license",
            "url": "https://github.com/Clueless-Community/fintech-api/blob/main/LICENSE.md",
        },
        "endpoints": {
            "/simple_interest_rate": "Calculate simple interest rates",
            "/future_sip": "Calculate Future Value of SIP",
            "/calculate_pension": "Calculate pension",
            "/payback_period": "Calculate payback period",
            "/compound_interest": "Calculate compound interest amount",
            "/certificate_of_deposit": "Calculate certificate of deposit (CD)",
            "/inflation": "Calculate Inflated amount",
            "/effective_annual_rate": "Calculate Effective Annual Rate",
            "/roi": "Calculate return on investment",
            "/jensens_alpha": "Calculate Jensen's Alpha of a market return",
            "/wacc": "Calculate Weighted Average Cost of Capital (WACC)",
            "/loan_emi": "Calculate Loan EMI",
            "/asset_portfolio": "Calculate Variance of a Two Asset Portfolio",
            "/put_call_parity": "Calculate Future Price in Pull-Call Parity",
            "/bep": "Calculate Break Even Point",
            "/fcff": "Calculate Free Cash Flow to Firm",
            "/price_to_earning_ratio": "Calculate price to earning ratio",
            "/dividend_yield_ratio": "Calculate dividend yield ratio",
            "/dividend_payout_ratio": "Calculate dividend payout ratio",
            "/debt_to_income_ratio": "Calculate debt to income ratio per month",
            "/fixed_charges_coverage_ratio": "Calculate fixed charges coverage ratio",
            "/inventory_shrinkage_rate": "Calculate inventory shrinkage rate",
            "/markup_percentage": "Calculate markup percentage",
            "/sharpe_ratio": "Calculate sharpe ratio",
            "/purchasing_power": "Calculate Purchasing Power",
            "/monthly_emi": "Monthly EMI",
            "/doubling_time": "Doubling Time",
            "/weighted_average": "Weighted Average",
            "/capital_Asset_Pricing_Model": "Calculating Capital Asset Pricing Model",
            "/cost_of_equity": "Calculate cost of equity",
            "/cogs": "Calculate Cost of Goods Sold",
            "/ruleof72": "Calculate Rule of 72",
            "/acid_test_ratio": "Calculate Acid test ratio",
            "/inflation_adjusted_return": "Calculate Inflation Adjusted Return",
            "/cogr": "Calculate Compound Annual Growth Rate",
            "/current_liability_coverage_ratio": "Calculating current liability coverage ratio",
            "/levered_beta": "Levered Beta",
            "/monthly_payment": "Monthly payment",
            "/convexity_duration": "Convexity Adjusted Duration",
            "/current_ratio": "Current Ratio",
            "/inventory_turnover_ratio": "Inventory Turnover Ratio",
            "/inflation_rate": "Inflation Rate",
            "/herfindal_Index": "Calculating herfindal Index",
            "/discount_opex": "Discount OPEX",
            "/project_efficiency": "Project Efficiency",
            "/real_gdp": "Real GDP",
            "/excess_reserves": "Excess Reserves",
            "/discounted_cash_flow": "Discounted cash flow",
            "/gdp_growth_rate": "GDP Growth Rate",
            "/credit_card_equation": "Credit Card Equation",
            "/credit_card_payoff": "Credit Card Payoff using Debt Avalanche method",
            "/future_value_of_ordinary_due": "Calculating future value of ordinary annuity",
            "/future_value_of_annuity_due": "Calculating future value of annuity due",
            "/present_value_of_annuity_due": "Calculating present value of annuity due",
            "/compound_annual_growth_rate": "Calculating compound annual growth rate",
            "/loan_to_value": "Calculating loan to value ratio",
            "/retention_ratio": "Calculating retention ratio",
            "/tax_equivalent_yield": "Calculating tax equivalent yield",
            "/year_to_year": "Calculating Year to Year Growth",
            "/future_value_of_annuity": "Calculating future worth of annuity",
            "/balloon_balance": "Calculating Balloon Balance of a Loan",
            "/periodic_lease_payment": "Calculating Periodic lease payment",
            "/weighted_average_of_values": "Calculating weighted average",
            "/discounted_payback_period": "Calculating discounted payback period",
            "/yield_to_maturity": "Calculating Yield to Maturity",
            "/perpetuity_payment": "Calculating perpetuity payment",
            "/zero_coupoun_bond_value": "Calculating zero coupoun bond value",
            "/zero_coupoun_bond_yield": "Calculating Zero Coupon Bond Effective Yield",
            "/profitability_index": "Calculating profitability index",
            "/profitability_index2": "Calculating profitability index using annual cash flows",
            "/receivables_turnover_ratio": "Calculating receivables turnover ratio",
            "/remaining_balance": "Calculating remaining balance",
            "/net_present_value": "Calculating net present value",
            "/leverage_ratio_income": "Calculate Leverage Ratio",
            "/leverage_ratio_equity": "Calculate Leverage Ratio",
            "/time_period_required_for_growth": "Calculating the time period required for exponential growth",
            "/preferred-stock-value": "Calculating the preferred stock value",
            "/asset_turnover_ratio": "Calculate asset turnover ratio",
            "/bid-ask-spread": "Calculating the Bid Ask Spread",
            "/calculate-period-FV-PV-rate": "Calculating No of Periods(Time in years) with respect to Present value(PV) and Future value(FV)",
            "/balloon-loan-payment": "Calculating the payments on a loan that has a balance remaining after all periodic payments are mad using balloon laon payment formula",
            "/monthly_lease_payment": "Calculating Monthly lease payment",
            "/401k": "Calculating an estimate of the 401(k) balance at retirement",
            "/roth-ira": "This calculator estimates the balances of Roth IRA savings and regular taxable savings.",
            "/mortgage-amortization": "Calculating annual or monthly amortization schedule for a mortgage loan.",
            "/fha-loan": "",
            "/enterprise-value": "Calculating Enterprise Value for a publicly listed company.",
            "/salary-calculate": "Converts salary amounts to their corresponding values based on payment frequency.",
            "/personal_loan": "Calculate personal loan",
            "/lumpsum": "",
            "/refinance": "Calculate refinance",
            "/commission_calc": "compute any one of the following, given inputs for the remaining two: sales price, commission rate, or commission.",
            "/college_cost": "calculate total college fee of one year assuming full tuition fee is being paid.",
            "/diluted-earnings-per-share": "Calculate Diluted Earnings Per Share (EPS).",
            "/asdcr": "Calculate Annual Debt Service Coverage Ratio",
            "/portfolio_return_monte_carlo":"Calculates Portfolio returns based on Monte Carlo Simulation",
            "/profit_percent": "Calculates the profit percentage",
            "/loss_percent": "Calculates the loss percentage",
            "/average_payment_period": "Calculate Average Payment Period a metric that allows a business to see how long it takes on average to pay its vendors.",
            "/modified_internal_rate_of_return": "Calculate modified internal rate of return",
            "/interest_coverage_ratio": "Calculates interest coverage ratio",
            "/margin_of_safety": "Calculates margin of safety",
    
        },
    }

class UnauthorizedException(HTTPException):
    def __init__(self, detail="Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )

# Validate access token (Not for all endpoints)
def validate_access_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        token = credentials.credentials
        payload = jwt.decode(token,"fintech-api", algorithms=["HS256"])
        return payload
    except jwt.exceptions.DecodeError:
        raise UnauthorizedException()


# Endpoint to generate access token
@app.get("/generate-access-token")
def generate_access_token():
    token = jwt.encode({},"fintech-api", algorithm="HS256")
    return {"access_token": token}

# Endpoints to calculate simple interest.

@app.post(
    "/simple_interest_rate",
    tags=["simple_interest_rate"],
    description="Calculate simple interest rates",
)
def simple_interest_rate(request: SimpleInterestRateRequest):
    return simple_interest_rate_task(request.amount_paid, request.principle_amount, request.months)

# Endpoints to calculate Future sip

@app.post(
    "/future_sip",
    tags=["future_sip"],
    description="Calculate Future Value of SIP",
)
def future_sip(
    request: futureSip,
    payload: dict = Depends(validate_access_token)
):
    return future_sip_task(request.interval_investment, request.rate_of_return, request.number_of_payments)

# Endpoints to calculate Future value

@app.post(
    "/calculate_pension",
    tags=["calculate_pension"],
    description="Calculate pension",
)
def calculate_pension(
    request: calculatePension
):
    return calculate_pension_task(request.monthly_investment_amount, request.no_of_years, request.annuity_rates, request.annuity_purchased, request.yearly_interest_rates)


# endpoint for payback period
@app.post(
    "/payback_period",
    tags=["payback_period_years"],
    description="Calculate payback period",
)
def payback_period(
    request: paybackPeriod,
):
    return payback_period_task(request.initial_investment, request.cashflow)


# Endpoints to calculate Compound Interest.
@app.post(
    "/compound_interest",
    tags=["compound_interest_amount"],
    description="Calculate compound interest amount",
)
def compound_interest(
    request: compoundInterest
):
    return compound_interest_task(request.principal_amount, request.interest_rate, request.years ,request.compounding_period)


# Endpoints to calculate certificate of deposit (CD)
@app.get(
    "/certificate_of_deposit",
    tags=["certificate_of_deposit"],
    description="Calculate certificate of deposit (CD)",
)
def certificate_of_deposit(
    principal_amount: float, interest_rate: float, yrs: int, compounding_per_yr: int
):
    return certificate_of_deposit_task(principal_amount, interest_rate, yrs, compounding_per_yr)


# EndPoint to calculate Inflation
@app.get("/inflation", tags=["inflated"], description="Calculate Inflated amount")
def inflation(present_amount: float, inflation_rate: float, years: float):
    return inflation_task(present_amount, inflation_rate, years)


# Endpoint to Calculate Effective Annual Rate
@app.get(
    "/effective_annual_rate",
    tags=["Effective Annual Rate"],
    description="Calculate Effective Annual Rate",
)
def effective_annual_rate(annual_interest_rate: float, compounding_period: int):
    return effective_annual_rate_task(annual_interest_rate, compounding_period)

@app.get(
    "/roi", tags=["return_on_investment"], description="Calculate return on investment"
)
def return_on_investment(current_value_of_investment: float, cost_of_investment: float):
    return return_on_investment_task(current_value_of_investment, cost_of_investment)


# Endpoint to calculate Jensen's Alpha
@app.get(
    "/jensens_alpha",
    tags=["jensens_alpha"],
    description="Calculate Jensen's Alpha of a market return",
)
def jensens_alpha(
    return_from_investment: float,
    return_of_appropriate_market_index: float,
    risk_free_rate: float,
    beta: float,
):
    return jensens_alpha_task( return_from_investment, return_of_appropriate_market_index, risk_free_rate, beta)


# Endpoint to calculate WACC
@app.get(
    "/wacc",
    tags=["wacc"],
    description="Calculate Weighted Average Cost of Capital (WACC)",
)
def weighted_average_cost_of_capital(
    firm_equity, firm_debt, cost_of_equity, cost_of_debt, corporate_tax_rate
):
    return weighted_average_cost_of_capital_task( firm_equity, firm_debt, cost_of_equity, cost_of_debt, corporate_tax_rate)


@app.get(
    "/loan_emi",
    tags=["load_emi"],
    description="Calculate Loan EMI",
)
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    return loan_emi_task(principle_amount, annual_rate, months)


# Endpoint to calculate Variance of a Two Asset Portfolio
@app.get(
    "/asset_portfolio",
    tags=["asset_portfolio"],
    description="Calculate Variance of a Two Asset Portfolio",
)
def asset_portfolio(
    price_A: float,
    price_B: float,
    return_A: float,
    return_B: float,
    standard_dev_A: float,
    standard_dev_B: float,
    correlation: float,
):
    return asset_portfolio_task(
        price_A, price_B, return_A, return_B, standard_dev_A, standard_dev_B, correlation
    )


# Endpoint to Calculate Future Price in Put-Call Parity
@app.get(
    "/put_call_parity",
    tags=["/put_call_parity"],
    description="Calculate Future Price in Pull-Call Parity",
)
def put_call_parity(call_price: float, put_price: float, strike_price: float):
    return put_call_parity_task(call_price, put_price, strike_price)


# Endpoint to calculate break even point
@app.get(
    "/bep",
    tags=["bep"],
    description="Calculate Break Even Point",
)
def break_even_point(fixed_cost: float, selling_price: float, variable_cost: float):
    return break_even_point_task(fixed_cost, selling_price, variable_cost)


# Endpoint to calculate free cash flow to firm
@app.get(
    "/fcff",
    tags=["fcff"],
    description="Calculate Free Cash Flow to Firm",
)
def free_cash_flow_to_firm(
    sales: float,
    operating_cost: float,
    depreciation: float,
    interest: float,
    tax_rate: float,
    fcInv: float,
    wcInv: float,
):
    return free_cash_flow_to_firm_task(
        sales, operating_cost, depreciation, interest, tax_rate, fcInv, wcInv
    )


# Endpoint to calculate Price-to-earning ratio
@app.get(
    "/price_to_earning_ratio",
    tags=["price_to_earning_ratio"],
    description="Calculate price to earning ratio",
)
def price_to_earning_ratio(share_price: float, earnings_per_share: float):
    return price_to_earning_ratio_task(share_price, earnings_per_share)


# Endpoint to calculate Dividend yield ratio


@app.get(
    "/dividend_yield_ratio",
    tags=["dividend_yield_ratio"],
    description="Calculate dividend yield ratio",
)
def dividend_yield_ratio(dividend_per_share: float, share_price: float):
    return dividend_yield_ratio_task(dividend_per_share, share_price)

# Endpoint to calculate Dividend payout ratio
@app.get(
    "/dividend_payout_ratio",
    tags=["dividend_payout_ratio"],
    description="Calculate dividend payout ratio",
)
def dividend_payout_ratio(dividend_per_share: float, earnings_per_share: float):
    return dividend_payout_ratio_task(dividend_per_share, earnings_per_share)


# Endpoint to calculate DTI
@app.get(
    "/debt_to_income_ratio",
    tags=["debt_to_income_ratio"],
    description="Calculate debt to income ratio per month",
)
def debt_to_income_ratio(annual_income: float, total_debt_per_month: float):
    return debt_to_income_ratio_task(annual_income, total_debt_per_month)


# Endpoint to calculate fixed charge coverage ratio:
@app.get(
    "/fixed_charges_coverage_ratio",
    tags=["fixed_charges_coverage_ratio"],
    description="Calculate fixed charges coverage ratio",
)
def fixed_charge_coverage_ratio(
    earnings_before_interest_taxes: float,
    fixed_charge_before_tax: float,
    interest: float,
):
    return fixed_charge_coverage_ratio_task(
        earnings_before_interest_taxes, fixed_charge_before_tax, interest
    )


# Endpoint to calculate Inventory Shrinkage Rate
@app.get(
    "/inventory_shrinkage_rate",
    tags=["inventory_shrinkage_rate"],
    description="Calculate inventory shrinkage rate",
)
def inventory_shrinkage_rate(recorded_inventory: float, actual_inventory: float):
    return inventory_shrinkage_rate_task(recorded_inventory, actual_inventory)


# Endpoint to calculate Markup Percentage
@app.get(
    "/markup_percentage",
    tags=["markup_percentage"],
    description="Calculate markup percentage",
)
def markup_percentage(price: float, cost: float):
    return markup_percentage_task(price, cost)


# Endpoint to calculate Sharpe ratio
@app.get(
    "/sharpe_ratio",
    tags=["sharpe_ratio"],
    description="Calculate sharpe ratio",
)
def sharpe_ratio(
    portfolio_return: float,
    risk_free_rate: float,
    standard_deviation_of_portfolio: float,
):
    return sharpe_ratio_task(portfolio_return, risk_free_rate, standard_deviation_of_portfolio)


# Endpoint to calculate purchase power
@app.get(
    "/purchasing_power",
    tags=["purchasing_power"],
    description="Calculate Purchasing Power",
)
def purchasing_power(initial_amount: float, annual_inflation_rate: float, time: float):
    return purchasing_power_task(initial_amount, annual_inflation_rate, time)


# Endpoint to calculate Monthly EMI
@app.get(
    "/monthly_emi",
    tags=["monthly_emi"],
    description="Monthly EMI",
)
def monthly_emi(loan_amt: float, interest_rate: float, number_of_installments: float):
    return monthly_emi_task(loan_amt, interest_rate, number_of_installments)


# Endpoint to calculate doubling time
@app.get(
    "/doubling_time",
    tags=["doubling_time"],
    description="Doubling Time",
)
def doubling_time(r: float):
    return doubling_time_task(r)


# Endpoint to calculate weighted average
@app.post(
    "/weighted_average",
    tags=["weighted_average"],
    description="Weighted Average",
)
def weighted_average(ratio: list, rates: list):
    return weighted_average_task(ratio, rates)


# Endpoint to calculate Capital Asset Pricing Model
@app.get(
    "/capital_Asset_Pricing_Model",
    tags=["capital_Asset_Pricing_Model"],
    description="Calculating Capital Asset Pricing Model",
)
def Capital_Asset_Pricing_Model(
    risk_free_interest_rate: float,
    beta_of_security: float,
    expected_market_return: float,
):
    return Capital_Asset_Pricing_Model_task(
        risk_free_interest_rate, beta_of_security, expected_market_return
    )

# Endpoint to calculate cost of equity
@app.get(
    "/cost_of_equity",
    tags=["cost_of_equity"],
    description="Calculate cost of equity",
)
def cost_of_equity(
    risk_free_rate_of_return: float, Beta: float, market_rate_of_return: float
):
    return cost_of_equity_task(risk_free_rate_of_return, Beta, market_rate_of_return)


# Endpoint to calculate cost of goods sold
@app.get(
    "/cogs",
    tags=["cogs"],
    description="Calculate Cost of Goods Sold",
)
def cost_of_goods_sold(
    beginning_inventory: float, purchases: float, ending_inventory: float
):
    return cost_of_goods_sold_task(beginning_inventory, purchases, ending_inventory)


# Endpoint to calculate rule of 72
@app.get(
    "/ruleof72",
    tags=["ruleof72"],
    description="Calculate Rule of 72",
)
def rule_of_72(rate_of_roi: float):
    return rule_of_72_task(rate_of_roi)


# Endpoint to calculate acid test ratio
@app.get(
    "/acid_test_ratio",
    tags=["acid_test_ratio"],
    description="Calculate Acid test ratio",
)
def acid_test_ratio(
    cash: float,
    marketable_securities: float,
    accounts_receivable: float,
    current_liabilities: float,
):
    return acid_test_ratio_task(
        cash, marketable_securities, accounts_receivable, current_liabilities
    )


# Endpoint to calculate inflation adjusted return
@app.get(
    "/inflation_adjusted_return",
    tags=["inflation_adjusted_return"],
    description="Calculate Inflation Adjusted Return",
)
def inflation_adjusted_return(
    beginning_price: float,
    ending_price: float,
    dividends: float,
    beginning_cpi_level: float,
    ending_cpi__level: float,
):
    return inflation_adjusted_return_task(
        beginning_price,
        ending_price,
        dividends,
        beginning_cpi_level,
        ending_cpi__level,
    )


# Endpoint to calculate compound annual growth rate
@app.get(
    "/cogr",
    tags=["cogr"],
    description="Calculate Compound Annual Growth Rate",
)
def compound_annual_growth_rate(
    beginning_value: float, ending_value: float, years: int
):
    return compound_annual_growth_rate_task(beginning_value, ending_value, years)


# Endpoint to calculate current liability coverage ratio
@app.get(
    "/current_liability_coverage_ratio",
    tags=["current_liability_coverage_ratio"],
    description="Calculating current liability coverage ratio",
)
def current_liability_coverage_ratio(
    net_cash_from_operating_activities: float,
    total_current_liabilities: float,
    number_of_liabilities: int,
):
    return current_liability_coverage_ratio_task(
        net_cash_from_operating_activities, total_current_liabilities, number_of_liabilities
    )


@app.get(
    "/levered_beta",
    tags=["levered_beta"],
    description="Levered Beta",
)
def levered_beta(unlevered_beta: float, tax_rate: float, debt: float, equity: float):
    return levered_beta_task(unlevered_beta, tax_rate, debt, equity)


@app.get(
    "/monthly_payment",
    tags=["monthly_payment"],
    description="Monthly payment",
)
def monthly_payment(
    principal: float,
    interest_rate: float,
    number_of_periods: float,
    payments_per_period: float,
):
    return monthly_payment_task(principal, interest_rate, number_of_periods, payments_per_period)


@app.get(
    "/convexity_duration",
    tags=["convexity_duration"],
    description="Convexity Adjusted Duration",
)
def duration(rate, coupon_rate, frequency, face_value, settlement_date, maturity_date):
    return duration_task(rate, coupon_rate, frequency, face_value, settlement_date, maturity_date)


# Endpoint to calculate current ratio
@app.get(
    "/current_ratio",
    tags=["current_ratio"],
    description="Current Ratio",
)
def current_ratio(total_current_assets: float, total_liabilities: float):
    return current_ratio_task(total_current_assets, total_liabilities)


# Endpoint to calculate inventory turnover ratio
@app.get(
    "/inventory_turnover_ratio",
    tags=["inventory_turnover_ratio"],
    description="Inventory Turnover Ratio",
)
def inventory_turnover_ratio(
    cost_of_goods_sold: float, beginning_inventory: float, ending_inventory: float
):
    return inventory_turnover_ratio_task(
        cost_of_goods_sold, beginning_inventory, ending_inventory
    )


# Endpoint to calculate inflation rate
@app.get(
    "/inflation_rate",
    tags=["inflation_rate"],
    description="Inflation Rate",
)
def inflation_rate(bigger_year: int, smaller_year: int, base_year: int):
    return inflation_rate_task(bigger_year, smaller_year, base_year)


# Endpoint to calculate Herfindahl index
@app.get(
    "/herfindahl_Index",
    tags=["herfindahl_Index"],
    description="Calculating herfindahl Index",
)
def herfindahl_Index(Firms_market_shares: str):
    return herfindahl_Index_task(Firms_market_shares)


@app.get(
    "/discount_opex",
    tags=["discount_opex"],
    description="Discount OPEX",
)
def discount_opex(annual_opex: float, wacc: float, project_lifetime: float):
    return discount_opex_task(annual_opex, wacc, project_lifetime)


@app.get(
    "/project_efficiency",
    tags=["project_efficiency"],
    description="Project Efficiency",
)
def project_efficiency(annual_production: float, collector_surface: float, dni: float):
    return project_efficiency_task(annual_production, collector_surface, dni)


@app.get(
    "/real_gdp",
    tags=["real_gdp"],
    description="Real GDP",
)
def real_gdp(nominal_gdp: float, gdp_deflator: float):
    return real_gdp_task(nominal_gdp, gdp_deflator)


@app.get(
    "/excess_reserves",
    tags=["excess_reserves"],
    description="Excess Reserves",
)
def excess_reserves(deposits: float, reserve_requirement: float):
    return excess_reserves_task(deposits, reserve_requirement)


@app.get(
    "/discounted_cash_flow",
    tags=["discounted_cash_flow"],
    description="Discounted cash flow",
)
def discounted_cash_flow(
    real_feed_in_tariff: float,
    annual_production: float,
    wacc: float,
    project_lifetime: float,
):
    return discounted_cash_flow_task(
        real_feed_in_tariff, annual_production, wacc, project_lifetime
    )


@app.get(
    "/gdp_growth_rate",
    tags=["gdp_growth_rate"],
    description="GDP Growth Rate",
)
def gdp_growth_rate(current_year_gdp: float, last_year_gdp: float):
    return gdp_growth_rate_task(current_year_gdp, last_year_gdp)


@app.get(
    "/credit_card_equation",
    tags=["credit_card_equation"],
    description="Credit Card Equation",
)
def credit_card_equation(
    balance: float, monthly_payment: float, daily_interest_rate: float
):
    return credit_card_equation_task(balance, monthly_payment, daily_interest_rate)


@app.post(
    "/credit_card_payoff",
    tags=["credit_card_payoff"],
    description="Credit Card Payoff using Debt Avalanche method",
)
def credit_card_payoff(
    debts: list, interest_rates: list, minimum_payments: list, monthly_payment: int,
    payload: dict = Depends(validate_access_token)
):
    return credit_card_payoff_task(
        debts, interest_rates, minimum_payments, monthly_payment
    )


# Endpoint to calculate future value of the ordinary annuity
@app.get(
    "/future_value_of_ordinary_due",
    tags=["future_value_of_ordinary_due"],
    description="Calculating future value of ordinary annuity",
)
def future_value_of_ordinary_due(
    periodic_payment: float, number_of_periods: int, effective_interest_rate: float
):
    return future_value_of_ordinary_due_task( periodic_payment, number_of_periods, effective_interest_rate)


# Endpoint to calculate future value of the annuity due
@app.post(
    "/future_value_of_annuity_due",
    tags=["future_value_of_annuity_due"],
    description="Calculating future value of annuity due",
)
def future_value_of_annuity_due(
    request: futureValueOfAnnuity
):
    return future_value_of_annuity_due_task(request.periodic_payment, request.interest_rate, request.number_of_payments)


# Endpoint to calculate present value of the annuity due
@app.get(
    "/present_value_of_annuity_due",
    tags=["present_value_of_annuity_due"],
    description="Calculating present value of annuity due",
)
def present_value_of_annuity_due(
    periodic_payment: float, number_of_periods: int, rate_per_period: float
):
    return present_value_of_annuity_due_task( periodic_payment, number_of_periods, rate_per_period)


# Endpoint to calculate loan to value
@app.get(
    "/loan_to_value",
    tags=["loan_to_value"],
    description="Calculating loan to value ratio",
)
def loan_to_value(mortgage_value: float, appraised_value: float):
    return loan_to_value_task(mortgage_value, appraised_value)


# Endpoint to calculate retention ratio
@app.get(
    "/retention_ratio",
    tags=["retention_ratio"],
    description="Calculating retention ratio",
)
def retention_ratio(net_income: float, dividends: float):
    return retention_ratio_task(net_income, dividends)


# Endpoint to calculate tax equivalent yield
@app.get(
    "/tax_equivalent_yield",
    tags=["tax_equivalent_yield"],
    description="Calculating tax equivalent yield",
)
def tax_equivalent_yield(tax_free_yield: float, tax_rate: float):
    return tax_equivalent_yield_task(tax_free_yield, tax_rate)


# endpoint to calculate year over year growth
@app.get(
    "/year_to_year",
    tags=["year_to_year"],
    description="Calculating Year to Year Growth",
)
def year_over_year(later_period_value: float, earlier_period_value: float):
    return year_over_year_task(later_period_value, earlier_period_value)


@app.get(
    "/future_value_of_annuity",
    tags=["future_value_of_annuity"],
    description="Calculating future worth of annuity",
)
def future_value_of_annuity(
    payments_per_period: float, interest_rate: float, number_of_periods: float
):
    return future_value_of_annuity_task(
        payments_per_period, interest_rate, number_of_periods
    )


# endpoint to calculate Balloon Balance of a Loan
@app.get(
    "/balloon_balance",
    tags=["balloon_balance"],
    description="Calculating Balloon Balance of a Loan",
)
def balloon_balance(
    present_value: float,
    payment: float,
    rate_per_payment: float,
    number_of_payments: float,
):
    return balloon_balance_task(
        present_value, payment, rate_per_payment, number_of_payments
    )


# Endpoint to calculate Periodic lease payment
@app.get(
    "/periodic_lease_payment",
    tags=["periodic_lease_payment"],
    description="Calculating Periodic lease payment",
)
def periodic_lease_payment(
    Asset_value: float,
    monthly_lease_interest_rate: float,
    number_of_lease_payments: float,
):
    return periodic_lease_payment_task(
        Asset_value, monthly_lease_interest_rate, number_of_lease_payments
    )


# Endpoint to calculate Weighted average
@app.get(
    "/weighted_average_of_values",
    tags=["weighted_average"],
    description="Calculating weighted average",
)
def weighted_average_of_values(Assigned_weight_values: str, data_point_values: str):
    return weighted_average_of_values_task(Assigned_weight_values, data_point_values)


# endpoint to calculate discounted payback period
@app.get(
    "/discounted_payback_period",
    tags=["discounted_payback_period"],
    description="Calculating discounted payback period",
)
def discounted_payback_period(outflow: float, rate: float, periodic_cash_flow: float):
    return discounted_payback_period_task(outflow, rate, periodic_cash_flow)


# endpoint to calculate yield to maturity
@app.get(
    "/yield_to_maturity",
    tags=["yield_to_maturity"],
    description="Calculating Yield to Maturity",
)
def yield_to_maturity(
    bond_price: float, face_value: float, coupon_rate: float, years_to_maturity: float
):
    return yield_to_maturity_task(
        bond_price, face_value, coupon_rate, years_to_maturity
    )


# endpoint to calculate perpetuity payment
@app.get(
    "/perpetuity_payment",
    tags=["perpetuity_payment"],
    description="Calculating perpetuity payment",
)
def perpetuity_payment(present_value: float, rate: float):
    return perpetuity_payment_task(present_value, rate)


# endpoint to calculate Zero Coupon Bond value
@app.get(
    "/zero_coupon_bond_value",
    tags=["zero_coupon_bond_value"],
    description="Calculating zero coupon bond value",
)
def zero_coupon_bond_value(
    face_value: float, rate_of_yield: float, time_of_maturity: float
):
    return zero_coupon_bond_value_task(
        face_value, rate_of_yield, time_of_maturity
    )


# endpoint to calculate Zero Coupon Bond Effective Yield
@app.get(
    "/zero_coupon_bond_yield",
    tags=["zero_coupon_bond_yield"],
    description="Calculating Zero Coupon Bond Effective Yield",
)
def zero_coupon_bond_yield(
    face_value: float, present_value: float, time_of_maturity: float
):
    return zero_coupon_bond_yield_task(face_value, present_value, time_of_maturity)


# Endpoint to calculate Profitability Index
@app.get(
    "/profitability_index",
    tags=["profitability_index"],
    description="Calculating profitability index",
)
def profitability_index(initial_investment: float, pv_of_future_cash_flows: float):
    return profitability_index_task(initial_investment, pv_of_future_cash_flows)


# Endpoint to calculate Profitability index using annual cash flows
@app.get(
    "/profitability_index2",
    tags=["profitability_index"],
    description="Calculating profitability index using annual cash flows",
)
def profitability_index2(
    initial_investment: float, annual_cash_flows: str, discount_rate: float
):
    return profitability_index2_task(initial_investment, annual_cash_flows, discount_rate)


# Endpoint to calculate Receivables Turnover Ratio
@app.get(
    "/receivables_turnover_ratio",
    tags=["receivables_turnover_ratio"],
    description="Calculating receivables turnover ratio",
)
def receivables_turnover_ratio(sales_revenue: float, avg_accounts_receivable: float):
    return receivables_turnover_ratio_task(sales_revenue, avg_accounts_receivable)


@app.get(
    "/remaining_balance",
    tags=["remaining_balance"],
    description="Calculating remaining balance",
)
def remaining_balance(
    regular_payment: float,
    interest_rate_per_period: float,
    number_of_payments: float,
    number_of_payments_done: float,
):
    return remaining_balance_task(
        regular_payment,
        interest_rate_per_period,
        number_of_payments,
        number_of_payments_done,
    )


# Endpoint to calculate net present value
@app.get(
    "/net_present_value",
    tags=["net present value"],
    description="Calculating net present value",
)
def net_present_value(cash_flows: str, discount_rate: float, initial_investment: float):
    return net_present_value_task(cash_flows, discount_rate, initial_investment)


# Endpoint to Calculate Leverage Ratio By Income
@app.get(
    "/leverage_ratio_income",
    tags=["Leverage Ratio By Income"],
    description="Calculate Leverage Ratio",
)
def leverage_income(debt_payments: int, income: int):
    return leverage_income_task(debt_payments, income)


# Endpoint to Calculate Leverage Ratio By equity
@app.get(
    "/leverage_ratio_equity",
    tags=["Leverage Ratio By Equity"],
    description="Calculate Leverage Ratio",
)
def leverage_equity(debt_payments: int, equity: int):
    return leverage_equity_task(debt_payments, equity)


# Endpoint to calculate the time period required for exponential growth
@app.get(
    "/time_period_required_for_growth",
    tags=["time_period_required_for_growth"],
    description="Calculating the time period required for exponential growth",
)
def time_period_required_for_growth(interest_rate: float, growth_factor: int):
    return time_period_required_for_growth_task(interest_rate, growth_factor)


# Endpoint to calculate preferred stock value
@app.get(
    "/preferred_stock_value",
    tags=["preferred_stock_value"],
    description="Calculating the preferred stock value",
)
def preferred_stock_value(dividend: float, discount_rate: float):
    return preferred_stock_value_task(dividend, discount_rate)


# Endpoint to calculate asset turnover ratio
@app.get(
    "/asset_turnover_ratio",
    tags=["asset_turnover_ratio"],
    description="Calculate asset turnover ratio",
)
def asset_turnover_ratio(
    net_sales: float, total_asset_beginning: float, total_asset_ending: float
):
    return asset_turnover_ratio_task(net_sales, total_asset_beginning, total_asset_ending)


# Endpoint to calculate Bid Ask Spread
@app.get(
    "/bid-ask-spread",
    tags=["bid_ask_spread"],
    description="Calculating the Bid Ask Spread",
)
def bid_ask_spread(ask_price: float, bid_price: float):
    return bid_ask_spread_task(ask_price, bid_price)


@app.get(
    "/calculate-period-FV-PV-rate",
    tags=["calculate-period-FV-PV-rate"],
    description="Calculating No of Periods(Time in years) with respect to Present value(PV) and Future value(FV)",
)
def CalculatePeriods(present_val: float, future_val: float, rate: float):
    return CalculatePeriods_task(present_val, future_val, rate)


@app.get(
    "/balloon-loan-payment",
    tags=["Balloon-loan-payment"],
    description="Calculating the payments on a loan that has a balance remaining after all periodic payments are mad using balloon loan payment formula",
)
def balloon_loan_payment(
    principal: float,
    interest_rate: float,
    term_years: float,
    balloon_payment_year: float,
):
    return balloon_loan_payment_task(
        principal, interest_rate, term_years, balloon_payment_year
    )

# Endpoint to calculate monthly lease payment
@app.get(
    "/monthly_lease_payment",
    tags=["monthly_lease_payment"],
    description="Calculating Monthly lease payment",
)
def monthly_lease_payment(
    Asset_value: float,
    monthly_lease_interest_rate: float,
    number_of_lease_payments: float,
):
    return monthly_lease_payment_task(
        Asset_value, monthly_lease_interest_rate, number_of_lease_payments
    )


# End point to calculate 401k
@app.get(
    "/401k",
    tags=["401k"],
    description="Calculating an estimate of the 401(k) balance at retirement",
)
def estimate_401k(
    income: float,
    contribution_percentage: float,
    current_age: int,
    age_at_retirement: int,
    rate_of_return: float,
    salary_increase_rate: float,
    withdraw_tax_rate: float,
):
    return estimate_401k_task( income, contribution_percentage, current_age, age_at_retirement, rate_of_return, salary_increase_rate, withdraw_tax_rate)


@app.get(
    "/roth-ira",
    tags=["Roth-IRA"],
    description="This calculator estimates the balances of Roth IRA savings and regular taxable savings.",
)
def roth_ira(
    principal: float,
    interest_rate: float,
    years: int,
    tax_rate: float,
    annual_contribution: float,
):
    return roth_ira_task(principal, interest_rate, years, tax_rate, annual_contribution)


# Endpoint to calculate Mortgage Amortization
@app.get(
    "/mortgage-amortization",
    tags=["mortgage-amortization"],
    description="Calculating annual or monthly amortization schedule for a mortgage loan.",
)
def mortgage_amortization(
    mortgage_amount: float,
    mortgage_deposit: float,
    annual_interest_rate: float,
    loan_term: int,
):
    return mortgage_amortization_task(mortgage_amount, mortgage_deposit, annual_interest_rate, loan_term)


# Endpoint to calculate FHA loans
@app.get(
    "/fha-loan",
    tags=["Federal Housing Administration Loans"],
    description="FHA loans are mortgages insured by the Federal Housing Administration, the largest mortgage insurer in the world.",
)
def fha_loan(
    mortgage_amount: float,
    mortgage_deposit_percentage: float,
    annual_interest_rate: float,
    fha_annual_interest_rate: float,
    loan_term: int,
):
    return fha_loan_task(mortgage_amount, mortgage_deposit_percentage, annual_interest_rate, fha_annual_interest_rate, loan_term)


# Endpoint to calculate Enterprise Value
@app.get(
    "/enterprise-value",
    tags=["Enterprise Value"],
    description="Calculating Enterprise Value for a publicly listed company.",
)
def calculate_enterprise_value(
    share_price: float,
    fully_diluted_shares_outstanding: int,
    total_debt: float,
    preferred_stock: float,
    non_controlling_interest: float,
    cash_and_cash_equivalents: float,
):
    return calculate_enterprise_value_task(share_price, fully_diluted_shares_outstanding, total_debt, preferred_stock, non_controlling_interest, cash_and_cash_equivalents)


# Endpoint to calculate Salary
@app.get(
    "/salary-calculate",
    tags=["salary-calculate"],
    description="Converts salary amounts to their corresponding values based on payment frequency.",
)
def salary_calculate(
    salary_amount: float,
    payment_frequency: str,
    hours_worked_per_day: int,
    days_worked_per_week: int,
):
    return salary_calculate_task(salary_amount, payment_frequency, hours_worked_per_day, days_worked_per_week)


@app.get(
    "/personal_loan",
    tags=["personal_loan"],
    description="Calculate personal loan",
)
def personal_loan(
    loan_amount: float, interest_rate: float, loan_term_years: int, loan_start_date: str
):
    return personal_loan_task(loan_amount, interest_rate, loan_term_years, loan_start_date)


# Endpoint to calculate lump-sum mutual fund investment
@app.get("/lumpsum")
async def calculate_lumpsum(principal: float, interest_rate: float, years: int):

    return calculate_lumpsum_task(principal, interest_rate, years)


# Endpoint to calculate FHA loan
@app.get("/fha-loan")
async def fha_loan(
    home_price: float,
    down_payment_percentage: float,
    loan_term_years: float,
    interest_rate: float,
    fha_annual_mip_percentage: float,
):
    return fha_loan_task(
        home_price,
        down_payment_percentage,
        loan_term_years,
        interest_rate,
        fha_annual_mip_percentage,
    )


# Endpoint to calculate refinance
@app.get(
    "/refinance",
    tags=["refinance_calculator"],
    description="Calculate refinance",
)
def refinance(
    current_loan_amount: float,
    current_interest_rate: float,
    current_loan_term_years: int,
    time_remaining_years: int,
    new_interest_rate: float,
    new_loan_term_years: int,
    cash_out_amount: float,
):
    return refinance_task(
        current_loan_amount,
        current_interest_rate,
        current_loan_term_years,
        time_remaining_years,
        new_interest_rate,
        new_loan_term_years,
        cash_out_amount,
    )


# Endpoint to compute any one of the following, given inputs for the remaining two: sales price, commission rate, or commission.
@app.get(
    "/commission_calc",
    tags=["commission_calc"],
    description="compute any one of the following, given inputs for the remaining two: sales price, commission rate, or commission.",
)
def commission_calc(
    sales_price: float = None, commission_rate: float = None, commission: float = None
):
    return commission_calc_task(sales_price, commission_rate, commission)


# Endpoint to compute Total college expenses


@app.get(
    "/college_cost",
    tags=["college_cost"],
    description="calculate total college fee of one year assuming full tuition fee is being paid.",
)
def college_cost(
    book_cost: float,
    college_tuition: float,
    Devices: float,
    travel_expenses: float,
    hostel_charges: float,
    mess_fee: float,
    miscellaneous: float,
):
    return college_cost_task(
        book_cost,
        college_tuition,
        Devices,
        travel_expenses,
        hostel_charges,
        mess_fee,
        miscellaneous,
    )


# Endpoint to calculate Diluted EPS
@app.get(
    "/diluted-earnings-per-share",
    tags=["diluted_earnings_per_share"],
    description="Calculate Diluted Earnings Per Share (EPS).",
)
def calculate_diluted_eps(
    net_income: float,
    weighted_avg_shares: float,
    dilutive_securities: float,
):
    return calculate_diluted_eps_task( net_income, weighted_avg_shares, dilutive_securities)


# Endpoint to calculate maturity value for fixed deposit with intrest compounded.

# Endpoint to calculate Return of Investment on equity funds


@app.get(
    "/roi_equity_funds",
    tags=["roi_equity_funds"],
    description="Calculating return of investment on equity funds.",
)
def calculate_roi_equity_funds(
    amount_invested: float,
    amount_returned: float,
    tenure: float,
):
    return calculate_roi_equity_funds_task(
        amount_invested,
        amount_returned,
        tenure,
    )


# Endpoint to compute Student loan and monthly emi for the same


@app.get(
    "/student_loan",
    tags=["student_loan"],
    description="Calculate Student loan",
)
def student_loan(principal: int, tenure: int, interest_rate: float):
    return student_loan_task(principal, tenure, interest_rate)

@app.get(
    "/calculate_gst",
    tags=["calculate_gst"],
    description="Calculate GST (Goods and Service Tax)",
)
def calculate_gst(price, gst_rate):
    return calculate_gst_task(price, gst_rate)


# Endpoint For calculated annual income needed during retiremnet period
@app.get(
    "/calculate_retirement_goals",
    tags=["calculate_retirement_goals"],
    description="Calculate amount annually needed during retirement years.",
)
def calculate_retirement_goals(
    retirement_age: int,
    annual_retirement_expenses: int,
    inflation_rate: float,
    annual_retirement_income: int,
    current_age: int,
):
    return calculate_retirement_goals_task(
        retirement_age,
        annual_retirement_expenses,
        inflation_rate,
        annual_retirement_income,
        current_age,
    )

    # Endpoint for calculating marketcap value


@app.get(
    "/calculate_market_cap",
    tags=["calculate_market_cap"],
    description="calculation of marketcap",
)
def calculate_market_cap(
    current_market_share_price: int, total_number_of_shares_outstanding: int
):
    return calculate_market_cap_task( current_market_share_price, total_number_of_shares_outstanding)


# Endpoint to calculate Annual Debt Service Coverage Ratio (ADSCR)
@app.get(
    "/asdcr",
    tags=["annual_debt_service_coverage_ratio"],
    description="Calculate Annual Debt Service Coverage Ratio",
)
def asdcr(
    net_operating_cost: float,
    depreciation: float,
    non_cash_expenses: float,
    annual_debt_service: float,
):
    return asdcr_task( net_operating_cost, depreciation, non_cash_expenses, annual_debt_service)

# Endpoint to calculate Value Added Tax (VAT)
@app.get(
    "/calculate_vat",
    tags=["VAT"],
    description="Calculate VAT for both excluding and including amounts",
)
async def calculate_vat(price: float, vat_rate: float):
    calculate_vat_price = await calculate_vat_task(price, vat_rate)
    return calculate_vat_price



# Endpoint For calculating bond equivalent yield
@app.get(
    "/bond_equivalent_yield",
    tags=["bond_equivalent_yield"],
    description="Calculate bond equivalent yield",
)
def bond_equivalent_yield(
    face_value: float, purchase_price: float, days_to_maturity: int
):
    return bond_equivalent_yield_task( face_value, purchase_price, days_to_maturity)


@app.get("/loan-affordability")
def calculate_loan_affordability(
    income: float,  # annual Income
    expenses: float,  # annual expenses
    loan_term: int,  # loan term period
    interest_rate: float,  # annual interest rate
):
    return calculate_loan_affordability_task(
        income, expenses, loan_term, interest_rate
    )


@app.get(
    "/calculate_bvps",
    tags=["calculate_bvps"],
    description="Calculate BVPS (Book value per share)",
)
def calculate_bvps(stockholders_equity, preferred_stock, average_outstanding_shares):
    return calculate_bvps_task(stockholders_equity, preferred_stock, average_outstanding_shares)


@app.get(
    "/calculate_gratuity",
    tags=["Gratuity"],
    description="Calculate gratuity",
)
def calculate_gratuity(last_salary: float, tenure_years: int, tenure_months: int):
    return calculate_gratuity_task(last_salary, tenure_years, tenure_months)


@app.get(
    "/personal_savings",
    tags=["personal_savings"],
    description="Calculate Simple Personal Savings",
)
def personal_savings(init: int,
                     monthly: int,
                     tenure: float):
    return personal_savings_task(init, monthly, tenure)


@app.get(
    "/accrint",
    tags=["accrint"],
    description="Calculate the accrued interest for a security that pays periodic interest.",
)
def accrued_interest(
    issue_date: str,
    settlement_date: str,
    rate: float,
    par: float,
    frequency: int = 1,
    basis: int = 0,
):
    return accrued_interest_task(
        issue_date, settlement_date, rate, par, frequency, basis
    )


@app.get('/mortrages', tags=["mortrage"], description="Endpoint to calculate Mortrages")
def mortrage(princial: int, interest_rate: float, years: int, down_payment: int, property_tax_rate: float, insurance_rate: float):

    return mortrage_task(princial, interest_rate, years, down_payment, property_tax_rate, insurance_rate)


@app.get(
    "/calculate_net_profit_margin",
    tags=["net_profit_margin"],
    description="Calculate net profit margin",
)
def calculate_net_profit_margin(revenue: float,
                                cost_of_goods_sold: float,
                                operating_expenses: float,
                                other_expenses: float,
                                interest: float,
                                taxes: float):
    return calculate_net_profit_margin_task(revenue, cost_of_goods_sold, operating_expenses, other_expenses, interest, taxes)


@app.get(
    "/calculate_expected_return_of_portfolio",
    tags=["expected_return_of_portfolio"],
    description="Calculate expected return of portfolio",
)
def calculate_expected_return_of_portfolio(no_of_investments: int,
                                           investment_amount: list,
                                           rate_of_return: list):
    return calculate_expected_return_of_portfolio_task(no_of_investments, investment_amount, rate_of_return)

# Endpoint to calculate Net annual salary of an employee


@app.get(
    "/calculate_salary",
    tags=["calculate_salary"],
    description="Calculate Net annual salary of an employee",
)
def calculate_salary(base: int,
                     jb: int,
                     stock: int,
                     pb: int,
                     bonus: int,
                     ptax: int,
                     deduction: int):
    return calculate_salary_task(base, jb, stock, pb, bonus, ptax, deduction)


@app.get(
    '/social_securities',
    tags=['Social Security'],
    description="Endpoint to calculate Social securities"
)
def ss(birth_date: str, earnings: int, retirement_age: int):

    return ss_task(birth_date, earnings, retirement_age)


@app.get(
    "/calculate_post_tax_return_percentage",
    tags=["post_tax_return_percentage"],
    description="Calculate post tax return percentage",
)
def calculate_post_tax_return_percentage(tax_rate_percentage: float,
                                         annual_net_income: float,
                                         initial_cost_of_investment: float):
    return calculate_post_tax_return_percentage_task(tax_rate_percentage, annual_net_income, initial_cost_of_investment)

# Endpoint for function Treynor Ratio

@app.post(
    "/treynor_ratio",
    tags=["treynor_ratio"],
    description="Calculate Treynor ratio",
)
def treynor_ratio(
    returns: list[float], risk_free_rate: float, beta: float
):
    return treynor_ratio_task(returns, risk_free_rate, beta)

# Endpoint for function Loan to Value Ratio


@app.get(
    "/loan_to_value_ratio",
    tags=["loan_to_value_ratio"],
    description="Calculate loan amount to value of collateral ratio",
)
def loan_to_value_ratio(loan_amount: float, value_of_collateral: float):
    return loan_to_value_ratio_task(loan_amount, value_of_collateral)

# Endpoint for function Free Cash Flow To Equity


@app.get(
    "/free_cash_flow_to_equity",
    tags=["free_cash_flow_to_equity"],
    description="Calculate Free Cash Flow to Equity",
)
def free_cash_flow_to_equity(
        total_revenues: float,
        total_expenses: float,
        initial_cost_of_asset: float,
        lifetime_of_asset: float,
        change_in_PPE: float,
        current_depreciation: float,
        current_assets: float,
        current_liabilities: float,
        amount_a_company_borrows: float,
        debt_it_repays: float):
    return free_cash_flow_to_equity_task( total_revenues, total_expenses, initial_cost_of_asset, lifetime_of_asset, change_in_PPE, current_depreciation, current_assets, current_liabilities, amount_a_company_borrows, debt_it_repays)

@app.get(
    "/net_worth",
    tags=["net_worth"],
    description="Calculate net worth",
)
def net_worth_calculation(assets: float, liabilities: float, loans: float, mortgages: float):
    return net_worth_calculation_task(assets, liabilities, loans, mortgages)


## Endpoint for function Capital Gains Yield

app.get(
	"/capital_gains_yield",
	tags=["capital_gains_yield"],
	description="Calculate Capital Gains Yield of a Stock",
)
def capital_gains_yield(inital_price: float, price_after_first_period: float):
    return capital_gains_yield_task(inital_price, price_after_first_period)

@app.get(
    "/calculate_macaulay_duration",
    tags=["Macaulay_duration"],
    description="Calculate macaulay duration",
)
def calculate_macaulay_duration(
    face_value : float, coupon_rate : float, dt : int, month : int, year : int, coupon_frequency : int, discount_rate : float
):
    '''
    Macaulay duration is the weighted average term to maturity of the cash flows from a bond. 
    Inputs:  face value of bond, coupon rate, dt, month, year of maturity, coupon frequency, discount rate
    Ouput: Macaulay duration in years 
    '''
    return calculate_macaulay_duration_task(face_value, coupon_rate, dt, month, year, coupon_frequency, discount_rate)  
      
@app.get(
    "/calculate_financial_leverage",
    tags=["financial_leverage"],
    description="Calculate financial leverage",
)
def calculate_financial_leverage(total_assets : float,
                                 total_liabilities : float,
                                 short_term_debt : float,
                                 long_term_debt : float
                                 ):
    return calculate_financial_leverage_task(total_assets, total_liabilities, short_term_debt, long_term_debt)


@app.get(
        "/portfolio_return_monte_carlo", 
        tags=["portfolio_return"], 
        description="Estimate portfolio return using Monte Carlo simulation"
)
def portfolio_return_monte_carlo(principal: float, 
                                 expected_return_range_start: float, 
                                 expected_return_range_end: float,
                                 volatility_range_start: float,
                                 volatility_range_end: float,
                                 num_simulations: float):
    return portfolio_return_monte_carlo_task(principal, expected_return_range_start, expected_return_range_end, volatility_range_start, volatility_range_end, num_simulations)
#Endpoint for function Capitalization Rate

@app.get(
    "/capitalization_rate",
    tags=["capitalization_rate"],
    description="Calculate capitalization rate for a given property.",
)
def capitalization_rate(
        rental_income: float,
        amenities: float,
        propertyManagement: float,
        propertyTaxes:float,
        insurance: float,
        current_market_value: float):
    return capitalization_rate_task(rental_income, amenities, propertyManagement, propertyTaxes, insurance, current_market_value)

@app.get(
    "/accounts_payable_turnover_ratio",
    tags=["accounts_payable_turnover_ratio"],
    description="Calculates the Accounts Payable Turnover Ratio",
)
def accounts_payable_turnover_ratio(total_supply_purchases: float,
                                    beginning_accounts_payable: float,
                                    ending_accounts_payable: float):
    return accounts_payable_turnover_ratio_task(total_supply_purchases, beginning_accounts_payable, ending_accounts_payable)


@app.post(
    "/capm",
    tags=["Capital Asset Pricing Model (CAPM)"],
    description="Estimate the expected return on an investment.",
)
def capm(request: capmRequest):
    return calculate_capm(request.risk_free_return, request.sensitivity, request.expected_market_return)

# Endpoint to calculate Debt Service Coverage Ratio

@app.post(
    "/debt_service_coverage_ratio",
    tags=["debt_service_coverage_ratio"],
    description="Calculate Debt Service Coverage Ratio",
)
def debt_service_coverage_ratio(request: DebtServiceCoverageRatio):
    return debt_service_coverage_ratio_task(request.revenue,
	request.operating_expenses,
	request.interest,
	request.tax_rate,
	request.principal)


@app.post(
    "/modified_internal_rate_of_return",
    tags=["mirr"],
    description="Calculate Modified Internal Rate of Return (MIRR)",
)
def calculate_modified_internal_rate_of_return(
    request: ModifiedInternalRateOfReturn
):
    return calculate_modified_internal_rate_of_return_task(
        request.ending_cash_flow,
        request.initial_cash_flow,
        request.number_of_periods,
    )
    

#Endpoint to calculate profit percentage
@app.post(
    "/profit_percent",
    tags=["profit_percentage"],
    description="Calculates the profit percentage",
)
def profit_percent(request: ProfitPercentage):
    return profit_percentage_task(request.profit, request.cost_price)

#Endpoint to calculate loss percentage
@app.post(
    "/loss_percent",
    tags=["loss_percentage"],
    description="Calculates the loss percentage",
)
def loss_percent(request: ProfitPercentage):
    return loss_percentage_task(request.loss, request.cost_price)

# Endpoint to calculate Defensive Interval Ratio

@app.post(
    "/defensive_interval_ratio",
    tags=["defensive_interval_ratio"],
    description="Calculate Defensive Interval Ratio",
)
def defensive_interval_ratio(request: DefensiveIntervalRatio):
    return defensive_interval_ratio_task(request.cash, request.marketable_securities, 
    request.net_receivables, request.annual_operating_expenses , request.non_cash_charges)

# Endpoint to calculate Rate of return

@app.post(
    "/rate_of_return",
    tags=["rate_of_return"],
    description="Calculate Rate of return",
)
def rate_of_return(request: RateofReturn):
    return calculate_rate_of_return(request.initial_investment,
	request.final_value,
	request.cash_flows,
	request.time_period,
	request.holding_period)
# Endpoint to calculate Financial assest Ratio

@app.post(
    "/financial_assest_ratio",
    tags=["financial_assest_ratio"],
    description="Calculate financial assest Ratio",
)
def financial_assest_ratio(request: financialAssestRatio):
    return financial_assest_ratio(request.current_assets,
	request.current_liabilities,
	request.total_debt,
	request.total_equity,
	request.net_income,
    request.total_revenue)


# Endpoint to calculate Cash Conversion Cycle

@app.post(
    "/cash_conversion_cycle",
    tags=["cash_conversion_cycle"],
    description="Calculate Cash Conversion Cycle",
)
def cash_conversion_cycle(request: CashConversionCycle):
    return cash_conversion_cycle_task(request.beginning_inventory , request.ending_inventory ,
    request.beginning_receivables, request.ending_receivables , request.beginning_payable, 
    request.ending_payable , request.net_credit_sales , request.cost_of_goods_sold)

# Endpoint to calculate Policy Premium

@app.post(
    "/policy_premium",
    tags=["policy_premium"],
    description="Calculate Policy premium",
)
def policy_premium(request: PolicyPremium):
    return calculate_policy_premium(request.policy_type,
	request.age,
	request.coverage_amount,
	request.deductible,
	request.num_claims,
    request.num_accidents)
# Endpoint to calculate Price Elasticity 

@app.post(
    "/price_elasticity",
    tags=["price_elasticity"],
    description="Calculate Cash Conversion Cycle",
)
def price_elasticity(request: PriceElasticity):
    return calculate_price_elasticity(request.initial_price , 
    request.final_price ,
    request.initial_quantity, 
    request.final_quantity )

# Endpoint to calculate Average Payment Period
@app.post(
    "/average_payment_period",
    tags=["average_payment_period"],
    description="Calculate Average Payment Period",
)
def average_payment_period(request: AveragePaymentPeriod):
    return average_payment_period_task(request.beginning_accounts_payable , 
    request.ending_accounts_payable , request.total_credit_purchases)

# Endpoint to calculate Saving Goal 

@app.post(
    "/saving_goal",
    tags=["saving_goal"],
    description="Calculate Saving Goal",
)
def saving_goal(request: SavingGoal):
    return saving_goal(request.current_savings , 
    request.monthly_contributions ,
    request.interest_rate, 
    request.goal_amount )

# Endpoint to calculate Interest Coverage Ratio

@app.post(
    "/interest_coverage_ratio",
    tags=["interest_coverage_ratio"],
    description="Calculates interest coverage ratio",
)
def interest_coverage_ratio(request: InterestCoverageRatio):
    return interest_coverage_ratio_task(request.revenue, request.cost_of_goods_services,
    request.operating_expenses, request.interest_expense)

# Endpoint to calculate Tax Bracket Calculator

@app.post(
    "/tax_bracket_calculator",
    tags=["tax_bracket_calculator"],
    description="Calculates Tax Bracket Calculator",
)
def tax_bracket_calculator(request: TaxBracketCalculator):
    return interest_coverage_ratio_task(request.income, request.filing_status)

# Endpoint to calculate Margin of Safety

@app.post(
    "/margin_of_safety",
    tags=["margin_of_safety"],
    description="Calculates margin of safety",
)
def margin_of_safety(request: MarginOfSafety):
    return margin_of_safety_task(request.current_sales, request.break_even_point)
