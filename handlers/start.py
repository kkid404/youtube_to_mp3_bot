from aiogram import types

from settings import dp, bot
from data.user import UserService

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет! Я бот, который реагирует на команду /start.")
    id = UserService.get_by_id(message.chat.id)

    if id == False:
        UserService.add(message.from_user.id, message.from_user.username)