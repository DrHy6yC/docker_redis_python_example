from .config_db import *

from icecream import ic

from .database import DBMYSQL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine


def get_async_engine(async_dsn_db: str, is_echo: bool) -> AsyncEngine:
    """
    Функция запуска главного движка sql/подключения синхронно
    :dsn_db: принимает в себя строку подключения
    :is_echo: включения/отключения транслирования команд SQL генерируемых sqlalchemy в консоль
    :return: возвращает экземпляр класса Engine из sqlalchemy.engine.base
    """
    engine = create_async_engine(
        url=async_dsn_db,
        echo=is_echo

    )
    return engine


db_mysql = DBMYSQL()

is_created_db = DB_IS_CREATED
is_echo_db = DB_ECHO
ic(is_created_db, is_echo_db)

async_dsn = db_mysql.get_async_dsn()
sql_async_engine = get_async_engine(async_dsn, is_echo_db)
async_session_sql_connect = async_sessionmaker(sql_async_engine)
