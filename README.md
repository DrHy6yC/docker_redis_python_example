Пробую обернуть бота в контейнер и запускать вместе с контейнерами бд

Настройки .env:

#Настройки Redis
REDIS_HOST=localhost
REDIS_PORT=6380
REDIS_PASSWORD=passwd
REDIS_USER=user_redis
REDIS_USER_PASSWORD=user_passwd

#Настройки Postgres
PG_HOST=localhost
PG_PORT=5432
PG_USER=user_pg
PG_PASSWORD=passwd
PG_DB=Bot
PG_DATA=/var/lib/postgresql/data/pgdata

#Настройки PGadmin
PGADMIN_DEFAULT_EMAIL=example@m.ru
PGADMIN_DEFAULT_PASSWORD=passwd
PGADMIN_CONFIG_SERVER_MODE=False

#Настройки MySQL
MYSQL_ROOT_PASSWORD=passwd
MYSQL_DATABASE=Bot
MYSQL_USER=user_mysql
MYSQL_PASSWORD=passwd