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

