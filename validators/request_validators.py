from pydantic import BaseModel

class SimpleInterestRateRequest(BaseModel):
    amount_paid: float
    principle_amount: float
    months: int

class futureSip(BaseModel):
    interval_investment: float
    rate_of_return: float
    number_of_payments: int

class calculatePension(BaseModel):
    monthly_investment_amount: float
    no_of_years: int
    annuity_rates: float
    annuity_purchased: float
    yearly_interest_rates: float

class paybackPeriod(BaseModel):
    years_before_recovery: int
    unrecovered_cost: float
    cash_flow: float

class compoundInterest(BaseModel):
    principal_amount: float
    interest_rate: float
    years: int
    compounding_period: int

class certificateOfDeposit(BaseModel):
    principal_amount: float
    interest_rate: float
    yrs: int
    compounding_per_yr: int

class inflation(BaseModel):
    present_amount: float
    inflation_rate: float
    years: float

class effectiveAnnualRate(BaseModel):
    annual_interest_rate: float
    compounding_period: int

class roi(BaseModel):
    current_value_of_investment: float
    cost_of_investment: float

class compoundedAnnualGrowthRate(BaseModel):
    end_investment_value: float
    initial_investment_value: float
    years: int

class jensensAlpha(BaseModel):
    return_from_investment: float
    return_of_appropriate_market_index: float
    risk_free_rate: float
    beta: float

class wacc(BaseModel):
    firm_equity: float
    firm_debt: float
    cost_of_equity: float
    cost_of_debt: float
    corporate_tax_rate: float

class loanEmi(BaseModel):
    principle_amount: float
    annual_rate: float
    months: int

class assetPortfolio(BaseModel):
    price_A: float
    price_B: float
    return_A: float
    return_B: float
    standard_dev_A: float
    standard_dev_B: float
    correlation: float

class putCallParity(BaseModel):
    call_price: float
    put_price: float
    strike_price: float

class bep(BaseModel):
    fixed_cost: float
    selling_price: float
    variable_cost: float

class fcff(BaseModel):
    sales: float
    operating_cost: float
    depreciation: float
    interest: float
    tax_rate: float
    fcInv: float
    wcInv: float

class priceToEarningRatio(BaseModel):
    share_price: float
    earnings_per_share: float

class dividendYieldRatio(BaseModel):
    dividend_per_share: float
    share_price: float

class dividendPayoutRatio(BaseModel):
    dividend_per_share: float
    earnings_per_share: float

class debtToIncomeRatio(BaseModel):
    annual_income: float
    total_debt_per_month: float

class fixedChargesCoverageRatio(BaseModel):
    earnings_before_interest_taxes: float
    fixed_charge_before_tax: float
    interest: float

class inventoryShrinkageRate(BaseModel):
    recorded_inventory: float
    actual_inventory: float

class markupPercentage(BaseModel):
    price: float
    cost: float

class sharpeRatio(BaseModel):
    return_of_portfolio: float
    risk_free_rate: float
    standard_deviation_of_portfolio: float

class purchasingPower(BaseModel):
    current_amount: float
    current_inflation_rate: float
    target_inflation_rate: float

class monthlyEmi(BaseModel):
    principal_amount: float
    annual_rate: float
    months: int

class doublingTime(BaseModel):
    principal_amount: float
    annual_rate: float

class weightedAverage(BaseModel):
    values: list
    weights: list

class capitalAssetPricingModel(BaseModel):
    risk_free_rate: float
    beta: float
    expected_market_return: float

class costOfEquity(BaseModel):
    risk_free_rate: float
    beta: float
    expected_market_return: float

class cogs(BaseModel):
    beginning_inventory: float
    ending_inventory: float
    cost_of_goods_sold: float

class ruleof72(BaseModel):
    rate: float

class acidTestRatio(BaseModel):
    cash: float
    marketable_securities: float
    accounts_receivable: float
    current_liabilities: float

class inflationAdjustedReturn(BaseModel):
    nominal_return: float
    inflation_rate: float

class cogr(BaseModel):
    beginning_value: float
    ending_value: float
    number_of_periods: int

class currentLiabilityCoverageRatio(BaseModel):
    cash_flow_from_operations: float
    current_liabilities: float

class leveredBeta(BaseModel):
    unlevered_beta: float
    debt_to_equity_ratio: float
    tax_rate: float

class monthlyPayment(BaseModel):
    principal_amount: float
    annual_rate: float
    months: int

class convexityDuration(BaseModel):
    convexity: float
    duration: float
    change_in_yield: float

class currentRatio(BaseModel):
    current_assets: float
    current_liabilities: float

class inventoryTurnoverRatio(BaseModel):
    cost_of_goods_sold: float
    average_inventory: float

class inflationRate(BaseModel):
    current_price_index: float
    previous_price_index: float

class herfindalIndex(BaseModel):
    market_share: list

class discountOpex(BaseModel):  
    discount_rate: float
    opex: float

class projectEfficiency(BaseModel):
    cost_of_project: float
    present_value_of_cash_inflows: float

class realGDP(BaseModel):
    nominal_gdp: float
    gdp_deflator: float

class excessReserves(BaseModel):
    deposits: float
    required_reserves: float

class discountedCashFlow(BaseModel):
    cash_flow: float
    discount_rate: float
    time_period: int

class gdpGrowthRate(BaseModel):
    current_gdp: float
    previous_gdp: float

class creditCardEquation(BaseModel):
    balance: float
    interest_rate: float
    monthly_payment: float

class creditCardPayoff(BaseModel):
    balance: float
    interest_rate: float
    monthly_payment: float

class futureValueOfOrdinaryDue(BaseModel):
    periodic_payment: float
    interest_rate: float
    number_of_payments: int

class futureValueOfAnnuityDue(BaseModel):
    periodic_payment: float
    interest_rate: float
    number_of_payments: int

class presentValueOfAnnuityDue(BaseModel):
    periodic_payment: float
    interest_rate: float
    number_of_payments: int

class compoundAnnualGrowthRate(BaseModel):
    beginning_value: float
    ending_value: float
    number_of_periods: int

class loanToValue(BaseModel):
    loan_amount: float
    value_of_property: float

class retentionRatio(BaseModel):
    net_income: float
    dividends: float

class taxEquivalentYield(BaseModel):
    tax_free_yield: float
    tax_rate: float

class yearToYear(BaseModel):
    current_year: float
    previous_year: float

class futureValueOfAnnuity(BaseModel):
    periodic_payment: float
    interest_rate: float
    number_of_payments: int

class balloonBalance(BaseModel):
    loan_amount: float
    interest_rate: float
    number_of_payments: int

class periodicLeasePayment(BaseModel):
    present_value: float
    interest_rate: float
    number_of_payments: int

class weightedAverageOfValues(BaseModel):
    values: list
    weights: list

class discountedPaybackPeriod(BaseModel):
    cash_flow: float
    discount_rate: float

class yieldToMaturity(BaseModel):
    current_bond_price: float
    face_value: float
    years_to_maturity: int
    coupon_rate: float

class perpetuityPayment(BaseModel):
    interest_rate: float
    present_value: float

class zeroCoupounBondValue(BaseModel):
    face_value: float
    interest_rate: float
    years_to_maturity: int


class profitabilityIndex(BaseModel):
    initial_investment: float
    cash_flow: float
    discount_rate: float

class profitabilityIndex2(BaseModel):
    initial_investment: float
    cash_flow: float
    discount_rate: float
    number_of_years: int

class receivablesTurnoverRatio(BaseModel):
    net_credit_sales: float
    average_accounts_receivable: float

class remainingBalance(BaseModel):
    loan_amount: float
    interest_rate: float
    number_of_payments: int

class netPresentValue(BaseModel):
    initial_investment: float
    cash_flow: float
    discount_rate: float

class leverageRatioIncome(BaseModel):
    total_debt: float
    net_income: float

class leverageRatioEquity(BaseModel):
    total_debt: float
    total_equity: float

class timePeriodRequiredForGrowth(BaseModel):
    present_value: float
    future_value: float
    rate: float

class preferredStockValue(BaseModel):
    dividend: float
    required_rate_of_return: float

class assetTurnoverRatio(BaseModel):
    net_sales: float
    average_total_assets: float

class bidAskSpread(BaseModel):
    bid_price: float
    ask_price: float

class calculatePeriodFV(BaseModel):
    present_value: float
    future_value: float
    rate: float


class mortgageAmortization(BaseModel):
    loan_amount: float
    interest_rate: float
    number_of_payments: int

class enterpriseValue(BaseModel):
    market_capitalization: float
    total_debt: float
    cash_and_cash_equivalents: float

class salaryCalculate(BaseModel):
    salary: float
    pay_frequency: str

class lumpsum(BaseModel):
    initial_investment: float
    interest_rate: float
    number_of_payments: int

class refinance(BaseModel):
    current_loan_balance: float
    current_interest_rate: float
    current_loan_term: int
    new_interest_rate: float
    new_loan_term: int

class commissionCalc(BaseModel):
    sales_price: float
    commission_rate: float
    commission: float

class collegeCost(BaseModel):
    tuition_fee: float
    annual_increase: float
    years: int

class dilutedEps(BaseModel):
    net_income: float
    weighted_average_shares: float
    dilutive_securities: float

class asdcr(BaseModel):
    net_operating_income: float
    total_debt_service: float

class calculateGst(BaseModel):
    price: float
    gst_rate: float

class calculateMarketCap(BaseModel):
    price_per_share: float
    number_of_shares: float

class calculateExpectedReturnOfPortfolio(BaseModel):
    expected_return_of_asset_1: float
    expected_return_of_asset_2: float
    weight_of_asset_1: float
    weight_of_asset_2: float

class calculateFinancialLeverage(BaseModel):
    total_assets: float
    total_equity: float

class calculateGratuity(BaseModel):
    basic_salary: float
    dearness_allowance: float
    number_of_years: float
    gratuity_rate: float

class calculateMacaulayDuration(BaseModel):
    cash_flow: float
    discount_rate: float
    time_period: int

class calculateNetProfitMargin(BaseModel):
    net_income: float
    net_sales: float

class calculatePostTaxReturnPercentage(BaseModel):
    pre_tax_return: float
    tax_rate: float

class calculateSalary(BaseModel):
    salary: float
    pay_frequency: str

class capitalGainsYield(BaseModel):
    initial_price: float
    ending_price: float
    dividends: float

class capitalizationRate(BaseModel):
    net_operating_income: float
    property_value: float

class freeCashFlowToEquity(BaseModel):
    net_income: float
    capital_expenditure: float
    change_in_working_capital: float
    debt_issued: float
    debt_repaid: float

class loanAffordability(BaseModel):
    monthly_income: float
    monthly_debt: float
    interest_rate: float
    loan_term: int

class bondEquivalentYield(BaseModel):
    face_value: float
    price: float
    days_to_maturity: int

class calculateVat(BaseModel):
    price: float
    vat_rate: float

class loanToValueRatio(BaseModel):
    loan_amount: float
    value_of_property: float

class mortrage(BaseModel):
    loan_amount: float
    interest_rate: float
    number_of_payments: int

class netWorth(BaseModel):
    assets: float
    liabilities: float

class personalSavings(BaseModel):
    annual_salary: float
    monthly_expenses: float
    savings_rate: float
    annual_raise: float
    current_savings: float
    years: int

class portfolioReturnMonteCarlo(BaseModel):
    initial_investment: float
    annual_contribution: float
    annual_return: float
    standard_deviation: float
    years: int
    iterations: int

class calculateRetirementGoals(BaseModel):
    current_age: float
    retirement_age: float
    annual_salary: float
    annual_savings: float
    retirement_savings: float
    retirement_expenses: float
    retirement_income: float
    retirement_inflation: float

class balloonLoanPayment(BaseModel):
    loan_amount: float
    interest_rate: float
    number_of_payments: int

class monthlyLeasePayment(BaseModel):
    present_value: float
    interest_rate: float
    number_of_payments: int

class estimate401k(BaseModel):
    current_age: float
    retirement_age: float
    current_401k_balance: float
    annual_contribution: float
    annual_salary: float
    annual_raise: float
    employer_match: float
    employer_max_match: float

class rothIra(BaseModel):
    current_age: float
    retirement_age: float
    annual_contribution: float
    annual_salary: float
    annual_raise: float
    current_roth_balance: float
    expected_annual_return: float

class personalLoan(BaseModel):
    loan_amount: float
    interest_rate: float
    number_of_payments: int

class calculateBvps(BaseModel):
    total_equity: float
    number_of_shares: float

class capmRequest(BaseModel):
    risk_free_return:float
    sensitivity:float
    expected_market_return:float

class DebtServiceCoverageRatio(BaseModel):
	revenue: float
	operating_expenses: float
	interest: float
	tax_rate: float
	principal: float
        
class ProfitPercentage(BaseModel):
    profit: float
    cost_price: float

class LossPercentage(BaseModel):
    loss: float
    cost_price: float

class DefensiveIntervalRatio(BaseModel):
	cash: float 
	marketable_securities: float
	net_receivables: float
	annual_operating_expenses: float 
	non_cash_charges: float
        
class RateofReturn(BaseModel):
    initial_investment: float 
    final_value: float
    cash_flows: float
    time_period: float
    holding_period: float
      
class financialAssestRatio(BaseModel):
    current_assets: float
    current_liabilities: float
    total_debt: float
    total_equity: float
    net_income: float
    total_revenue: float

class CashConversionCycle(BaseModel):
	beginning_inventory: float 
	ending_inventory: float  
	beginning_receivables: float 
	ending_receivables: float  
	beginning_payable: float 
	ending_payable: float
	cost_of_goods_sold: float
	net_credit_sales: float
        
class PolicyPremium(BaseModel):
    policy_type: str
    age: int 
    coverage_amount: int  
    deductible: int 
    num_claims: int  
    num_accidents: int 
	

class PriceElasticity(BaseModel):
	initial_price: float 
	final_price: float  
	initial_quantity: float 
	final_quantity: float  

class AveragePaymentPeriod(BaseModel):
	beginning_accounts_payable: float
	ending_accounts_payable: float
	total_credit_purchases: float

class SavingGoal(BaseModel):
    current_savings: float 
    monthly_contributions : float  
    interest_rate: float 
    goal_amount: float

class ModifiedInternalRateOfReturn(BaseModel):
	ending_cash_flow: float
	initial_cash_flow: float
	number_of_periods: int

class InterestCoverageRatio(BaseModel):
	revenue:float
	cost_of_goods_services:float
	operating_expenses:float
	interest_expense:float

class TaxBracketCalculator(BaseModel):
	income:float
	filing_status:str

class MarginOfSafety(BaseModel):
	current_sales:float 
	break_even_point: float
