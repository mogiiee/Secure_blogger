from fastapi import FastAPI, Body, Depends, Request, HTTPException
from app.model import PostSchema, UserLoginSchema, details
from app.responses import response
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer
from . import db, ops
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


posts = [
    {"id": 1, "title": "some title 1", "content": "some content 1"},
    {"id": 2, "title": "some title 2", "content": "some content 2"},
    {"id": 3, "title": "some title 3", "content": "some content 3"},
]

users = []

@app.post("/pill", tags=["pill"])
async def pill_details(signup_details: Request):
    infoDict = await signup_details.json()
    infoDict = dict(infoDict)
    # Checking if email already exists
    db.collection.insert_one(infoDict)
    return response(True, str(infoDict))

@app.get("/", tags=["greetings"])
async def greet():
    return {"hello ": "world"}


@app.get("/posts", tags=["Posts"])
async def get_posts():
    return {"data": posts}


@app.get("/posts/{id}", tags=["Posts"])
async def get_one_post(id: int):
    if id > len(posts):
        return response(False, "this ID does not exist")
    else:
        for post in posts:
            if post["id"] == id:
                return response(True, post)


@app.post("/posts", tags=["Posts"], dependencies=[Depends(JWTBearer())])
async def add_post(post: PostSchema):
    collection = dict(db.collection.insert_one(post))
    print(type(collection))

    # post.id = len(posts) + 1
    # posts.append(dict(post))
    return response(True, post)


@app.post("/user/signup", tags=["User"])

async def user_signup(new_user: details):
    payload = jsonable_encoder(new_user)
    try:
        ops.inserter(payload)
        return response(True,signJWT(payload))
    except Exception as e:
        return response(False,str(e))


@app.post("/user/login", tags=["User"])
async def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return response(False, "invalid user pls login again")


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

