from typing import List
from database.connection import client
from fastapi import APIRouter, Body, HTTPException, status
from models.heart_condition import Heart
from schemas.heart_condition import heartEntity, heartsEntity
from bson import ObjectId

prediction_router = APIRouter(
    tags=["Prediction"]
)

@prediction_router.post("/")
async def get_prediction(body: Heart = Body(...)):
    return heartsEntity(client.heart_disease_api.heart_condition.find())