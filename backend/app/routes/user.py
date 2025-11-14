# routes/user.py
# FastAPI endpoints for user operations

from fastapi import APIRouter, HTTPException
from models.user import User
from database.mongo import users_collection
from bson.objectid import ObjectId

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register")
def register_user(user: User):
    user_dict = user.dict()
    user_dict.pop("id")  
    result = users_collection.insert_one(user_dict)
    return {"message": "User registered", "id": str(result.inserted_id)}


@router.get("/{user_id}")
def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(404, "User not found")
    user["id"] = str(user["_id"])
    return user
