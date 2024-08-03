from icecream import ic

from fastapi import FastAPI

from db_worker import filling_min_db

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/clear_db")
async def clear_db():
    await filling_min_db()
    ic('База пересоздана')
    return {"База пересоздана": "ОК!"}
