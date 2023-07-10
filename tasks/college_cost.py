from helpers import functions
from fastapi import HTTPException, status

def college_cost_task(
    book_cost: float,
    college_tuition: float,
    Devices: float,
    travel_expenses: float,
    hostel_charges: float,
    mess_fee: float,
    miscellaneous: float,
):
    try:
        cost = functions.college_cost(
            book_cost,
            college_tuition,
            Devices,
            travel_expenses,
            hostel_charges,
            mess_fee,
            miscellaneous,
        )
        return {
            "Tag": "College Cost",
            "Books cost of one year": book_cost,
            "College tuition fee per year": college_tuition,
            "Electronic devices cost": Devices,
            "Monthly Travel expenses": travel_expenses,
            "Monthly Hostel charges": hostel_charges,
            "Monthly mess fee": mess_fee,
            "monthly miscellaneous expenses": miscellaneous,
            "Total cost of one year": cost,
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)