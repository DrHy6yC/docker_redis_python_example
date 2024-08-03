from typing import Union
from sqlalchemy.ext.asyncio import AsyncEngine

from .engine import async_session_sql_connect, sql_async_engine
from .models import *


ModelsORM = UsersORM, QuizzesORM, ConstantsORM, UserQuizzesORM, UserLevelsORM, QuizeAnswersORM, \
    QuizeQuestionsORM, UserAnswersORM


async def async_create_all_table(async_engine: AsyncEngine) -> None:
    """
    Пересоздает(Если есть) все таблицы наследуемые от Base
    :param async_engine: Принимает sql_async_engine/подключение
    :return: Ничего не возвращает
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_insert_data_list_to_bd(list_data: list[Union[ModelsORM]]) -> None:
    async with async_session_sql_connect() as session_sql:
        session_sql.add_all(list_data)
        await session_sql.commit()


async def filling_min_db() -> None:
    """
        Функция для перезаписи БД и заполнение необходимых параметров для начала работы бота:

        * Константы
        * Тесты
        * Уровни

    """
    help_txt = """  
    Этот бот умеет:

    * Переводить словосочетания в инлайн режиме если упомянуть @English_bot_help_HW_bot в сообщениях;

    * Ещё запускать тесты, которые подскажут твой уровень знания английского (Грамматика). 

    В скором времени будет напоминать о тех словах что нужно выучить.
    """

    hi_txt = """   
    Привет, @FIO! Это бот который проверит твои знания по английскому языку.

    Используй кнопку помощи, если хочешь узнать что может бот сейчас.

    Или переходи сразу к тесту и удивись своему уровню!
    """

    TEXT_HI = ConstantsORM(
        CONSTANT_NAME='TEXT_HI',
        CONSTANT_VALUE=hi_txt
    )

    TEXT_HELP = ConstantsORM(
        CONSTANT_NAME='TEXT_HELP',
        CONSTANT_VALUE=help_txt
    )

    CREATE_TIME_BD = ConstantsORM(
        CONSTANT_NAME='CREATE_TIME_BD',
        CONSTANT_VALUE=str(datetime.datetime.now())
    )

    status_quize_Selected = QuizeStatusesORM(
        ID=1,
        STATUS_TEXT='Selected'
    )

    status_quize_Launched = QuizeStatusesORM(
        ID=2,
        STATUS_TEXT='Launched'
    )
    status_quize_Stopped = QuizeStatusesORM(
        ID=3,
        STATUS_TEXT='Stopped'
    )
    status_quize_Revoked = QuizeStatusesORM(
        ID=4,
        STATUS_TEXT='Revoked'
    )
    status_quize_Completed = QuizeStatusesORM(
        ID=5,
        STATUS_TEXT='Completed'
    )

    status_quize_Deleted = QuizeStatusesORM(
        ID=6,
        STATUS_TEXT='Deleted'
    )

    level_A0 = UserLevelsORM(
        LEVEL_TEXT='No level',
        MIN_LEVEL_SCORE=0,
        MAX_LEVEL_SCORE=5
    )

    level_A1 = UserLevelsORM(
        LEVEL_TEXT='Beginner (A1)',
        MIN_LEVEL_SCORE=6,
        MAX_LEVEL_SCORE=30
    )

    level_A2 = UserLevelsORM(
        LEVEL_TEXT='Elementary (A2)',
        MIN_LEVEL_SCORE=31,
        MAX_LEVEL_SCORE=60
    )

    level_B1 = UserLevelsORM(
        LEVEL_TEXT='Pre-Intermediate (B1)',
        MIN_LEVEL_SCORE=61,
        MAX_LEVEL_SCORE=90
    )

    level_B2 = UserLevelsORM(
        LEVEL_TEXT='Intermediate (B2)',
        MIN_LEVEL_SCORE=91,
        MAX_LEVEL_SCORE=100
    )

    await async_create_all_table(sql_async_engine)
    await async_insert_data_list_to_bd([
        TEXT_HI, TEXT_HELP, CREATE_TIME_BD,
        status_quize_Selected, status_quize_Launched, status_quize_Stopped,
        status_quize_Revoked, status_quize_Completed, status_quize_Deleted,
        level_A0, level_A1, level_A2, level_B1, level_B2,
    ])

    # await async_import_survey_csv("English Level test. Grammar.csv",
    #                               "Основной тест для проверки уровня английского (грамматика)")
    #
    # await async_import_survey_csv("Who test.csv",
    #                               "Микро тест для проверки работоспособности теста")
