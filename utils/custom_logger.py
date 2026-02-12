"""
This is utils.custom_logger.py file
I make this for checking how this will work
"""


from pathlib import Path


import logging


from utils.config_settings import enable_console_logging, LOG_FILE_NAME


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="{asctime} - {levelname} - {name} - {filename} - {lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)


file_handler = logging.FileHandler(
    filename=Path("files_and_folders") / LOG_FILE_NAME,
    mode="a",
    encoding="utf-8",
)
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)


if enable_console_logging:
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)
    console_handler.setFormatter(formatter)


if __name__ == "__main__":
    logger.debug("Somethings Happens")
