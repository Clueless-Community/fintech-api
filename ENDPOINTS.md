<h1 align=center> Endpoints we are providing 💫</h1>

**GET** `/simple_interest_rate`

- Required parameters : `amount_paid`, `principle_amount` and `months`
- Sample output

```py
{
    "Tag": "Simple Interest Rate",
    "Total amount paid": 5000.0,
    "Principle amount": 4500.0,
    "Interest Paid": 500.0,
    "Interest Rate": "11.11111111111111%"
}
```

**GET** `/payback_period`

- Required parameters : `years_before_recovery`, `unrecovered_cost` and`cash_flow`
- Sample output

```py
{
    "Tag": "Payback period",
    "Years before full recovery": 7,
    "Unrecovered cost at start of the year": 23000.0,
    "Cash flow during the year": 7000.0,
    "Payback period": "10.285714285714285"
}

```

**GET** `/compound_interest`
+ Required parameters : `principal_amount`, `intrest_rate`  , `years` and `compounding_period`
+ Sample output
```py
{
    "Tag": "Compound Intrest Amount",
    "Principle amount": 1000.0,
    "Intrest Rate": 0.05,
    "Time in Years": 2,
    "Compounding Period": 1,
    "Amount after intrest": "1102.5"
}
```

**GET** `/effective_annual_rate`
+ Required parameters : `annual_interest_rate`and `compounding_period`
+ Sample output
```py
{
  "Tag": "Effective Annual Rate",
  "Annual Intrest Rate": 0.05,
  "Compounding Period": 2,
  "Effective Annual Rate (in percentage)": "5.062499999999992%"

**GET** `/certificate_of_deposit`
+ Required parameters : `principal_amount`, `interest_rate`, `yrs`, and `compounding_per_yr`
+ Sample output
```py
{
    "Tag": "Certificate of Deposit (CD)",
    "Principal amount": 5000.0,
    "Interest Rate": 5.0,
    "Time in Years": 3,
    "Number of Compounding per Year": 1,
    "Certificate of Deposit (CD)": 5788.13,
}
```

**GET** `/roi`
+ Required parameters : `current_value_of_investment` and`cost_of_investment`
+ Sample output
```py
{
    "Tag": "Return on Investment",
  "Current Value of Investment": 120,
  "Cost of Investment": 100,
  "Return on Investment": "20.0%"
 }
 ```
 **GET** `/cagr`
 + Required parameters : `end_investment_value`, `initial_investment_value` and`years`
 + Sample output
 ```py
 {
    "Tag":"Compounded Annual Growth Rate",
    "End investment value":100000,
    "Initial investment value":70000,
    "Years":3,
    "Compunded Annual Growth Rate":0.12624788
 }
 ```
**GET** `/asset_portfolio`

- Required parameters : `price_A`, `price_B`, `return_A`, `return_B`, `standard_dev_A`, `standard_dev_B` and `correlation` where A and B refer to the 2 stocks.
- Sample output

```py
{
     "Tag": "Portfolio Variance",
     "Expected Returns": 16.8%,
     "Portfolio Variance": 0.046,
}
```

**GET** `/wacc`

- Required parameters : `firm_equity`, `firm_debt`, `cost_of_equity`, `cost_of_debt`, `corporate_tax_rate`
- Sample output
```py
{
    "Tag": "Weighted Average Cost of Capital(WACC)",
    "Marketvalue of firm's equity" : 30000000,
    "Market value of firm's debt" : 2000000,
    "Cost of equity" : 0.09,
    "Cost of debt" : 0.06,
    "Corporate tax rate" : 0.21,
    "WACC" : 7.3%,
}
```

**GET** `/loan_emi`

- Required parameters : `principle_amount`, `annual_rate` and `months`
- Sample output

```py
{
    "Tag": "Loan Emi",
    "Princiapl amount borrowed": 100000.0,
    "Annual Rate of interest": 7.0,
    "Total number of monthly payments": 120,
    "EMI": "1161.085",
    "Total Amount Payble": "139330.175",
    "Interest amount": "39330.175"
}
```

**GET** `/put-call-parity`

- Required parameters : `call_price`, `put_price` and `strike_price`
- Sample output

```py
{
  "Tag": "Pull Call Parity",
  "Future Price": "800.0",
  "Call Price": "1000.0",
  "Put Price": "500.0",
  "Strike Price": "300.0"
}
```

**GET** `/bep`

- Required parameters : `fixed_cost`, `selling_price` and `variable_cost`
- Sample Output

```py
{
    "Tag" : "Break Even Point (BEP)",
    "Fixed costs" : 2000,
    "Selling price per unit" : 1.50,
    "Variable cost per unit" : 0.40,
    "Break Even Point in units" : 1818.0,
    "Break Even Point in Rupees" : 2727,
}
```

**GET** `\fcff`
- Required parameters : `sales`,`operating_cost`,`depreciation`, `interest`,`tax_rate`,`fcInv` and `wcInv`
- Sample Output (for sales = 200, operating_cost = 20, depreciation = 20, interest = 30, tax_rate = 40%, wcInv = -40 and fcInv = 0
```py
{
    "Tag" : "Free Cash Flow to Firm (FCFF)",
    "Earnings before interest, taxes, depreciation and amortization" : 80.0,
    "Earnings before interest and taxes : " : 60.0 ,
    "Net Income" : 18.0,
    "Free Cash Flow to Firm" : 46.0,
}
```

**GET** `/price_to_earning_ratio`

- Required parameters : `share_price`, `earnings_per_share`
- Sample Output

```py
{
    "Tag" : "Price to Earning ratio",
    "Share price" : 200.0,
    "Earning per share" : 20.0,
    "Price to Earning ratio" : 10.0%,
}
```

**GET** `/dividend_yield_ratio`

- Required parameters : `dividend_per_share`, `share_price`
- Sample Output

```py
{
    "Tag":"Dividend yield ratio",
    "Dividend per share" : 200.0,
    "Share price" : 20.0,
    "Dividend yield ratio" : 10.0%,
}
```


**GET** `/dividend_payout_ratio`

- Required parameters : `dividend_per_share`, `earnings_per_share`
- Sample Output

```py
{
    "Tag":"Dividend payout ratio",
    "Dividend per share" : 200.0,
    "Earnings per share" : 20.0,
    "Dividend payout ratio" : 10.0%,
}
```


**GET** `/debt_to_income_ratio`
- Required parameters : `annual_income`, `total_debt_per_month`
- Sample Output
```py
{
  "Tag": "Debt to income ratio",
  "Annual income": 72000,
  "Total debt per month": 3600,
  "Debt to income ratio per month": "60.0%"
 }
```

**GET** `/fixed_charge_coverage_ratio`
- Required parameters : `earnings_before_interest_taxes`, `fixed_charge_before_tax`,`interest`
- Sample Output
```py
{

    "Tag":"fixed charges coverage ratio",
    "Earnings before interest taxes" : 3000000.0,
    "Fixed charge before tax" : 500000.0,
    "Interest" : 300000.0,
    "Fixed charges coverage ratio" : 4.375%,
}
```

**GET** `/inventory_shrinkage rate`
- Required parameters : `recorded_inventory`, `actual_inventory`
- Sample Output
```py
{
    "Tag":"Inventory shrinkage rate",
    "Recorded Inventory" : 38000,
    "Actual Inventory" : 35000,
    "Invenory Shrinkage Rate" : 0.07894736842105263,
    "Invenory Shrinkage Rate (%)" : 7.894736842105263,
}
```

**GET** `/markup_percentage`

- Required parameters : `price`, `cost`
- Sample Output
```py
{
    "Tag": "Markup Percentage",
    "Price": 50,
    "Cost": 5,
    "Markup Percentage": 900
}
```

**GET** `/sharpe_ratio`

- Required parameters : `portfolio_return`, `risk_free_rate`,`standard_deviation_of_portfolio`
- Sample Output
```py
{

  "Tag": "Sharpe Ratio",
  "Portfolio Return": 25,
  "Risk Free Rate": 5,
  "Standard Deviation of Portfolio": 10,
  "Sharpe Ratio": "2.0"

}
```

**GET** `/Capital_Asset_Pricing_Model`

- Required parameters : `risk_free_interest_rate`, `beta_of_security`,`expected_market_return`
- Sample Output
```py
{

  "Tag": "Capital_Asset_Pricing_Model",
  "risk_free_interest_rate": 2.5 + "%",
  "beta_of_security": 1.25,
  "expected_market_return": 7.5 + "%",
  "Capital_Asset_Pricing_Model": "11.9%"

}
```

**GET** `/cost_of_equity`
- Required parameters : `risk_free_rate_of_return`, `Beta`, `market_rate_of_return`
- Sample Output
```py
{
    "Tag": "Cost of Equity",
    "Risk free rate of return": 100,0,
    "Beta": 3.0,
    "Market rate of return ": 200.0,
    "Cost of equity": 400.0%

}
```

**GET** `/cogs`
- Required parameters : `beginning_inventory`,`purchases` and `ending_inventory`
- Sample Output
```py
{
   "Tag": "Cost of Goods Sold",
  "Beginning Inventory": 2000,
  "Purchases during the period": 1500,
  "Ending Inventory": 1000,
  "Cost of Goods Sold(In Rupees)": "2500.0"
}
```

**GET** `/purchasing_power`
+ Required parameters : `initial_amount`, `annual_inflation_rate`  , `time`
+ Sample output
```py
{
     "Tag": "Purchasing Power",
     "Initial Amount": 10000,
     "Annual Inflation Rate": 5,
     "Time in years": 10,
     "Purchasing Power": 6139.13253540759
}
```
**GET** `/monthly_emi`
+ Required parameters : `loan_amt`,`interest_rate`,`number_of_installments`
+ Sample output
```py
{
    "Tag": "Monthly EMI",
    "Loan Amount": 500000,
    "Interest Rate":8,
    "Number of Installments":24,
    "Total EMI": 22613.645728092295
}
```

**GET** `/doubling_time`
+ Required parameters : `r`
+ Sample output
```py
{
    "Tag": "Doubling Time",
    "Rate of Interest": 8,
    "Time in years to double the money": 9.006468342000588
}
```

**GET** `/weighted_average`
+ Required parameters : `ratio`,`rates`
+ Sample output
```py
{
    "Tag": "Weighted Average",
    "Ratio of each investment principal": [0.20, 0.25, 0.35,0.10, 0.10],
    "Rates":[7.5, 8.5, 8, 5, 6],
    "Weighted average : ": 7.525
}
```

=======
**GET** `/ruleof72`
- Required parameters : `rate_of_roi` it should be in percentage only
- Sample output
```py
{
    "Tag": "Rule of 72",
    "Rate of ROI": 5,
    "Time peroid in which investment get double(in years)": "14.4"
}
```
**GET** `/acid-test-ratio`
- Required parameters : `cash`,`marketable_securities`,`accounts_receivable` and `current_liabilities` Note : cash = cash + cash equivalents
- Sample Outuputs
```py
{
    "Tag": "Acid Test Ratio",
    "Cash and Cash Equivalents": 10000,
    "Marketable Securities": 5000,
    "Accounts Receivable": 20000,
    "Current Liabilities": 30000,
    "Acid Test Ratio (Quick Ratio)": "1.17"
}
```
**GET** `/inflation-adjusted-return`
- Required parameters : `beginning_price`, `ending_price`, `dividends`, `beginning_cpi_level` and `ending_cpi_level`
- Sample output
```py
{
    "Tag": "Inflation Adjusted Return",
    "Stock Return": "0.23333333333333334%",
    "Inflation Rate": "0.03%",
    "Inflation Adjusted Return": "19.74%"
}
```
**GET** `/cogr`
- Required parameters : `beginning_value`, `ending_value` and `years`
- Sample output
```py
{
    "Tag": "Coumpound Annual Growth Rate",
    "Beginning Value": 176000,
    "Ending Value": 64900,
    "Compound Annual Growth Rate": "39.5%"
}
```

**GET** `/levered_beta`
- Required parameters : `unlevered_beta`, `tax_rate`, `debt`,`equity`
- Sample output
```py
{
    "Tag": "Levered Beta",
    "Unlevered Beta": 10.0,
    "Tax rate":0.5,
    "debt": 100.0,
    "Equity": 50.0,
    "Levered Beta":20.0% 
}
```

**GET** `/convexity_duration`
- Required parameters : `rate`,`coupon_rate`,`frequency`,`face_value`,`settlement_date`,`maturity_date`
- Sample output
```py
{
        "Tag": "Convexity Adjusted Duration",   
        "Market Rate": 6,
        "Coupon rate":10,
        'Frequency':2
        "Face Value": 100,
        "Settlement Date": '1-1-2020',
        "Maturity Date": '10-10-2024',
        "Convexity Adjusted Duration":3.437535660034277
}
```
