from pydantic import BaseModel, EmailStr

class Account(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@uhuy.com",
                "password": "uhuy!"
            }
        }

class AccountSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@uhuy.com",
                "password": "uhuy!"
            }
        }