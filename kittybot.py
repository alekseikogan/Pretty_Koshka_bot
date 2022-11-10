import os
import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from dotenv import load_dotenv

load_dotenv()
secret_token = os.getenv('TOKEN')
updater = Updater(token=secret_token)
URL = ''


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(
        chat.id,
        get_new_image()
    )


def say_hello(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Ты пишешь мне, но я еще слишком тупенький для умного ответа...'
    )


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup(
        [['/newcat']],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}! Посмотри, какого котика я тебе нашёл!',
        reply_markup=button
    )
    context.bot.send_photo(
        chat.id,
        get_new_image()
    )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hello))
updater.start_polling()
updater.idle()
