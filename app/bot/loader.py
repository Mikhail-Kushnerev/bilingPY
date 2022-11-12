import aiohttp
from aiogram import Dispatcher, Bot

from constants import URL


bot = Bot(token="5652289739:AAEIkn3epwvziotTZW27rDQMJkIeXbL1B_o")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def hi(message):
    session = aiohttp.ClientSession()
    async with session.post(f'{URL}' + "sam"):
        ...
    await session.close()
    await message.answer("Q")

