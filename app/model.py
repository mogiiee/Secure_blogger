from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)


class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None, primary_key=True)
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


