# routes/traffic.py
"""
Traffic API routes:
- Live congestion
- Estimated delay time
- Road closure reports
"""

from fastapi import APIRouter
from services.traffic_service import TrafficService

router = APIRouter()
traffic_service = TrafficService()

@router.get("/live")
def get_live_traffic():
    return traffic_service.get_live_traffic()

@router.get("/eta")
def calculate_eta(origin: str, destination: str):
    return traffic_service.get_eta(origin, destination)
