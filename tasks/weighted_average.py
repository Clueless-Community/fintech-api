from helpers import functions
from fastapi import HTTPException, status

def weighted_average_task(ratio: list, rates: list):
    try:
        weighted_average = functions.weighted_average(ratio, rates)
        return {
            "Tag": "Weighted Average",
            "Ratio of each investment principal": ratio,
            "Rates": rates,
            "Weighted average : ": f"{weighted_average}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)