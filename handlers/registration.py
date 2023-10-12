from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

reg_router = Router()


class RegisterUser(StatesGroup):
    name = State()
    students_amount = State()


@reg_router.message(F.text == 'Register!')
async def ask_name(message: types.Message) -> None:
    await message.reply("What's your name?", reply_markup=ReplyKeyboardRemove())



