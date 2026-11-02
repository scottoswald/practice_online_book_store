import sys
import os

from app import app
from database_connection import DatabaseConnection

# Two methods to do this:

# 1. Use our normal seed from SQL file method...

def test_create_user_is_saved_to_database_using_seed(db_connection):
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # seed the user table
    db_connection.seed("seeds/users.sql")

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()

   # send the request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'


# 2. Execute a 'TRUNCATE' command, so no need to seed or have a 'db_connection' argument...

def test_create_user_is_saved_to_database_using_execute_truncate():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()

    # use execute to send a TRUNCATE TABLE query
    connection.execute("TRUNCATE TABLE users;")

   # send the request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'


