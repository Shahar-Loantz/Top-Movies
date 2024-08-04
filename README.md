# IMDB Top 250 Movies API

## Description

This project is a FastAPI application that retrieves data from the IMDB Top 250 Movies list. Users can query the data with specific fields and perform searches within those fields.

## Project Structure
<br />
project-root/<br />
│<br />
├── data/<br />
│   ├── movies.json<br />
│   └── movies.csv<br />
│<br />
├── logs/<br />
│   └── scrape.log<br />
│   └── app.log<br />
│<br />
├── scraper/<br />
│   ├── __init__.py<br />
│   ├── scrape.py<br />
│   ├── movie_details.py<br />
│   ├── data_handler.py<br />
│   └── logger.py<br />
│<br />
├── tests/<br />
│   └── test_main.py<br />
│<br />
├── main.py<br />
├── models.py<br />
├── requirements.txt<br />
├── .gitignore<br />
└── README.md<br />

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
  "search_criteria": {<br />
    "name": "Godfather",<br />
    "actors": "Francis"<br />
  }<br />
}<br />

  **Response Example:**<br />
[<br />
    {<br />
        "name": "2. The Godfather",<br />
        "actors": "Francis Ford Coppola, Mario Puzo, Francis Ford Coppola, Marlon Brando, Al Pacino",<br />
        "rank": 2,<br />
        "description": "Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son, Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.",<br />
        "featured_review": "N/A",<br />
        "created_at": "2024-08-04T14:29:13.432423",<br />
        "updated_at": "2024-08-04T14:29:13.432426"<br />
    },<br />
    {<br />
        "name": "4. The Godfather Part II",<br />
        "actors": "Francis Ford Coppola, Francis Ford Coppola, Mario Puzo, Al Pacino, Robert De Niro",<br />
        "rank": 4,<br />
        "description": "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.",<br />
        "featured_review": "N/A",<br />
        "created_at": "2024-08-04T14:29:16.063882",<br />
        "updated_at": "2024-08-04T14:29:16.063885"<br />
    }<br />
]<br />









  

