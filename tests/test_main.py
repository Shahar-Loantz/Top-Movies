# import pytest
# from fastapi.testclient import TestClient
# from main import app, load_data

# # Mock data for testing
# mock_data = [
#     {
#         "name": "Inception",
#         "actors": "Leonardo DiCaprio",
#         "rank": 1,
#         "description": "A thief who steals corporate secrets through the use of dream-sharing technology.",
#         "featured_review": "Amazing movie with a complex plot.",
#         "created_at": "2024-01-01T00:00:00",
#         "updated_at": "2024-01-01T00:00:00"
#     },
#     {
#         "name": "The Dark Knight",
#         "actors": "Christian Bale",
#         "rank": 2,
#         "description": "When the menace known as The Joker emerges from his mysterious past.",
#         "featured_review": "A brilliant depiction of Batman.",
#         "created_at": "2024-01-01T00:00:00",
#         "updated_at": "2024-01-01T00:00:00"
#     }
# ]

# # Mock the load_data function to return mock_data
# def mock_load_data():
#     return mock_data

# # Replace the actual load_data function with the mock
# app.dependency_overrides[load_data] = mock_load_data

# client = TestClient(app)

# def test_read_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Welcome to the Movie API! Use POST /movies/ to query movie data."}

# def test_get_movies():
#     response = client.post("/movies/", json={})
#     response_data = response.json()
#     assert response.status_code == 200
#     assert len(response_data) == len(mock_data), "Number of results does not match"
    
#     for item in response_data:
#         assert any(
#             item["name"] == expected_item["name"] and
#             item["actors"] == expected_item["actors"] and
#             item["rank"] == expected_item["rank"] and
#             item["description"] == expected_item["description"] and
#             item["featured_review"] == expected_item["featured_review"]
#             for expected_item in mock_data
#         ), f"Item {item} does not match any expected result"

# def test_get_movies_with_fields():
#     response = client.post("/movies/", json={"fields": ["name", "actors"]})
#     response_data = response.json()
#     assert response.status_code == 200
    
#     expected_result = [
#         {"name": "Inception", "actors": "Leonardo DiCaprio"},
#         {"name": "The Dark Knight", "actors": "Christian Bale"}
#     ]
    
#     assert len(response_data) == len(expected_result), "Number of results does not match"

#     for item in response_data:
#         assert any(
#             item["name"] == expected_item["name"] and
#             item["actors"] == expected_item["actors"]
#             for expected_item in expected_result
#         ), f"Item {item} does not match any expected result"

# def test_get_movies_with_search_criteria():
#     response = client.post("/movies/", json={"search_criteria": {"name": "Inception"}})
#     response_data = response.json()
#     assert response.status_code == 200
    
#     expected_result = [mock_data[0]]
    
#     assert len(response_data) == len(expected_result), "Number of results does not match"
    
#     for item in response_data:
#         assert any(
#             item["name"] == expected_item["name"] and
#             item["actors"] == expected_item["actors"] and
#             item["rank"] == expected_item["rank"] and
#             item["description"] == expected_item["description"] and
#             item["featured_review"] == expected_item["featured_review"]
#             for expected_item in expected_result
#         ), f"Item {item} does not match any expected result"

# def test_get_movies_with_multiple_search_criteria():
#     response = client.post("/movies/", json={ "search_criteria": {"name": "Inception", "actors": "Leonardo DiCaprio"}})
#     response_data = response.json()
#     assert response.status_code == 200
    
#     expected_result = [mock_data[0]]
    
#     assert len(response_data) == len(expected_result), "Number of results does not match"
    
#     for item in response_data:
#         assert any(
#             item["name"] == expected_item["name"] and
#             item["actors"] == expected_item["actors"] and
#             item["rank"] == expected_item["rank"] and
#             item["description"] == expected_item["description"] and
#             item["featured_review"] == expected_item["featured_review"]
#             for expected_item in expected_result
#         ), f"Item {item} does not match any expected result"

# def test_get_movies_with_invalid_field():
#     response = client.post("/movies/", json={"fields": ["invalid_field"]})
#     assert response.status_code == 400
#     assert "Invalid fields requested" in response.json()["detail"]

# def test_get_movies_with_invalid_search_field():
#     response = client.post("/movies/", json={"search_criteria": {"invalid_field": "value"}})
#     assert response.status_code == 400
#     assert "Search field 'invalid_field' does not exist in the data" in response.json()["detail"]




import pytest
from fastapi.testclient import TestClient
from main import app, load_data
from unittest.mock import patch

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
    with patch('main.load_data', return_value=mock_movies):
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
