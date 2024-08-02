import requests
from bs4 import BeautifulSoup
from .logger import scraper_logger


def get_movie_details(url):
    scraper_logger.info(f"Fetching movie details from {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        scraper_logger.info(f"Successfully fetched details for {url}")
    except requests.RequestException as e:
        scraper_logger.error(f"Error fetching details for {url}: {e}")
        return {}

    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        actors = ', '.join([actor.text.strip() for actor in soup.select('a[href^="/name/"]')[:5]])
        description = soup.find('span', {'data-testid': 'plot-l'}).text.strip() if soup.find('span', {'data-testid': 'plot-l'}) else 'N/A'
        featured_review = soup.find('div', {'data-testid': 'reviews-summary'}).text.strip() if soup.find('div', {'data-testid': 'reviews-summary'}) else 'N/A'
        
        scraper_logger.info(f"Successfully extracted details for {url}")

        return {
            'actors': actors,
            'description': description,
            'featured_review': featured_review
        }
    except Exception as e:
        scraper_logger.error(f"Error extracting details for {url}: {e}")
        scraper_logger.exception(e)
        return {}
