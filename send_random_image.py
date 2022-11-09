import os
import requests
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
secret_token = os.getenv('TOKEN')
bot = Bot(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 672534822

# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')

# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url)