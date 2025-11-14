# database/mongo.py
"""
Creates a MongoDB client connection for storing:
- User accounts
- Saved routes
- Historical predictions
"""

from pymongo import MongoClient

def get_mongo_client():
    client = MongoClient("mongodb://localhost:27017/")
    return client
