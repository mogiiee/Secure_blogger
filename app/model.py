from pydantic import BaseModel, EmailStr
from typing import Union


class PostSchema(BaseModel):
    id: int
    title: str
    content: str 

class details(BaseModel):
    _id: 0
    first_name: str
    last_name: Union[str, None] = None
    phone_number: int = None

class UserSchema(BaseModel):
    _id : 0
    name: str
    email: EmailStr 
    password: str 
    something: str

    class config:
        main_schema = {
            "demo user": {
                "_id": 0,
                "username": "amogh",
                "email": "amogh@gmail.com",
                "password": "123amogh",
            }
        }


class UserLoginSchema(BaseModel):
    _id: 0
    email: EmailStr 
    password: str

    class config:
        main_schema = {
            "demo user": 
            {"email": "amogh@gmail.com",
             "password": "123amogh"
             }
        }
