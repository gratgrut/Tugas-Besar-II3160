def heartEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "id":item["id"],
        "name": item["name"],
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

def heartsEntity(entity) -> list:
    return [heartEntity(item) for item in entity]