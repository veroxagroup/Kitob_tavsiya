
from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from Inline import tavsiyapromax, timeread, mmaqsad
from Outline import tavsiya
from States import Kitobtavsiya


async def bot_ishlaganda(bot: Bot):
    await bot.send_message(chat_id=8819927088,text="Bot ishga tushdi...")


async def bot_toxtaganda(bot: Bot):
    await bot.send_message(chat_id=8819927088,text="Bot ishdan to'xtadi..." )


async def start(message: Message, state: FSMContext):
    await state.clear()

    await message.answer("Salom! Kitob tavsiya botiga xush kelibsiz!\n""Sizga mos kitobni topish uchun bir nechta savol beraman.",reply_markup=tavsiya)


async def yosh_sorash(message: Message, state: FSMContext):
    await message.answer("Yoshingiz nechida?")
    await state.set_state(Kitobtavsiya.yosh)


async def yosh(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(yosh=int(message.text))

        await message.answer("Qaysi turdagi kitob yoqadi?\nVariantlarni tanlang:",reply_markup=tavsiyapromax)
        await state.set_state(Kitobtavsiya.janr)

    else:
        await message.answer("Yoshingizni to'g'ri son bilan kiriting!")


async def kitob_fav(message: Message, state: FSMContext):
    await state.update_data(janr=message.text)

    await message.answer("Kuniga qancha vaqt kitob o'qiysiz?\nVariantlarni tanlang:",reply_markup=timeread)
    await state.set_state(Kitobtavsiya.vaqt)


async def savol(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)

    await message.answer("Kitob o'qishdan maqsadingiz nima?\nVariantlarni tanlang:",reply_markup=mmaqsad)
    await state.set_state(Kitobtavsiya.maqsad)


async def final(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)


    await message.answer(

        "Sizga tavsiyam: Atomic Habits\n"
        "Sabab: Bu kitob foydali odatlarni shakllantirishga "
        "va o'z ustingizda ishlashga yordam beradi.\n"
        "Kuniga 30 daqiqa o'qishdan boshlashingiz mumkin.")

    await state.clear()
