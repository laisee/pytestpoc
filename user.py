import random

MIN_AGE = 0
MAX_AGE = 100

MIN_BALANCE = 0
MAX_BALANCE = 8800


class User:
    def __init__(self, name="gavin", age=(MIN_AGE + MAX_AGE) / 2, balance=0):
        self.name = name
        self.balance = balance
        self.age = age

    def Name(self):
        return self.name

    def __repr__(self):
        return f"{self.name} [{self.age}] has balance ${self.balance}"

    def __str__(self):
        return f"{self.name} [{self.age}] has balance ${self.balance}"
