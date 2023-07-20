from helpers import functions
from fastapi import HTTPException, status

def cash_conversion_cycle_task(beginning_inventory: float, ending_inventory: float, beginning_receivables: float, 
ending_receivables: float, beginning_payable: float, ending_payable: float, cost_of_goods_sold: float,
net_credit_sales: float):
    try:
        average_inventory = beginning_inventory - ending_inventory / 2
        average_receivables = beginning_receivables - ending_receivables / 2
        average_payable = beginning_payable - ending_payable / 2
        days_of_inventory_outstanding = (average_inventory / cost_of_goods_sold) * 365 
        days_of_sales_outstanding = (average_receivables / net_credit_sales) * 365
        days_of_payables_outstanding = (average_payable / cost_of_goods_sold / 365)
        ccc = functions.cash_conversion_cycle(beginning_inventory, ending_inventory, beginning_receivables, 
		ending_receivables, beginning_payable, ending_payable, cost_of_goods_sold, net_credit_sales)
        return {
            "Tag": "Cash Conversion Cycle",
            "Beginning Inventory": beginning_inventory,
            "Ending Inventory": ending_inventory,
            "Average Inventory": average_inventory,
            "Beginning Receivables": beginning_receivables,
            "Ending Receivables": ending_receivables,
            "Average Receivables": average_receivables,
            "Beginning Payable": beginning_payable,
            "Ending Payable": ending_payable,
            "Average Payable": average_payable,
            "Days of inventory_outstanding": days_of_inventory_outstanding,
            "Days of Sales Outstanding": days_of_sales_outstanding,
            "Days of Payables Outstanding": days_of_payables_outstanding,
            "Cash Conversion Cycle": f"{ccc} days",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
