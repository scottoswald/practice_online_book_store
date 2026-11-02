from film import Film

class FilmRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    # id is now the third arugemnt (see book.py to get reason why)
    def all(self):
        rows = self._connection.execute('SELECT * FROM films')
        films = []
        for row in rows:
            item = Film(row["title"], row["genre"], row["release_year"], row["rating"], row["id"])
            films.append(item)
        return films