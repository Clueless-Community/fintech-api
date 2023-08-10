def ppf_calculator(depos:int,tenure:int,interest:float):
    try:
        rate = functions.ppf_calculator(depos, tenure, interest)
        return {
            "Tag": "PPF Calculator",
            "Total amount invested annualy": depos,
            "No. of years": tenure,
            "percentage interst rate": interest,
            "Final Total value": f"{total_value}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)