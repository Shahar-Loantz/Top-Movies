# IMDB Top 250 Movies API

## Description

This project is a FastAPI application that retrieves data from the IMDB Top 250 Movies list. Users can query the data with specific fields and perform searches within those fields.

## Project Structure

project-root/<br />
│<br />
├── data/<br />
│ ├── movies.json # Contains scraped movie data<br />
│ └── movies.csv # Contains scraped movie data in CSV format<br />
│<br />
├── scraper/<br />
│ ├── init.py<br />
│ ├── scrape.py # Script to scrape movie data from IMDB<br />
│ ├── movie_details.py # Module to fetch movie details<br />
│ ├── data_handler.py # Module to save data to JSON and CSV<br />
│ └── logger.py # Logging configuration<br />
│<br />
├── main.py # FastAPI application<br />
├── models.py # Pydantic models for request validation<br />
├── requirements.txt # List of project dependencies<br />
├── .gitignore # Git ignore file<br />
└── README.md # Project documentation<br />

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shahar-Loantz/Top-Movies
2. **Navigate to the project directory:**
   ```bash
   cd <your-project-directory>
3. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

## Running the Scraping Process

To scrape the IMDB Top 250 movies and save the data:

1. **Ensure the virtual environment is activated.**

2. **Run the run.py script:**
   ```bash
   python run.py
This will execute the scraping process, save the data to movies.json and movies.csv, and log the activity.



## Running the Application

1. **Ensure the virtual environment is activated.**

2. **Run the FastAPI application using Uvicorn:**
   ```bash
   uvicorn main:app --reload

The application will be available at http://127.0.0.1:8000/.

## Testing the Endpoints
**Root Endpoint**
- GET /

  Returns a welcome message.

**Movies Endpoint**
- POST /movies/

  Retrieve filtered movie data.

  **Request Body Example:**<br />
  {<br />
    "fields": ["name", "actors", "rank", "description", "featured_review", "created_at", "updated_at"],<br />
    "search_field": "actors",<br />
    "search_value": "Peter"<br />
  }<br />

  **Response Example:**<br />
  [<br />
    {<br />
        "name": "7. The Lord of the Rings: The Return of the King",<br />
        "actors": "Peter Jackson, J.R.R. Tolkien, Fran Walsh, Philippa Boyens, Elijah Wood",<br />
        "rank": 7,<br />
        "description": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",<br />
        "featured_review": "N/A",<br />
        "created_at": "2024-08-03T20:45:27.036514",<br />
        "updated_at": "2024-08-03T20:45:27.036516"<br />
    },<br />
    {<br />
        "name": "9. The Lord of the Rings: The Fellowship of the Ring",<br />
        "actors": "Peter Jackson, J.R.R. Tolkien, Fran Walsh, Philippa Boyens, Elijah Wood",<br />
        "rank": 9,<br />
        "description": "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",<br />
        "featured_review": "N/A",<br />
        "created_at": "2024-08-03T20:45:30.760104",<br />
        "updated_at": "2024-08-03T20:45:30.760107"<br />
    },<br />
    {<br />
        "name": "12. The Lord of the Rings: The Two Towers",<br />
        "actors": "Peter Jackson, J.R.R. Tolkien, Fran Walsh, Philippa Boyens, Elijah Wood",<br />
        "rank": 12,<br />
        "description": "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",<br />
        "featured_review": "N/A",<br />
        "created_at": "2024-08-03T20:45:37.678552",<br />
        "updated_at": "2024-08-03T20:45:37.678555"<br />
    }<br />
]<br />









  

