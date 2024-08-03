# main.py

from fastapi import FastAPI, HTTPException
from typing import List, Optional
import json
import os
from models import MovieQuery

app = FastAPI()

# Path to the JSON data file
DATA_FILE_PATH = os.path.join('data', 'movies.json')

# Function to load data from the JSON file
def load_data():
    try:
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found")

@app.post("/movies/")
def get_movies(query: MovieQuery):
    movies = load_data()

    if query.fields:
        filtered_movies = []
        for movie in movies:
            filtered_movie = {field: movie.get(field) for field in query.fields if field in movie}
            filtered_movies.append(filtered_movie)
        movies = filtered_movies

    if query.search_field and query.search_value:
        movies = [movie for movie in movies if query.search_field in movie and query.search_value.lower() in str(movie[query.search_field]).lower()]

    return movies


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}
