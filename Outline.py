from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

tavsiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Boshlash")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)