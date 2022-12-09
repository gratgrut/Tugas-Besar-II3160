from pydantic import BaseModel
from bson import ObjectId

class Heart(BaseModel):
    _id: ObjectId()
    id: int
    name: str
    age: int
    sex: bool
    cp: int
    trestbps: int
    chol: int
    fbs: bool
    restecg: int
    thalach: int
    exang: bool
    oldpeak: float
    slope: int
    ca: int
    thal: int
    target: bool

    class Config:
        schema_extra = {
            "example": {
                "_id": 3847587462483,
                "id": 5,
                "name": "Nappie Dearden",
                "age": 54,
                "sex": 1,
                "cp": 2,
                "trestbps": 120,
                "chol": 258,
                "fbs": 0,
                "restecg": 0,
                "thalach": 147,
                "exang": 0,
                "oldpeak": 0.4,
                "slope": 1,
                "ca": 0,
                "thal": 3,
                "target": 1
            }
        }

class Prediction(BaseModel):
    _id: ObjectId()
    id: int
    name: str
    age: int
    sex: bool
    cp: int
    trestbps: int
    chol: int
    fbs: bool
    restecg: int
    thalach: int
    exang: bool
    oldpeak: float
    slope: int
    ca: int
    thal: int

    class Config:
        schema_extra = {
            "example": {
                "_id": 3847587462483,
                "id": 5,
                "name": "Nappie Dearden",
                "age": 54,
                "sex": 1,
                "cp": 2,
                "trestbps": 120,
                "chol": 258,
                "fbs": 0,
                "restecg": 0,
                "thalach": 147,
                "exang": 0,
                "oldpeak": 0.4,
                "slope": 1,
                "ca": 0,
                "thal": 3,
            }
        }