from os import path, getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher


# Загрузка переменных окружения из файла .env
load_dotenv()
API_TOKEN = getenv('API_TOKEN')
WEBHOOK_URL  = getenv('WEBHOOK_URL ')


# Инициализируйте бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)