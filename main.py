import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from models import account
from routes.account import account_router
from utils import get_hash, encode_token, SECRET, authorize


load_dotenv()

app = FastAPI()


app.include_router(account_router, prefix="/account")

@app.get("/")
def hello(request: Request):
    authorize(request)
    return{"message":"Welcome!"}
