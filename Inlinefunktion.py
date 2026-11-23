from aiogram.types import CallbackQuery

async def tavsiyapmx(callback:CallbackQuery):
    await callback.message.answer("Roman")

async def tavsiya1(callback: CallbackQuery):
    await callback.message.answer("Ilmiy")

async def tavsiya2(callback: CallbackQuery):
    await callback.message.answer("Motivatsiya")

async def tavsiya3(callback:CallbackQuery):
    await callback.message.answer("Diniy")

async def tavsiya4(callback:CallbackQuery):
    await callback.message.answer("IT/texnik")


async def timered(callback:CallbackQuery):
    await  callback.message.answer("10-30 min")

async def timered1(callback:CallbackQuery):
    await  callback.message.answer("30-60 min")

async def timered2(callback:CallbackQuery):
    await  callback.message.answer("1 sot +")


async def maqsad(callback:CallbackQuery):
    await callback.message.answer("Bilimni oshirish")

async def maqsad1(callback:CallbackQuery):
    await callback.message.answer("Dam olish")

async def maqsad2(callback:CallbackQuery):
    await callback.message.answer("Ish uchun organish")


