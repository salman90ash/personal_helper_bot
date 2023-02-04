from aiogram import types, Dispatcher
from tg_bot.bot import bot
from tg_bot.settings import ADMIN_ID


async def inbox(message: types.Message):
    # print(message)
    text = message.text
    send_msg = await bot.send_message(chat_id=message.from_user.id, text=text, parse_mode='HTML')
    # print(message)
    # await message.delete()
    # await main()


# async def send_msg():
#     msg = await bot.send_message(chat_id=ADMIN_ID, text='text', parse_mode='HTML')
#     print(msg)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(inbox)
