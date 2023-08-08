import math
import numpy as np
import pandas as pd
import math
import datetime
from dateutil.relativedelta import relativedelta
from typing import Union


# Function to Calculate Simple Interest Rate
def simple_interest_rate(amount_paid: float, principle_amount: float, months: int):
    term = months / 12
    interest_paid = amount_paid - principle_amount
    rate = decimal_to_percent(interest_paid) / (principle_amount * term)
    return rate


# Calculate percent to decimal
# def percent_to_decimal(percent: int | float) -> float:
#     return (percent / 100)
def percent_to_decimal(percent: Union[int, float]) -> float:
    return (percent / 100)

# Calculate decimal to percent


def decimal_to_percent(decimal: Union[int, float]) -> float:
    return decimal * 100


# Function to Calculate Loan Emi
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    monthly_rate = percent_to_decimal(annual_rate) / 12
    emi = (principle_amount * monthly_rate * (1 + monthly_rate) ** months) / (
        ((1 + monthly_rate) ** months - 1)
    )
    return emi


def future_sip(
    interval_investment: float, rate_of_return: float, number_of_payments: int
):
    interest = percent_to_decimal(rate_of_return) / 12
    value = (
        interval_investment
        * ((1 + interest) ** number_of_payments - 1)
        * (1 + interest)
        / interest
    )
    return value


def payback_period(
    years_before_recovery: int, unrecovered_cost: float, cash_flow: float
):
    period = years_before_recovery + (unrecovered_cost / cash_flow)
    return period


# Function to Calculate Compound Intrest
def compound_interest(
    principal_amount: float, intrest_rate: float, years: int, compounding_period: int
):
    amount = principal_amount * (
        pow((1 + (intrest_rate / compounding_period)),
            (compounding_period * years))
    )
    print(amount)
    return amount


# Function to Calculate Inflation
def inflation(present_amount: float, inflation_rate: float, years: int):
    future_amount = present_amount * (
        pow((1 + percent_to_decimal(inflation_rate)), years)
    )
    return future_amount


# Function to Calculate Effective Annual Rate
def effective_annual_rate(annual_interest_rate: float, compounding_period: int):
    EAR = pow((1 + (annual_interest_rate / compounding_period)),
              compounding_period) - 1
    return EAR


# Function to Calculate Certificate of Deposit (CD)
def certificate_of_deposit(
    principal_amount: float, interest_rate: float, yrs: int, compounding_per_yr: int
):
    cd = principal_amount * (
        1 + interest_rate / decimal_to_percent(compounding_per_yr)
    ) ** (compounding_per_yr * yrs)
    return float(cd)


# Function to Calculate Return on Investment
def return_on_investment(current_value_of_investment: float, cost_of_investment: float):
    roi = (current_value_of_investment -
           cost_of_investment) / cost_of_investment
    return decimal_to_percent(roi)


# Function to calculate Jensens Alpha
def jensens_alpha(
    return_from_investment: float,
    return_of_appropriate_market_index: float,
    risk_free_rate: float,
    beta: float,
):
    alpha = return_from_investment - (
        risk_free_rate + beta *
        (return_of_appropriate_market_index - risk_free_rate)
    )
    return alpha


# Function to calculate Weighted Average Cost of Capital (WACC)
def weighted_average_cost_of_capital(
    firm_equity: float,
    firm_debt: float,
    cost_of_equity: float,
    cost_of_debt: float,
    corporate_tax_rate: float,
):
    v = firm_debt + firm_equity
    wacc = (firm_equity * cost_of_equity / v) + (
        firm_debt * cost_of_debt * (1 - corporate_tax_rate) / v
    )
    return wacc


# Function to calculate variance of a two asset portfolio
def asset_portfolio(
    price_A: float,
    price_B: float,
    retrun1: float,
    return2: float,
    standard_dev_A: float,
    standard_dev_B: float,
    stock_correlation: float,
):
    weight_A = price_A / (price_A + price_B)
    weight_B = price_B / (price_A + price_B)
    cov = stock_correlation * standard_dev_A * standard_dev_B
    portfolio_variance = (
        weight_A * weight_A * standard_dev_A * standard_dev_A
        + weight_B * weight_B * standard_dev_B * standard_dev_B
        + 2 * weight_A * weight_B * cov
    )
    return portfolio_variance


# Function to calculate the future price in a put - call parity
def put_call_parity(call_price: float, put_price: float, strike_price: float):
    future_price = call_price + strike_price - put_price
    return future_price


# Function to calculate break even point
def break_even_point(fixed_cost: float, selling_price: float, variable_cost: float):
    contribution_margin = selling_price - variable_cost
    units = fixed_cost // contribution_margin
    rupees = fixed_cost // (contribution_margin / selling_price)
    return units, rupees


# Function to calculate free cash flow to firm
def free_cash_flow_to_firm(
    sales: float,
    operating_cost: float,
    depreciation: float,
    interest: float,
    tax_rate: float,
    fcInv: float,
    wcInv: float,
):
    ebitda = sales - operating_cost
    ebit = ebitda - depreciation
    ebt = ebit - interest
    eat = ebt - ebt / (tax_rate * 0.01)
    wcInv = abs(wcInv)

    return (ebit * (1 - tax_rate * 0.01)) + depreciation - fcInv - wcInv


# Function to calculate the Price-to-Earning ratio (P/E ratio):
def price_to_earning_ratio(share_price: float, earnings_per_share: float):
    p_e_ratio = share_price // earnings_per_share
    return p_e_ratio


# Function to calculate the Dividend yield ratio:
def dividend_yield_ratio(dividend_per_share: float, share_price: float):
    dividend_yield = dividend_per_share // share_price
    return dividend_yield


# Function to calculate the dividend payout ratio
def dividend_payout_ratio(dividend_per_share: float, earnings_per_share: float):
    dividend_payout = dividend_per_share // earnings_per_share
    return dividend_payout


# Function to calculate the debt-to-income ratio (DTI ratio):
def debt_to_income_ratio(annual_income: float, total_debt_per_month: float):
    income_per_month = percent_to_decimal(annual_income) / 12
    DTI = total_debt_per_month // income_per_month
    return DTI


# Function to calculate the Fixed-charge coverage ratio :
def fixed_charge_coverage_ratio(
    earnings_before_interest_taxes: float,
    fixed_charge_before_tax: float,
    interest: float,
):
    a = earnings_before_interest_taxes + fixed_charge_before_tax
    b = interest + fixed_charge_before_tax
    fccr = a // b
    return fccr


# Function to calculate Inventory Shrinkage
def inventory_shrinkage_rate(recorded_inventory: float, actual_inventory: float):
    inventory_shrinkage_rate = (
        recorded_inventory - actual_inventory
    ) / recorded_inventory
    return inventory_shrinkage_rate


# Function to calculate Markup Percentage
def markup_percentage(price: float, cost: float):
    markup_percentage = decimal_to_percent((price - cost) / cost)
    return markup_percentage


# Function to calculate Sharpe Ratio
def sharpe_ratio(
    portfolio_return: float,
    risk_free_rate: float,
    standard_deviation_of_portfolio: float,
):
    sharpe_ratio_val = (portfolio_return - risk_free_rate) / standard_deviation_of_portfolio
    return sharpe_ratio_val


# Function to calculate Purchasing Power
def purchasing_power(initial_amount: float, annual_inflation_rate: float, time: float):
    a = initial_amount * ((100 / (100 + annual_inflation_rate)) ** time)
    return a


# Function to create Monthly EMI
def monthly_emi(loan_amt: float, interest_rate: float, number_of_installments: float):
    emi = (
        loan_amt
        * interest_rate
        * ((1 + interest_rate) ** number_of_installments)
        / ((1 + interest_rate) ** number_of_installments - 1)
    )
    return emi


# Function to calculate doubling time
def doubling_time(r: float):
    t = math.log(2) / math.log(1 + percent_to_decimal(r))
    return t


# Function to calculate Weighted Average
def weighted_average(ratio: list, rates: list):
    wa = 0
    for i in range(len(ratio)):
        wa = wa + ratio[i] * rates[i]
    # print("Weighted Average returns: ",wa)
    return wa


# Function to calculate calculate Capital Asset Pricing Model
def Capital_Asset_Pricing_Model(
    risk_free_interest_rate: float,
    beta_of_security: float,
    expected_market_return: float,
):
    capital_asset_expected_return = risk_free_interest_rate + beta_of_security * (
        expected_market_return - risk_free_interest_rate
    )
    return capital_asset_expected_return


# Function to calculate cost of equity:
def cost_of_equity(
    risk_free_rate_of_return: float, Beta: float, market_rate_of_return: float
):
    costOfEquity = risk_free_rate_of_return + Beta * (
        market_rate_of_return - risk_free_rate_of_return
    )
    return costOfEquity


# Function to calculate cost of goods sold
def cost_of_goods_sold(
    beginning_inventory: float, purchases: float, ending_inventory: float
):
    cogs = beginning_inventory + purchases - ending_inventory
    return cogs


# Function to calculate Rule of 72
def rule_of_72(rate_of_roi: float):
    time_period = 72 / rate_of_roi
    return time_period


# Function to calculate Acid test ratio
def acid_test_ratio(
    cash: float,
    marketable_securitie: float,
    accounts_receivable: float,
    current_liabilities: float,
):
    ratio = (cash + marketable_securitie +
             accounts_receivable) / current_liabilities
    return round(ratio, 2)


# Function to calculate inflation adjusted return
def inflation_adjusted_return(
    beginning_price: float,
    ending_price: float,
    dividends: float,
    beginning_cpi_level: float,
    ending_cpi__level: float,
):
    stock_return = (ending_price - beginning_price +
                    dividends) / beginning_price

    inflation = (ending_cpi__level - beginning_cpi_level) / beginning_cpi_level

    inflation_adj = decimal_to_percent(
        (1 + stock_return) / (1 + inflation) - 1)
    return round(inflation_adj, 2)


# Function to calculate compound annual growth rate
def compound_annual_growth_rate(
    beginning_value: float, ending_value: float, years: int
):
    rate = decimal_to_percent(
        pow((beginning_value / ending_value), 1 / years) - 1)
    return round(rate, 1)


# Function to calculate current liability coverage ratio
def current_liability_coverage_ratio(
    net_cash_from_operating_activities: float,
    total_current_liabilities: float,
    number_of_liabilities: int,
):
    average_current_liabilities = total_current_liabilities / number_of_liabilities
    current_liability_coverage_ratio = (
        net_cash_from_operating_activities / average_current_liabilities
    )
    return current_liability_coverage_ratio


# Function to calculate Levered beta:
def levered_beta(unlevered_beta: float, tax_rate: float, debt: float, equity: float):
    l_beta = unlevered_beta * (1 + (1 - tax_rate) * (debt // equity))
    return l_beta


# Function to calculate monthly payment:
def monthly_payment(
    principal: float,
    interest_rate: float,
    number_of_periods: float,
    payments_per_period: float,
):
    a = principal * (interest_rate // payments_per_period)
    b = 1 - (1 + (interest_rate // payments_per_period)) ** (
        -payments_per_period * number_of_periods
    )
    monthly_pay = a // b
    return monthly_pay


# Function to calculate Duration With Convexity Adjustment
def duration(
    rate: float,
    coupon_rate: float,
    frequency: float,
    face_value: float,
    settlement_date: float,
    maturity_date: float,
):
    try:
        settlement_date = pd.to_datetime(settlement_date, format="%d/%m/%Y")

    except:
        settlement_date = pd.to_datetime(settlement_date, format="%d-%m-%Y")

    try:
        maturity_date = pd.to_datetime(maturity_date, format="%d/%m/%Y")
    except:
        maturity_date = pd.to_datetime(maturity_date, format="%d-%m-%Y")
    data = pd.DataFrame()
    rate = percent_to_decimal(rate)
    coupon_rate = percent_to_decimal(coupon_rate)

    n = pd.to_numeric(
        ((pd.to_datetime(maturity_date) - pd.to_datetime(settlement_date)) / 365).days
    )
    total_payment = n * frequency
    coupon_payment = coupon_rate / frequency * face_value
    payment = [coupon_payment] * \
        (total_payment - 1) + [coupon_payment + face_value]
    data["period"] = pd.DataFrame(np.arange(1, total_payment + 1))
    data["payment"] = pd.DataFrame(payment)
    data["dcoupon"] = data["payment"] / \
        ((1 + rate / frequency) ** data["period"])
    data["pv"] = data["dcoupon"] / frequency * \
        data["period"] / data["dcoupon"].sum()
    duration = data["pv"].sum()
    m_duration = duration / (1 + rate / frequency)

    factor = 1 / (data["dcoupon"].sum() * (1 + rate / frequency) ** 2)
    data["cf"] = (
        data["dcoupon"]
        * (data["period"] ** 2 + data["period"])
        / (1 + rate / frequency) ** data["period"]
    )
    convexity = factor * data["cf"].sum()

    result = round(duration, 3)

    return result


# Function to calculate current ratio
def current_ratio(total_current_assets: float, total_liabilities: float):
    ratio = total_current_assets / total_liabilities
    return round(ratio, 3)


# Function to calculate inventory turnover ratio
def inventory_turnover_ratio(
    cost_of_goods_sold: float, beginning_inventory: float, ending_inventory: float
):
    avg_inventory = (beginning_inventory + ending_inventory) / 2
    ratio = cost_of_goods_sold / avg_inventory
    return round(ratio, 2)


# Function to calculate Inflation Rate
def inflation_rate(bigger_year: int, smaller_year: int, base_year: int):
    inflation_rate = decimal_to_percent(
        (bigger_year - smaller_year) / base_year)
    return inflation_rate


# Function to calculate Herfindal index
def herfindal_Index(Firms_market_shares: str):
    market_share_list = []
    i = 0
    breaker = 0
    while i < len(Firms_market_shares):
        share = ""
        if Firms_market_shares[i] == " ":
            for j in range(breaker, i):
                share = share + Firms_market_shares[j]
            market_share_list.append(int(share))
            breaker = i + 1
        i = i + 1
    market_share_list.append(
        int(
            Firms_market_shares[len(Firms_market_shares) -
                                2: len(Firms_market_shares)]
        )
    )
    herfindal_Index = 0
    for i in market_share_list:
        herfindal_Index = herfindal_Index + i**2
    herfindal_Index = herfindal_Index
    return herfindal_Index


# function to calculate discount opex
def discount_opex(annual_opex: float, wacc: float, project_lifetime: float):
    a = annual_opex // wacc
    b = 1 - 1 // ((1 + wacc) ** project_lifetime)
    dis_opex = a * b
    return dis_opex


# function to calculate project efficiency
def project_efficiency(annual_production: float, collector_surface: float, dni: float):
    project_eff = annual_production // (collector_surface * dni)
    return project_eff


# Function to calculate Real GDP
def real_gdp(nominal_gdp: float, gdp_deflator: float):
    real_gdp = decimal_to_percent(nominal_gdp / gdp_deflator)
    return real_gdp


# Function to calculate excess reserves
def excess_reserves(deposits: float, reserve_requirement: float):
    excess_reserves = deposits - deposits * reserve_requirement
    return excess_reserves


# function to calculate discounted cash flow
def discounted_cash_flow(
    real_feed_in_tariff: float,
    annual_production: float,
    wacc: float,
    project_lifetime: float,
):
    a = (real_feed_in_tariff * annual_production) // wacc
    b = 1 - (1 // (1 + wacc) ** project_lifetime)
    d_cash_flow = a * b
    return d_cash_flow


# Function to calculate GDP growth rate
def gdp_growth_rate(current_year_gdp: float, last_year_gdp: float):
    gdp_growth_rate = decimal_to_percent(
        (current_year_gdp - last_year_gdp) / last_year_gdp
    )
    return gdp_growth_rate


# function to calculate credit card equation
def credit_card_equation(
    balance: float, monthly_payment: float, daily_interest_rate: float
):
    a = np.log(1 + (balance // monthly_payment) *
               (1 - (daily_interest_rate) ** 30))
    b = np.log(1 + daily_interest_rate)
    N = -(1 // 30) * (a // b)
    return N


# function to calculate the payoff of multiple credit cards using Debt Avalanche method
def credit_card_payoff(
    debts: list, interest_rates: list, minimum_payments: list, monthly_payment: int
):
    cards = []

    for i in range(len(debts)):
        cards.append(
            {
                "index": i,
                "debt": int(debts[i]),
                "minimum_payment": int(minimum_payments[i]),
                "interest_rate": int(interest_rates[i]),
                "interest_paid": 0,
                "month": 0,
                "total_payment": 0,
            }
        )
    # Sort the list of dictionaries by interest rate, in descending order
    cards.sort(key=lambda x: x["interest_rate"], reverse=True)

    extra = 0
    while sum(d["debt"] for d in cards) > 0:
        highest_interest_index = cards.index(
            max((d for d in cards if d["debt"] > 0),
                key=lambda x: x["interest_rate"])
        )  # highest index of the interest rate
        total_minimum_payment = sum(
            c["minimum_payment"] for c in cards if c["debt"] > 0
        )
        extra_payment = monthly_payment - total_minimum_payment + extra
        extra = 0
        for i in range(len(cards)):
            if cards[i]["debt"] > 0:
                interest = round(
                    percent_to_decimal(
                        cards[i]["debt"] * cards[i]["interest_rate"])
                    / 12,
                    2,
                )
                payment = cards[i]["minimum_payment"]
                cards[i]["interest_paid"] += interest
                cards[i]["month"] += 1
                if i == highest_interest_index:
                    payment += extra_payment
                if payment > cards[i]["debt"]:
                    extra = payment - cards[i]["debt"]
                    cards[i]["total_payment"] += cards[i]["debt"]
                    cards[i]["debt"] = 0
                else:
                    cards[i]["debt"] -= payment
                    cards[i]["total_payment"] += payment
                if cards[i]["debt"] == 0:
                    cards[i]["total_payment"] += cards[i]["interest_paid"]

    cards.sort(key=lambda x: x["index"])

    return cards


# function to calculate future value of the ordinary annuity
def future_value_of_ordinary_due(
    periodic_payment: float, number_of_periods: int, effective_interest_rate: float
):
    future_value_of_ordinary_due = (
        periodic_payment
        * (((1 + effective_interest_rate) ** (number_of_periods)) - 1)
        / effective_interest_rate
    )
    return future_value_of_ordinary_due


# Function to calculate future value of annuity due
def future_value_of_annuity_due(
    periodic_payment: float, number_of_periods: int, effective_interest_rate: float
):
    future_value_of_annuity_due = (
        periodic_payment
        * (((1 + effective_interest_rate) ** (number_of_periods)) - 1)
        * (1 + effective_interest_rate)
        / effective_interest_rate
    )
    return future_value_of_annuity_due


# Function to calculate present value of annuity due
def present_value_of_annuity_due(
    periodic_payment: float, number_of_periods: int, rate_per_period: float
):
    present_value_of_annuity_due = periodic_payment + periodic_payment * (
        (1 - (1 + rate_per_period) ** (-number_of_periods + 1)) / rate_per_period
    )
    return present_value_of_annuity_due


# Function to calculate loan to value
def loan_to_value(mortage_value: float, appraised_value: float):
    ratio = mortage_value / appraised_value
    return decimal_to_percent(ratio)


# Function to calculate Retention Rate
def retention_ratio(net_income: float, dividends: float):
    retention_ratio = (net_income - dividends) / net_income
    return retention_ratio


# Function to calculate Tax Equivalent Yield
def tax_equivalent_yield(tax_free_yield: float, tax_rate: float):
    tax_equivalent_yield = tax_free_yield / (1 - tax_rate)
    return tax_equivalent_yield


# Function to calculate year over year growth
def year_over_year(later_period_value: float, earlier_period_value: float):
    growth = (later_period_value - earlier_period_value) / earlier_period_value
    return decimal_to_percent(growth)


# function to calculate future value of the annuity
def future_value_of_annuity(
    payments_per_period: float, interest_rate: float, number_of_periods: float
):
    a = (((interest_rate + 1) ** number_of_periods) - 1) // interest_rate
    fva = payments_per_period * a
    return fva


# Function to calculate Balloon Balance of a Loan
def balloon_balance_of_loan(
    present_value: float,
    payment: float,
    rate_per_payment: float,
    number_of_payments: float,
):
    balloon_balance_of_loan = present_value * (
        (1 + rate_per_payment) ** number_of_payments
    ) - payment * (
        (((1 + rate_per_payment) ** number_of_payments) - 1) / rate_per_payment
    )
    return balloon_balance_of_loan


# Function to calculate discounted payback period
def discounted_payback_period(outflow: float, rate: float, periodic_cash_flow: float):
    discounted_payback_period = np.log(
        1 / (1 - (outflow * rate / periodic_cash_flow)),10
    ) / np.log(1 + rate,10)
    return discounted_payback_period


# Function to calculate periodic lease payment
def periodic_lease_payment(
    Asset_value: float,
    monthly_lease_interest_rate: float,
    number_of_lease_payments: float,
):
    periodic_lease_payment = (Asset_value * monthly_lease_interest_rate) / (
        1 - (1 / (1 + monthly_lease_interest_rate) ** number_of_lease_payments)
    )
    return periodic_lease_payment


# Function to calculate weighted average
def weighted_average_of_values(Assigned_weight_values: str, data_point_values: str):
    weights = list(map(int, Assigned_weight_values.split()))
    data_values = list(map(int, data_point_values.split()))
    total_data_point_weighted_value = 0
    sum_assigned_weight_values = 0
    for i in weights:
        sum_assigned_weight_values = sum_assigned_weight_values + i
    for i in range(len(weights)):
        total_data_point_weighted_value = total_data_point_weighted_value + (
            weights[i] * data_values[i]
        )

    weighted_average = total_data_point_weighted_value / sum_assigned_weight_values
    return weighted_average


# Function to calculate Yield to maturity
def yield_to_maturity(
    bond_price: float, face_value: float, coupon_rate: float, years_to_maturity: float
):
    yield_cal = (
        coupon_rate * percent_to_decimal(face_value)
        + (face_value - bond_price) / years_to_maturity
    ) / ((face_value + bond_price) / 2)
    return round(decimal_to_percent(yield_cal), 2)


# Function to calculate perpetuity payment
def perpetuity_payment(present_value: float, rate: float):
    payment = present_value * percent_to_decimal(rate)
    return payment


# Function to calculate Zero Coupon Bond value
def zero_coupon_bond_value(
    face_value: float, rate_of_yield: float, time_of_maturity: float
):
    zcbv = face_value / \
        pow((1 + percent_to_decimal(rate_of_yield)), time_of_maturity)
    return round(zcbv, 2)


# function to calculate Zero Coupon Bond Effective Yield
def zero_coupon_bond_yield(
    face_value: float, present_value: float, time_of_maturity: float
):
    zcby = pow((face_value / present_value), (1 / time_of_maturity)) - 1
    return round(decimal_to_percent(zcby), 1)


# Function to calculate Profitability Index
def profitability_index(initial_investment: float, pv_of_future_cash_flows: float):
    profitability_index = pv_of_future_cash_flows / initial_investment
    return profitability_index


# Function to calculate Profitability index using annual cash flows
def profitability_index2(
    initial_inverstment: float, annual_cash_flows: str, discount_rate: float
):
    annual_cash_flow_list = list(map(int, annual_cash_flows.split()))
    pv_cash_flow_list = []
    for i in range(len(annual_cash_flow_list)):
        pv_cash_flow_list.append(
            (annual_cash_flow_list[i])
            / ((1 + percent_to_decimal(discount_rate)) ** (i + 1))
        )
    total_pv_cash_flow = sum(pv_cash_flow_list)
    profitability_index = total_pv_cash_flow / initial_inverstment
    return profitability_index


# Function to calculate Receivables Turnover Ratio
def receivables_turnover_ratio(sales_revenue: float, avg_accounts_receivable: float):
    receivables_turnover_ratio = sales_revenue / avg_accounts_receivable
    return receivables_turnover_ratio


# Function to calculate Remaiing balance
def remaining_balance(
    regular_payment: float,
    interest_rate_per_period: float,
    number_of_payments: float,
    number_of_payments_done: float,
):
    B = regular_payment * (
        (
            1
            - (
                (1 + interest_rate_per_period)
                ** (-(number_of_payments - number_of_payments_done))
            )
        )
        // interest_rate_per_period
    )
    return B


# Function to calculate Net present value
def net_present_value(cash_flows: str, discount_rate: float, initial_investment: float):
    cash_flow_list = list(map(int, cash_flows.split()))
    net_present_value = -1 * (initial_investment)
    for i in range(len(cash_flow_list)):
        net_present_value = net_present_value + (
            cash_flow_list[i] /
            ((1 + percent_to_decimal(discount_rate)) ** (i + 1))
        )
    return net_present_value


def leverage_income(debt_payments: int, income: int):
    return float(debt_payments) / float(income)


def leverage_equity(debt: int, equity: int):
    return float(debt) / float(equity)


# Function to calculate time period required for given growth
def time_period_required_for_growth(interest_rate: float, growth_factor: int):
    time_period_required_for_growth = math.log(growth_factor) / math.log(
        1 + percent_to_decimal(interest_rate)
    )
    return time_period_required_for_growth


# Function to calculate preferred stock value
def preferred_stock_value(dividend: float, discount_rate: float):
    preferred_stock_value = dividend / discount_rate
    return preferred_stock_value


# Function to calculate present value of annuity due
def present_value_of_annuity_due(
    periodic_payment: float, number_of_periods: int, rate_per_period: float
):
    present_value_of_annuity_due = (
        periodic_payment
        * ((1 - (1 / (1 + rate_per_period) ** (number_of_periods))) / rate_per_period)
        * (1 + rate_per_period)
    )
    return present_value_of_annuity_due


# Function to Calculate Asset Turnover Ratio
def asset_turnover_ratio(
    net_sales: float, total_asset_beginning: float, total_asset_ending: float
):
    avg_total_asset = (total_asset_beginning + total_asset_ending) / 2
    asset_turnover_ratio = net_sales / avg_total_asset
    return asset_turnover_ratio


# Function to calculate Bid Ask Spread
def bid_ask_spread(ask_price: float, bid_price: float):
    bid_ask_spread = ask_price - bid_price
    return bid_ask_spread


# Function To calculate No of Periods(Time in years) with respect to Present value(PV) and Future value(FV)
def CalculatePeriods(present_val: float, future_val: float, rate: float):
    n = math.log(future_val / present_val) / \
        math.log(1 + percent_to_decimal(rate))
    return n


# Function to calculate payments on a loan that has balance remaining after all periodic payments
# are made
def balloon_loan_payment(
    principal: float,
    interest_rate: float,
    term_years: float,
    balloon_payment_year: float,
):
    monthly_interest_rate = percent_to_decimal(interest_rate) / 12
    months_paid = balloon_payment_year * 12
    rs = (1 + monthly_interest_rate) ** months_paid
    term_months = term_years * 12
    monthly_payment = (principal * monthly_interest_rate) / (
        1 - 1 / (1 + monthly_interest_rate) ** term_months
    )
    balloon_payment = principal * rs - monthly_payment * (
        (rs - 1) / monthly_interest_rate
    )
    return balloon_payment


# Function to calculate Monthly lease payment
def monthly_lease_payment(
    Asset_value: float,
    monthly_lease_interest_rate: float,
    number_of_lease_payments: float,
):
    periodic_payment = periodic_lease_payment(
        Asset_value, monthly_lease_interest_rate, number_of_lease_payments
    )
    monthly_payment = periodic_payment / number_of_lease_payments
    return monthly_payment


# Function to calculate 401k
def calculate_401k(
    income: float,
    contribution_percentage: float,
    current_age: int,
    age_at_retirement: int,
    rate_of_return: float,
    salary_increase_rate: float,
):
    contribution_amount = income * percent_to_decimal(contribution_percentage)
    number_of_years = age_at_retirement - current_age
    amount = 0
    for _ in range(number_of_years):
        amount = (amount + contribution_amount) * (
            1 + percent_to_decimal(rate_of_return)
        )
        contribution_amount = (contribution_amount) * (
            1 + percent_to_decimal(salary_increase_rate)
        )
    return round(amount, 3)


# Function to calculate Mortgage Amortization
def calculate_mortgage_interest(
    mortgage_amount: float,
    mortgage_deposit: float,
    annual_interest_rate: float,
    loan_term: int,
):
    annual_interest_rate = percent_to_decimal(annual_interest_rate)
    loan_amount = mortgage_amount * percent_to_decimal(100 - mortgage_deposit)
    power = (1 + annual_interest_rate) ** loan_term
    mortgage_annual_payment = loan_amount * \
        (annual_interest_rate * power) / (power - 1)
    return round(mortgage_annual_payment, 3)


# Function to calculate the FHA mortgage
def calculate_fha_mortgage_interest(
    mortgage_amount: float,
    mortgage_deposit_percentage: float,
    annual_interest_rate: float,
    fha_annual_interest_rate: float,
    loan_term: int,
):
    mortgage_amount = mortgage_amount - (
        mortgage_amount * percent_to_decimal(mortgage_deposit_percentage) * 0.1
    )

    # Calculate upfront MIP and monthly <MIP> interest rates
    upfront_mip_percentage = 1.75
    upfront_mip = mortgage_amount * percent_to_decimal(upfront_mip_percentage)
    monthly_mip_percentage = percent_to_decimal(fha_annual_interest_rate) / 12
    monthly_mip = mortgage_amount * monthly_mip_percentage

    # Calculate monthly mortage payment
    loan_term_months = loan_term * 12
    monthly_interest_rate = percent_to_decimal(annual_interest_rate) / 12
    power = (1 + monthly_interest_rate) ** loan_term_months
    monthly_payment = mortgage_amount * \
        (monthly_interest_rate * power) / (power - 1)

    # Calculate total FHA loan amount and total monthly payment
    total_fha_loan_amount = mortgage_amount + upfront_mip
    total_monthly_payment = monthly_payment + monthly_mip

    total_loan_cost = total_monthly_payment * loan_term_months + upfront_mip
    return (
        upfront_mip,
        monthly_payment,
        monthly_mip,
        total_fha_loan_amount,
        total_monthly_payment,
        total_loan_cost,
    )


def roth_ira(
    principal: float,
    interest_rate: float,
    years: int,
    tax_rate: float,
    annual_contribution: float,
):
    roth_ira_balance = principal
    taxable_balance = principal
    for _ in range(years):
        roth_ira_balance = (roth_ira_balance + annual_contribution) * (
            1 + percent_to_decimal(interest_rate)
        )
        taxable_balance = (taxable_balance + annual_contribution) * (
            1 + percent_to_decimal(interest_rate) *
            (1 - percent_to_decimal(tax_rate))
        )
    return math.ceil(roth_ira_balance), math.ceil(taxable_balance)


# Function to calculate Enterprise Value
def calculate_enterprise_value(
    share_price: float,
    fully_diluted_shares_outstanding: int,
    total_debt: float,
    preferred_stock: float,
    non_controlling_interest: float,
    cash_and_cash_equivalents: float,
):
    equity_value = share_price * fully_diluted_shares_outstanding
    enterprise_value = (
        equity_value
        + total_debt
        + preferred_stock
        + non_controlling_interest
        - cash_and_cash_equivalents
    )
    return round(enterprise_value, 2)


# Function to convert salary_amount amounts to their corresponding values based on payment frequency.
def salary_calculate(
    salary_amount: float, payment_frequency: str, hours_per_day: int, days_per_week: int
):
    # Get the total salary of the corresponding frequency
    salaries = {
        "hourly": {
            # Assuming there are 4.333333 weeks in a month (in real-time), 13 week quarters in a year & 52 weeks in a year
            "hourly": salary_amount,
            "daily": salary_amount * hours_per_day,
            "weekly": salary_amount * hours_per_day * days_per_week,
            "bi-weekly": salary_amount * hours_per_day * days_per_week * 2,
            "monthly": salary_amount * hours_per_day * days_per_week * 4.333333,
            "quarterly": salary_amount * hours_per_day * days_per_week * 13,
            "yearly": salary_amount * hours_per_day * (days_per_week * 52),
        },
        "daily": {
            # Assuming there are 4.333333 weeks in a month, and 3 months in a quarter & 52 working weeks
            "hourly": salary_amount / hours_per_day,
            "daily": salary_amount,
            "weekly": salary_amount * days_per_week,
            "bi-weekly": salary_amount * days_per_week * 2,
            "monthly": salary_amount * (days_per_week * 4.333333),
            "quarterly": salary_amount * days_per_week * (4.333333 * 3),
            "yearly": salary_amount * days_per_week * 52,
        },
        "weekly": {
            # Assuming there are 4.333333 weeks in a month, 13 weeks in a quarter & 2 weeks make up a bi-week
            "hourly": salary_amount / (hours_per_day * days_per_week),
            "daily": salary_amount / days_per_week,
            "weekly": salary_amount,
            "bi-weekly": salary_amount * 2,
            "monthly": salary_amount * 4.333333,
            "quarterly": salary_amount * 13,
            "yearly": salary_amount * 52,
        },
        "bi-weekly": {
            # Assuming there are 2 bi-weekly periods in a month & round(6.5223214,1) bi-weekly periods in a quarter
            "hourly": salary_amount / (hours_per_day * days_per_week * 2),
            "daily": salary_amount / (days_per_week * 2),
            "weekly": salary_amount / 2,
            "bi-weekly": salary_amount,
            "monthly": salary_amount * 2,
            "quarterly": salary_amount * 6.5,
            "yearly": salary_amount * 26,
        },
        "monthly": {
            # Assuming there are 2 bi-weekly periods, 4.333333 weeks in a month & 3 months in a quarter
            "hourly": salary_amount / (hours_per_day * days_per_week * 4.333333),
            "daily": salary_amount / (days_per_week * 4.333333),
            "weekly": salary_amount / 4.333333,
            "bi-weekly": salary_amount / (4.333333 / 2),
            "monthly": salary_amount,
            "quarterly": salary_amount * 3,
            "yearly": salary_amount * 12,
        },
        "quarterly": {
            # Assuming there are 3 months, 13 weeks in a quarter, and 4 quarters in a year
            "hourly": salary_amount / ((13 * days_per_week) * hours_per_day),
            "daily": salary_amount / (13 * days_per_week),
            "weekly": salary_amount / 13,
            "bi-weekly": salary_amount / 13 * 2,
            "monthly": salary_amount / 3,
            "quarterly": salary_amount,
            "yearly": salary_amount * 4,
        },
        "yearly": {
            # Assuming there are 4 quarters, 12 months, 26 bi-weeks & 52 weeks in a year.
            "hourly": salary_amount / (hours_per_day * days_per_week * 52),
            "daily": salary_amount / (52 * days_per_week),
            "weekly": salary_amount / 52,
            "bi-weekly": salary_amount / 26,
            "monthly": salary_amount / 12,
            "quarterly": salary_amount / 4,
            "yearly": salary_amount,
        },
    }

    if payment_frequency not in salaries.keys():
        return {"error": "Invalid payment frequency."}

    # Get the rounded off values for the salaries (to 2 decimal places)
    return {k: round(v, 2) for k, v in salaries[payment_frequency].items()}


# Function to Calculate Personal Loan and visualization monthly payments (schedule)
# interest_rate - % per year; loan_term - years; loan_start_date - format %B %Y (February 2023)
def personal_loan(
    loan_amount: float, interest_rate: float, loan_term_years: int, loan_start_date: str
):
    loan_term_month = loan_term_years * 12
    interest_rate_month = percent_to_decimal(interest_rate) / 12
    monthly_payment = (
        loan_amount
        * interest_rate_month
        / (1 - (1 + interest_rate_month) ** (-loan_term_month))
    )
    total_cost_loan = monthly_payment * loan_term_month
    total_interest_paid = total_cost_loan - loan_amount

    dframe = pd.DataFrame(
        columns=[
            "Date",
            "Principal",
            "Interest",
            "Remaining balance",
            "Principal Total",
            "Interest Total",
        ]
    )
    date = datetime.datetime.strptime(loan_start_date, "%B %Y")
    principal_total = interest_total = 0
    remain_balance = loan_amount
    for i in range(loan_term_years * 12):
        date = date + relativedelta(months=1)
        interest = remain_balance * percent_to_decimal(interest_rate) / 12
        interest_total = interest_total + interest
        principal = monthly_payment - interest
        principal_total = principal_total + principal
        remain_balance = remain_balance - principal
        dframe.loc[i, :] = (
            date.strftime("%B %Y"),
            round(principal, 2),
            round(interest, 2),
            round(remain_balance, 2),
            round(principal_total, 2),
            round(interest_total, 2),
        )

    return {
        "Monthly payment": monthly_payment,
        "Total interest paid": total_interest_paid,
        "Total cost loan": total_cost_loan,
        "Schedule": dframe.to_json(),
    }


# Function to calculate lump-sum mutual fund investment
def calculate_lumpsum(principal, interest_rate, years):
    total_amount = principal * \
        ((1 + percent_to_decimal(interest_rate)) ** years)
    interest_earned = total_amount - principal
    return (total_amount, interest_earned)


def main():
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate (%): "))
    years = int(input("Enter the number of years: "))
    total_amount, interest_earned = calculate_lumpsum(
        principal, interest_rate, years)
    print(f"Total Amount: Rs.{total_amount:.2f}")
    print(f"Interest Earned: Rs.{interest_earned:.2f}")


if __name__ == "__main__":
    main()


# Function to calculate FHA loan
def calculate_fha_loan():
    # Get user input for home price, down payment percentage, loan term, interest rate, and FHA annual MIP
    home_price = float(input("Enter home price: "))
    down_payment_percentage = float(input("Enter down payment percentage: "))
    loan_term_years = float(input("Enter loan term (years): "))
    interest_rate = float(input("Enter interest rate (%): "))
    fha_annual_mip_percentage = float(
        input("Enter FHA annual MIP percentage (%): "))

    # Calculate down payment and base loan amount
    down_payment = home_price * percent_to_decimal(down_payment_percentage)
    base_loan_amount = home_price - down_payment

    # Calculate upfront MIP and monthly MIP
    upfront_mip_percentage = 1.75
    upfront_mip = base_loan_amount * percent_to_decimal(upfront_mip_percentage)
    monthly_mip_percentage = percent_to_decimal(fha_annual_mip_percentage) / 12
    monthly_mip = base_loan_amount * monthly_mip_percentage

    # Calculate monthly mortgage payment
    loan_term_months = loan_term_years * 12
    monthly_interest_rate = percent_to_decimal(interest_rate) / 12
    monthly_payment = (
        base_loan_amount
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** loan_term_months
    ) / ((1 + monthly_interest_rate) ** loan_term_months - 1)

    # Calculate total FHA loan amount and total monthly payment
    total_fha_loan_amount = base_loan_amount + upfront_mip
    total_monthly_payment = monthly_payment + monthly_mip

    # Calculate total cost of loan
    total_cost_of_loan = total_monthly_payment * loan_term_months + upfront_mip

    # Print output
    print(f"\nDown payment: ${down_payment:.2f}")
    print(f"FHA base loan amount: ${base_loan_amount:.2f}")
    print(f"FHA upfront MIP: ${upfront_mip:.2f}")
    print(f"Monthly mortgage payment: ${monthly_payment:.2f}")
    print(f"Monthly MIP: ${monthly_mip:.2f}")
    print(f"Total FHA loan amount: ${total_fha_loan_amount:.2f}")
    print(f"Total monthly payment: ${total_monthly_payment:.2f}")
    print(f"Total cost of loan: ${total_cost_of_loan:.2f}")


# Function to Calculate Refinance and side-by-side comparison with existing loan
# interest_rate - % per year; loan_term - years
def refinance_calculator(
    current_loan_amount: float,
    current_interest_rate: float,
    current_loan_term_years: int,
    time_remaining_years: int,
    new_interest_rate: float,
    new_loan_term_years: int,
    cash_out_amount: float,
):
    loan_term_month = current_loan_term_years * 12
    interest_rate_month = percent_to_decimal(current_interest_rate) / 12
    current_monthly_payment = (
        current_loan_amount
        * interest_rate_month
        / (1 - (1 + interest_rate_month) ** (-loan_term_month))
    )
    term_years_pass = loan_term_month - 12 * time_remaining_years
    balance_left_loan = (
        current_loan_amount * (1 + interest_rate_month) ** (term_years_pass)
    ) - (
        current_monthly_payment
        * ((1 + interest_rate_month) ** term_years_pass - 1)
        / interest_rate_month
    )
    new_loan_amount = balance_left_loan - cash_out_amount
    current_total_cost_left = current_monthly_payment * 12 * time_remaining_years
    current_total_interest_paid = current_total_cost_left - balance_left_loan

    new_credit = personal_loan(
        new_loan_amount,
        new_interest_rate,
        new_loan_term_years,
        datetime.datetime.now().strftime("%B %Y"),
    )

    return {
        "Balance left on loan": balance_left_loan,
        "New loan amount": new_loan_amount,
        "Current monthly payment": current_monthly_payment,
        "New monthly payment": new_credit["Monthly payment"],
        "Monthly savings": current_monthly_payment - new_credit["Monthly payment"],
        "Current left interest paid": current_total_interest_paid,
        "New total interest paid": new_credit["Total interest paid"],
        "Total interest saving": current_total_interest_paid
        - new_credit["Total interest paid"],
        "Current total cost left": current_total_cost_left,
        "New total cost loan": new_credit["Total cost loan"],
        "Total cost saving": current_total_cost_left - new_credit["Total cost loan"],
    }


# calculate_fha_loan()

# Function to compute any one of the following, given inputs for the remaining two: sales price, commission rate, or commission for a simple percentage commission structure.


def commission_calc(
    sales_price: float = None, commission_rate: float = None, commission: float = None
):
    if sales_price == None and commission_rate != None and commission != None:
        output = 100 * commission / commission_rate
    elif sales_price != None and commission_rate == None and commission != None:
        output = 100 * commission / sales_price
    elif sales_price != None and commission_rate != None and commission == None:
        output = percent_to_decimal(sales_price * commission_rate)

    return output


# Function to calculate total college fee of one year assuming full tuition fee is being paid.
def college_cost(
    book_cost: float,
    college_tuition: float,
    Devices: float,
    travel_expenses: float,
    hostel_charges: float,
    mess_fee: float,
    miscellaneous: float,
):
    Total_cost_ofOneYear = (
        book_cost
        + college_tuition
        + Devices
        + (travel_expenses * 12)
        + (hostel_charges * 12)
        + (mess_fee * 12)
        + (miscellaneous * 12)
    )
    return Total_cost_ofOneYear


def future_sip(
    interval_investment: float, rate_of_return: float, number_of_payments: int
):
    interest = percent_to_decimal(rate_of_return) / 12
    value = (
        interval_investment
        * ((1 + interest) ** number_of_payments - 1)
        * (1 + interest)
        / interest
    )
    return value


def calculate_pension(
    monthty_investment_amount: float,
    no_of_years: float,
    annuity_rates: float,
    annuity_purchased: float,
    yearly_interest_rates: float,
):
    total_corpus = 0
    yearly_pension_amount = 12 * monthty_investment_amount
    for i in range(0, no_of_years + 1):
        yearly_pension_amount += yearly_pension_amount * percent_to_decimal(
            yearly_interest_rates
        )
        total_corpus += yearly_pension_amount
    total_corpus = round(total_corpus, 2)
    annuity_pension = total_corpus * percent_to_decimal(annuity_purchased)
    lump_sum_pension = total_corpus - annuity_pension
    monthly_pension = round(percent_to_decimal(
        annuity_pension * annuity_rates) * 12, 2)
    return (total_corpus, lump_sum_pension, monthly_pension)


# Function to Calculate Diluted EPS
def diluted_eps(net_income, weighted_avg_shares, dilutive_securities):
    diluted_eps = net_income / (weighted_avg_shares + dilutive_securities)
    return diluted_eps


# Function to calculate maturity value of a Fixed deposit.
def fixed_deposit_maturity(
    principle_amount: float, years: int, compounding: str, roi: float
):
    types_of_componding = {"yearly": 1,
                           "halfyearly": 2, "quaterly": 4, "monthly": 12}
    if compounding in types_of_componding.keys():
        n = types_of_componding[compounding]
        A = principle_amount * \
            (1 + (percent_to_decimal(roi) / n)) ** (n * years)
        return round(A, 2)


# Function to calculate maturity value of a Recurring deposit.
def recurring_deposit_maturity(
    principle_amount: float, years: int, compounding: str, roi: float
):
    types_of_componding = {"yearly": 1,
                           "halfyearly": 2, "quaterly": 4, "monthly": 12}
    if compounding in types_of_componding.keys():
        months = years * 12
        n = types_of_componding[compounding]
        res = 0.0
        for i in range(1, months + 1):
            res += principle_amount * (1 + (percent_to_decimal(roi) / n)) ** (
                n * (i / 12)
            )
        return round(res, 2)


# Function for calculating annual income neended during retiremnet period
def calculate_retirement_goals(
    retirement_age: int,
    annual_retirement_expenses: int,
    inflation_rate: float,
    annual_retirement_income: int,
    current_age: int,
):
    retirement_duration = retirement_age - current_age
    amount = (annual_retirement_expenses - annual_retirement_income) * (
        1 + inflation_rate
    ) ** retirement_duration
    return amount


# Function to calculate Student loan and monthly emi for the same
def student_loan(principal: int, tenure: int, interest_rate: float):
    monthly_interest_rate = percent_to_decimal(interest_rate) / 12
    total_months = tenure * 12
    n = principal * monthly_interest_rate * \
        pow(1 + monthly_interest_rate, total_months)
    d = pow(1 + monthly_interest_rate, total_months) - 1
    emi = n / d
    total_amount = emi * total_months
    return int(emi), int(total_amount)


# Function to Calculate Return of Investment on some equity funds
def calculate_roi_equity_funds(amount_invested, amount_returned, tenure):
    roi_equity_funds = (amount_returned - amount_invested) / amount_invested
    annualized_roi = (1 + (amount_returned / amount_invested)
                      ) ** (1 / tenure) - 1
    return (decimal_to_percent(roi_equity_funds), decimal_to_percent(annualized_roi))


# Function to calculate GST (Goods and Service Tax)
def calculate_gst(price, gst_rate):
    gst_amount = price * percent_to_decimal(gst_rate)
    total_price = price + gst_amount
    return gst_amount, total_price


# function to calculate marketcap


def calculate_market_cap(
    current_market_share_price, total_number_of_shares_outstanding
):
    market_cap = current_market_share_price * total_number_of_shares_outstanding
    return market_cap


# Calculate Annual Debt Service Coverage Ratio (ADSCR)
def annual_debt_service_coverage_ratio(
    net_operating_cost: float,
    depreciation: float,
    non_cash_expenses: float,
    annual_debt_service: float,
):
    adscr_ratio = (
        net_operating_cost + depreciation + non_cash_expenses
    ) / annual_debt_service
    return adscr_ratio


# Function to Calculate Value Added Tax (VAT)
def calculate_vat():
    while True:
        try:
            price = float(input("Enter the price: "))
            vat_rate = float(input("Enter the VAT rate (%): "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    excluding_vat = price / (1 + percent_to_decimal(vat_rate))
    including_vat = price
    vat_amount = price - excluding_vat

    print(f"Price (excluding VAT): {excluding_vat:.2f}")
    print(f"Price (including VAT): {including_vat:.2f}")
    print(f"VAT Amount: {vat_amount:.2f}")


# Function to calculate BEY (Bond Equivalent Yield)
def calculate_bond_equivalent_yield(face_value, purchase_price, days_to_maturity):
    roi = (face_value - purchase_price) / purchase_price
    bey = roi * 365 / days_to_maturity
    return bey


# function to calculate max_loan_amount for calculating loan affordability for a particular person
def calculate_max_loan_amount(income, expenses, loan_term, interest_rate):
    monthly_income = income / 12
    monthly_expenses = expenses / 12

    loan_factor = 1 - (1 + percent_to_decimal(interest_rate)) ** -loan_term
    max_loan_amount = (
        (monthly_income - monthly_expenses)
        * loan_factor
        / percent_to_decimal(interest_rate)
    )

    return max_loan_amount


# Function to calculate BVPS (Book value per share)
def calculate_bvps(stockholders_equity, preferred_stock, average_outstanding_shares):
    """
    Calculate the book value per share using the given values.

    Args:
        stockholders_equity (float): Total stockholders' equity.
        preferred_stock (float): Value of preferred stock.
        average_outstanding_shares (float): Average number of outstanding shares.

    Returns:
        float: The book value per share.
    """
    book_value = (stockholders_equity - preferred_stock) / \
        average_outstanding_shares
    return book_value


# function to calculate the gratuity amount
def calculate_gratuity(
    last_salary: float, tenure_years: int, tenure_months: int
) -> float:
    if tenure_months >= 12:
        raise Exception
    round_off = 1 if tenure_months > 6 else 0
    tenure = tenure_years + round_off
    if tenure < 5:
        return 0
    return round((15 * last_salary * tenure) / 26)


# Function to calculate Personal Savings
def personal_savings(init: int, monthly: int, tenure: float):
    a = monthly * 12 * tenure
    total_amount = a + init
    return total_amount


def accrint(
    issue_date: str,
    settlement_date: str,
    rate: float,
    par: float,
    frequency: int = 1,
    basis: int = 0,
):
    """
    A function to calculate the accrued interest for a security that pays periodic interest.

    Args:
        issue_date: str (MM-DD-YYYY)
        settlement_date: str (MM-DD-YYYY)
        rate: float (indicates rate in percent)
        par: float
        frequency: int
        basis: int (between 0 and 4)

    Returns:
        acrrued_interest : float

    Examples:
        accrint("01-01-2012","15-02-2012",5.25,5000,4,3)
        >> 32.363013698630134
    """
    rate = rate / 100
    issue_date = datetime.datetime.strptime(issue_date, "%d-%m-%Y")
    settlement_date = datetime.datetime.strptime(settlement_date, "%d-%m-%Y")
    # Validate basis value
    if basis not in range(5):
        raise ValueError(
            "Invalid basis value. Expected a value between 0 and 4.")

    # Calculate the number of interest periods based on the specified basis
    if basis == 0:  # US (NASD) 30/360 basis
        periods = (settlement_date.year - issue_date.year) * frequency + (
            settlement_date.month - issue_date.month
        ) / 12 * frequency
    elif basis == 1:  # Actual/actual basis
        periods = (settlement_date - issue_date).days / 365 * frequency
    elif basis == 2:  # Actual/360 basis
        periods = (settlement_date - issue_date).days / 360 * frequency
    elif basis == 3:  # Actual/365 basis
        periods = (settlement_date - issue_date).days / 365 * frequency
    elif basis == 4:  # European 30/360 basis
        periods = (settlement_date.year - issue_date.year) * frequency + (
            settlement_date.month - issue_date.month
        ) / 12 * frequency
        if settlement_date.day == 31:
            periods -= 1 / 12 * frequency

    # Calculate the accrued interest
    accrint = par * rate * periods / frequency

    return accrint


def calculate_mortgage(principal, interest_rate, years, down_payment=0, property_tax_rate=0, insurance_rate=0):
    """
    Calculate the monthly mortgage payment and provide additional information about the mortgage.

    Args:
        principal (float): The principal amount (loan amount).
        interest_rate (float): The annual interest rate (in percentage).
        years (int): The number of years for the mortgage.
        down_payment (float, optional): The down payment amount (default: 0).
        property_tax_rate (float, optional): The annual property tax rate (in percentage) (default: 0).
        insurance_rate (float, optional): The annual insurance rate (in percentage) (default: 0).

    Returns:
        dict: A dictionary containing the monthly mortgage payment and additional mortgage information.
    """
    monthly_interest_rate = interest_rate / 100 / 12  # Monthly interest rate
    num_payments = years * 12  # Total number of payments

    # Calculate the loan amount after down payment
    loan_amount = principal - down_payment

    # Calculate the monthly mortgage payment
    monthly_payment = (
        loan_amount
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** num_payments
        / ((1 + monthly_interest_rate) ** num_payments - 1)
    )

    # Calculate the total payment over the mortgage term
    total_payment = monthly_payment * num_payments

    # Calculate the total property tax over the mortgage term
    total_property_tax = property_tax_rate / 100 * principal * years

    # Calculate the total insurance cost over the mortgage term
    total_insurance_cost = insurance_rate / 100 * principal * years

    # Calculate the total cost of the mortgage (principal + interest + property tax + insurance)
    total_cost = total_payment + total_property_tax + total_insurance_cost

    # Calculate the loan-to-value (LTV) ratio
    ltv_ratio = (loan_amount / principal) * 100

    # Create a dictionary with the mortgage information
    mortgage_info = {
        "monthly_payment": monthly_payment,
        "total_payment": total_payment,
        "total_property_tax": total_property_tax,
        "total_insurance_cost": total_insurance_cost,
        "total_cost": total_cost,
        "loan_to_value_ratio": ltv_ratio,
    }

    return mortgage_info


def calculate_social_security(birth_date, earnings, retirement_age):
    """
    Calculate the estimated monthly Social Security benefits based on the birth date, earnings, and retirement age.

    Args:
        birth_date (str): The birth date in the format 'YYYY-MM-DD'.
        earnings (float): The average indexed monthly earnings.
        retirement_age (int): The desired retirement age.

    Returns:
        float: The estimated monthly Social Security benefits.
    """
    birth_date = pd.to_datetime(birth_date)
    current_date = pd.to_datetime('today')
    age = pd.Timedelta(current_date - birth_date).days / 365.25

    # Determine the full retirement age based on the year of birth
    if birth_date.year < 1938:
        full_retirement_age = 65
    elif birth_date.year < 1943:
        full_retirement_age = 65 + (birth_date.year - 1937) * 2
    else:
        full_retirement_age = 66

    # Calculate the reduction factor for claiming benefits before full retirement age
    if retirement_age < full_retirement_age:
        reduction_factor = 1 - \
            ((full_retirement_age - retirement_age) * 5 / 900)
    else:
        # No reduction if retirement age is at or after full retirement age
        reduction_factor = 1.0

    # Calculate the primary insurance amount (PIA)
    pia = earnings * reduction_factor

    # Calculate the estimated monthly Social Security benefits
    monthly_benefits = pia / 12

    # Predict future benefits
    years_to_retirement = retirement_age - age
    future_benefits = monthly_benefits * (1 + 0.02) ** years_to_retirement

    return monthly_benefits, future_benefits


# Function to calculate net profit margin
def calculate_net_profit_margin(
        revenue: float,
        cost_of_goods_sold: float,
        operating_expenses: float,
        other_expenses: float,
        interest: float,
        taxes: float):
    net_profit_margin = ((revenue-cost_of_goods_sold -
                         operating_expenses-other_expenses-interest-taxes)/revenue)*100
    return net_profit_margin

# Function to calculate expected return of portfolio


def calculate_expected_return_of_portfolio(
        no_of_investments: int,
        investment_amount: list,
        rate_of_return: list):
    total_value_of_portfolio = 0
    for i in range(no_of_investments):
        total_value_of_portfolio += investment_amount[i]

    weight_of_investment = []
    for i in range(no_of_investments):
        weight_of_investment.append(investment_amount/total_value_of_portfolio)

    expected_return_of_portfolio = 0
    for i in range(no_of_investments):
        expected_return_of_portfolio += weight_of_investment[i] * \
            rate_of_return[i]

    return expected_return_of_portfolio

# Function to calculate net annual salary


def calculate_salary(base: int,
                     jb: int,
                     stock: int,
                     pb: int,
                     bonus: int,
                     ptax: int,
                     deduction: int):
    total_amount = (base*12)+jb+stock+pb+bonus
    tax = (ptax/100)*total_amount
    ctc = total_amount-tax-deduction
    return ctc

# function to calculate the Sharpe ratio in Python

def loan_to_value_ratio(
        loan_amount: float,
        value_of_collateral: float):
    ratio = (loan_amount / value_of_collateral) * 100
    return ratio

# Function to calculate post tax return percentage


def calculate_post_tax_return_percentage(tax_rate_percentage: float,
                                         annual_net_income: float,
                                         initial_cost_of_investment: float
                                         ):
    rate_of_return_percentage = (
        annual_net_income / initial_cost_of_investment)*100
    post_tax_return_percentage = rate_of_return_percentage - \
        (rate_of_return_percentage * tax_rate_percentage)/100

    return post_tax_return_percentage

# Function to calculate the Treynor Ratio in python


def calculate_treynor_ratio(returns, risk_free_rate, beta):
    """
    Calculates the Treynor Ratio for a given set of returns, risk-free rate, and beta.
    Parameters:
    - returns (float or list): The returns of the investment/portfolio.
      If a single value is provided, it is assumed to be the total return.
      If a list is provided, it is assumed to be a series of periodic returns.
    - risk_free_rate (float): The risk-free rate of return.
    - beta (float): The beta coefficient of the investment/portfolio.
    Returns:
    - treynor_ratio (float): The calculated Treynor Ratio.
    Note:
    The Treynor Ratio is calculated as (returns - risk-free rate) / beta.
    """

    if isinstance(returns, list):
        # Calculate the total return if periodic returns are provided
        returns = sum(returns)

    treynor_ratio = (returns - risk_free_rate) / beta
    return treynor_ratio


# Example usage
returns = 0.1  # Total return of the investment/portfolio
risk_free_rate = 0.05  # Risk-free rate of return
beta = 1.2  # Beta coefficient

treynor_ratio = calculate_treynor_ratio(returns, risk_free_rate, beta)
print(f"Treynor Ratio: {treynor_ratio}")

# Function to Calculate Free Cash Flow to Equity


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

    net_income = total_revenues - total_expenses,
    depreciation_and_amortization = initial_cost_of_asset / lifetime_of_asset,
    capEx = change_in_PPE + current_depreciation,
    change_in_working_capital = current_assets - current_liabilities,
    net_borrowing = amount_a_company_borrows - debt_it_repays,

    fcfe = net_income + depreciation_and_amortization - \
        capEx - change_in_working_capital + net_borrowing
    return fcfe

#Function to Calculate Capital Gains Yield

def capital_gains_yield(
	inital_price : float,
	price_after_first_period : float):
    '''
        Capital Gains Yield used to calculate a company's total stock return 
        if a company does not pay dividends. 
        inital_price indicates Inital Stock Price,
        price_after_first_period indicates Stock Price after first period
    '''
    gains_yield = ((price_after_first_period - inital_price) / inital_price) * 100
    return gains_yield

#function to calculate macaulay duration
def calculate_macaulay_duration(face_value : float, coupon_rate : float, dt : int, month : int, year : int, coupon_frequency : int, discount_rate : float):
    cash_flows = []
    maturity_date = datetime.date(year, month, dt)
    years_to_maturity = (maturity_date - datetime.date.today()).days / 365.25

    # Calculate the coupon payment amount
    coupon_payment = face_value * coupon_rate / coupon_frequency

    # Generate the cash flows
    for i in range(1, int(years_to_maturity * coupon_frequency) + 1):
        if i == int(years_to_maturity * coupon_frequency):
            # Last period's cash flow includes the final coupon payment plus the face value
            cash_flows.append(coupon_payment + face_value)
        else:
            cash_flows.append(coupon_payment)

    duration = 0.0
    present_value = 0.0
    
    
    for i, cash_flow in enumerate(cash_flows):
        present_value += cash_flow / (1 + discount_rate) ** (i + 1)
        duration += (i + 1) * (cash_flow / (1 + discount_rate) ** (i + 1))

    return round((duration / present_value)/ coupon_frequency, 2)

# Function to calculate Financial Leverage
def calculate_financial_leverage(total_assets : float,
                                 total_liabilities : float,
                                 short_term_debt : float,
                                 long_term_debt : float
                                 ):
    debt = short_term_debt + long_term_debt

    shareholder_equity = total_assets - total_liabilities

    financial_leverage = debt / shareholder_equity

    return financial_leverage

# Function to estimate the portfolio return using Monte Carlo simulation.
def portfolio_return_monte_carlo(principal, expected_return_range_start,expected_return_range_end, volatility_range_start,volatility_range_end, num_simulations):
    portfolio_returns = np.zeros(int(num_simulations))

    min_return, max_return = expected_return_range_start, expected_return_range_end
    min_volatility, max_volatility = volatility_range_start, volatility_range_end

    for i in range(int(num_simulations)):
        random_return = np.random.uniform(min_return, max_return)
        random_volatility = np.random.uniform(min_volatility, max_volatility)
        random_returns = np.random.normal(random_return, random_volatility)
        portfolio_value = principal * np.prod(1 + random_returns)
        portfolio_returns[i] = (portfolio_value - principal) / principal

    portfolio_stats = {
        "Portfolio Returns": portfolio_returns.tolist(),
        "Average Return": np.mean(portfolio_returns),
        "Standard Deviation": np.std(portfolio_returns),
        "Min Return": np.min(portfolio_returns),
        "Max Return": np.max(portfolio_returns),
        "Positive Returns": len(portfolio_returns[portfolio_returns > 0]),
        "Negative Returns": len(portfolio_returns[portfolio_returns < 0])
    }

    return portfolio_stats

# Function to calculate Accounts Payable Turnover Ratio
def accounts_payable_turnover_ratio(total_supply_purchases: float,
                                    beginning_accounts_payable: float,
                                    ending_accounts_payable: float):
    
    average_accounts_payable = (beginning_accounts_payable + ending_accounts_payable)/2
    ap_turnover_ratio = total_supply_purchases/average_accounts_payable

    return ap_turnover_ratio


# Function to Calculate Capitalization Rate 

def capitalization_rate(
        rental_income: float,
        amenities: float,
        propertyManagement: float,
        propertyTaxes:float,
        insurance: float,
        current_market_value: float):
  annual_income = rental_income + amenities
  expenses = propertyManagement + propertyTaxes + insurance
  net_operating_income = annual_income - expenses
  rate = (net_operating_income / current_market_value) * 100
  return rate

#Function to calculate net worth
def net_worth_calculation(assets: float, liabilities: float, loans: float, mortgages: float):
 
    total_liabilities = liabilities + loans + mortgages
    net_worth = assets - total_liabilities
    return {
            "Tag": "Net Worth",
            "Assets": assets,
            "Liabilities": total_liabilities,
            "Net Worth": net_worth,
        }


def capm_calculation(risk_free_return:float, sensitivity:float, expected_market_return:float):
    expected_asset_return = risk_free_return + sensitivity * (expected_market_return - risk_free_return)
    return expected_asset_return

# Function to Calculate Debt Service Coverage Ratio. 

def debt_service_coverage_ratio(revenue: float, operating_expenses: float, interest: float, 
tax_rate: float, principal: float):
    tax_rate = tax_rate / 100
    net_operating_income = revenue - operating_expenses
    total_debt_service = (interest * (1 - tax_rate)) + principal
    ratio = net_operating_income / total_debt_service
    return ratio 

#Function to calculate profit percentage
def profit_percentage(profit: float, cost_price: float):
    profit_percent = (profit / cost_price) * 100
    return profit_percent

#Function to calculate loss percentage
def loss_percentage(loss: float, cost_price: float):
    loss_percent = (loss / cost_price) * 100
    return loss_percent

## Function to Calculate Defensive Interval Ratio

def defensive_interval_ratio(cash: float, marketable_securities: float,
net_receivables: float, annual_operating_expenses: float, non_cash_charges: float):
	current_assets = cash + marketable_securities + net_receivables	
	daily_operational_expenses  = (annual_operating_expenses - non_cash_charges) / 365
	ratio = current_assets / daily_operational_expenses
	return ratio

# Function to Calculate Debt Service Coverage Ratio. 

def rate_of_return(initial_investment: float, final_value: float ):
    rate_of_return = ((final_value - initial_investment) / initial_investment) * 100
    return rate_of_return 

  ## Function to Calculate Financial Assest Ratio

def calculate_financial_asset_ratios(current_assets, current_liabilities, total_debt, total_equity, net_income, total_revenue, total_assets):

    current_ratio = current_assets / current_liabilities
    debt_to_equity_ratio = total_debt / total_equity
    return_on_assets = net_income / total_assets
    return_on_equity = net_income / total_equity
    profit_margin = net_income / total_revenue

    ratios = {
        "current_ratio": current_ratio,
        "debt_to_equity_ratio": debt_to_equity_ratio,
        "return_on_assets": return_on_assets,
        "return_on_equity": return_on_equity,
        "profit_margin": profit_margin
    }

    return ratios

# Function to Calculate Cash Conversion Cycle

def cash_conversion_cycle(beginning_inventory: float, ending_inventory: float, beginning_receivables: float, 
ending_receivables: float, beginning_payable: float, ending_payable: float, cost_of_goods_sold: float, 
net_credit_sales: float):
	average_inventory = beginning_inventory - ending_inventory / 2
	average_receivables = beginning_receivables - ending_receivables / 2
	average_payable = beginning_payable - ending_payable / 2
	days_of_inventory_outstanding = (average_inventory / cost_of_goods_sold) * 365 
	days_of_sales_outstanding = (average_receivables / net_credit_sales) * 365
	days_of_payables_outstanding = (average_payable / cost_of_goods_sold / 365)
	ccc = days_of_inventory_outstanding + days_of_sales_outstanding - days_of_payables_outstanding
	return ccc

# Function to Calculate Policy Premium. 

def calculate_policy_premium_ratios(premiums_collected, claims_paid, commissions_paid, operating_expenses):
    loss_ratio = (claims_paid / premiums_collected) * 100
    expense_ratio = ((commissions_paid + operating_expenses) / premiums_collected) * 100
    combined_ratio = loss_ratio + expense_ratio
    profit_margin = 100 - combined_ratio

    ratios = {
        "loss_ratio": loss_ratio,
        "expense_ratio": expense_ratio,
        "combined_ratio": combined_ratio,
        "profit_margin": profit_margin
    }

    return ratios
# Function to Calculate Price Elasticity for demand Calculator

def calculate_price_elasticity(initial_price: float, final_price: float, initial_quantity: float, final_quantity: float):
    percentage_change_price = (final_price - initial_price) / initial_price
    percentage_change_quantity = (final_quantity - initial_quantity) / initial_quantity
    price_elasticity = percentage_change_quantity / percentage_change_price

    return price_elasticity

# Function to Calculate Average Payment Period

def average_payment_period(beginning_accounts_payable: float, ending_accounts_payable: float,
total_credit_purchases: float):
    average_accounts_payable = (beginning_accounts_payable + ending_accounts_payable) / 2
    app = average_accounts_payable / (total_credit_purchases / 365)
    return app

# Function to Saving Goal Calculator

def saving_goal(current_savings: float, monthly_contributions: float, interest_rate: float, goal_amount: float):
    savings_ratio = current_savings / goal_amount
    return savings_ratio

# Function to calculate Modified Internal Rate of Return (MIRR)

def calculate_modified_internal_rate_of_return(ending_cash_flow: float,
                                                initial_cash_flow: float,
                                                number_of_periods: int):
    mirr = ((ending_cash_flow / initial_cash_flow) ** (1 / number_of_periods)) - 1
    return mirr*100

# Function to Calculate Interest Coverage Ratio

def interest_coverage_ratio(revenue:float, cost_of_goods_services:float, operating_expenses:float, 
interest_expense:float):
	EBIT = revenue - cost_of_goods_services - operating_expenses
	ratio = EBIT / interest_expense 
	return ratio


# Function to Calculate Tax Bracket Calculator

def tax_bracket_calculator(income:float, filing_status:str):
        tax_brackets = {
            'single': {0: 0.10, 9875: 0.12, 40125: 0.22, 85525: 0.24, 163300: 0.32, 207350: 0.35, 518400: 0.37},
            'married_joint': {0: 0.10, 19750: 0.12, 80250: 0.22, 171050: 0.24, 326600: 0.32, 414700: 0.35, 622050: 0.37},
            'head_of_household': {0: 0.10, 14100: 0.12, 53700: 0.22, 85500: 0.24, 163300: 0.32, 207350: 0.35, 518400: 0.37}
        }

        if filing_status not in tax_brackets:
            raise ValueError("Invalid filing status.")

        applicable_brackets = tax_brackets[filing_status]
        tax_liability = 0
        remaining_income = income

        for bracket, tax_rate in applicable_brackets.items():
            if remaining_income <= bracket:
                tax_liability += remaining_income * tax_rate
                break
            else:
                taxable_income_in_bracket = bracket - max(0, income - remaining_income)
                tax_liability += taxable_income_in_bracket * tax_rate
                remaining_income -= taxable_income_in_bracket

        tax_ratio = tax_liability / income

        return {"Tax Ratio": "{:.2%}".format(tax_ratio)}

# Function to Calculate Margin of Safety

def margin_of_safety(current_sales:float, break_even_point: float):
	margin = ((current_sales - break_even_point) / current_sales) * 100
	return margin
