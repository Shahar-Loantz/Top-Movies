# # main.py

# from fastapi import FastAPI, HTTPException
# from typing import List, Optional, Dict
# from pydantic import BaseModel
# from pymongo import MongoClient
# import os
# from database.db import movies_collection, actors_collection
# from database.db_models import Movie, Actor
# from models import MovieQuery
# from scraper.logger import app_logger as logger
# from datetime import datetime

# app = FastAPI()

# # Function to load movies from MongoDB
# def load_movies():
#     try:
#         movies = list(movies_collection.find({}, {"_id": 0}))  # Exclude the MongoDB _id field
#         return movies
#     except Exception as e:
#         logger.error(f"Error loading data from MongoDB: {e}")
#         raise HTTPException(status_code=500, detail="Error loading data from MongoDB")

# # Function to load actors from MongoDB
# def load_actors():
#     try:
#         actors = list(actors_collection.find({}, {"_id": 0}))  # Exclude the MongoDB _id field
#         return actors
#     except Exception as e:
#         logger.error(f"Error loading data from MongoDB: {e}")
#         raise HTTPException(status_code=500, detail="Error loading data from MongoDB")

# @app.post("/movies/")
# def get_movies(query: MovieQuery):
#     movies = load_movies()
#     original_count = len(movies)
#     logger.info(f"Loaded {original_count} movies from MongoDB")

#     # Handle field filtering
#     valid_fields = ['name', 'actors', 'rank', 'description', 'featured_review', 'created_at', 'updated_at']
#     if query.fields:
#         invalid_fields = [field for field in query.fields if field not in valid_fields]
#         if invalid_fields:
#             logger.error(f"Invalid fields requested: {invalid_fields}")
#             raise HTTPException(status_code=400, detail=f"Invalid fields requested: {invalid_fields}")

#         filtered_movies = []
#         for movie in movies:
#             filtered_movie = {field: movie.get(field) for field in query.fields if field in movie}
#             filtered_movies.append(filtered_movie)
#         movies = filtered_movies

#     # Handle multi-field search
#     if query.search_criteria:
#         for field, value in query.search_criteria.items():
#             if field not in valid_fields:
#                 logger.error(f"Search field '{field}' does not exist in the data")
#                 raise HTTPException(status_code=400, detail=f"Search field '{field}' does not exist in the data")
        
#         for field, value in query.search_criteria.items():
#             movies = [movie for movie in movies if field in movie and value.lower() in str(movie[field]).lower()]

#     logger.info(f"Returning {len(movies)} filtered movies")
#     return movies

# @app.post("/actors/")
# def add_actor(actor: Actor):
#     try:
#         actor_data = actor.dict()
#         actors_collection.insert_one(actor_data)
#         logger.info(f"Actor {actor.name} added to MongoDB")
#         return {"message": "Actor added successfully"}
#     except Exception as e:
#         logger.error(f"Error adding actor to MongoDB: {e}")
#         raise HTTPException(status_code=500, detail="Error adding actor to MongoDB")

# @app.get("/actors/")
# def get_actors():
#     actors = load_actors()
#     logger.info(f"Loaded {len(actors)} actors from MongoDB")
#     return actors

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data, POST /actors/ to add an actor, and GET /actors/ to get actor data."}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)




# main.py

from fastapi import FastAPI, HTTPException
from typing import List, Optional, Dict
from pydantic import BaseModel
from pymongo import MongoClient
import os
from database.db import movies_collection, actors_collection
from database.db_models import Movie, Actor
from models import MovieQuery
from logger import app_logger as logger
from datetime import datetime

app = FastAPI()

# Function to load movies from MongoDB
def load_movies():
    try:
        logger.debug("Attempting to load movies from MongoDB")
        movies = list(movies_collection.find({}, {"_id": 0}))  # Exclude the MongoDB _id field
        logger.debug(f"Loaded {len(movies)} movies")
        return movies
    except Exception as e:
        logger.error(f"Error loading data from MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Error loading data from MongoDB")

# Function to load actors from MongoDB
def load_actors():
    try:
        logger.debug("Attempting to load actors from MongoDB")
        actors = list(actors_collection.find({}, {"_id": 0}))  # Exclude the MongoDB _id field
        logger.debug(f"Loaded {len(actors)} actors")
        return actors
    except Exception as e:
        logger.error(f"Error loading data from MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Error loading data from MongoDB")

@app.post("/movies/")
def get_movies(query: MovieQuery):
    logger.debug("Received request to get movies")
    movies = load_movies()
    original_count = len(movies)
    logger.info(f"Loaded {original_count} movies from MongoDB")

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

@app.post("/actors/")
def add_actor(actor: Actor):
    try:
        logger.info(f"Received request to add actor: {actor}")
        actor_data = actor.dict()
        logger.info(f"Actor data to insert: {actor_data}")
        print("check")
        # Insert the actor data into the actors collection
        insert_result = actors_collection.insert_one(actor_data)
    
        logger.debug(f"Insertion result: {insert_result.acknowledged}, Inserted ID: {insert_result.inserted_id}")
        logger.info(insert_result)
        print(insert_result.acknowledged)

        if insert_result.acknowledged:
            logger.info(f"Actor {actor.name} added to MongoDB with ID {insert_result.inserted_id}")
        else:
            logger.error("Failed to insert actor into MongoDB")

        return {"message": "Actor added successfully"}
    except Exception as e:
        logger.error(f"Error adding actor to MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Error adding actor to MongoDB")

@app.get("/actors/")
def get_actors():
    logger.debug("Received request to get actors")
    actors = load_actors()
    logger.info(f"Loaded {len(actors)} actors from MongoDB")
    return actors

@app.get("/")
def read_root():
    logger.debug("Received request to read root")
    return {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data, POST /actors/ to add an actor, and GET /actors/ to get actor data."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
