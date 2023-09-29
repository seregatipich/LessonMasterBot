from os import getenv
from asyncio import run

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import registration


async def start():
    load_dotenv()
    bot = Bot(token=getenv('TELEGRAM_TOKEN'))
    dp = Dispatcher()

    dp.include_router(registration.reg_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(start())
