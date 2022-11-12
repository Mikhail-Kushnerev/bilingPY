import uvicorn
from aiogram.utils.executor import start_webhook
from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot

from api import main_router
from bot import dp, bot
from core import settings


app = FastAPI()

app.include_router(main_router)

WEBHOOK_PATH = f"/bot/{settings.token}"
WEBHOOK_URL = "https://362a-178-66-157-187.eu.ngrok.io" + WEBHOOK_PATH


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(
        url=WEBHOOK_URL
    )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    pass


@app.post("/{name}")
async def say_name(name: str):
    print(name)
    return name


@app.get("/")
async def q_guys():
    return {"details": "q"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )