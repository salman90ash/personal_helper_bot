from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tg_bot.settings import ADMIN_ID
from tg_bot.bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from wol.app import run_app
import json
import aiohttp


async def wol(message: types.Message):
    await run_app()
    await message.answer(text='answer')
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(wol, commands=['wol'])
