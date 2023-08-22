import os

from aiogram import types

from settings import dp, bot
from models import Yt, Converter

@dp.message_handler(commands=['convert'])
async def convert_video_to_audio(message: types.Message):
    # Получаем ссылку на видео из аргументов команды
    args = message.get_args().split()
    if len(args) == 0:
        await message.reply("Пожалуйста, укажите ссылку на видео после команды /convert.")
        return

    video_url = args[0]
    yt = Yt()
    convert = Converter()

    video = yt.download(video_url)
    audio = convert.mp4_to_mp3(video)
    with open(audio, "rb") as audio_file:
        await bot.send_audio(message.chat.id, audio_file)

    os.remove(audio)