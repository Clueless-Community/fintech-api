from helpers import functions
from fastapi import HTTPException, status

def calculate_salary_task(base: int,
                     jb: int,
                     stock: int,
                     pb: int,
                     bonus: int,
                     ptax: int,
                     deduction: int):
    try:
        calculate_salary = functions.calculate_salary(
            base, jb, stock, pb, bonus, ptax, deduction)
        return {

            "Tag": "Net Salary Calculator",
            "Base Salary per month": base,
            "joining bonus/retention bonus": jb,
            "RSU/stock bonus": stock,
            "performance bonus": pb,
            "any additional bonus": bonus,
            "tax percentage": ptax,
            "any additional deduction": deduction,
            "ctc calculated": f"{ctc}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)