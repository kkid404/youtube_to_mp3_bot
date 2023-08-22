from aiogram import types

from settings import dp, bot

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет! Я бот, который реагирует на команду /start.")