
from helpers import functions
from fastapi import HTTPException, status


def interest_coverage_ratio_task(revenue:float, cost_of_goods_services:float, operating_expenses:float, interest_expense:float):
	try:
		EBIT = revenue - cost_of_goods_services - operating_expenses
		ratio = functions.interest_coverage_ratio(revenue, cost_of_goods_services, operating_expenses, interest_expense)
		return{
			"Tag": "Interest Coverage Ratio",
			"Revenue": revenue,
			"Cost of Goods and Services": cost_of_goods_services,
			"Operating Expenses": operating_expenses,
			"Interest Expenses": interest_expense,
			"Earnings Before Interest and Taxes": EBIT,
			"Interest Coverage Ratio": f"{ratio}%",
		}

	except:
        	return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
