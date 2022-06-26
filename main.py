from fastapi import FastAPI  # import packages
from mode import User
from typing import List

app = FastAPI()
list_username = list()
a = 10

dataBase : List[User] = [
    User(
        username = "User 1"
    )
]

@app.get("/home") # calliing route
def write_home():
    return dataBase;

@app.post("/username")
def post_data(username : User):
    list_username.append(username)
    #a = 20
    return {
        "username": username
    }
