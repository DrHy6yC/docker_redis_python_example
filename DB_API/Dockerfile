FROM python:3.10.14-alpine3.19
LABEL db_api="0.0.1-beta"

ENV DB_IS_CREATED=True
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_USER=user
ENV DB_PASS=pass
ENV DB_NAME=Bot
ENV DB_SQLite=Bot
ENV DB_DBMS=PGSQL
ENV DB_ECHO=True

WORKDIR /db_api/app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /db_api/app

CMD ["uvicorn", "app_db_api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]