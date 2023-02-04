from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

EXECUTABLE_PATH = os.environ.get('EXECUTABLE_PATH')
PROXY_OPTIONS = os.environ.get('PROXY_OPTIONS')
LOGIN = os.environ.get('LOGIN_ROUTER')
PASSWORD = os.environ.get('PASSWORD_ROUTER')
URL = os.environ.get('URL_ROUTER')
