from aiogram import types

from settings import dp, bot
from data.user import UserService

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет! \nОтправляй мне команду /convert ссылка_на_видео\nи я отправлю его тебе в mp3!")
    id = UserService.get_by_id(message.chat.id)

    if id == False:
        UserService.add(message.from_user.id, message.from_user.username)