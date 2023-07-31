| Endpoint                         | Description                            | Parameters                                                     |
|----------------------------------|----------------------------------------|----------------------------------------------------------------|
| GET /simple_interest_rate        | Calculate simple interest rates        | - `amount_paid` (float): The amount paid.                      |
|                                  |                                        | - `principle_amount` (float): The principle amount.            |
|                                  |                                        | - `months` (int): The number of months.                        |
| GET /future_sip                  | Calculate Future Value of SIP          | - `interval_investment` (float): The interval investment       |
|                                  |                                        | - `rate_of_return` (float): The rate of return.                |
|                                  |                                        | - `number_of_payments` (int): The number of payments.          |
|  POST /net_income                | Calculate Net Income                   | - `revenue` (float): The revenue.                              |
|                                  |                                        | - `expenses` (float): The revenue.                             |
|  POST/break_even_point           | Calculate Break-even point             | - `fixed_costs` (int): The Fixed Cost                          |
|                                  |                                        | - `sales_price_per_unit`(float):The sales price per unit       |
|                                  |                                        | - `variable_price_per_unit`(float):variable price per unit     |
|POST/day_sales_in_inventory_ratio | Calculate Day Sales in Inventory Ratio | - `avg_inventory` (int): The average inventory.                |
|                                  |                                        | - `cost_of_goods_sold` (int):The cost of goods sold.           |
|                                  |                                        | - `no_of_days` (int): The number of days.                      |
| POST /cash_ratio                 | Calculate Cash Ratio                   | - `cash` (float): The Cash Amount                              |
|                                  |                                        | - `cash_equivalents` (float): The cash equivalents.            |
|                                  |                                        | - `current_liabilities` (float):The Current liabilities.       |
