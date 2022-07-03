from fastapi import FastAPI  # import packages
from mode import User
from typing import List

app = FastAPI()
list_username = list()
a = 10

dataBase : List[User] = [
    User(
        #username = "User 1
        heartbeat = 90
    )
]

@app.get("/home") # calliing route
def write_home():
    return dataBase;

#@app.post("/username")
#def post_data(username : User):
    #dataBase.append(username)
    #a = 20
    #return {
        #"username": username
    #}

@app.post("/username")
def post_data(heartbeat : User):
    dataBase.append(heartbeat)
    #a = 20
    return {
        "heartbeat": heartbeat
    }
