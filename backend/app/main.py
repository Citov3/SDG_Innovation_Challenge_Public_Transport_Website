# main.py
"""
Main entry point for the backend.

This file initializes:
- FastAPI application
- All route blueprints
- Middleware (CORS, Logging, etc.)
- DB connections (optional)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from routes import mta, traffic, eco, user

app = FastAPI(
    title="Transit Optimization API",
    description="Backend for multimodal transit, eco-scoring, and routing",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route blueprints
app.include_router(mta.router, prefix="/mta")
app.include_router(traffic.router, prefix="/traffic")
app.include_router(eco.router, prefix="/eco")
app.include_router(user.router, prefix="/user")

@app.get("/")
def home():
    return {"message": "Transit Optimization Backend Running"}

