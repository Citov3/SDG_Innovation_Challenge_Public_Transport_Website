# models/user.py
# Pydantic model for user accounts

from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None              # MongoDB ID (stringified ObjectId)
    name: str
    email: EmailStr
    password: str                          # Will be hashed before saving
    saved_routes: List[str] = []           # List of saved route IDs
    preferred_mode: Optional[str] = None   # bus, subway, bike, walking
