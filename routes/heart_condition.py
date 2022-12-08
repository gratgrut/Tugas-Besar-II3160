from typing import List
from database.connection import client
from fastapi import APIRouter, Body, HTTPException, status
from models.heart_condition import Heart
from schemas.heart_condition import heartEntity, heartsEntity
from bson import ObjectId

heart_router = APIRouter(
    tags=["Hearts"]
)

# newheart = Heart()

# def create_heart(id, name, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
#     newheart._id=ObjectId()
#     newheart.id = id
#     newheart.name = name
#     newheart.age = age
#     newheart.sex = sex
#     newheart.cp = cp
#     newheart.trestbps = trestbps
#     newheart.chol = chol
#     newheart.fbs = fbs
#     newheart.restecg = restecg
#     newheart.thalach = thalach
#     newheart.exang = exang
#     newheart.oldpeak = oldpeak
#     newheart.slope = slope
#     newheart.ca = ca
#     newheart.thal = thal
#     newheart.target = target
#     return dict(newheart)

    
# hearts = pydantic.parse_file_as(path='heart.json', type_=Heart)

@heart_router.get("/", response_model=List[Heart])
async def retrieve_all_hearts() -> List[Heart]:
    return heartsEntity(client.heart_disease_api.heart_condition.find())

@heart_router.get("/{id}")
async def retrieve_heart(id: int) -> Heart:
    return heartEntity(client.heart_disease_api.heart_condition.find_one({"id":id}))

# @heart_router.get("/{id}", response_model=Heart)
# async def retrieve_heart(id: int) -> Heart:
#     for heart in hearts:
#         if heart.id == id:
#             return heart
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Heart condition with supplied ID does not exist"
#     )

@heart_router.post("/new")
async def add_heart(body: Heart = Body(...)) -> dict:
    client.heart_disease_api.heart_condition.insert_one(dict(body))
    return {
        "message": "Heart condition added"
    }

# @heart_router.delete("/{id}")
# async def delete_heart(id: int) -> dict:
#     for heart in hearts:
#         if heart.id == id:
#             hearts.remove()
#             print(heart)
#             return {
#                 "message": "Heart condition deleted"
#             }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Heart condition with supplied ID does not exist"
#     )

@heart_router.put("/{id}")
async def update_heart(id, heart: Heart):
    client.heart_disease_api.heart_condition.find_one_and_update({"id":id},{"$set":dict(heart)})
    return heartEntity(client.heart_disease_api.heart_condition.find_one({}))

@heart_router.delete("/{id}")
async def delete_heart(id: int):
    return heartEntity(client.heart_disease_api.heart_condition.find_one_and_delete({"id":id}))
    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail="Heart condition with supplied ID does not exist"
    # )