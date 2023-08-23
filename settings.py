import logging
from os import path, getenv
from dotenv import load_dotenv

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения из файла .env
load_dotenv()
API_TOKEN = getenv('API_TOKEN')
WEBHOOK_URL  = getenv('WEBHOOK_URL ')
HOST = getenv("DB_HOST")
USERNAME = getenv("DB_USERNAME")
PASSWORD = getenv("DB_PASSWORD")
DATABASE = getenv("DB_DATABASE")
PORT = getenv("DB_PORT")
ADMIN = getenv("ADMIN")

if "," in ADMIN:
    ADMIN = ADMIN.split(",")
else:
    if len(ADMIN) >= 1:
        ADMIN = [ADMIN]
    else:
        logger.warning("Admin ID is not specified")

# Инициализируйте бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

