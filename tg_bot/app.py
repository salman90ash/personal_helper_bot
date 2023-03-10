from aiogram import executor
from config_bot import dp
from handlers import client, common
import datetime

# import asyncio
# import aioschedule as schedule


client.register_handlers_client(dp)
common.register_handlers_common(dp)


async def time():
    print(datetime.datetime.now())


# async def scheduler():
#     schedule.every().day.at("08:00").do(updates, '')
#     schedule.every().day.at("10:00").do(updates, '')
#     schedule.every().day.at("12:00").do(updates, '')
#     schedule.every().day.at("14:00").do(updates, '')
#     schedule.every().day.at("16:00").do(updates, '')
#     schedule.every().day.at("18:00").do(updates, '')
#     schedule.every().day.at("20:00").do(updates, '')
#     while True:
#         await schedule.run_pending()
#         await asyncio.sleep(1)


async def on_startup(_):
    print('bot activated')
    print(datetime.datetime.now())
    # asyncio.create_task(scheduler())


if __name__ == "__main__":
    # from rzn.tg.handlers.common import dp
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
