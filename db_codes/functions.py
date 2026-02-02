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


class WishItemNotFound(Exception):
    pass


class WishItemOwnerNotMatch(Exception):
    pass


class WishItemUnknownError(Exception):
    """Something went wrong in the DB layer that is not covered by other custom errors."""

    pass


def verify_login_credentials(
    db_engine: Engine,
    username: str,
    password: str,
) -> UserModel | None:
    """
    Here i will pass the user's db's username and password
    it will check if correct it will send the user_obj or None otherwise
    """
    with Session(db_engine) as session:
        statement = select(UserModel).where(UserModel.username == username)
        results = session.exec(statement)
        user_obj = results.one_or_none()

        if not user_obj:
            logger.info(f"`{username}` is not present in the user table.")
            return None

        if user_obj.password == password:
            logger.debug(f"`{username}` and the `password` Has Been Matched Now...")
            return user_obj

        else:
            logger.info(f"`{username}` and `password` not matched now.")
            return None


def find_user_obj_from_user_id(
    db_engine: Engine,
    user_id: str,
) -> UserModel | None:
    """
    If the user exists it will send the user obj
    else it will send None
    """
    with Session(db_engine) as session:
        # i think later i need to do something to check if the user_id can be make as int or not
        statement = select(UserModel).where(UserModel.id_ == int(user_id))
        results = session.exec(statement)
        user_obj = results.one_or_none()
    return user_obj


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


def add_one_wish_item_for_a_user(
    db_engine: Engine,
    username: str,
    wish_name: str,
    wish_price: float,
    wish_link: str,
) -> WishItemModel | None:
    """
    If the wish item has insert successfully it will return the wish model obj else None
    Here i will pass the username of the user against whom i want to add
    some wish items list so i will do it here
    i need to make ti try except like this
    """
    wish_item_obj = WishItemModel(
        name=wish_name,
        price=wish_price,
        link=wish_link,
    )
    with Session(db_engine) as session:
        statement = select(UserModel).where(UserModel.username == username)
        results = session.exec(statement=statement)
        user_obj = results.one_or_none()
        if not user_obj:
            return None
        # i need to hink return somethign else, as when user will not has any wish items it should return None or empty list both will same not Noen i am confused
        user_obj.wish_items.append(wish_item_obj)
        session.add(user_obj)
        session.commit()
        session.refresh(wish_item_obj)
        return wish_item_obj


def get_wish_item_info(
    db_engine: Engine,
    wish_uuid: str,
) -> WishItemModel | None:
    """
    i want to pass the  wish item's  uuid
    and it should return the wish_model obj else none
    """
    with Session(db_engine) as session:
        statement = select(WishItemModel).where(WishItemModel.uuid == wish_uuid)
        results = session.exec(statement=statement)
        wish_obj = results.one_or_none()
        return wish_obj
    

    

def get_all_wish_items_for_a_user(
    db_engine: Engine,
    user_id: int,
) -> list[WishItemModel] | None:
    """
    here i will pass the username and it will return all the wishitems he owns
    then i think to iterate over those items and get a somethign to shows users
    """
    with Session(db_engine) as session:
        statement = select(UserModel).where(UserModel.id_ == user_id)
        results = session.exec(statement=statement)
        user_obj = results.one_or_none()
        if not user_obj:
            return None

        all_wish_items = user_obj.wish_items
        return all_wish_items


def delete_wish_item(
    db_engine: Engine,
    wish_uuid: str,
    user_id: int,
):
    """
    It will try to delete the wishitem by taking its uuid and user_id which is id_
    column's value and it will try to return true if success
    What Raise it can be
    WishItemNotFound
    WishItemOwnerNotMatch
    WishItemUnknownError
    """

    try:
        with Session(db_engine) as session:
            statement = select(WishItemModel).where(WishItemModel.uuid == wish_uuid)
            results = session.exec(statement=statement)
            wish_obj = results.one_or_none()

            if not wish_obj:
                raise WishItemNotFound()

            if wish_obj.user_id == user_id:
                session.delete(wish_obj)
                session.commit()
                return True

            else:
                raise WishItemOwnerNotMatch()

    except (WishItemNotFound, WishItemOwnerNotMatch):
        raise

    except Exception as e:
        logger.warning(msg="Somethigns wrong happens outside the custom error, " f"{e}")
        raise WishItemUnknownError() from e


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


def edit_old_wish_item(
    db_engine: Engine,
    wish_uuid: str,
    user_id: int,
    new_name: str,
    new_price: int,
    new_link: str,
):
    """
    i want if the edit was successfull it will return the wishitemmodel
    else it can raise some error or maybe none i need to think this
    It will try to edit the row of wish_item and then if any problem
    What Raise it can be
    WishItemNotFound
    WishItemOwnerNotMatch
    WishItemUnknownError
    """

    try:
        with Session(db_engine) as session:
            statement = select(WishItemModel).where(WishItemModel.uuid == wish_uuid)
            results = session.exec(statement=statement)
            wish_obj = results.one_or_none()

            if not wish_obj:
                raise WishItemNotFound()

            if wish_obj.user_id == user_id:
                wish_obj.name = new_name
                wish_obj.price = new_price
                wish_obj.link = new_link
                session.add(wish_obj)
                session.commit()
                session.refresh(wish_obj)
                return wish_obj

            else:
                raise WishItemOwnerNotMatch()

    except (WishItemNotFound, WishItemOwnerNotMatch):
        raise

    except Exception as e:
        logger.warning(msg="Somethigns wrong happens outside the custom error, " f"{e}")
        raise WishItemUnknownError() from e
