from helpers import functions
from fastapi import HTTPException, status

def accounts_payable_turnover_ratio_task(total_supply_purchases: float,
                                    beginning_accounts_payable: float,
                                    ending_accounts_payable: float):
    try:
        ap_turnover_ratio = functions.accounts_payable_turnover_ratio(total_supply_purchases,
                                                         beginning_accounts_payable,
                                                         ending_accounts_payable)
        return {
            "Tag": "Accounts Payable Turnover Ratio",
            "Total Supply Purchases": total_supply_purchases,
            "Beginning Accounts Payable": beginning_accounts_payable,
            "Ending Accounts Payable": ending_accounts_payable,
            "Accounts Payable Turnover Ratio": ap_turnover_ratio
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)