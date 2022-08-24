from create_bot import bot


async def send_information_task(tg_login, task):
    await bot.send_message(tg_login, f"Вам назначена задача!\n"
                                     f"Номер задачи: {task[1]}\n"
                                     f"Заголовок: {task[5]}\n"
                                     f"Приоритет: {task[6]}\n")
