from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def welcome_kb() -> ReplyKeyboardMarkup:
    buttons = [[KeyboardButton(text='Start')]]
    kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return kb
