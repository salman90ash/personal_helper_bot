from tg_bot.settings import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

my_bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(my_bot, storage=storage)
