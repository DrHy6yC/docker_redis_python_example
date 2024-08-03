from os import getenv
from dotenv import load_dotenv


def get_bool_from_str(text: str) -> bool:
    """
    Переводит строку из .env в python bool
    :return: Возвращает True когда param=True, в остальных случаях -> False
    """
    result: bool = False
    if text.lower() == "true":
        result = True
    return result


load_dotenv()

DB_IS_CREATED: bool = get_bool_from_str(getenv('DB_IS_CREATED'))
DB_HOST: str = getenv('DB_HOST')
DB_PORT: str = getenv('DB_PORT')
DB_USER: str = getenv('DB_USER')
DB_PASS: str = getenv('DB_PASS')
DB_NAME: str = getenv('DB_NAME')
DB_SQLite: str = getenv('DB_SQLite')
DB_DBMS: str = getenv('DB_DBMS')
DB_ECHO: bool = get_bool_from_str(getenv('DB_ECHO'))
