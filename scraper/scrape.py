import requests
from bs4 import BeautifulSoup
from .logger import scraper_logger
from datetime import datetime
from .data_handler import save_to_json, save_to_csv
from .movie_details import get_movie_details

IMDB_TOP_250_URL = 'https://www.imdb.com/chart/top/'

def get_top_250_movies():
    scraper_logger.info("Fetching the IMDB top 250 page")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(IMDB_TOP_250_URL, headers=headers)
        response.raise_for_status()
        scraper_logger.info("Successfully fetched the IMDB top 250 page")
    except requests.RequestException as e:
        scraper_logger.error(f"Error fetching the IMDB top 250 page: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    movie_entries = soup.find_all('a', class_='ipc-title-link-wrapper')
    scraper_logger.info(f"Found {len(movie_entries)} movie entries")

    movies = []
    for index, entry in enumerate(movie_entries):
        rank = index + 1
        scraper_logger.info(f"Processing movie rank {rank}")
        
        try:
            movie_name = entry.find('h3', class_='ipc-title__text').text.strip()
            movie_url = entry.get('href')

            movie_detail_url = f'https://www.imdb.com{movie_url}'
            movie_details = get_movie_details(movie_detail_url)

            movie_record = {
                'name': movie_name,
                'actors': movie_details['actors'],
                'rank': rank,
                'description': movie_details['description'],
                'featured_review': movie_details['featured_review'],
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }

            movies.append(movie_record)
            scraper_logger.info(f"Successfully processed movie: {movie_name} (Rank: {rank})")

        except Exception as e:
            scraper_logger.error(f"Error processing movie at rank {rank}: {e}")
            scraper_logger.exception(e)
    
    scraper_logger.info(f"Successfully scraped {len(movies)} movies")
    save_to_json(movies, 'movies.json')
    save_to_csv(movies, 'movies.csv')

    return movies


