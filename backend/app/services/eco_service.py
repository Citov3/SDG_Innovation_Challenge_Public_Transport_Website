# services/eco_service.py
"""
Calculates carbon footprint based on:
- Transportation mode
- Distance traveled
- Adjusted emission factors
"""

class EcoService:

    # Emission factors per km (example values)
    FACTORS = {
        "subway": 0.04,
        "bus": 0.12,
        "car": 0.25,
        "bike": 0.0,
        "walk": 0.0
    }

    def calculate_emissions(self, mode: str, distance: float):
        factor = self.FACTORS.get(mode.lower(), 0.2)
        emissions = factor * distance
        return {
            "mode": mode,
            "distance_km": distance,
            "co2_kg": round(emissions, 3)
        }
