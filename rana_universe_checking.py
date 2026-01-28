"""
This is for checking my differnet code logic
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from db_codes import functions
from db_codes.db_make import engine

y = functions.find_user_obj_from_username(engine, "a")
print(y)


# x = functions.add_new_user(
#     db_engine=engine,
#     first_name="Rana",
#     username="asdfsdfsdfdsfdn",
#     password="aaa",
# )


# print("x value is", x)
# print("Upper i want to print")

# print(type(x))
# print(x.__repr__())
