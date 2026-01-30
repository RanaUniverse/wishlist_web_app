"""
This is for checking my differnet code logic
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


import random

from db_codes.functions import add_one_wish_item_for_a_user, find_user_obj_from_username, get_all_wish_items_for_a_user
from db_codes.models import UserModel, WishItemModel
from db_codes.db_make import engine

wish_obj = WishItemModel(
    name="Apple",
    price=33.22,
    link="https://www.google.com/search?q=apple",
)



y = add_one_wish_item_for_a_user(
    engine,
    "ranaa",
    wish_name="dfd",
    wish_price=float(random.randint(1, 999999)),
    wish_link="https://www.google.com/search?q=appsdfdsfle",
)
print(type(y))
print(y)


