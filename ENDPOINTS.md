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
+ Required parameters : `gain_from_investment` and`cost_of_investment`
+ Sample output
```py
{
    "Tag":"Return on Investment",
    "Gain from Investment":100,
    "Cost of Investment":2,
    "Return on Investment":f"49.0%"
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