import pytest
import random

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[: current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from conftest import idbal, idfn, idage, PEOPLE
from user import User, MIN_AGE, MAX_AGE, MIN_BALANCE, MAX_BALANCE


class TestUser(object):
    """
    """

    @pytest.mark.user
    def test_user_name_is_correct2(self, user):
        assert user.name is not None, f"User {user} {type(user)}"

    @pytest.mark.user
    def test_user_age_is_correct2(self, user):
        assert user.age >= 0, f"User {user} {type(user)}"

    @pytest.mark.user
    def test_user_balance_is_correct2(self, user):
        assert user.balance >= 0, f"User {user} {type(user)}"

    @pytest.mark.user
    def test_user_default_all(self, user_default):
        # assert user_default.Name() == PEOPLE[0]["name"], "User name {}".format(user_default.Name())
        assert user_default.Name() in [user["name"] for user in PEOPLE], "User name {}".format(
            user_default.Name()
        )
        assert user_default.balance == 0
        assert user_default.age == (MIN_AGE + MAX_AGE) / 2

    @pytest.mark.user
    def test_user_default_balance_is_correct(self, user_default):
        assert user_default.balance == 0

    @pytest.mark.user
    def test_user_default_age_is_correct(self, user_default):
        assert user_default.age == (MIN_AGE + MAX_AGE) / 2


    @pytest.mark.user
    def test_user_default_name_is_correct(self, user_default):
        assert user_default.Name() in [user["name"] for user in PEOPLE], "User name {}".format(
            user_default.Name()
        )


    @pytest.mark.user
    def test_user_name_is_correct(self, user):
        idx = [user["name"] for user in PEOPLE].index(user.Name())
        assert idx >= 0, f"Error - could not locate user name '{user.Name()}' in PEOPLE list [{[user['name'] for user in PEOPLE]}]"


    @pytest.mark.parametrize(
        "balance", [100, 200, 300, 400, 500, 600, 700, 800, 900], ids=idbal
    )
    @pytest.mark.parametrize("age", [10, 20, 30, 40, 50, 60, 70, 80, 90], ids=idage)
    @pytest.mark.user
    def test_user_str_is_correct(self, user, age, balance):
        assert str(user) == f"{user.name} [{user.age}] has balance ${user.balance}"


    @pytest.mark.user
    @pytest.mark.parametrize(
        "balance", [100, 200, 300, 400, 500, 600, 700, 800, 900], ids=idbal
    )
    @pytest.mark.parametrize("age", [10, 20, 30, 40, 50, 60, 70, 80, 90], ids=idage)
    def test_user_repr_is_correct(self, user, age, balance):
        assert repr(user) == f"{user.name} [{user.age}] has balance ${user.balance}"


    @pytest.mark.user
    @pytest.mark.parametrize(
        "balance", [100, 200, 300, 400, 500, 600, 700, 800, 900], ids=idbal
    )
    def test_user_bal_is_correct(self, user, balance):
        assert user.balance <= MAX_BALANCE and user.balance >= MIN_BALANCE
    

    @pytest.mark.user
    @pytest.mark.parametrize("age", [10, 20, 30, 40, 50, 60, 70, 80, 90], ids=idage)
    def test_user_age_is_correct(self, user, age):
        assert user.age < MAX_AGE and user.age >= MIN_AGE
