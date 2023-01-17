import math
import numpy as np
import pandas as pd

# Function to Calculate Simmple Interest Rate
def simple_interest_rate(amount_paid: float, principle_amount: float, months: int):
    term = months / 12
    interest_paid = amount_paid - principle_amount
    rate = (interest_paid * 100) / (principle_amount * term)
    return rate


# Function to Calculate Loan Emi
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    monthly_rate = annual_rate / 1200
    emi = (principle_amount * monthly_rate * (1 + monthly_rate) ** months) / (
        ((1 + monthly_rate) ** months - 1)
    )
    return emi


def future_sip(
    interval_investment: float, rate_of_return: float, number_of_payments: int
):
    interest = (rate_of_return / 100) / 12
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
        pow((1 + (intrest_rate / compounding_period)), (compounding_period * years))
    )
    print(amount)
    return amount


# Function to Calculate Inflation
def inflation(present_amount: float, inflation_rate: float, years: int):
    future_amount = present_amount * (pow((1 + inflation_rate / 100), years))
    return future_amount


# Function to Calculate Effective Annual Rate
def effective_annual_rate(annual_interest_rate: float, compounding_period: int):
    EAR = pow((1 + (annual_interest_rate / compounding_period)), compounding_period) - 1
    return EAR


# Function to Calculate Certificate of Deposit (CD)
def certificate_of_deposit(
    principal_amount: float, interest_rate: float, yrs: int, compounding_per_yr: int
):
    cd = principal_amount * (1 + interest_rate / (100 * compounding_per_yr)) ** (
        compounding_per_yr * yrs
    )
    return float(cd)


# Function to Calculate Return on Investment
def return_on_investment(current_value_of_investment: float, cost_of_investment: float):
    roi = (current_value_of_investment - cost_of_investment) / cost_of_investment
    roi *= 100
    return roi


# Function to calculate Compounded Annual Growth Rate (CAGR)
def compounded_annual_growth_rate(
    end_investment_value: float, initial_investment_value: float, years: int
):
    n = 1 / years
    cagr = (end_investment_value / initial_investment_value) ** n - 1
    return cagr


# Function to calculate Jensens Alpha
def jensens_alpha(
    return_from_investment: float,
    return_of_appropriate_market_index: float,
    risk_free_rate: float,
    beta: float,
):
    alpha = return_from_investment - (
        risk_free_rate + beta * (return_of_appropriate_market_index - risk_free_rate)
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
    income_per_month = annual_income / 1200
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
    markup_percentage = ((price - cost) / cost) * 100
    return markup_percentage


# Function to calculate Sharpe Ratio
def sharpe_ratio(
    portfolio_return: float,
    risk_free_rate: float,
    standard_deviation_of_portfolio: float,
):
    sharpe_ratio = (portfolio_return - risk_free_rate) / standard_deviation_of_portfolio
    return sharpe_ratio


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
    t = math.log(2) / math.log(1 + (r / 100))
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
    ratio = (cash + marketable_securitie + accounts_receivable) / current_liabilities
    return round(ratio, 2)


# Function to calculate inflation adjusted return
def inflation_adjusted_return(
    beginning_price: float,
    ending_price: float,
    dividends: float,
    beginning_cpi_level: float,
    ending_cpi__level: float,
):
    stock_return = (ending_price - beginning_price + dividends) / beginning_price

    inflation = (ending_cpi__level - beginning_cpi_level) / beginning_cpi_level

    inflation_adj = ((1 + stock_return) / (1 + inflation) - 1) * 100
    return round(inflation_adj, 2)


# Function to calculate compound annual growth rate
def compound_annual_growth_rate(
    beginning_value: float, ending_value: float, years: int
):
    rate = (pow((beginning_value / ending_value), 1 / years) - 1) * 100
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
    rate = rate / 100
    coupon_rate = coupon_rate / 100

    n = pd.to_numeric(
        ((pd.to_datetime(maturity_date) - pd.to_datetime(settlement_date)) / 365).days
    )
    total_payment = n * frequency
    coupon_payment = coupon_rate / frequency * face_value
    payment = [coupon_payment] * (total_payment - 1) + [coupon_payment + face_value]
    data["period"] = pd.DataFrame(np.arange(1, total_payment + 1))
    data["payment"] = pd.DataFrame(payment)
    data["dcoupon"] = data["payment"] / ((1 + rate / frequency) ** data["period"])
    data["pv"] = data["dcoupon"] / frequency * data["period"] / data["dcoupon"].sum()
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
    inflation_rate = ((bigger_year - smaller_year) / base_year) * 100
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
    market_share_list.append(int(Firms_market_shares[len(Firms_market_shares)-2:len(Firms_market_shares)]))
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
    real_gdp = (nominal_gdp / gdp_deflator) * 100
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
    gdp_growth_rate = ((current_year_gdp - last_year_gdp) / last_year_gdp) * 100
    return gdp_growth_rate


#function to calculate credit card equation
def credit_card_equation(balance:float,monthly_payment:float,daily_interest_rate:float):
    a = np.log(1+(balance//monthly_payment)*(1-(daily_interest_rate)**30))
    b = np.log(1+daily_interest_rate)
    N = -(1//30)*(a//b)
    return N

# function to calculate future value of the ordinary annuity
def future_value_of_ordinary_due(periodic_payment: float, number_of_periods: int, effective_interest_rate: float):
    future_value_of_ordinary_due = periodic_payment*(((1+effective_interest_rate)**(number_of_periods))-1)/effective_interest_rate
    return future_value_of_ordinary_due

# Function to calculate future value of annuity due
def future_value_of_annuity_due(periodic_payment: float, number_of_periods: int, effective_interest_rate: float):
    future_value_of_annuity_due = periodic_payment*(((1+effective_interest_rate)**(number_of_periods))-1)*(1+effective_interest_rate)/effective_interest_rate
    return future_value_of_annuity_due

# Function to calculate present value of annuity due
def present_value_of_annuity_due(periodic_payment: float, number_of_periods: int, rate_per_period: float):
    present_value_of_annuity_due = periodic_payment + periodic_payment*((1-(1+rate_per_period)**(-number_of_periods+1))/rate_per_period)
    return present_value_of_annuity_due

#function to calculate compound annual growth rate
def compound_annual_growth_rate_1(ending_value:float,beginning_value:float,number_of_periods:float):
    a = (ending_value//beginning_value)**(1//number_of_periods)
    cagr = a - 1
    return cagr

# Function to calculate loan to value
def loan_to_value(mortage_value:float,appraised_value: float):
    ratio = mortage_value / appraised_value
    return ratio*100

#Function to calculate Retention Rate
def retention_ratio(net_income:float,dividends:float):
    retention_ratio = (net_income-dividends)/net_income
    return retention_ratio

#Function to calculate Tax Equivalent Yield
def tax_equivalent_yield(tax_free_yield:float,tax_rate:float):
    tax_equivalent_yield = tax_free_yield/(1-tax_rate)
    return tax_equivalent_yield

# Function to calculate year over year growth
def year_over_year(later_period_value:float,earlier_period_value:float):
    growth = (later_period_value - earlier_period_value) / earlier_period_value
    return growth*100


#function to calculate future value of the annuity
def future_value_of_annuity(payments_per_period:float,interest_rate:float,number_of_periods:float):
    a = (((interest_rate+1)**number_of_periods)-1)//interest_rate
    fva = payments_per_period*a
    return fva


# Function to calculate Balloon Balance of a Loan
def balloon_balance_of_loan(present_value:float, payment:float, rate_per_payment:float, number_of_payments:float):
    balloon_balance_of_loan = present_value*((1+rate_per_payment)**number_of_payments) - payment*((((1+rate_per_payment)**number_of_payments)-1)/rate_per_payment)
    return balloon_balance_of_loan

#Function to calculate discounted payback period
def discounted_payback_period(outflow:float,rate:float,periodic_cash_flow:float):
    discounted_payback_period = np.log(1/(1-(outflow*rate/periodic_cash_flow)))/np.log(1+rate)
    return discounted_payback_period


# Function to calculate periodic lease payment
def periodic_lease_payment(Asset_value: float, monthly_lease_interest_rate: float, number_of_lease_payments: float):
    periodic_lease_payment = (Asset_value*monthly_lease_interest_rate)/(1-(1/(1+monthly_lease_interest_rate)**number_of_lease_payments))
    return periodic_lease_payment


# Function to calculate weighted average
def weighted_average_of_values(Assigned_weight_values: str, data_point_values: str):
    weights = list(map(int,Assigned_weight_values.split()))
    data_values = list(map(int,data_point_values.split()))
    total_data_point_weighted_value = 0
    sum_assigned_weight_values = 0
    for i in weights:
        sum_assigned_weight_values = sum_assigned_weight_values + i
    for i in range(len(weights)):
        total_data_point_weighted_value = total_data_point_weighted_value + (weights[i]*data_values[i])

    weighted_average = total_data_point_weighted_value/sum_assigned_weight_values
    return weighted_average


# Function to calculate Yield to maturity
def yield_to_maturity(bond_price:float,face_value:float,coupon_rate:float,years_to_maturity:float):
    yield_cal = (coupon_rate * face_value/100 + (face_value - bond_price)/years_to_maturity) / ((face_value + bond_price) / 2)
    return round(yield_cal*100,2)


# Function to calculate perpetuity payment
def perpetuity_payment(present_value:float,rate:float):
    payment = present_value * (rate/100)
    return payment


# Function to calculate Zero Coupon Bond value
def zero_coupon_bond_value(face_value:float,rate_of_yield:float,time_of_maturity:float):
    zcbv = face_value / pow((1+rate_of_yield/100), time_of_maturity)
    return round(zcbv,2)


# function to calculate Zero Coupon Bond Effective Yield
def zero_coupon_bond_yield(face_value:float, present_value:float, time_of_maturity:float):
    zcby = pow((face_value / present_value),(1/time_of_maturity)) - 1
    return round(zcby*100,1)

# Function to calculate Profitability Index
def profitability_index(initial_investment:float, pv_of_future_cash_flows:float):
    profitability_index = pv_of_future_cash_flows/initial_investment
    return profitability_index


# Function to calculate Profitability index using annual cash flows
def profitability_index2(initial_inverstment: float, annual_cash_flows: str, discount_rate: float):
    annual_cash_flow_list = list(map(int,annual_cash_flows.split()))
    pv_cash_flow_list = []
    for i in range(len(annual_cash_flow_list)):
        pv_cash_flow_list.append((annual_cash_flow_list[i])/((1+(discount_rate/100))**(i+1)))
    total_pv_cash_flow = sum(pv_cash_flow_list)
    profitability_index = total_pv_cash_flow/initial_inverstment
    return profitability_index

# Function to calculate Receivables Turnover Ratio
def receivables_turnover_ratio(sales_revenue:float, avg_accounts_receivable:float):
    receivables_turnover_ratio = sales_revenue/avg_accounts_receivable
    return receivables_turnover_ratio

#Function to calculate Remaiing balance
def remaining_balance(regular_payment:float,interest_rate_per_period:float,number_of_payments:float,number_of_payments_done:float):
    B = regular_payment*((1-((1+interest_rate_per_period)**(-(number_of_payments-number_of_payments_done))))//interest_rate_per_period)
    return B

# Function to calculate Net present value
def net_present_value(cash_flows: str, discount_rate: float, initial_investment: float):
    cash_flow_list = list(map(int, cash_flows.split()))
    net_present_value = -1*(initial_investment)
    for i in range(len(cash_flow_list)):
        net_present_value = net_present_value + (cash_flow_list[i]/((1+(discount_rate/100))**(i+1)))
    return net_present_value

def leverage_income(debt_payments: int, income: int):
    return float(debt_payments)/float(income)


def leverage_equity(debt: int, equity: int):
    return float(debt)/float(equity)

# Function to calculate time period required for given growth
def time_period_required_for_growth(interest_rate: float, growth_factor: int ):
    time_period_required_for_growth = math.log(growth_factor) / math.log(1 + interest_rate/100)
    return time_period_required_for_growth
