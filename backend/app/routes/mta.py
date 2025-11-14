# routes/mta.py
"""
Defines REST API endpoints related to:
- MTA station status
- Train arrival predictions
- GTFS schedule lookups
"""

from fastapi import APIRouter
from services.mta_service import MTAService

router = APIRouter()
mta_service = MTAService()

@router.get("/status")
async def get_mta_status():
    """
    Returns real-time status for subway lines & stations.
    """
    return mta_service.get_system_status()

@router.get("/schedule/{station_id}")
async def get_schedule(station_id: str):
    """
    Returns next scheduled trains for a specific station.
    """
    return mta_service.get_station_schedule(station_id)
