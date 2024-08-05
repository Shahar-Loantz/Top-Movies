# import logging

# def setup_logger(name, log_file, level=logging.INFO):
#     formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
#     file_handler = logging.FileHandler(log_file)
#     file_handler.setFormatter(formatter)
    
#     stream_handler = logging.StreamHandler()
#     stream_handler.setFormatter(formatter)
    
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     logger.addHandler(file_handler)
#     logger.addHandler(stream_handler)
    
#     return logger

# scraper_logger = setup_logger('scraper_logger', 'scrape.log')



# scraper/logger.py

import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger

# Default application logger
app_logger = setup_logger('app_logger', 'logs/app.log')

# Scraper-specific logger (if needed)
scraper_logger = setup_logger('scraper_logger', 'logs/scrape.log')
