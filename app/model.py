from pydantic import BaseModel, EmailStr


class PostSchema(BaseModel):
    id: int
    title: str
    content: str 


class UserSchema(BaseModel):
    ObjectId : int
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
    ObjectId: int
    email: EmailStr 
    password: str

    class config:
        main_schema = {
            "demo user": 
            {"email": "amogh@gmail.com",
             "password": "123amogh"
             }
        }
