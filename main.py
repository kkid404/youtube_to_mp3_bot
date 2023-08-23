import logging

from aiogram.utils import executor

from settings import bot, dp, WEBHOOK_URL
import handlers
from data import Base, engine


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    await bot.set_webhook(WEBHOOK_URL)
    
    logger.info("Bot has been started and webhook is set up.")
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)