from aiogram.fsm.state import StatesGroup,State


class Kitobtavsiya(StatesGroup):
    yosh = State()
    janr = State()
    vaqt = State()
    maqsad = State()