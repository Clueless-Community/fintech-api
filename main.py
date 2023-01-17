from fastapi import FastAPI, HTTPException, status
from helpers import functions

app = FastAPI(
    title="FinTech API",
    description="An API that helps you to deal with your financial calculations.",
    version="1",
    contact={
        "name": "Clueless Community",
        "url": "https://www.clueless.tech/",
        "email": "https://www.clueless.tech/contact-us",
    },
    license_info={
        "name": " MIT license",
        "url": "https://github.com/Clueless-Community/fintech-api/blob/main/LICENSE.md",
    },
)


@app.get("/")
def index():
    return {
        "title": "FinTech API",
        "description": "An API that helps you to deal with your financial calculations.",
        "version": "1",
        "contact": {
            "name": "Clueless Community",
            "url": "https://www.clueless.tech/",
            "email": "https://www.clueless.tech/contact-us",
        },
        "license_info": {
            "name": " MIT license",
            "url": "https://github.com/Clueless-Community/fintech-api/blob/main/LICENSE.md",
        },
        "endpoints": {"/simple_interest": "Calculate simple interest rates"},
    }


# Endpoints to calculate simple interest.
@app.get(
    "/simple_interest_rate",
    tags=["simple_interest_rate"],
    description="Calculate simple interest rates",
)
def simple_interest_rate(amount_paid: float, principle_amount: float, months: int):
    try:
        rate = functions.simple_interest_rate(amount_paid, principle_amount, months)
        return {
            "Tag": "Simple Interest Rate",
            "Total amount paid": amount_paid,
            "Principle amount": principle_amount,
            "Interest Paid": amount_paid - principle_amount,
            "Interest Rate": f"{rate}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/future_sip",
    tags=["future_sip"],
    description="Calculate Future Value of SIP",
)
def future_sip(
    interval_investment: float, rate_of_return: float, number_of_payments: int
):
    try:
        value = functions.future_sip(
            interval_investment, rate_of_return, number_of_payments
        )
        return {
            "Tag": "Future Value of SIP",
            "Investment at every Interval": interval_investment,
            "Interest": (rate_of_return / 100) / 12,
            "Number of Payments": number_of_payments,
            "Future Value": f"{value}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint for payback period
@app.get(
    "/payback_period",
    tags=["payback_period_years"],
    description="Calculate payback period",
)
def payback_period(
    years_before_recovery: int, unrecovered_cost: float, cash_flow: float
):
    try:
        period = functions.payback_period(
            years_before_recovery, unrecovered_cost, cash_flow
        )
        return {
            "Tag": "Payback period",
            "Years before full recovery": years_before_recovery,
            "Unrecovered cost at start of the year": unrecovered_cost,
            "Cash flow during the year": cash_flow,
            "Payback period": f"{period}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoints to calculate Compound Intrest.
@app.get(
    "/compound_interest",
    tags=["compound_interest_amount"],
    description="Calculate compound interest amount",
)
def compound_intrest(
    principal_amount: float, intrest_rate: float, years: int, compounding_period: int
):
    try:
        amount = functions.compound_interest(
            principal_amount, intrest_rate, years, compounding_period
        )
        return {
            "Tag": "Compound Intrest Amount",
            "Principle amount": principal_amount,
            "Intrest Rate": intrest_rate,
            "Time in Years": years,
            "Compounding Period": compounding_period,
            "Amount after intrest": f"{amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoints to calculate certificate of deposit (CD)
@app.get(
    "/certificate_of_deposit",
    tags=["certificate_of_deposit"],
    description="Calculate certificate of deposit (CD)",
)
def certificate_of_deposit(
    principal_amount: float, interest_rate: float, yrs: int, compounding_per_yr: int
):
    try:
        cd = functions.certificate_of_deposit(
            principal_amount, interest_rate, yrs, compounding_per_yr
        )
        return {
            "Tag": "Certificate of Deposit (CD)",
            "Principal amount": principal_amount,
            "Interest Rate": interest_rate,
            "Time in Years": yrs,
            "Number of Compounding per Year": compounding_per_yr,
            "Certificate of Deposit (CD)": f"{cd}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# EndPoint to calculate Inflation
@app.get("/inflation", tags=["inflated"], description="Calculate Inflated amount")
def inflation(present_amount: float, inflation_rate: float, years: float):
    try:
        future_amount = functions.inflation(present_amount, inflation_rate, years)
        return {
            "Tag": "Inflated Amount",
            "Present Amount": present_amount,
            "Inflation Rate": inflation_rate,
            "Time in Years": years,
            "Future Amount": f"{future_amount}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to Calculate Effective Annual Rate
@app.get(
    "/effective_annual_rate",
    tags=["Effective Annual Rate"],
    description="Calculate Effective Annual Rate",
)
def inflation(annual_interest_rate: float, compounding_period: int):
    try:
        Eff_annual_rate = functions.effective_annual_rate(
            annual_interest_rate, compounding_period
        )
        Eff_annual_rate_percentage = Eff_annual_rate * 100
        return {
            "Tag": "Effective Annual Rate",
            "Annual Intrest Rate": annual_interest_rate,
            "Compounding Period": compounding_period,
            "Effective Annual Rate (in percentage)": f"{Eff_annual_rate_percentage}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/roi", tags=["return_on_investment"], description="Calculate return on investment"
)
def return_on_investment(current_value_of_investment: float, cost_of_investment: float):
    try:
        roi = functions.return_on_investment(
            current_value_of_investment, cost_of_investment
        )

        return {
            "Tag": "Return on Investment",
            "Current Value of Investment": current_value_of_investment,
            "Cost of Investment": cost_of_investment,
            "Return on Investment": f"{roi}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Compounded Annual Growth Rate.
@app.get(
    "/compounded_annual_growth_rate",
    tags=["compounded_annual_growth_rate"],
    description="Calculate compounded annual growth rate",
)
def compounded_annual_growth_rate(
    end_investment_value: float, initial_investment_value: float, years: int
):
    try:
        cagr = functions.compounded_annual_growth_rate(
            end_investment_value, initial_investment_value, years
        )

        return {
            "Tag": "Compounded Annual Growth Rate",
            "End investment value": end_investment_value,
            "Initial investment value": initial_investment_value,
            "Years": years,
            "Compounded Annual Growth Rate": f"{cagr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        alpha = functions.jensens_alpha(
            return_from_investment,
            return_of_appropriate_market_index,
            risk_free_rate,
            beta,
        )
        return {
            "Tag": "Jensen's Alpha",
            "Total return from investment": return_from_investment,
            "Return of appropriate market index": return_of_appropriate_market_index,
            "Risk free rate": risk_free_rate,
            "Beta of the portfolio investment w.r.t chosen market index": beta,
            "Alpha of the return ": f"{alpha}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate WACC
@app.get(
    "/wacc",
    tags=["wacc"],
    description="Calculate Weighted Average Cost of Capital (WACC)",
)
def weighted_average_cost_of_capital(
    firm_equity, firm_debt, cost_of_equity, cost_of_debt, corporate_tax_rate
):
    try:
        wacc = functions.wacc(
            firm_equity, firm_debt, cost_of_equity, cost_of_debt, corporate_tax_rate
        )
        return {
            "Tag": "Weighted Average Cost of Capital (WACC)",
            "Market value of firm's equity": firm_equity,
            "Market value of firm's debt": firm_debt,
            "Cost of equity": cost_of_equity,
            "Cost of debt": cost_of_debt,
            "Corporate tax rate": corporate_tax_rate,
            "WACC": f"{wacc}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/loan_emi",
    tags=["load_emi"],
    description="Calculate Loan EMI",
)
def loan_emi(principle_amount: float, annual_rate: float, months: int):
    try:
        emi = functions.loan_emi(principle_amount, annual_rate, months)
        return {
            "Tag": "Loan Emi",
            "Princiapl amount borrowed": principle_amount,
            "Annual Rate of interest": annual_rate,
            "Total number of monthly payments": months,
            "EMI": f"{round(emi,3)}",
            "Total Amount Payble": f"{round(emi*months,3)}",
            "Interest amount": f"{round(emi*months-principle_amount,3)}",
        }
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        weight_A = price_A / (price_A + price_B)
        weight_B = price_B / (price_A + price_B)
        cov = correlation * standard_dev_A * standard_dev_B
        portfolio_variance = (
            weight_A * weight_A * standard_dev_A * standard_dev_A
            + weight_B * weight_B * standard_dev_B * standard_dev_B
            + 2 * weight_A * weight_B * cov
        )
        expected_return = 100 * (weight_A * return_A + weight_B * return_B)
        return {
            "Tag": "Portfolio Variance",
            "Expected Returns": f"{expected_return}%",
            "Portfolio Variance": f"{portfolio_variance}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to Calculate Future Price in Put-Call Parity
@app.get(
    "/put_call_parity",
    tags=["/put_call_parity"],
    description="Calculate Future Price in Pull-Call Parity",
)
def put_call_parity(call_price: float, put_price: float, strike_price: float):
    try:
        future_amount = functions.put_call_parity(call_price, put_price, strike_price)
        return {
            "Tag": "Pull Call Parity",
            "Future Price": f"{future_amount}",
            "Call Price": f"{call_price}",
            "Put Price": f"{put_price}",
            "Strike Price": f"{strike_price}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate break even point
@app.get(
    "/bep",
    tags=["bep"],
    description="Calculate Break Even Point",
)
def break_even_point(fixed_cost: float, selling_price: float, variable_cost: float):
    try:

        bep = functions.break_even_point(fixed_cost, selling_price, variable_cost)
        return {
            "Tag": "Break Even Point (BEP)",
            "Fixed costs": fixed_cost,
            "Selling price per unit": selling_price,
            "Variable cost per unit": variable_cost,
            "Break Even Point in units": f"{bep[0]}",
            "Break Even Point in Rupees": f"{bep[1]}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        ebitda = sales - operating_cost
        ebit = ebitda - depreciation
        ebt = ebit - interest

        eat = ebt - ebt * (tax_rate * 0.01)
        fcff = functions.free_cash_flow_to_firm(
            sales, operating_cost, depreciation, interest, tax_rate, fcInv, wcInv
        )
        return {
            "Tag": "Free Cash Flow to Firm (FCFF)",
            "Earnings before interest, taxes, depreciation and amortization": f"{ebitda}",
            "Earnings before interest and taxes : ": f"{ebit}",
            "Net Income": f"{eat}",
            "Free Cash Flow to Firm": f"{fcff}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Price-to-earning ratio
@app.get(
    "/price_to_earning_ratio",
    tags=["price_to_earning_ratio"],
    description="Calculate price to earning ratio",
)
def price_to_earning_ratio(share_price: float, earnings_per_share: float):
    try:
        p_e_ratio = functions.price_to_earning(share_price, earnings_per_share)
        return {
            "Tag": "Price to Earning ratio",
            "Share price": share_price,
            "Earning per share": earnings_per_share,
            "Price to Earning ratio": f"{p_e_ratio}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Dividend yield ratio


@app.get(
    "/dividend_yield_ratio",
    tags=["dividend_yield_ratio"],
    description="Calculate dividend yield ratio",
)
def dividend_yield_ratio(dividend_per_share: float, share_price: float):
    try:
        dividend_yield = functions.dividend_yield_ratio(dividend_per_share, share_price)
        return {
            "Tag": "Dividend yield ratio",
            "Dividend per share": dividend_per_share,
            "Share price": share_price,
            "Dividend yield ratio": f"{dividend_yield}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Dividend payout ratio
@app.get(
    "/dividend_payout_ratio",
    tags=["dividend_payout_ratio"],
    description="Calculate dividend payout ratio",
)
def dividend_payout_ratio(dividend_per_share: float, earnings_per_share: float):
    try:
        dividend_payout = functions.dividend_payout_ratio(
            dividend_per_share, earnings_per_share
        )
        return {
            "Tag": "Dividend payout ratio",
            "Dividend per share": dividend_per_share,
            "Share price": earnings_per_share,
            "Dividend yield ratio": f"{dividend_payout}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate DTI
@app.get(
    "/debt_to_income_ratio",
    tags=["debt_to_income_ratio"],
    description="Calculate debt to income ratio per month",
)
def debt_to_income_ratio(annual_income: float, total_debt_per_month: float):
    try:
        DTI = functions.debt_to_income_ratio(annual_income, total_debt_per_month)
        return {
            "Tag": "Debt to income ratio",
            "Annual income": annual_income,
            "Total debt per month": total_debt_per_month,
            "Debt to income ratio per month": f"{DTI}%",
        }
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


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
    try:
        fccr = functions.fixed_charge_coverage_ratio(
            earnings_before_interest_taxes, fixed_charge_before_tax, interest
        )
        return {
            "Tag": "fixed charges coverage ratio",
            "Earnings before interest taxes": earnings_before_interest_taxes,
            "Fixed charge before tax": fixed_charge_before_tax,
            "Interest": interest,
            "Fixed charge coverage ratio": f"{fccr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Inventory Shrinkage Rate
@app.get(
    "/inventory_shrinkage_rate",
    tags=["inventory_shrinkage_rate"],
    description="Calculate inventory shrinkage rate",
)
def inventory_shrinkage_rate(recorded_inventory: float, actual_inventory: float):
    try:
        inventory_shrinkage_rate = functions.inventory_shrinkage_rate(
            recorded_inventory, actual_inventory
        )
        return {
            "Tag": "Inventory shrinkage rate",
            "Recorded Inventory": recorded_inventory,
            "Actual Inventory": actual_inventory,
            "Invenory Shrinkage Rate": inventory_shrinkage_rate,
            "Invenory Shrinkage Rate (%)": inventory_shrinkage_rate * 100,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Markup Percentage
@app.get(
    "/markup_percentage",
    tags=["markup_percentage"],
    description="Calculate markup percentage",
)
def markup_percentage(price: float, cost: float):
    try:
        markup_percentage = functions.markup_percentage(price, cost)
        return {
            "Tag": "Markup Percentage",
            "Price": price,
            "Cost": cost,
            "Markup Percentage": markup_percentage,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        sharpe_ratio = functions.sharpe_ratio(
            portfolio_return, risk_free_rate, standard_deviation_of_portfolio
        )
        return {
            "Tag": "Sharpe Ratio",
            "Portfolio Return": portfolio_return,
            "Risk Free Rate": risk_free_rate,
            "Standard Deviation of Portfolio": standard_deviation_of_portfolio,
            "Sharpe Ratio": f"{sharpe_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate purchase power
@app.get(
    "/purchasing_power",
    tags=["purchasing_power"],
    description="Calculate Purchasing Power",
)
def purchasing_power(initial_amount: float, annual_inflation_rate: float, time: float):
    try:
        purchasing_power = functions.purchasing_power(
            initial_amount, annual_inflation_rate, time
        )
        return {
            "Tag": "Purchasing Power",
            "Initial Amount": initial_amount,
            "Annual Inflation Rate": annual_inflation_rate,
            "Time in years": time,
            "Purchasing Power": f"{purchasing_power}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Monthly EMI
@app.get(
    "/monthly_emi",
    tags=["monthly_emi"],
    description="Monthly EMI",
)
def monthly_emi(loan_amt: float, interest_rate: float, number_of_installments: float):
    try:
        monthly_emi = functions.monthly_emi(
            loan_amt, interest_rate, number_of_installments
        )
        return {
            "Tag": "Monthly EMI",
            "Loan Amount": loan_amt,
            "Interest Rate": interest_rate,
            "Number of Installments": number_of_installments,
            "Total EMI": f"{monthly_emi}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate doubling time
@app.get(
    "/doubling_time",
    tags=["doubling_time"],
    description="Doubling Time",
)
def doubling_time(r: float):
    try:
        doubling_time = functions.doubling_time(r)
        return {
            "Tag": "Doubling Time",
            "Rate of Interest": r,
            "Time in years to double the money": f"{doubling_time}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate weighted average
@app.get(
    "/weighted_average",
    tags=["weighted_average"],
    description="Weighted Average",
)
def weighted_average(ratio: list, rates: list):
    try:
        weighted_average = functions.weighted_average(ratio, rates)
        return {
            "Tag": "Weighted Average",
            "Ratio of each investment principal": ratio,
            "Rates": rates,
            "Weighted average : ": f"{weighted_average}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        Capital_Asset_Pricing_Model = functions.Capital_Asset_Pricing_Model(
            risk_free_interest_rate, beta_of_security, expected_market_return
        )
        return {
            "Tag": "Capital Asset Pricing Model",
            "Risk free interest rate": risk_free_interest_rate,
            "Beta of security": beta_of_security,
            "Expected market return": expected_market_return,
            "Capital asset expected return": f"{Capital_Asset_Pricing_Model}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate cost of equity
@app.get(
    "/cost_of_equity",
    tags=["cost_of_equity"],
    description="Calculate cost of equity",
)
def cost_of_equity(
    risk_free_rate_of_return: float, Beta: float, market_rate_of_return: float
):
    try:
        costOfEquity = functions.cost_of_equity(
            risk_free_rate_of_return, Beta, market_rate_of_return
        )
        return {
            "Tag": "Cost of Equity",
            "Risk free rate of return": risk_free_rate_of_return,
            "Beta": Beta,
            "Market rate of return ": market_rate_of_return,
            "Cost of equity": f"{costOfEquity}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate cost of goods sold
@app.get(
    "/cogs",
    tags=["cogs"],
    description="Calculate Cost of Goods Sold",
)
def cost_of_goods_sold(
    beginning_inventory: float, purchases: float, ending_inventory: float
):
    try:
        cogs = functions.cost_of_goods_sold(
            beginning_inventory, purchases, ending_inventory
        )
        return {
            "Tag": "Cost of Goods Sold",
            "Beginning Inventory": beginning_inventory,
            "Purchases during the period": purchases,
            "Ending Inventory": ending_inventory,
            "Cost of Goods Sold(In Rupees)": f"{cogs}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate rule of 72
@app.get(
    "/ruleof72",
    tags=["ruleof72"],
    description="Calculate Rule of 72",
)
def rule_of_72(rate_of_roi: float):
    try:
        time_period = functions.rule_of_72(rate_of_roi)
        return {
            "Tag": "Rule of 72",
            "Rate of ROI": rate_of_roi,
            "Time peroid in which investment get double(in years)": f"{time_period}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate acid test ratio
@app.get(
    "/acid_test_ratio",
    tags=["acid_test_ratio"],
    description="Calculate Acid test ratio",
)
def acid_test_ratio(
    cash: float,
    marketable_securitie: float,
    accounts_receivable: float,
    current_liabilities: float,
):
    try:
        ratio = functions.acid_test_ratio(
            cash, marketable_securitie, accounts_receivable, current_liabilities
        )
        return {
            "Tag": "Acid Test Ratio",
            "Cash and Cash Equivalents": cash,
            "Marketable Securities": marketable_securitie,
            "Accounts Receivable": accounts_receivable,
            "Current Liabilities": current_liabilities,
            "Acid Test Ratio (Quick Ratio)": f"{ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        stock_return = (ending_price - beginning_price + dividends) / beginning_price
        inflation = (ending_cpi__level - beginning_cpi_level) / beginning_cpi_level
        inflation_adj_return = functions.inflation_adjusted_return(
            beginning_price,
            ending_price,
            dividends,
            beginning_cpi_level,
            ending_cpi__level,
        )
        return {
            "Tag": "Inflation Adjusted Return",
            "Stock Return": f"{stock_return}%",
            "Inflation Rate": f"{inflation}%",
            "Inflation Adjusted Return": f"{inflation_adj_return}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate compound annual growth rate
@app.get(
    "/cogr",
    tags=["cogr"],
    description="Calculate Compound Annual Growth Rate",
)
def compound_annual_growth_rate(
    beginning_value: float, ending_value: float, years: int
):
    try:
        rate = functions.compound_annual_growth_rate(
            beginning_value, ending_value, years
        )
        return {
            "Tag": "Coumpound Annual Growth Rate",
            "Beginning Value": beginning_value,
            "Ending Value": ending_value,
            "Compound Annual Growth Rate": f"{rate}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        current_liability_coverage_ratio = functions.current_liability_coverage_ratio(
            net_cash_from_operating_activities,
            total_current_liabilities,
            number_of_liabilities,
        )
        return {
            "Tag": "current liability coverage ratio",
            "net cash from operating activities": net_cash_from_operating_activities,
            "total current liabilities": total_current_liabilities,
            "number of liabilities": number_of_liabilities,
            "current liability coverage ratio": f"{current_liability_coverage_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/levered_beta",
    tags=["levered_beta"],
    description="Levered Beta",
)
def levered_beta(unlevered_beta: float, tax_rate: float, debt: float, equity: float):
    try:
        l_beta = functions.levered_beta(unlevered_beta, tax_rate, debt, equity)
        return {
            "Tag": "Levered Beta",
            "Unlevered Beta": unlevered_beta,
            "Tax rate": tax_rate,
            "debt": debt,
            "Equity": equity,
            "Levered Beta": f"{l_beta}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        monthly_pay = functions.monthly_payment(
            principal, interest_rate, number_of_periods, payments_per_period
        )
        return {
            "Tag": "Monthly Payment",
            "Principal": principal,
            "Interest Rate": interest_rate,
            "Number of Periods": number_of_periods,
            "Payments per period": payments_per_period,
            "Levered Beta": f"{monthly_pay}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/convexity_duration",
    tags=["convexity_duration"],
    description="Convexity Adjusted Duration",
)
def duration(rate, coupon_rate, frequency, face_value, settlement_date, maturity_date):
    try:
        duration = functions.duration(
            rate, coupon_rate, frequency, face_value, settlement_date, maturity_date
        )
        return {
            "Tag": "Convexity Adjusted Duration",
            "Market Rate": rate,
            "Coupon rate": coupon_rate,
            "Frequency": frequency,
            "Face Value": face_value,
            "Settlement Date": settlement_date,
            "Maturity Date": maturity_date,
            "Convexity Adjusted Duration": f"{duration}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate current ratio
@app.get(
    "/current_ratio",
    tags=["current_ratio"],
    description="Current Ratio",
)
def current_ratio(total_current_assets: float, total_liabilities: float):
    try:
        ratio = functions.current_ratio(total_current_assets, total_liabilities)
        return {
            "Tag": "Current Ratio",
            "Total Current Assets": total_current_assets,
            "Total Liabilities": total_liabilities,
            "Current Ratio": f"{ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate inventory turnover ratio
@app.get(
    "/inventory_turnover_ratio",
    tags=["inventory_turnover_ratio"],
    description="Inventory Turnover Ratio",
)
def inventory_turnover_ratio(
    cost_of_goods_sold: float, beginnning_inventory: float, ending_inventory: float
):
    try:
        ratio = functions.inventory_turnover_ratio(
            cost_of_goods_sold, beginnning_inventory, ending_inventory
        )
        return {
            "Tag": "Inventory Turnover Ratio",
            "Cost of Goods Sold": cost_of_goods_sold,
            "Inventory Turnover Ratio": f"{ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate inflation rate
@app.get(
    "/inflation_rate",
    tags=["inflation_rate"],
    description="Inflation Rate",
)
def inflation_rate(bigger_year: int, smaller_year: int, base_year: int):
    try:
        inflation_rate = functions.inflation_rate(bigger_year, smaller_year, base_year)
        return {
            "Tag": "Inflation Rate",
            "Bigger Year": bigger_year,
            "Smaller Year": smaller_year,
            "Base Year": base_year,
            "Inflation Rate": inflation_rate,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Herfindal index
@app.get(
    "/herfindal_Index",
    tags=["herfindal_Index"],
    description="Calculating herfindal Index",
)
def herfindal_Index(Firms_market_shares: str):
    try:
        herfindal_Index = functions.herfindal_Index(Firms_market_shares)
        return {
            "Tag": "Herfindal Index",
            "Firms market shares": Firms_market_shares,
            "Herfindal Index": f"{herfindal_Index}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/discount_opex",
    tags=["discount_opex"],
    description="Discount OPEX",
)
def discount_opex(annual_opex: float, wacc: float, project_lifetime: float):
    try:
        dis_opex = functions.discount_opex(annual_opex, wacc, project_lifetime)
        return {
            "Tag": "Discount OPEX",
            "Annual OPEX": annual_opex,
            "WACC": wacc,
            "project lifetime": project_lifetime,
            "Discount opex": f"{dis_opex}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/project_efficiency",
    tags=["project_efficiency"],
    description="Project Efficiency",
)
def project_efficiency(annual_production: float, collector_surface: float, dni: float):
    try:
        project_eff = functions.project_efficiency(
            annual_production, collector_surface, dni
        )
        return {
            "Tag": "Project efficiency",
            "Annual production": annual_production,
            "collector surface": collector_surface,
            "dni": dni,
            "Discount opex": f"{project_eff}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/real_gdp",
    tags=["real_gdp"],
    description="Real GDP",
)
def real_gdp(nominal_gdp: float, gdp_deflator: float):
    try:
        real_gdp = functions.real_gdp(nominal_gdp, gdp_deflator)
        return {
            "Tag": "Real GDP",
            "Nominal GDP": nominal_gdp,
            "GDP Deflator": gdp_deflator,
            "Real GDP": real_gdp,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/excess_reserves",
    tags=["excess_reserves"],
    description="Excess Reserves",
)
def excess_reserves(deposits: float, reserve_requirement: float):
    try:
        excess_reserves = functions.excess_reserves(deposits, reserve_requirement)
        return {
            "Tag": "Excess Reserves",
            "Deposits": deposits,
            "Reserve Requirement": reserve_requirement,
            "Excess Reserves": excess_reserves,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        d_cash_flow = functions.discounted_cash_flow(
            real_feed_in_tariff, annual_production, wacc, project_lifetime
        )
        return {
            "Tag": "Discounted cash flow",
            "Real feed in teriff": real_feed_in_tariff,
            "annual production": annual_production,
            "wacc": wacc,
            "project lifetime": project_lifetime,
            "discounted cash flow": f"{d_cash_flow}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/gdp_growth_rate",
    tags=["gdp_growth_rate"],
    description="GDP Growth Rate",
)
def gdp_growth_rate(current_year_gdp: float, last_year_gdp: float):
    try:
        gdp_growth_rate = functions.gdp_growth_rate(current_year_gdp, last_year_gdp)
        return {
            "Tag": "GDP Growth Rate",
            "Current Year GDP": current_year_gdp,
            "Last Year GDP": last_year_gdp,
            "GDP Growth Rate": gdp_growth_rate,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/credit_card_equation",
    tags=["credit_card_equation"],
    description="Credit Card Equation",
)
def credit_card_equation(
    balance: float, monthly_payment: float, daily_interest_rate: float
):
    try:
        N = functions.credit_card_equation(
            balance, monthly_payment, daily_interest_rate
        )
        return {
            "Tag": "Credit card equation",
            "Balance": balance,
            "Monthly Payment": monthly_payment,
            "daily interest rate": daily_interest_rate,
            "credit card equation": f"{N}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate future value of the ordinary annuity
@app.get(
    "/future_value_of_ordinary_due",
    tags=["future_value_of_ordinary_due"],
    description="Calculating future value of ordinary annuity",
)
def future_value_of_ordinary_due(
    periodic_payment: float, number_of_periods: int, effective_interest_rate: float
):
    try:
        future_value_of_ordinary_due = functions.future_value_of_ordinary_due(
            periodic_payment, number_of_periods, effective_interest_rate
        )
        return {
            "Tag": "Future value of the ordinary annuity",
            "Periodic payment": periodic_payment,
            "Number of periods": number_of_periods,
            "Effective interest rate": effective_interest_rate,
            "Number of periods": f"{future_value_of_ordinary_due}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate future value of the annuity due
@app.get(
    "/future_value_of_annuity_due",
    tags=["future_value_of_annuity_due"],
    description="Calculating future value of annuity due",
)
def future_value_of_annuity_due(
    periodic_payment: float, number_of_periods: int, effective_interest_rate: float
):
    try:
        future_value_of_annuity_due = functions.future_value_of_annuity_due(
            periodic_payment, number_of_periods, effective_interest_rate
        )
        return {
            "Tag": "Future value of the ordinary annuity",
            "Periodic payment": periodic_payment,
            "Number of periods": number_of_periods,
            "Effective interest rate": effective_interest_rate,
            "Number of periods": f"{future_value_of_annuity_due}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate present value of the annuity due
@app.get(
    "/present_value_of_annuity_due",
    tags=["present_value_of_annuity_due"],
    description="Calculating present value of annuity due",
)
def present_value_of_annuity_due(
    periodic_payment: float, number_of_periods: int, rate_per_period: float
):
    try:
        present_value_of_annuity_due = functions.present_value_of_annuity_due(
            periodic_payment, number_of_periods, rate_per_period
        )
        return {
            "Tag": "Present value of annuity due",
            "Periodic payment": periodic_payment,
            "Number of periods": number_of_periods,
            "Rate Per Period": rate_per_period,
            "PV of Annuity Due": f"{present_value_of_annuity_due}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/compound_annual_growth_rate",
    tags=["compound_annual_growth_rate"],
    description="Calculating compound annual growth rate",
)
def compound_annual_growth_rate_1(
    ending_value: float, beginning_value: float, number_of_periods: float
):
    try:
        cagr = functions.compound_annual_growth_rate_1(
            ending_value, beginning_value, number_of_periods
        )
        return {
            "Tag": "compound annual growth rate 1",
            "ending_value": ending_value,
            "beginning value": beginning_value,
            "Number of periods": number_of_periods,
            "compound annual growth rate": f"{cagr}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate loan to value
@app.get(
    "/loan_to_value",
    tags=["loan_to_value"],
    description="Calculating loan to value ratio",
)
def loan_to_value(mortage_value: float, appraised_value: float):
    try:
        ratio = functions.loan_to_value(mortage_value, appraised_value)
        return {
            "Tag": "Loan to Value (LTV) ratio",
            "Mortage Value": mortage_value,
            "Appraised Property Value": appraised_value,
            "Loan to Value ratio": f"{ratio}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate retention ratio
@app.get(
    "/retention_ratio",
    tags=["retention_ratio"],
    description="Calculating retention ratio",
)
def retention_ratio(net_income: float, dividends: float):
    try:
        retention_ratio = functions.retention_ratio(net_income, dividends)
        return {
            "Tag": "Retention Ratio",
            "Net Income": net_income,
            "Dividends": dividends,
            "Retention Ratio": retention_ratio,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate tax equivalent yield
@app.get(
    "/tax_equivalent_yield",
    tags=["tax_equivalent_yield"],
    description="Calculating tax equivalent yield",
)
def tax_equivalent_yield(tax_free_yield: float, tax_rate: float):
    try:
        tax_equivalent_yield = functions.tax_equivalent_yield(tax_free_yield, tax_rate)
        return {
            "Tag": "Tax Equivalent Yield",
            "Tax Free Yield": tax_free_yield,
            "Tax Rate": tax_rate,
            "Tax Equivalent Yield": tax_equivalent_yield,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint to calculate year over year growth
@app.get(
    "/year_to_year",
    tags=["year_to_year"],
    description="Calculating Year to Year Growth",
)
def year_over_year(later_period_value: float, earlier_period_value: float):
    try:
        growth = functions.year_over_year(later_period_value, earlier_period_value)
        return {
            "Tag": "Year to Year Growth",
            "Year to Year growth": f"{growth}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/future_value_of_annuity",
    tags=["future_value_of_annuity"],
    description="Calculating future worth of annuity",
)
def future_value_of_annuity(
    payments_per_period: float, interest_rate: float, number_of_periods: float
):
    try:
        fva = functions.future_value_of_annuity(
            payments_per_period, interest_rate, number_of_periods
        )
        return {
            "Tag": "Future value of annuity",
            "Payments per periods": payments_per_period,
            "interest rate": interest_rate,
            "number of periods": number_of_periods,
            "future value of annuity": f"{fva}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        balloon_balance = functions.balloon_balance_of_loan(
            present_value, payment, rate_per_payment, number_of_payments
        )
        return {
            "Tag": "Balloon Balance of a Loan",
            "Present Value (Original Balance)": present_value,
            "Payment": payment,
            "Rate per Payment": rate_per_payment,
            "Number of Payments": number_of_payments,
            "Future Value (Balloon Balance)": balloon_balance,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        pmt = functions.periodic_lease_payment(
            Asset_value, monthly_lease_interest_rate, number_of_lease_payments
        )
        return {
            "Tag": "Periodic Lease Payment",
            "Asset value": Asset_value,
            "Monthly lease interest rate": monthly_lease_interest_rate,
            "Number of lease payments": number_of_lease_payments,
            "Periodic Lease Payment": f"{pmt}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Weighted average
@app.get(
    "/weighted_average_of_values",
    tags=["weighted_average"],
    description="Calculating weighted average",
)
def weighted_average_of_values(Assigned_weight_values: str, data_point_values: str):
    try:
        weighted_average = functions.weighted_average_of_values(
            Assigned_weight_values, data_point_values
        )
        return {
            "Tag": "weighted_average",
            "Assigned weight values": Assigned_weight_values,
            "Data point values": data_point_values,
            "Weighted average": f"{weighted_average}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint to calculate discounted payback period
@app.get(
    "/discounted_payback_period",
    tags=["discounted_payback_period"],
    description="Calculating discounted payback period",
)
def discounted_payback_period(outflow: float, rate: float, periodic_cash_flow: float):
    try:
        discounted_payback_period = functions.discounted_payback_period(
            outflow, rate, periodic_cash_flow
        )
        return {
            "Tag": "Discounted Payback Period",
            "Initial Investment (Outflow)": outflow,
            "Rate": rate,
            "Periodic Cash Flow": periodic_cash_flow,
            "Discounted Payback Period": discounted_payback_period,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint to calculate yield to maturity
@app.get(
    "/yield_to_maturity",
    tags=["yield_to_maturity"],
    description="Calculating Yield to Maturity",
)
def yield_to_maturity(
    bond_price: float, face_value: float, coupon_rate: float, years_to_maturity: float
):
    try:
        yield_cal = functions.yield_to_maturity(
            bond_price, face_value, coupon_rate, years_to_maturity
        )
        return {
            "Tag": "Yield To Maturity",
            "Face Value": face_value,
            "Years to maturity": years_to_maturity,
            "Yield to Maturity": f"{yield_cal}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint to calculate perpetuity payment
@app.get(
    "/perpetuity_payment",
    tags=["perpetuity_payment"],
    description="Calculating perpetuity payment",
)
def perpetuity_payment(present_value: float, rate: float):
    try:
        payment = functions.perpetuity_payment(present_value, rate)
        return {
            "Tag": "Perpetuity Payment",
            "Present Value": present_value,
            "Perpetuity Payment": f"{payment}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint to calculate Zero Coupon Bond value
@app.get(
    "/zero_coupoun_bond_value",
    tags=["zero_coupoun_bond_value"],
    description="Calculating zero coupoun bond value",
)
def zero_coupon_bond_value(
    face_value: float, rate_of_yield: float, time_of_maturity: float
):
    try:
        zcbv = functions.zero_coupon_bond_value(
            face_value, rate_of_yield, time_of_maturity
        )
        return {
            "Tag": "Zero Coupon Bond Value",
            "Face Value": face_value,
            "Rate of yield": f"{rate_of_yield}%",
            "Zero Coupon Bond Value": zcbv,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# endpoint to calculate Zero Coupon Bond Effective Yield
@app.get(
    "/zero_coupoun_bond_yield",
    tags=["zero_coupoun_bond_yield"],
    description="Calculating Zero Coupon Bond Effective Yield",
)
def zero_coupon_bond_yield(
    face_value: float, present_value: float, time_of_maturity: float
):
    try:
        zcby = functions.zero_coupon_bond_yield(
            face_value, present_value, time_of_maturity
        )
        return {
            "Tag": "Zero Coupon Bond Effective Yield",
            "Face Value": face_value,
            "Present Value": present_value,
            "Time to maturity": time_of_maturity,
            "Zero Coupon Bond Effective Yield": f"{zcby}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Profitability Index
@app.get(
    "/profitability_index",
    tags=["profitability_index"],
    description="Calculating profitability index",
)
def profitability_index(initial_investment: float, pv_of_future_cash_flows: float):
    try:
        profitability_index = functions.profitability_index(
            initial_investment, pv_of_future_cash_flows
        )
        return {
            "Tag": "Profitability Index",
            "Initial Investment": initial_investment,
            "PV of Future Cash Flows": pv_of_future_cash_flows,
            "Profitability Index": profitability_index,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Profitability index using annual cash flows
@app.get(
    "/profitability_index2",
    tags=["profitability_index"],
    description="Calculating profitability index using annual cash flows",
)
def profitability_index2(
    initial_inverstment: float, annual_cash_flows: str, discount_rate: float
):
    try:
        profitability_index = functions.profitability_index2(
            initial_inverstment, annual_cash_flows, discount_rate
        )
        return {
            "Tag": "profitability_index",
            "initial_inverstment": initial_inverstment,
            "annual_cash_flows": annual_cash_flows,
            "discount_rate": discount_rate,
            "profitability index": f"{profitability_index}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate Receivables Turnover Ratio
@app.get(
    "/receivables_turnover_ratio",
    tags=["receivables_turnover_ratio"],
    description="Calculating receivables turnover ratio",
)
def receivables_turnover_ratio(sales_revenue: float, avg_accounts_receivable: float):
    try:
        receivables_turnover_ratio = functions.receivables_turnover_ratio(
            sales_revenue, avg_accounts_receivable
        )
        return {
            "Tag": "Receivables Turnover Ratio",
            "Sales Revenue": sales_revenue,
            "Avg Accounts Receivables": avg_accounts_receivable,
            "Receivables Turnover Ratio": receivables_turnover_ratio,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(
    "/remaining_balance",
    tags=["remainig_balance"],
    description="Calculating remaining balance",
)
def remaining_balance(
    regular_payment: float,
    interest_rate_per_period: float,
    number_of_payments: float,
    number_of_payments_done: float,
):
    try:
        B = functions.remaining_balance(
            regular_payment,
            interest_rate_per_period,
            number_of_payments,
            number_of_payments_done,
        )
        return {
            "Tag": "Remainig balance",
            "regular_payment": regular_payment,
            "interest rate per period": interest_rate_per_period,
            "number of payments": number_of_payments,
            "number of payments done": number_of_payments_done,
            "remaining balance": B,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to calculate net present value
@app.get(
    "/net_present_value",
    tags=["net present value"],
    description="Calculating net present value",
)
def net_present_value(cash_flows: str, discount_rate: float, initial_investment: float):
    try:
        net_present_value = functions.net_present_value(
            cash_flows, discount_rate, initial_investment
        )
        return {
            "Tag": "Net present value",
            "cash flows": cash_flows,
            "discount rate": discount_rate,
            "initial investment": initial_investment,
            "Net present value": net_present_value,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to Calculate Leverage Ratio By Income
@app.get(
    "/leverage_ratio_income",
    tags=["Leverage Ratio By Income"],
    description="Calculate Leverage Ratio",
)
def leverage_income(debt_payments: int, income: int):
    try:
        leverage_ratio = functions.leverage_income(debt_payments, income)

        return {
            "Tag": "Leverage Ratio By Income",
            "Debt ": debt_payments,
            "Income": income,
            "Leverage Ratio": f"{leverage_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to Calculate Leverage Ratio By equity
@app.get(
    "/leverage_ratio_equity",
    tags=["Leverage Ratio By Equity"],
    description="Calculate Leverage Ratio",
)
def leverage_equity(debt_payments: int, equity: int):
    try:
        leverage_ratio = functions.leverage_equity(debt_payments, equity)

        return {
            "Tag": "Leverage Ratio By Equity",
            "Debt ": debt_payments,
            "Equity": equity,
            "Leverage Ratio": f"{leverage_ratio}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Endpoint to calculate the time period required for exponential growth
@app.get(
    "/time_period_required_for_growth",
    tags = ["time_period_required_for_growth"],
    description = "Calculating the time period required for exponential growth",
)
def time_period_required_for_growth(interest_rate: float, growth_factor: int ):
    try:
        time_period_required_for_growth = functions.time_period_required_for_growth(interest_rate,growth_factor)
        return{
            "Tag" :"Time period required for exponential growth",
            "interest rate" : interest_rate,
            "growth factor" : growth_factor
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
