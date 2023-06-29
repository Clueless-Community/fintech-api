from helpers import functions
from fastapi import HTTPException, status

def free_cash_flow_to_equity_task(
        total_revenues: float,
        total_expenses: float,
        initial_cost_of_asset: float,
        lifetime_of_asset: float,
        change_in_PPE: float,
        current_depreciation: float,
        current_assets: float,
        current_liabilities: float,
        amount_a_company_borrows: float,
        debt_it_repays: float):
    try:
        fcfe = functions.free_cash_flow_to_equity(
            total_revenues, total_expenses, initial_cost_of_asset, lifetime_of_asset,
            change_in_PPE, current_depreciation, current_assets, current_liabilities,
            amount_a_company_borrows, debt_it_repays
        )
        net_income = total_revenues - total_expenses,
        depreciation_and_amortization = initial_cost_of_asset / lifetime_of_asset,
        capEx = change_in_PPE + current_depreciation,
        change_in_working_capital = current_assets - current_liabilities,
        net_borrowing = amount_a_company_borrows - debt_it_repays,

        return {
            "Tag": "Free Cash Flow to Equity",
            "Total Revenues": total_revenues,
            "Total Expenses": total_expenses,
            "Inital Cost of Asset": initial_cost_of_asset,
            "Life Time of Asset": lifetime_of_asset,
            "Change in Price, Property or Equity": change_in_PPE,
            "Current Depreciation": current_depreciation,
            "Current Assets": current_assets,
            "Current Liabilities": current_liabilities,
            "Amount a Company Borrows": amount_a_company_borrows,
            "Debt it Repays": debt_it_repays,
            "Net Income": net_income,
            "Depreciation and Amortization": depreciation_and_amortization,
            "Capital Expenditures": capEx,
            "Change in Working Capital": change_in_working_capital,
            "Net Borrowing": net_borrowing,
            "Free Cash Flow to Equity": fcfe
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)