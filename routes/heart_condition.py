from typing import List
from database.connection import conn
from fastapi import APIRouter, Body, HTTPException, status
from models.heart_condition import Heart
import pydantic

heart_router = APIRouter(
    tags=["Hearts"]
)

# hearts = pydantic.parse_file_as(path='heart.json', type_=Heart)

@heart_router.get("/", response_model=List[Heart])
async def retrieve_all_hearts() -> List[Heart]:
    return conn.loacl.user.find()

@heart_router.get("/{id}", response_model=Heart)
async def retrieve_heart(id: int) -> Heart:
    for heart in hearts:
        if heart.id == id:
            return heart
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Heart condition with supplied ID does not exist"
    )

@heart_router.post("/new")
async def add_heart(body: Heart = Body(...)) -> dict:
    hearts.append(body)
    return {
        "message": "Heart condition added"
    }

@heart_router.delete("/{id}")
async def delete_heart(id: int) -> dict:
    for heart in hearts:
        if heart.id == id:
            hearts.remove()
            print(heart)
            return {
                "message": "Heart condition deleted"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Heart condition with supplied ID does not exist"
    )