from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
import json
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Load the movies data from the JSON file
def load_movies_data():  
    try:
        with open('data/movies.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Movies data not found")

movies_data = load_movies_data()

# Define a Pydantic model for the movie
class Movie(BaseModel):
    name: Optional[str] = None
    actors: Optional[str] = None
    rank: Optional[int] = None
    description: Optional[str] = None
    featured_review: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@app.get("/movies/", response_model=List[Movie])
def get_movies(
    name: Optional[str] = Query(None),
    actors: Optional[str] = Query(None),
    rank: Optional[int] = Query(None),
    description: Optional[str] = Query(None),
    featured_review: Optional[str] = Query(None),
    fields: Optional[List[str]] = Query(None)
):
    filtered_movies = []
    
    for movie in movies_data:
        if name and name.lower() not in movie.get('name', '').lower():
            continue
        if actors and actors.lower() not in movie.get('actors', '').lower():
            continue
        if rank and rank != movie.get('rank'):
            continue
        if description and description.lower() not in movie.get('description', '').lower():
            continue
        if featured_review and featured_review.lower() not in movie.get('featured_review', '').lower():
            continue
        
        if fields:
            filtered_movie = {field: movie.get(field) for field in fields if field in movie}
            filtered_movies.append(filtered_movie)
        else:
            filtered_movies.append(movie)
    
    return filtered_movies


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
