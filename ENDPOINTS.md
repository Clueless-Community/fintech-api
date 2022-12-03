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