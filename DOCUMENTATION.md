| Endpoint                    | Description                                  | Parameters                                                |
|-----------------------------|----------------------------------------------|-----------------------------------------------------------|
| GET /simple_interest_rate   | Calculate simple interest rates              | - `amount_paid` (float): The amount paid.                 |
|                             |                                              | - `principle_amount` (float): The principle amount.       |
|                             |                                              | - `months` (int): The number of months.                   |
| GET /future_sip             | Calculate Future Value of SIP                | - `interval_investment` (float): The interval investment  |
|                             |                                              | - `rate_of_return` (float): The rate of return.           |
|                             |                                              | - `number_of_payments` (int): The number of payments.     |
| --------------------------- | ----------------------------------------     | --------------------------------------------------------- |
| POST /capm                  | Calculate Capital Asset Pricing Model (CAPM) | - `risk_free_return` (float): Risk-free rate of return.            |
|                             |                                              | - `sensitivity` (float): Asset's sensitivity.            |
|                             |                                              | - `expected_market_return` (float): Expected return of the market. |

| --------------------------- | ----------------------------------------     | --------------------------------------------------------- |

| POST /risk_assessment        | Perform Risk Assessment                      | - `age` (integer): The age of the individual.           |
|                             |                                              | - `financial_goals` (string): Financial goals of individual|
|                             |                                              | - `investment_knowledge`(string):Investment knowledge level|
|                             |                                              |- `time_horizon` (string):Investment time horizon         |

| --------------------------- | ----------------------------------------     | --------------------------------------------------------- |

| GET /calculate_risk_score   |  Calculate Risk Score                        |  - `age` (integer): The age of the individual.           |
|                             |                                              | - `financial_goals` (string): Financial goals of individual|
|                             |                                              | - `investment_knowledge`(string):Investment knowledge level|
|                             |                                              |- `time_horizon` (string):Investment time horizon         |
