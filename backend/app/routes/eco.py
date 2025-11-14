# routes/eco.py
"""
Eco scoring routes:
- Carbon footprint for route
- Compare modes (subway vs car vs bus)
"""

from fastapi import APIRouter
from services.eco_service import EcoService

router = APIRouter()
eco = EcoService()

@router.get("/score")
def eco_score(mode: str, distance_km: float):
    """
    Returns estimated CO2 emissions for the given route.
    """
    return eco.calculate_emissions(mode, distance_km)
