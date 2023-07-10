from helpers import functions
from fastapi import HTTPException, status

def weighted_average_of_values_task(Assigned_weight_values: str, data_point_values: str):
    try:
        weighted_average = functions.weighted_average_of_values(
            Assigned_weight_values, data_point_values
        )
        return {
            "Tag": "weighted_average",
            "Assigned weight values": Assigned_weight_values,
            "Data point values": data_point_values,
            "Weighted average": f"{weighted_average}",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)