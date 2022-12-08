from database.connection import client
from models.heart_condition import Heart

def predictEntity(item) -> dict:
    return {
        "age": item["age"],
        "sex": item["sex"],
        "cp": item["cp"],
        "trestbps": item["trestbps"],
        "chol": item["chol"],
        "fbs": item["fbs"],
        "restecg": item["restecg"],
        "thalach": item["thalach"],
        "exang": item["exang"],
        "oldpeak": item["oldpeak"],
        "slope": item["slope"],
        "ca": item["ca"],
        "thal": item["thal"],
        "target": item["target"]
    }

def predictsEntity(entity) -> list:
    return [predictEntity(item) for item in entity]

db = predictsEntity(client.heart_disease_api.heart_condition.find({},
   { '_id': 0, "id": 0, "name":0 }))

print(db)
