"""
db_codes/db_make.py is the file which i need to import in the main.py
I need to have this fun which i need to call from this file to start working with my db
create_db_and_engine()
"""

from sqlmodel import SQLModel, create_engine


from db_codes.models import (
    UserModel,  # type: ignore
    WishItemModel,  # type: ignore
)

# from utils.config_settings import SQLITE_DATABASE_FILE_NAME
from utils.config import config_settings

# TODO i will make somethign to make the sqlite.db file here




engine = create_engine(url=config_settings.db_url)


def create_db_and_engine():
    """
    This will create the db file & connection with the db,
    i need to call this in the main.y
    """
    # sqlite_file_path.parent.mkdir(exist_ok=True)
    SQLModel.metadata.create_all(engine)
