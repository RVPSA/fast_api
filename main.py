from fastapi import FastAPI # import packages

app = FastAPI()
list_username = list()
@app.get("/home") # calliing route
def write_home():
    return {
        "Name": "ABCD",
        "Age": 24
    }
@app.post("/username")
def post_data(username : str):
    list_username.append(username)
    return {
        "username": list_username
    }
