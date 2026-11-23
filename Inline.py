from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tavsiyapromax = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(callback_data="J",text="Roman"),
        ],
        [
            InlineKeyboardButton(callback_data="A", text="Ilmiy")
        ],
        [
            InlineKeyboardButton(callback_data="N", text="Motivatsiya")
        ],
        [
            InlineKeyboardButton(callback_data="R", text="Diniy")
        ],
        [
            InlineKeyboardButton(callback_data="R2", text="IT/texnik")
        ]
    ]
)

timeread = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(callback_data="1",text="10-30 min"),
        ],
        [
            InlineKeyboardButton(callback_data="2", text="30-60 min")
        ],
        [
            InlineKeyboardButton(callback_data="3", text="1 soat +")
        ]
    ]
)

mmaqsad = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(callback_data="q",text="Bilimni oshirish")
        ],
        [
            InlineKeyboardButton(callback_data="w", text="Dam olish")
        ],
        [
            InlineKeyboardButton(callback_data="e", text="Ish uchun organish")
        ]
    ]
)