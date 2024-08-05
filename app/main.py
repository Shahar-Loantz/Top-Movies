# app/main.py

from fastapi import FastAPI
from routes import movies

app = FastAPI()

app.include_router(movies.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}
