from helpers import functions
from fastapi import HTTPException, status

def calculate_net_profit_margin_task(revenue: float,
                                cost_of_goods_sold: float,
                                operating_expenses: float,
                                other_expenses: float,
                                interest: float,
                                taxes: float):
    try:
        net_profit_margin = functions.calulate_net_profit_margin(
            revenue, cost_of_goods_sold, operating_expenses, other_expenses, interest, taxes)
        return {
            "Tag": "Calculate net profit margin",
            "Revenue": revenue,
            "Cost of goods sold": cost_of_goods_sold,
            "Operating Expenses": operating_expenses,
            "Interest": interest,
            "Taxes": taxes,
            "Net Profit Margin": net_profit_margin,

        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)