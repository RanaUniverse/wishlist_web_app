"""
db_codes/functions.py
Here i will make some functions which will i need to call easily in different
modules to work some about the databases
"""

from sqlalchemy import Engine

from sqlmodel import Session, select

from db_codes.models import UserModel, WishItemModel


def find_user_obj_from_username(
    db_engine: Engine,
    username: str,
):
    with Session(db_engine) as session:
        statement = select(UserModel).where(UserModel.username == username)
        results = session.exec(statement)
        user_obj = results.one()
        return user_obj


def add_new_user(
    db_engine: Engine,
    first_name: str,
    username: str,
    password: str,
    last_name: str | None = None,
    phone_no: str | None = None,
):
    """
    I wish i will provide one user details and it will
    insert the user data in the table and say me if not wrong
    """

    with Session(db_engine) as session:
        user_obj = UserModel(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            username=username,
            password=password,
        )
        session.add(user_obj)
        session.commit()
        return user_obj


def add_new_wish_item(
    db_engine: Engine,
    name: str,
    price: float,
    link: str,
    username: str,
):

    with Session(db_engine) as session:
        user_obj = find_user_obj_from_username(
            db_engine=db_engine,
            username=username,
        )
        if not user_obj:
            return None
        wish_obj = WishItemModel(
            name=name,
            price=price,
            link=link,
            user=user_obj,
        )
        session.add(wish_obj)
        session.commit()
        return wish_obj
