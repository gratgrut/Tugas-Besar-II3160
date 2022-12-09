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