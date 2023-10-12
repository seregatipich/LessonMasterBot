from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def welcome_kb() -> ReplyKeyboardMarkup:
    """Creates Reply Keyboard with one button"""
    buttons = [[KeyboardButton(text='Register!')]]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return keyboard


def main_menu_kb() -> ReplyKeyboardMarkup:
    buttons = [[KeyboardButton(text='add later')]]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
