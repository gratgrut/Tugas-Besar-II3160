from pydantic import BaseModel, EmailStr

class Account(BaseModel):
    email: EmailStr
    password: str

    class Config:
        extra = {
            "example": {
                "email": "fastapi@uhuy.com",
                "password": "uhuy!"
            }
        }

class AccountSignIn(BaseModel):
    email: EmailStr
    password: str

    extra = {
        "example": {
            "email": "fastapi@uhuy.com",
            "password": "uhuy!"
        }
    }