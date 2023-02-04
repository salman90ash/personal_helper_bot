import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
ADMIN_ID = int(os.environ.get('TELEGRAM_ADMIN_ID'))
