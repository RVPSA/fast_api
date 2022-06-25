from fastapi import FastAPI # import packages

app = FastAPI()

app.get("/home") # calliing route
def write_home():
    return {
        "Name": "ABCD",
        "Age": 24
    }
