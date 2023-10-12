from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.welcome import welcome_kb, main_menu_kb

common_router = Router()


@common_router.message(Command('start'))
async def welcome(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.reply("Hi!\nI'm LessonMasterBot and I'm here to help you plan your classes.")
    await message.reply('Do you want to register?', reply_markup=welcome_kb())


@common_router.message(Command('cancel'))
async def cancel_action(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.reply(text='Action canceled', reply_markup=main_menu_kb())