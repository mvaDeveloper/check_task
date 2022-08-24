from aiogram import executor

from create_bot import dp
from SendInformationTask import send_information_task
from data_base import db
import time


async def on_startup(_):
    db.sql_start()
    while True:
        tasks = await db.select_tasks('в работе')
        for task in tasks:
            tg_login = await db.select_user(task[2])
            await send_information_task(tg_login[0][0], task)
            await db.update_task(task[0], 'назначена')


async def on_shutdown(_):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
