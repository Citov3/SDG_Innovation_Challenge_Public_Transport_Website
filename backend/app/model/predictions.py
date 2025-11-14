# models/predictions.py

from pydantic import BaseModel
from typing import Optional, Dict

class RoutePrediction(BaseModel):
    best_route: Dict                        # Full route details
    eta_minutes: float                      # Estimated travel time
    congestion_level: Optional[str]         # "low", "medium", "high"
    carbon_savings_percent: float           # % saved vs driving
