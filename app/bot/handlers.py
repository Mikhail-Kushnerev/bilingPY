from aiogram import types

from bot import dp, send_msg
from constants import URL, TOKEN


@dp.message_handler(commands="start")
async def registration(message: types.Message):
    data = {
        "id": 1,
        "telegram_id": message.from_id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
    }
    url = f'{URL}/sign-up'
    response = await send_msg(url, data, "POST")
    if response.status == 422:
        await message.answer("Вы уже были зарегистрированы!")
    else:
        await message.answer("Вы успешно были зарегистрированы!")
