from aiogram import types, Dispatcher
from wol.app import run_app


async def wol(message: types.Message):
    await run_app()
    await message.answer(text='answer')
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(wol, commands=['wol'])
