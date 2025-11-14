# utils/geo_utils.py
# Used for calculating distances, ETA estimates, carbon numbers

from geopy.distance import geodesic

def calculate_distance(coord1, coord2):
    """
    Takes two coordinates:
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)
    Returns distance in kilometers.
    """
    return geodesic(coord1, coord2).km


def estimate_walking_time(distance_km):
    """ Walking speed ~ 5 km/h """
    return (distance_km / 5) * 60


def estimate_bike_time(distance_km):
    """ Bike speed ~ 15 km/h """
    return (distance_km / 15) * 60
