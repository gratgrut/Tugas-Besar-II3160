from fastapi import APIRouter, HTTPException, status

from models.account import Account, AccountSignIn

account_router = APIRouter(
    tags=["Account"],
)

accounts = {}


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
async def sign_account_in(account: AccountSignIn) -> dict:
    if account.email not in accounts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account does not exist"
        )

    if accounts[account.email].password != account.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "Account signed in successfully"
    }