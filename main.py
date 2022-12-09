from fastapi import FastAPI, Request
from routes.account import account_router
from routes.heart_condition import heart_router
from routes.prediction import prediction_router
from utils import authorize

app = FastAPI(
    title = "Heart Disease Prediction API",
    description="This is an API to get prediction if someone has a heart disease or not based on some parameters." 
)


app.include_router(account_router, prefix="/account")
app.include_router(heart_router, prefix="/heart")
app.include_router(prediction_router, prefix="/prediction")

@app.get("/")
def hello(request: Request):
    authorize(request)
    return{"message":"Welcome to Heart Disease Prediction API!"}
