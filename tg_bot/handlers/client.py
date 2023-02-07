import sys

sys.path.append("..")

from aiogram import types, Dispatcher
from wol.app import run_app
from tg_bot.settings import ADMIN_ID


async def wake_up(message: types.Message):
    run_app()
    await message.answer(text="Salman's computer is on!")
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(wake_up, commands=['wol'])
