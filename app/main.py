import uvicorn
from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot

from api import main_router
from bot import handlers_dp, bot
from constants import WEBHOOK_PATH, WEBHOOK_URL


app = FastAPI()

app.include_router(main_router)


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(
        url=WEBHOOK_URL
    )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(handlers_dp)
    Bot.set_current(bot)
    await handlers_dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    pass


@app.get("/")
async def q_guys():
    return {"details": "q"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
