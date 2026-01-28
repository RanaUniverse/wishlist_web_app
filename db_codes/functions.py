"""
db_codes/functions.py
Here i will make some functions which will i need to call easily in different
modules to work some about the databases
"""

from sqlalchemy import Engine
from sqlalchemy.exc import IntegrityError

from sqlmodel import Session, select

from db_codes.models import UserModel, WishItemModel

from utils.custom_logger import logger


def find_user_obj_from_username(
    db_engine: Engine,
    username: str,
):
    with Session(db_engine) as session:
        statement = select(UserModel).where(UserModel.username == username)
        results = session.exec(statement)
        user_obj = results.one_or_none()
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
    if the user not insert in the db i will return none
    """

    with Session(db_engine) as session:
        user_obj = UserModel(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            username=username,
            password=password,
        )
        try:
            session.add(user_obj)
            session.commit()
            session.refresh(user_obj)
            return user_obj

        except IntegrityError as e:
            logger.warning(
                "there is some integrity problem in the username column maybe" f"{e}"
            )
            return None

        except Exception as e:
            logger.warning(
                "Somethings wrong in db level has happens, when i try to add the user in the db"
                f"{e}"
            )
            return None


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
        session.refresh(wish_obj)
    return wish_obj
