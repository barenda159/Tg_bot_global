import telebot
import config
from test_klyuew import test_klyuew
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")

@bot.message_handler(commands=["test"])
def klyew(message):
    test_klyuew(message, bot, types)


bot.infinity_polling()