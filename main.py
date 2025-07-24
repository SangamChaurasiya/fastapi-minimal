# This is the entry point for our application.
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello from FastAPI"}
