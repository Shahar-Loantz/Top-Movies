from scraper.scrape import get_top_250_movies
from scraper.logger import scraper_logger

if __name__ == '__main__':
    scraper_logger.info("Starting the IMDB Top 250 movie scraper")
    
    try:
        movies = get_top_250_movies()
        
        if movies:
            scraper_logger.info("Printing scraped movie details")
            for movie in movies:
                print(f"Rank: {movie['rank']} - Name: {movie['name']}")
            
            scraper_logger.info(f"Scraping completed successfully with {len(movies)} movies scraped")
        else:
            scraper_logger.warning("No movies were scraped")
    
    except Exception as e:
        scraper_logger.error(f"An error occurred during scraping: {e}")
        scraper_logger.exception(e)
  
