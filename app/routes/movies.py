# app/routes/movies.py

from fastapi import APIRouter, HTTPException
from models import MovieQuery
from utils.data_loader import load_data
from utils.logger import app_logger as logger

router = APIRouter()

@router.post("/movies/")
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
