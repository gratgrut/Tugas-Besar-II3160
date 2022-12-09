from typing import List
from database.connection import client
from fastapi import APIRouter, Body, HTTPException, status, Request
from models.heart_condition import Heart
from schemas.heart_condition import heartEntity, heartsEntity
from utils import authorize

heart_router = APIRouter(
    tags=["Hearts"]
)

@heart_router.get("/", response_model=List[Heart])
async def retrieve_all_hearts(request: Request) -> List[Heart]:
    authorize(request)
    return heartsEntity(client.heart_disease_api.heart_condition.find())

@heart_router.get("/{id}")
async def retrieve_heart(id: int) -> Heart:
    try:
        result = heartEntity(client.heart_disease_api.heart_condition.find_one({"id":id}))
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Heart condition with supplied ID does not exist"
        )
    return result

@heart_router.post("/new")
async def add_heart(body: Heart = Body(...)) -> dict:
    client.heart_disease_api.heart_condition.insert_one(dict(body))
    return {
        "message": "Heart condition added"
    }

@heart_router.put("/{id}")
async def update_heart(id, heart: Heart):
    try:
        client.heart_disease_api.heart_condition.find_one_and_update({"id":id},{"$set":dict(heart)})
        return {
            "message": "Heart condition updated"
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Heart condition with supplied ID does not exist"
        )  

@heart_router.delete("/{id}")
async def delete_heart(id: int):
    try:
        result = heartEntity(client.heart_disease_api.heart_condition.find_one_and_delete({"id":id}))
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Heart condition with supplied ID does not exist"
        )
    return result