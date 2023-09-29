from aiogram import F, Router, types
from aiogram.filters import Command

from keyboards.start_registration import welcome_kb

reg_router = Router()


@reg_router.message(Command('start'))
async def welcome(message: types.Message) -> None:
    await message.reply('Hi! how is it going?')


@reg_router.message()
async def registration(message: types.Message) -> None:
    await message.reply('Hi!', reply_markup=welcome_kb())
