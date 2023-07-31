| Endpoint                       | Description                              | Parameters                                                             |
|--------------------------------|------------------------------------------|---------------------------------------------------------               |
| GET /simple_interest_rate      | Calculate simple interest rates          | - `amount_paid` (float): The amount paid.                              |
|                                |                                          | - `principle_amount` (float): The principle amount.                    |
|                                |                                          | - `months` (int): The number of months.                                |
| GET /future_sip                | Calculate Future Value of SIP            | - `interval_investment` (float): The interval investment               |
|                                |                                          | - `rate_of_return` (float): The rate of return.                        |
|                                |                                          | - `number_of_payments` (int): The number of payments.                  |
|POST/book_value_per_share_ratio |Calculating the Book Value Per Share Ratio| - `shareholders_equity`(int):Shareholders Equity                       |
|                                |                                          | - `preferred_equity`(int):Preferred Equity                             |
|                                |                                          | -` total_common_share_outstanding`(int):Total Common Share Outstanding |
|POST/operating_margin_ratio     |Calculating the Operating Margin Ratio    | -` operating_income`(int):Operating Income                             |
|                                |                                          | -` net_sales`(int):Net Sales                                           | 



