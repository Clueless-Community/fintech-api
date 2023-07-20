from helpers import functions
from fastapi import HTTPException, status

def project_efficiency_task(annual_production: float, collector_surface: float, dni: float):
    try:
        project_eff = functions.project_efficiency(
            annual_production, collector_surface, dni
        )
        return {
            "Tag": "Project efficiency",
            "Annual production": annual_production,
            "collector surface": collector_surface,
            "dni": dni,
            "Discount opex": f"{project_eff}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)