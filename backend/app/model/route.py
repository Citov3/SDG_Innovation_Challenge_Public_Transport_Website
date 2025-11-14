# models/route.py
# Represents a route that user generates/requests

from pydantic import BaseModel
from typing import List, Optional

class Route(BaseModel):
    id: Optional[str] = None
    origin: str                             # "34 St - Penn Station"
    destination: str                        # "Times Square"
    travel_time_minutes: float
    modes_used: List[str]                   # ["subway", "walk"]
    carbon_score: float                     # grams of CO2
    timestamp: Optional[str] = None         # When user requested the route
