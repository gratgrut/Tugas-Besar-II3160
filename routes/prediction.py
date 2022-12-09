from typing import List
from database.connection import client
from fastapi import APIRouter, Body, HTTPException, status
from models.heart_condition import Prediction
from schemas.heart_condition import heartEntity, heartsEntity
import numpy as np
import pickle

with open('./models/heart_disease_prediction.pickle', 'rb') as f:
    model = pickle.load(f)

prediction_router = APIRouter(
    tags=["Prediction"]
)

@prediction_router.post("/")
async def get_prediction(body: Prediction):

    # predictive system
    input = dict(body)
    # input = dicti.items()
    input_data = [input['age'], input['sex'], input['cp'], input['trestbps'], input['chol'], input['fbs'], input['restecg'], input['thalach'], input['exang'], input['oldpeak'], input['slope'], input['ca'], input['thal']]

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    # print(prediction)

    if (prediction[0]== 0):
        return ('The Person does not have a Heart Disease')
    else:
        return ('The Person has Heart Disease')
    # return heartsEntity(client.heart_disease_api.heart_condition.find())

# @prediction_router.get("/")
# async def testing():
#     return heart_data