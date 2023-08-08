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
| POST /debt_service_coverage_ratio | Calculate Debt Service Coverage Ratio  | - `revenue` (float): Amount of Company Revenue.           |
|                                   |                                        | - `operating_expenses` (float): Cost of operating expenses.|
|                                   |                                        | - `interest` (float): Amount of interest to be paid       |
|                                   |                                        | - `tax_rate` (float): The tax rate applied.               |
|                                   |                                        | - `principal` (float): Amount of principal borrowed.      |
| -------------------------------   | ------------------------------------   | --------------------------------------------------------- |
| POST /profit_percent | Calculate profit percentage  | - `profit` (float): Total profit earned.           |
|                                   |                                        | - `cost_price` (float): The original price of the item |
| POST /loss_percent | Calculate loss percentage  | - `loss` (float): Total loss occured.           |
|                                   |                                        | - `cost_price` (float): The original price of the item |
| POST /defensive_interval_ratio | Calculate Defensive Interval Ratio        | - `cash` (float): The amount of cash on hand.             |
|                                |                                           | - `marketable_securities` (float): The amount of marketable_securities.|
|                                |                                           | - `net_receivables` (float): The amount of net_receivables.|
|                                |                                           | - `annual_operating_expenses` (float): The amount of annual_operating_expenses.|
|                                |                                           | - `non_cash_charges` (float): The amount of non cash charges.|
|-----------------------------|----------------------------------------------|-----------------------------------------------------------|
| post /rate_of_return   | Calculate Rate of Return                         | - `initial_investment` (float): Initial amount invested.                 |
|                             |                                              | - `final_value` (float): the value of the investment at the end of the investment.       |
|                             |                                              | - `time_period` (float): The number of months.                   |
|                             |                                              | - `cash_flows`  (float): A list of cash flows over the investment period.                   |
|                             |                                              | - `holding_period` (float): The specific holding period of the investment.                   |
| --------------------------- | ----------------------------------------     | --------------------------------------------------------- |
| GET /financial_assest_ratio   | Calculate financial assest ratio           | - `current_assets` (float): used up within a short period.                 |
|                             |                                            | - `current_liabilities` (float): debts that are due .       |
|                             |                                              | - `total_debt` (float): aggregate amount of money.                   |
|                             |                                              | - `total_equity`(float): residual interest in the assets.                   |
|                             |                                              | - `net_income` (float): net earnings.                   |
|                             |                                              | - `total_revenue` (float): sum of all sales.                   |

|----------------------------|----------------------------------------|-------------------------------------------------------------------------------|
| GET /cash_conversion_cycle | Calculate Cash Conversion Cycle  | - `beginning_inventory` (float): The amount of inventory beginning the cycle. |
|                            |                                  | - `ending_inventory` (float): The final amount of inventory ending the cycle. |
|                            |                                  | - `beginning_receivables` (float): The amount of receivables beginning the cycle. |
|                            |                                  | - `ending_receivables` (float): The final amount of receivables ending the cycle. |
|                            |                                  | - `beginning_payable` (float): The amount of payable beginning the cycle. |
|                            |                                  | - `ending_payable` (float): The final amount of payable ending the cycle. |
|                            |                                  | - `cost_of_goods_sold` (float): The total cost related to producing goods sold by a business. |
|                            |                                  | - `net_credit_sales` (float): Sales where the cash is collected at a later date. |
|----------------------------|----------------------------------------|----------------------------------------------------------------------|
| GET /policy_premium | Calculate Policy Premium                | - `policy_type` (str): The type of insurance policy. |
|                            |                                  | - `age` (int): The age of the policyholder. |
|                            |                                  | - `coverage_amount` (int): The desired coverage amount for the policy. |
|                            |                                  | - `deductible` (int): The deductible amount for the policy.|
|                            |                                  | - `num_claims` (int): The number of claims made by the policyholder. |
|                            |                                  | - `num_accidents` (int): The number of accidents the policyholder has been involved in. |
| GET /price_elasticity | Price Elasticity for Demand Calculator | - `initial_price` (float): 
The initial price of the product or service. |
|                            |                                  | - `final_price` (float): The final price of the product or service. |
|                            |                                  | - `initial_quantity` (float): The initial quantity demanded of the product or service. |
|                            |                                  | - `final_quantity` (float): The final quantity demanded of the product or service. |
|----------------------------|----------------------------------------|----------------------------------------------------------------------|
| GET /average_payment_period | Calculate Average Payment Period       | - `beginning_accounts_payable` (float): The amount of accounts payable beginning the cycle. |
|                             |                                        | - `ending_inventory` (float): The final amount of accounts payable ending the cycle. |
|                             |                                        | - `total_credit_purchases` (float): The amount of purchases on credit during the cycle. |
|-----------------------------|----------------------------------------|---------------------------------------------------------------------|
| GET /saving_goal            | Saving Goal Calculator                 | - `current_savings` (float): The current amount of savings. |
|                             |                                        | - `monthly_contributions` (float): The amount of money contributed each month towards the savings goal. |
|                             |                                        | - `interest_rate` (float): The annual interest rate on the savings. |
|                             |                                        | - `goal_amount ` (float): The desired savings goal amount. |
|-----------------------------|----------------------------------------|----------------------------------------------------------------------|
| POST /interest_coverage_ratio | Calculate interest coverage ratio    | - `revenue` (float): The amount of income generated through business operations.  |
|                               |                                      | - `cost_of_goods_services` (float): Total amount of costs spent on goods and services.|
|                               |                                      | - `operating_expenses` (int): The amount of operating expenses. |
|                               |                                      | - `interest_expense` (int): The cost incurred by an entity for borrowed funds. |
|-------------------------------|----------------------------------------|---------------------------------------------------------|
| POST /tax_bracket_calculator | Calculate Tax Bracket Calculator    | - `income` (float): The total income earned by the individual.  |
|                               |                                      | - `filing_status` (String): The tax filing status of the individual.|
|-------------------------------|----------------------------------------|---------------------------------------------------------|
| POST /margin_of_safety        | Calculate margin of safety             | - `current_sales` (float): The amount of current sales. |
|                               |                                        | - `break_even_point` (float): The break_even_point amount. |
|--------------------------- ---|----------------------------------------|---------------------------------------------------------|
