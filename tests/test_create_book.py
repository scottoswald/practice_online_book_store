# from playwright.sync_api import Page, expect
# # from database_connection import DatabaseConnection
# # from book_repository import BookRepository


# def test_created_book_added(db_connection, page: Page):

#     # Connect to Database
#     db_connection.seed("seeds/books.sql")

#     # Go to books route
#     page.goto("http://127.0.0.1:5001/books")

#     # Fill in Title input
#     page.get_by_label("Title").fill("Mrs Dalloway")

#     # Fill in Author input
#     page.get_by_label("Author").fill("Virginia Woolf")

#     # Click the submit button
#     page.get_by_role("button", name="Submit").click()

#     # Find all the list elements
#     books = page.locator('li')

#     # A Playwright test - see that new title is added
#     expect(page.locator(".book-title")).to_have_text([
#         "The Gruffalo",
#         "Ada Twist, Scientist",
#         "The Girl Who Drank the Moon",
#         "Dragons in a Bag",
#         "Mrs Dalloway"
#     ])
    
#     # A Playwright test - see that new author is added
#     expect(page.locator(".book-author")).to_have_text([
#         "Julia Donaldson",
#         "Andrea Beaty",
#         "Kelly Barnhill",
#         "Zetta Elliott",
#         "Virginia Woolf",
#     ])

#     # A Playwright test - see that new book has increased the count of books
#     expect(books).to_have_count(5)

#     # A Playwright test - see that the last book's author is correct
#     expect(books.last).to_contain_text("by Virginia Woolf")

#     # A Pytest test - see that the created book is in the right format (from Python)
#     assert books.all_inner_texts()[-1] == "Mrs Dalloway\nby Virginia Woolf"

#     # A Playwright test - see that the created book is in the right format (on Browser)
#     expect(books.last).to_have_text("Mrs Dalloway\nby Virginia Woolf", use_inner_text=True)


from playwright.sync_api import Page
from database_connection import DatabaseConnection

def test_create_new_book(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("username").fill("test")
    page.get_by_label("password").fill("1234")
    page.get_by_role("button").click()

    page.goto("http://localhost:5001/books")
    page.get_by_label("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_label("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat)\nby Geronimo"
