import os

from aiogram import Bot, Dispatcher, executor, types, Router
from aiogram import F
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher()
router = Router()


@router.message(Command('start'))
async def welcome(message: types.Message) -> None:
    message.reply('sjdiajsif')


if __name__ == '__main__':
    executor.start_polling(dp)