from telegram import Bot
import requests

bot = Bot(token='5350323727:AAH7JCrAGwAtwSiM983TJ6FxS3k1trcIDHU')
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 672534822

# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')

# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url)