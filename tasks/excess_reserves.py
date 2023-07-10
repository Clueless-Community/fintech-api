from helpers import functions
from fastapi import HTTPException, status

def excess_reserves_task(deposits: float, reserve_requirement: float):
    try:
        excess_reserves = functions.excess_reserves(
            deposits, reserve_requirement)
        return {
            "Tag": "Excess Reserves",
            "Deposits": deposits,
            "Reserve Requirement": reserve_requirement,
            "Excess Reserves": excess_reserves,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)