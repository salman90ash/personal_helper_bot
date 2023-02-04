from aiogram import types, Dispatcher
import wol.app as wol


async def wake_up(message: types.Message):
    await wol.run_app()
    await message.answer(text='answer')
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(wake_up, commands=['wol'])
