from user import User

class UserRepository():

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # See all users
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["username"], row["password"], row["id"])
            users.append(item)
        return users

    # Create a new user
    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (username, password) VALUES (%s, %s)',
            [user.username, user.password]
        )
        return None