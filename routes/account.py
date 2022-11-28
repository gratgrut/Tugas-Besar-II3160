import json
from fastapi import APIRouter, HTTPException, status, Response
from utils import get_hash, encode_token, SECRET, authorize
from models.account import Account, AccountSignIn

account_router = APIRouter(
    tags=["Account"],
)

with open("users.json", "r") as read_file:
    accounts = json.load(read_file)



@account_router.post("/signup")
async def sign_account_up(data: Account) -> dict:
    if data.email in accounts:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account with supplied username exists"
        )

    accounts[data.email] = data

    return {
        "message": "Account successfully registered!"
    }


@account_router.post("/signin")
def sign_account_in(account: AccountSignIn, response: Response) -> dict:
    found = False
    for i in range (len(accounts)) :
        if (account.email == accounts[i]["email"]):
            found = True
            if (get_hash(account.password) == accounts[i]["password"]):
                token = encode_token(account.email)
                print(token)
                return { 
                    "message": "Account signed in successfully",
                    "data": { "token": token }
                }
            else:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return { "message": "Wrong password"}
    if not found:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": "User not found" }