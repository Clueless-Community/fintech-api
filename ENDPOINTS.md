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
