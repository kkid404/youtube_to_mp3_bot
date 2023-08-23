from aiogram import types
from aiogram.dispatcher.filters import IDFilter, Text

from settings import dp, bot, ADMIN
from keyboards import AdminKeyboard
from data.user import UserService


@dp.message_handler(IDFilter(chat_id=ADMIN))
async def get_all_users(message: types.Message, db = UserService, kb = AdminKeyboard()):
    await bot.send_message(
        message.from_user.id,
        f"{len(db.get_all()['chat_id'])} юзеров в базе.",
        reply_markup=kb.start_kb()
    )