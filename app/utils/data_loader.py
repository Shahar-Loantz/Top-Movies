# app/utils/data_loader.py

import json
import os
from fastapi import HTTPException
from utils.logger import app_logger as logger

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
