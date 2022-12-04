<h1 align=center> Endpoints we are providing 💫</h1>

**GET** `/simple_interest_rate`
+ Required parameters : `amount_paid`, `principle_amount` and `months`
+ Sample output
```py
{
    "Tag": "Simple Interest Rate",
    "Total amount paid": 5000.0,
    "Principle amount": 4500.0,
    "Interest Paid": 500.0,
    "Interest Rate": "11.11111111111111%"
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

