# services/mta_service.py
"""
Handles communication with MTA APIs & GTFS files.

This layer:
- Fetches real-time data from MTA API
- Parses GTFS schedule files
- Cleans + formats transit data for the API routes
"""

import requests
import json

class MTAService:

    def __init__(self):
        # Load API key (in real app, use environment variable)
        self.API_KEY = "YOUR_MTA_API_KEY"

    def get_system_status(self):
        """
        Fetch MTA real-time status feed.
        Returns delay info, line status, etc.
        """
        url = f"https://api.mta.info/serviceStatus?key={self.API_KEY}"
        response = requests.get(url)
        return response.json()

    def get_station_schedule(self, station_id):
        """
        Parses GTFS schedule to get next arrival times.
        """
        # Placeholder example
        return {
            "station": station_id,
            "next_trains": [
                {"line": "A", "arrival": "3 mins"},
                {"line": "C", "arrival": "8 mins"}
            ]
        }
