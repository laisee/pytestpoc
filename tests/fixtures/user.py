import pytest
from conftest import idfn

from user import User


PEOPLE = [
    {"name": "default", "age": 0, "balance": 0},
    {"name": "aidan", "age": 12, "balance": 1200},
    {"name": "claire", "age": 32, "balance": 3200},
    {"name": "gavin", "age": 52, "balance": 5200},
    {"name": "mike", "age": 16, "balance": 1600},
]

@pytest.fixture(params=PEOPLE, ids=idfn)
def user(request):
    return User(name=request.param["name"], age= request.param["age"], balance = request.param["balance"])
