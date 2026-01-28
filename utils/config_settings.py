# this is utils/config_settings.py
# Here i will keep some information about what to use for now i am using this
# later maybe i will use toml file for settings

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True


SECRET_KEY = "RanaUniverse"


# I did this below if true it will shows log in console
# otherwise if false it will not shows in console
# For local testing i will want this below to be True to shows the info in the temrinal
enable_console_logging: bool = True


# The logger files data will be saved here in thsi file
LOG_FILE_NAME = "web_app.log"


# The sqlite file name for database is below
SQLITE_DATABASE_FILE_NAME = "database.db"
