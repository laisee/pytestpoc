pytest_plugins = [
   "tests.fixtures.alpha",
   "tests.fixtures.beta",
   "tests.fixtures.zeta",
   "tests.fixtures.user",
   "tests.fixtures.user_default",
]

def idfn(val):
    return val["name"]


def idbal(val):
    return "bal{}".format(val)


def idage(val):
    return "age{}".format(val)


PEOPLE = [
    {"name": "default", "age": 0, "balance": 0},
    {"name": "aidan", "age": 12, "balance": 1200},
    {"name": "claire", "age": 32, "balance": 3200},
    {"name": "gavin", "age": 52, "balance": 5200},
    {"name": "mike", "age": 16, "balance": 1600},
]
