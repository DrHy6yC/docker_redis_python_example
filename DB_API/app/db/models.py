import datetime
from typing import Annotated

from sqlalchemy import BigInteger, String, Text, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

int_pk = Annotated[int, mapped_column(primary_key=True)]
big_int = Annotated[int, mapped_column(BigInteger)]
big_int_uniq = Annotated[int, mapped_column(BigInteger, unique=True)]
int_serv_def_0 = Annotated[int, mapped_column(server_default='0')]
int_serv_def_1 = Annotated[int, mapped_column(server_default='1')]

date_now = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

txt = Annotated[str, mapped_column(Text)]

str_512 = Annotated[str, mapped_column(String(512))]
str_256 = Annotated[str, mapped_column(String(256))]
str_50 = Annotated[str, mapped_column(String(50))]


# TODO тригер меняющий UPDATE_TIME при изменении таблиц
class Base(DeclarativeBase):
    """Базовый класс
    При запуске orm.create_all_table создаются все таблицы которые были унаследованны от класса Base

    Note:
        При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!
    """

    type_annotation = {
        str_50: String(50),
        str_256: String(256),
        str_512: String(512)

    }


class UsersORM(Base):
    """Класс Юзеров телеграмма

    Хранит информацию о пользователе полученную из тг

    Note:
    USER_TG_ID не всегда помещается в int, приходиться использовать bigint

    !При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!

    Attributes:
    ----------
    ID -  ИД в БД

    USER_TG_ID - Ид в тг

    USER_LOGIN - Логин в тг

    USER_FULL_NAME - Полное имя фамилия из тг

    USER_LEVEL: - Уровень который определяется после прохождения теста English Level test. Grammar

    USER_ACCESS: - Уровень доступа (Админ, Учитель, Пользователь)

    CREATE_TIME: - Дата внесения пользователя в БД

    UPDATE_TIME: - Дата изменения данных пользователя
    """

    __tablename__ = 'USERS'
    ID: Mapped[int_pk]
    USER_TG_ID: Mapped[big_int_uniq] = mapped_column(unique=True)
    USER_LOGIN: Mapped[str_256] = mapped_column(unique=True)
    USER_FULL_NAME: Mapped[str_256]
    USER_LEVEL: Mapped[int_serv_def_1] = mapped_column(
        ForeignKey('USER_LEVELS.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    USER_ACCESS: Mapped[int_serv_def_0]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class QuizzesORM(Base):
    """ Класс Опросника где находятся название теста и их описание

    Note:
        Не создавать тесты с именем 'Отмена',
        потому что первым регистрируется каллбэк хэндлером для функции delete_message
        с фильтром call_data_test.filter(name_test='Отмена')

        При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!


    Attributes
    ----------
    ID:
        ИД в БД
    QUIZE_NAME:
        Имя теста
    QUIZE_DESCRIPTION:
        Описание теста
    CREATE_TIME:
        Дата и время создания опросника
    UPDATE_TIME:
        Дата и время изменения опросника
    """

    __tablename__ = 'QUIZZES'
    ID: Mapped[int_pk]
    QUIZE_NAME: Mapped[str_50] = mapped_column(unique=True)
    QUIZE_DESCRIPTION: Mapped[str_256]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class QuizeQuestionsORM(Base):
    """ Класс с вопросами опросника
    Note:
        При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!

    Attributes
    ----------
    ID:
        ИД в БД
    ID_QUIZE:
        ИД опросника в таблице QUIZZES
    QUESTION_NUMBER:
        Номер вопроса
    QUESTION_TEXT:
        Текст вопроса
    CREATE_TIME:
        Дата и время создания вопроса
    UPDATE_TIME:
        Дата и время изменения вопроса
    """

    __tablename__ = 'QUIZE_QUESTIONS'
    ID: Mapped[int_pk]
    ID_QUIZE: Mapped[int] = mapped_column(
        ForeignKey('QUIZZES.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    QUESTION_NUMBER: Mapped[int]
    QUESTION_TEXT: Mapped[str_512]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class QuizeAnswersORM(Base):
    """
    При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!
    """

    __tablename__ = 'QUIZE_ANSWERS'
    ID: Mapped[int_pk] = mapped_column(autoincrement=True, )
    ID_QUIZE: Mapped[int] = mapped_column(
        ForeignKey('QUIZZES.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    QUESTION_NUMBER: Mapped[int]
    ANSWER_NUMBER: Mapped[int]
    ANSWER_TEXT: Mapped[str_512]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class QuizeTrueAnswersORM(Base):
    """
    При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!
    """

    __tablename__ = 'QUIZE_TRUE_ANSWERS'
    ID: Mapped[int_pk]
    ID_QUIZE: Mapped[int] = mapped_column(
        ForeignKey('QUIZZES.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    ID_ANSWER: Mapped[int] = mapped_column(
        ForeignKey('QUIZE_ANSWERS.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    QUESTION_NUMBER: Mapped[int]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class QuizeStatusesORM(Base):
    """
    При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!
    """

    __tablename__ = 'QUIZE_STATUSES'
    ID: Mapped[int_pk]
    STATUS_TEXT: Mapped[str_50] = mapped_column(unique=True)
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class UserQuizzesORM(Base):
    """ Класс запущенных пользователем тестов, каждый запущеный тест будет новой строкой в бд и новым объектом класса

    Note:
        При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!

    Attributes
    ----------
    ID:
        ИД в БД
    ID_USER_TG:
        ИД пользователя запустившего тест
    ID_QUIZE:
        ИД теста который запустил пользователь
    QUIZE_STATUS:
        Описывает в каком статусе сейчас тест
    QUESTION_NUMBER:
        Номер вопроса на котором остановился пользователь
    ID_ANSWER_LAST:
        Последний ответ пользователя
    QUIZE_SCORE:
        Кол-во очков которое получил пользователь за правильные ответы
    CREATE_TIME:
        Дата и время создания теста
    UPDATE_TIME:
        Дата и время изменения теста
    """

    __tablename__ = 'USER_QUIZZES'
    ID: Mapped[int_pk]
    ID_USER_TG: Mapped[big_int] = mapped_column(
        ForeignKey('USERS.USER_TG_ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    ID_QUIZE: Mapped[int_serv_def_0] = mapped_column(
        ForeignKey('QUIZZES.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    QUIZE_STATUS: Mapped[int] = mapped_column(
        ForeignKey('QUIZE_STATUSES.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    QUESTION_NUMBER: Mapped[int_serv_def_0]
    ID_ANSWER_LAST: Mapped[int_serv_def_0]
    QUIZE_SCORE: Mapped[int_serv_def_0]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class ConstantsORM(Base):
    __tablename__ = "CONSTANTS"
    ID: Mapped[int_pk]
    CONSTANT_NAME: Mapped[str_50] = mapped_column(unique=True)
    CONSTANT_VALUE: Mapped[str_512]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class UserLevelsORM(Base):
    """
    При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!
    """

    __tablename__ = 'USER_LEVELS'
    ID: Mapped[int_pk]
    LEVEL_TEXT: Mapped[str_50] = mapped_column(unique=True)
    MIN_LEVEL_SCORE: Mapped[int]
    MAX_LEVEL_SCORE: Mapped[int]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]


class UserAnswersORM(Base):
    """
    При создании в классе ForeignKey обратить внимание что имена колонок регистрозависимые!
    """

    __tablename__ = 'USER_ANSWERS'
    ID: Mapped[int_pk]
    ID_USER_TG: Mapped[big_int] = mapped_column(
        ForeignKey('USERS.USER_TG_ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    ID_USER_QUIZE: Mapped[int] = mapped_column(
        ForeignKey('USER_QUIZZES.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    ID_ANSWER: Mapped[int] = mapped_column(
        ForeignKey('QUIZE_ANSWERS.ID', ondelete='CASCADE', onupdate='CASCADE')
    )
    QUESTION_NUMBER: Mapped[int_serv_def_0]
    CREATE_TIME: Mapped[date_now]
    UPDATE_TIME: Mapped[date_now]