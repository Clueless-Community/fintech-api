| Endpoint                     | Description                            | Parameters                                              |
|---------------------------   |----------------------------------------|---------------------------------------------------------|
| GET /simple_interest_rate    | Calculate simple interest rates        | - `amount_paid` (float): The amount paid.               |
|                              |                                        | - `principle_amount` (float): The principle amount.     |
|                              |                                        | - `months` (int): The number of months.                 |
| GET /future_sip              | Calculate Future Value of SIP          | - `interval_investment` (float): The interval investment|
|                              |                                        | - `rate_of_return` (float): The rate of return.         |
|                              |                                        | - `number_of_payments` (int): The number of payments.   |
|POST/gross_margin_ratio       |Calculating the Gross Margin Ratio      | - `net_sales`(int):Net Sales                            |
|                              |                                        | - `gross_profit`(int):Gross Profit                      |
|POST/price_earnings_ratio     |Calculating the Price Earnings Ratio    | - `share_price`(int):Share Price                        |
|                              |                                        | - `earnings_per_share`(int):Earnings Per Shares         |
|POST/earnings_per_share_ratio |Calculating Earnings Per Share Ratio    | - `net_earnings`(int):Net Earnings                      |
|                              |                                        | - `total_share_outstanding`(int):Total Share Outstanding|
