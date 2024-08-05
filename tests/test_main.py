
# import pytest
# from fastapi.testclient import TestClient
# from main import app, load_data
# from unittest.mock import patch

# # Mock data
# mock_movies = [
#     {
#         "name": "The Shawshank Redemption",
#         "actors": ["Tim Robbins", "Morgan Freeman"],
#         "rank": 1,
#         "description": "Two imprisoned men bond over a number of years...",
#         "featured_review": "An inspiring story with brilliant performances...",
#         "created_at": "2024-08-01T00:00:00Z",
#         "updated_at": "2024-08-01T00:00:00Z"
#     },
#     {
#         "name": "The Godfather",
#         "actors": ["Marlon Brando", "Al Pacino"],
#         "rank": 2,
#         "description": "The aging patriarch of an organized crime dynasty...",
#         "featured_review": "A cinematic masterpiece...",
#         "created_at": "2024-08-01T00:00:00Z",
#         "updated_at": "2024-08-01T00:00:00Z"
#     }
# ]

# client = TestClient(app)

# @pytest.fixture
# def mock_load_data():
#     with patch('main.load_data', return_value=mock_movies):
#         yield

# def test_read_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}

# def test_get_movies_no_filter(mock_load_data):
#     response = client.post("/movies/", json={})
#     assert response.status_code == 200
#     assert response.json() == mock_movies

# def test_get_movies_with_fields(mock_load_data):
#     response = client.post("/movies/", json={"fields": ["name", "rank"]})
#     assert response.status_code == 200
#     assert response.json() == [
#         {"name": "The Shawshank Redemption", "rank": 1},
#         {"name": "The Godfather", "rank": 2}
#     ]

# def test_get_movies_with_search(mock_load_data):
#     response = client.post("/movies/", json={"search_criteria": {"name": "shawshank"}})
#     assert response.status_code == 200
#     assert response.json() == [
#         {
#             "name": "The Shawshank Redemption",
#             "actors": ["Tim Robbins", "Morgan Freeman"],
#             "rank": 1,
#             "description": "Two imprisoned men bond over a number of years...",
#             "featured_review": "An inspiring story with brilliant performances...",
#             "created_at": "2024-08-01T00:00:00Z",
#             "updated_at": "2024-08-01T00:00:00Z"
#         }
#     ]

# def test_invalid_field_filter(mock_load_data):
#     response = client.post("/movies/", json={"fields": ["invalid_field"]})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid fields requested: ['invalid_field']"}

# def test_invalid_search_field(mock_load_data):
#     response = client.post("/movies/", json={"search_criteria": {"invalid_field": "value"}})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Search field 'invalid_field' does not exist in the data"}




# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
from app.utils.data_loader import load_data

# Mock data
mock_movies = [
    {
        "name": "The Shawshank Redemption",
        "actors": ["Tim Robbins", "Morgan Freeman"],
        "rank": 1,
        "description": "Two imprisoned men bond over a number of years...",
        "featured_review": "An inspiring story with brilliant performances...",
        "created_at": "2024-08-01T00:00:00Z",
        "updated_at": "2024-08-01T00:00:00Z"
    },
    {
        "name": "The Godfather",
        "actors": ["Marlon Brando", "Al Pacino"],
        "rank": 2,
        "description": "The aging patriarch of an organized crime dynasty...",
        "featured_review": "A cinematic masterpiece...",
        "created_at": "2024-08-01T00:00:00Z",
        "updated_at": "2024-08-01T00:00:00Z"
    }
]

client = TestClient(app)

@pytest.fixture
def mock_load_data():
    with patch('app.utils.data_loader.load_data', return_value=mock_movies):
        yield

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}

def test_get_movies_no_filter(mock_load_data):
    response = client.post("/movies/", json={})
    assert response.status_code == 200
    assert response.json() == mock_movies

def test_get_movies_with_fields(mock_load_data):
    response = client.post("/movies/", json={"fields": ["name", "rank"]})
    assert response.status_code == 200
    assert response.json() == [
        {"name": "The Shawshank Redemption", "rank": 1},
        {"name": "The Godfather", "rank": 2}
    ]

def test_get_movies_with_search(mock_load_data):
    response = client.post("/movies/", json={"search_criteria": {"name": "shawshank"}})
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "The Shawshank Redemption",
            "actors": ["Tim Robbins", "Morgan Freeman"],
            "rank": 1,
            "description": "Two imprisoned men bond over a number of years...",
            "featured_review": "An inspiring story with brilliant performances...",
            "created_at": "2024-08-01T00:00:00Z",
            "updated_at": "2024-08-01T00:00:00Z"
        }
    ]

def test_invalid_field_filter(mock_load_data):
    response = client.post("/movies/", json={"fields": ["invalid_field"]})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid fields requested: ['invalid_field']"}

def test_invalid_search_field(mock_load_data):
    response = client.post("/movies/", json={"search_criteria": {"invalid_field": "value"}})
    assert response.status_code == 400
    assert response.json() == {"detail": "Search field 'invalid_field' does not exist in the data"}
