from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import Column, Integer, String
from app.db import base


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)


class UserSchema(BaseModel):
    __tablename__ = "Users"
    id = Column(Integer, index= True )
    name: str = Field(default=None)
    email: EmailStr = Field(default=None, primary_key= True)
    password: str = Field(default=None)

    class config:
        main_schema = {
            "demo user": {
                "username": "amogh",
                "email": "amogh@gmail.com",
                "password": "123amogh",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class config:
        main_schema = {
            "demo user": {"email": "amogh@gmail.com", "password": "123amogh"}
        }


class Users(base):
    __tablename__ = "Users"
    id = Column(Integer, index= True, primary_key= True)
    Username = Column(String)
    passoword = Column(String)
    email = Column(String)