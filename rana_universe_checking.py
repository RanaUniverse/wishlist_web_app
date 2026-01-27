"""
This is for checking my differnet code logic
"""

from db_codes import functions
from db_codes.db_make import engine

x = functions.add_new_user(
    db_engine=engine,
    first_name="Rana",
    username="somfkk9",
    password="aaa",
)


print(x)
print("Upper i want to print")

print(type(x))
print(x.__repr__())
