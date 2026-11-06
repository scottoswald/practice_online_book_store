import pytest
from user_repository import UserRepository
from user import User

class TestUserRepository:
    @pytest.fixture
    def user_repository(self, db_connection):
        return UserRepository(db_connection)


    def test_find_user(self, user_repository, db_connection):
        db_connection.seed("seeds/users.sql")
        login_details = user_repository.find_by_username("Test One")
        print(f"here are the login details - {login_details}")

        assert login_details.username == "Test One"
        assert login_details.password == "Test One PW"

    def test_find_non_user(self, user_repository, db_connection):
        db_connection.seed("seeds/users.sql")
        login_details = user_repository.find_by_username("Non User")
        
        assert login_details is None
