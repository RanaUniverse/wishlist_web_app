# This is utils/config_settings.py file
# I will want the values comes from the environment variables,
# Then it will be change this type accordingly in this file of code
# so that i can use this easily in all my places from import from here


import os
import sys

name_str = os.getenv("NAME")
FLASK_DEBUG_str = os.getenv("FLASK_DEBUG")
FLASK_HOST_str = os.getenv("FLASK_HOST")
FLASK_PORT_str = os.getenv("FLASK_PORT")
SECRET_KEY_str = os.getenv("SECRET_KEY")
LOG_FILE_NAME_str = os.getenv("LOG_FILE_NAME")
ENABLE_CONSOLE_LOGGING_str = os.getenv("ENABLE_CONSOLE_LOGGING")
SQLITE_DATABASE_FILE_NAME_str = os.getenv("SQLITE_DATABASE_FILE_NAME")


if not FLASK_DEBUG_str:
    sys.exit("The FLASK_DEBUG need to exists in the .env")
FLASK_DEBUG = FLASK_DEBUG_str.lower() == "true"


if not FLASK_HOST_str:
    sys.exit("The FLASK_HOST is not present in the .env")
FLASK_HOST = FLASK_HOST_str


if not FLASK_PORT_str:
    sys.exit("The FLASK_PORT is not present in the .env")
try:
    FLASK_PORT = int(FLASK_PORT_str)
except ValueError:
    sys.exit("FLASK_PORT must be a valid integer in .env")


if not SECRET_KEY_str:
    sys.exit("The SECRET_KEY is not present in the .env")
SECRET_KEY = SECRET_KEY_str


if not LOG_FILE_NAME_str:
    sys.exit("For logging the LOG_FILE_NAME should present in the .env")
LOG_FILE_NAME = LOG_FILE_NAME_str


if not ENABLE_CONSOLE_LOGGING_str:
    sys.exit("You need to say if console logging is enable or not in bool")
ENABLE_CONSOLE_LOGGING = ENABLE_CONSOLE_LOGGING_str.lower() == "true"


if not SQLITE_DATABASE_FILE_NAME_str:
    sys.exit("The Database file name required for sqlite in the .env file")
SQLITE_DATABASE_FILE_NAME = SQLITE_DATABASE_FILE_NAME_str


if __name__ == "__main__":
    print("This is running goodly`")

    print(SQLITE_DATABASE_FILE_NAME)
    print(type(SQLITE_DATABASE_FILE_NAME))
