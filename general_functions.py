import os
import urllib.parse
import requests
from dotenv import load_dotenv


def get_image_extension(url):
    return os.path.splitext(urllib.parse.unquote(url))[1]


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    with open(path, 'wb') as file:
        file.write(response.content)


def get_env_variables():
    load_dotenv()
    return {
        'nasa_api_key': os.getenv('NASA_API_KEY'),
        'tg_bot_token': os.getenv('TELEGRAM_BOT_TOKEN'),
        'tg_chat_id': os.getenv('TG_CHAT_ID'),
        'break_of_posting': int(os.getenv('BREAK_OF_POSTING'))
        }
