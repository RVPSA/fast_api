from fastapi import FastAPI  # import packages
from mode import User

app = FastAPI()
list_username = list()
a = 10
@app.get("/home") # calliing route
def write_home():
    return {
         "username": list_username
    }
@app.post("/username")
def post_data(username : User):
    list_username.append(username)
    #a = 20
    return {
        "username": username
    }
