# # main.py

# from fastapi import FastAPI, HTTPException
# from typing import List, Optional
# import json
# import os
# from models import MovieQuery

# app = FastAPI()

# # Path to the JSON data file
# DATA_FILE_PATH = os.path.join('data', 'movies.json')

# # Function to load data from the JSON file
# def load_data():
#     try:
#         with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="Data file not found")

# @app.post("/movies/")
# def get_movies(query: MovieQuery):
#     movies = load_data()

#     if query.fields:
#         filtered_movies = []
#         for movie in movies:
#             filtered_movie = {field: movie.get(field) for field in query.fields if field in movie}
#             filtered_movies.append(filtered_movie)
#         movies = filtered_movies

#     if query.search_field and query.search_value:
#         movies = [movie for movie in movies if query.search_field in movie and query.search_value.lower() in str(movie[query.search_field]).lower()]

#     return movies


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}




# main.py

from fastapi import FastAPI, HTTPException
from typing import List, Optional, Dict
import json
import os
from models import MovieQuery
from scraper.logger import app_logger as logger

app = FastAPI()

# Path to the JSON data file
DATA_FILE_PATH = os.path.join('data', 'movies.json')

# Function to load data from the JSON file
def load_data():
    try:
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise HTTPException(status_code=404, detail="Data file not found")

@app.post("/movies/")
def get_movies(query: MovieQuery):
    movies = load_data()
    original_count = len(movies)
    logger.info(f"Loaded {original_count} movies from data file")

    # Handle field filtering
    valid_fields = ['name', 'actors', 'rank', 'description', 'featured_review', 'created_at', 'updated_at']
    if query.fields:
        invalid_fields = [field for field in query.fields if field not in valid_fields]
        if invalid_fields:
            logger.error(f"Invalid fields requested: {invalid_fields}")
            raise HTTPException(status_code=400, detail=f"Invalid fields requested: {invalid_fields}")

        filtered_movies = []
        for movie in movies:
            filtered_movie = {field: movie.get(field) for field in query.fields if field in movie}
            filtered_movies.append(filtered_movie)
        movies = filtered_movies

    # Handle multi-field search
    if query.search_criteria:
        for field, value in query.search_criteria.items():
            if field not in valid_fields:
                logger.error(f"Search field '{field}' does not exist in the data")
                raise HTTPException(status_code=400, detail=f"Search field '{field}' does not exist in the data")
        
        for field, value in query.search_criteria.items():
            movies = [movie for movie in movies if field in movie and value.lower() in str(movie[field]).lower()]

    logger.info(f"Returning {len(movies)} filtered movies")
    return movies

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}
