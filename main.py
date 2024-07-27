from os import getenv
from dotenv import load_dotenv
import redis



load_dotenv()
r = redis.Redis(
    host=getenv('REDIS_HOST'),
    port=getenv('REDIS_PORT'),
    db=0, username=getenv('REDIS_USER'),
    password=getenv('REDIS_USER_PASSWORD')
)


try:
    info = r.info()
    print(info['redis_version'])
    response = r.ping()

    if response:

        print("Подключение успешно!")
        r.close()

    else:
        print("Не удалось подключиться к Redis.")
        r.close()

    r.set('user', 'plakdi')
    print(r.ping())
    print(type(r.get('user')))
except redis.exceptions.RedisError as e:
    print(f"Ошибка: {e}")
    r.close()
