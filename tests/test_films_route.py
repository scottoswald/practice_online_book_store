from database_connection import DatabaseConnection
from app import app

def test_films_responds_200():
    client = app.test_client()
    response = client.get("/films")
    assert response.status_code == 200

    