"""
db_codes/models.py
in this file i will create the logics of the models of what what i will have
"""

from uuid import uuid4


from flask_login import UserMixin  # type: ignore

from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)



def generate_hex_uuid4() -> str:
    return str(uuid4().hex)


class UserModel(SQLModel, UserMixin, table=True):
    """
    For now i am saving the password as plain str
    later i need to change this must
    """

    __tablename__: str = "user_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str | None = Field(default=None)
    phone_no: str | None = Field(default=None)
    username: str = Field(unique=True)
    password: str

    wish_items: list["WishItemModel"] = Relationship(back_populates="user")

    def get_id(self) -> str:
        """
        This is the method which will run by the flask-login
        it will get the unique identificaiton per user thats why i make this
        as the docs say this here-
        https://flask-login.readthedocs.io/en/latest/#your-user-class
        """
        return str(self.id_)


class WishItemModel(SQLModel, table=True):
    """
    All the item/object belongs to one user
    so it will need to make in this way
    """

    __tablename__: str = "wish_item_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    link: str

    uuid: str = Field(default_factory=generate_hex_uuid4, unique=True)

    user_id: int | None = Field(default=None, foreign_key="user_data.id_")

    user: UserModel = Relationship(back_populates="wish_items")
