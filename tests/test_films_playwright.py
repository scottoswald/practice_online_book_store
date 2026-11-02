from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/films")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Film List")

def test_has_film_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")

    list = page.locator("li")
    films = list.all_inner_texts()

    assert films == [
        "Monsters Inc - Animated - 2001 - G",
        "The Shawshank Redemption - Drama - 1994 - R",
        "The Godfather - Gangster - 1972 - R",
        "The Dark Knight - Superhero - 2008 - PG-13"
    ]