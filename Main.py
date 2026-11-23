
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import Inlinefunktion
import Function
from States import Kitobtavsiya

dp = Dispatcher()


TOKEN = "9264753995:AAGeKXY5RkbnupIQffxh35haFcwQRJF1_v8"

async def main():


    dp.startup.register(Function.bot_ishlaganda)
    dp.shutdown.register(Function.bot_toxtaganda)

    dp.message.register(Function.start, CommandStart())

    dp.message.register(Function.yosh_sorash,F.text == "Boshlash" )

    dp.callback_query.register(Inlinefunktion.tavsiyapmx,F.data == "J")
    dp.callback_query.register(Inlinefunktion.tavsiya1,F.data == "A")
    dp.callback_query.register(Inlinefunktion.tavsiya2, F.data == "N")
    dp.callback_query.register(Inlinefunktion.tavsiya3, F.data == "R")
    dp.callback_query.register(Inlinefunktion.tavsiya4, F.data =="R2")
    dp.message.register(Function.yosh, Kitobtavsiya.yosh)
    dp.callback_query.register(Inlinefunktion.timered, F.data == "1")
    dp.callback_query.register(Inlinefunktion.timered1,F.data=="2")
    dp.callback_query.register(Inlinefunktion.timered2,F.data =="3")
    dp.callback_query.register(Inlinefunktion.maqsad,F.data=="q")
    dp.callback_query.register(Inlinefunktion.maqsad1,F.data == "w")
    dp.callback_query.register(Inlinefunktion.maqsad2,F.data =="e")
    dp.message.register(Function.kitob_fav, Kitobtavsiya.janr)
    dp.message.register(Function.savol, Kitobtavsiya.vaqt)
    dp.message.register(Function.final, Kitobtavsiya.maqsad)

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

asyncio.run(main())