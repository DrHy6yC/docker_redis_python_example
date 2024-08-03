from icecream import ic
from db.db_worker import filling_min_db, async_insert_data_list_to_bd
from db.ORM import async_get_const
from db.models import *

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/clear_db")
async def clear_db():
    await filling_min_db()
    ic('База пересоздана')
    return {"База пересоздана": "ОК!"}


@app.get("/constants/{constant_name}")
async def read_item(constant_name: str):
    constant = await async_get_const(constant_name)
    return {
        "id": constant.ID,
        "name": constant.CONSTANT_NAME,
        "value": constant.CONSTANT_VALUE,
        "create_time": constant.CREATE_TIME
    }


@app.post("/constants/")
async def post_item(constant_name: str, constant_value: str):
    ic(constant_name, constant_value)
    constant = ConstantsORM(
        CONSTANT_NAME=constant_name,
        CONSTANT_VALUE=constant_value
    )
    await async_insert_data_list_to_bd([constant])
    constant = await async_get_const(constant_name)
    return {
        "id": constant.ID,
        "name": constant.CONSTANT_NAME,
        "value": constant.CONSTANT_VALUE,
        "create_time": constant.CREATE_TIME
    }
