from flask import Flask, render_template, request, redirect
from database_connection import DatabaseConnection
from book_repository import BookRepository
from film_repository import FilmRepository
from user_repository import UserRepository
from book import Book
from user import User

# instantiate a Flask app object
app = Flask(__name__)

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"


@app.route('/books', methods=['GET'])
def get_all_books():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  books = book_repository.all()
  return render_template("books.html", books = books)


@app.route('/books', methods=['POST'])
def create_book():
    # make a new database connection
    connection = DatabaseConnection()
    connection.connect()

    # make a new instance of BookRepository
    book_repository = BookRepository(connection)

    # get the request body
    book_details = request.form

    # my BookRepository expects an instance of Book, so make one here
    book = Book(title=book_details["title"], author=book_details["author"])

    # save the book
    book_repository.create(book)

    # return a 201, which means "created"
    return redirect("/books")


@app.route('/authors', methods=['GET'])
def authors():
    return [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)


@app.route('/films', methods=['GET'])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()

    return render_template("films.html", films = films)


@app.route('/users/new', methods=['GET'])
def get_signup_form():

  return render_template("signup_form.html")


@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()

    user_repository = UserRepository(connection)

    user_details = request.form

    user = User(username = user_details["username"], password = user_details["password"])

    print(user_details)

    user_repository.create(user)

    return redirect("/books")


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)