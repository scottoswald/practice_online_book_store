from playwright.sync_api import Page, expect
# from database_connection import DatabaseConnection
# from book_repository import BookRepository

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Here are all of our books:")

def test_has_ul(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    ul = page.locator("ul")

    expect(ul).to_contain_text("The Gruffalo")

def test_has_border(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    ul = page.locator("ul")

    expect(ul).to_have_css("border-top-style", "solid")
    expect(ul).to_have_css("border-top-width", "3px")


def test_book_list_contains_all_books(db_connection, page: Page):

    db_connection.seed("seeds/books.sql") 
    # Don't need the lines below, unlike when we tested databases, becuase its coved with 'books = page.locator('li')' ...
    # repository = BookRepository(db_connection)
    # books = repository.all()

    page.goto("http://127.0.0.1:5001/books")

    books = page.locator('li')

    expect(page.locator(".book-title")).to_have_text([
        "The Gruffalo",
        "Ada Twist, Scientist",
        "The Girl Who Drank the Moon",
        "Dragons in a Bag",
    ])
    expect(books).to_have_count(4)
    expect(books.first).to_contain_text("by Julia Donaldson")


def test_created_book_added(db_connection, page: Page):

    # Connect to Database
    db_connection.seed("seeds/books.sql")

    # Go to books route
    page.goto("http://127.0.0.1:5001/books")

    # Fill in Title input
    page.get_by_label("Title").fill("Mrs Dalloway")

    # Fill in Author input
    page.get_by_label("Author").fill("Virginia Woolf")

    # Click the submit button
    page.get_by_role("button", name="Submit").click()

    # Find all the list elements
    books = page.locator('li')

    # A Playwright test - see that new title is added
    expect(page.locator(".book-title")).to_have_text([
        "The Gruffalo",
        "Ada Twist, Scientist",
        "The Girl Who Drank the Moon",
        "Dragons in a Bag",
        "Mrs Dalloway"
    ])
    
    # A Playwright test - see that new author is added
    expect(page.locator(".book-author")).to_have_text([
        "Julia Donaldson",
        "Andrea Beaty",
        "Kelly Barnhill",
        "Zetta Elliott",
        "Virginia Woolf",
    ])

    # A Playwright test - see that new book has increased the count of books
    expect(books).to_have_count(5)

    # A Playwright test - see that the last book's author is correct
    expect(books.last).to_contain_text("by Virginia Woolf")

    # A Pytest test - see that the created book is in the right format (from Python)
    assert books.all_inner_texts()[-1] == "Mrs Dalloway\nby Virginia Woolf"

    # A Playwright test - see that the created book is in the right format (on Browser)
    expect(books.last).to_have_text("Mrs Dalloway\nby Virginia Woolf", use_inner_text=True)