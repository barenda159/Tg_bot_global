import telebot
from telebot.util import content_type_media

import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")

@bot.message_handler(content_types=['text'])
def feedback(message):
    bot.reply_to(message, "К вашим услугам")


bot.infinity_polling()