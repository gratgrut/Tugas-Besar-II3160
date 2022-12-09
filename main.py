import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from routes.account import account_router
from routes.heart_condition import heart_router
from routes.prediction import prediction_router
from utils import authorize


dotenv = load_dotenv()

app = FastAPI()


app.include_router(account_router, prefix="/account")
app.include_router(heart_router, prefix="/heart")
app.include_router(prediction_router, prefix="/prediction")

@app.get("/")
def hello(request: Request):
    authorize(request)
    return{"message":"Welcome to Heart Disease Prediction API!"}
