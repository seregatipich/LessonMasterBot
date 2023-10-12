from asyncio import run
from logging import INFO, basicConfig
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from dotenv import load_dotenv

from handlers import registration, common


async def start():
    basicConfig(
        level=INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    load_dotenv()
    bot = Bot(token=getenv('TELEGRAM_TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(registration.reg_router, common.common_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(start())
