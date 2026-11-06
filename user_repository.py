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

    
    # # Find a user
    # def find_by_username(self, username):
    #     user_details = self._connection.execute(
    #         'SELECT * FROM users WHERE username = %s', [username]
    #     )[0]

    #     return User(
    #         user_details["username"],
    #         user_details["password"],
    #         user_details["id"]
    #     )

    # Find a user
    def find_by_username(self, username):
        user_details = self._connection.execute(
            'SELECT * FROM users WHERE username = %s', [username]
        )
        
        if not user_details:
            return None
        
        else:
            user_detail = user_details[0]
            return User(
                user_detail["username"],
                user_detail["password"],
                user_detail["id"]
            )
