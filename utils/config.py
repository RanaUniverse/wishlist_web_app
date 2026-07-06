"""
utils/config.py

Here i will write the configuration settings from the .env file
And i will use this to take the values form the environemtn and use this
"""

from pathlib import Path


from pydantic import (
    Field,
)

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

# the test dir is for storing the logger and normal
# database sqlite .db file to store here
TEST_DIR = Path("test_data")
TEST_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class ConfigSettings(BaseSettings):
    """
    Env variable settings will be here
    """

    model_config = SettingsConfigDict(
        extra="ignore",
        env_ignore_empty=True,
    )

    # Flask Related Things
    app_host: str = Field(
        description="This will say about the host maybe localhost or 0.0.0.0",
    )
    app_port: int = Field(
        description="Port Number of 4 Digit to use here like default 5555 or 9999",
    )
    app_debug: bool = Field(
        description="I should not use true in deployment, for locally i can use true",
    )
    app_secret_key: str = Field(
        description="Secret key it will need by flask_login also to make encrypted thigns",
    )

    # logging related
    enable_console_logging: bool = True
    enable_file_logging: bool = True
    log_file_name: str = "web_app.log"

    # Database url below
    sqlite_filename: str = "database.db"
    # i keep below false so that by default i can use sqlite when
    # not pass in the environment variable
    use_postgres: bool = False

    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def sqlite_filepath(self) -> Path | None:
        """
        It will return None if he don't want to use sqlite
        else if he want to use sqlite db its filepath will be out
        """
        if self.use_postgres:
            return None
        else:
            sq_path = TEST_DIR / self.sqlite_filename
            return sq_path

    @property
    def db_url(self) -> str:
        if self.use_postgres:
            POSTGRES_URL = (
                f"postgresql+psycopg2://"
                f"{self.db_username}:"
                f"{self.db_password}@"
                f"{self.db_host}:"
                f"{self.db_port}/"
                f"{self.db_name}"
            )
            return POSTGRES_URL

        else:
            SQLITE_URL = f"sqlite:///" f"{self.sqlite_filepath}"

            return SQLITE_URL


# i will use this below instance in all my needed module
config_settings = ConfigSettings()  # type: ignore


if __name__ == "__main__":
    # print(config_settings)
    # print(config_settings.app_debug)
    # print(type(config_settings.app_debug))
    print(config_settings.db_url)
