import pytest
from user import User

@pytest.fixture
def user_default():
    return User()
