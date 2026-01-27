"""
db_codes/db_make.py is the file which i need to import in the main.py
I need to have this fun which i need to call from this file to start working with my db
create_db_and_engine()
"""

from pathlib import Path


from sqlmodel import SQLModel, create_engine


from db_codes.models import (
    UserModel,  # type: ignore
    WishItemModel,  # type: ignore
)


from utils.config_settings import SQLITE_DATABASE_FILE_NAME


# I need to import this so that i am calling the models before calling the making of the database


sqlite_file_path = Path.cwd() / SQLITE_DATABASE_FILE_NAME

sqlite_url = f"sqlite:///{sqlite_file_path}"


engine = create_engine(url=sqlite_url)


def create_db_and_engine():
    """
    This will create the db file & connection with the db,
    i need to call this in the main.y
    """
    sqlite_file_path.parent.mkdir(exist_ok=True)
    SQLModel.metadata.create_all(engine)
