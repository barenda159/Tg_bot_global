import telebot
import config
from ugadaika_kondratev import ugadaika_kondratev


from test_klyuew import test_klyuew
from telebot import types

from wiki_Sukhanov import wiki_Sukhanov, get_wiki_Sukhanov


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")


@bot.message_handler(commands=["ugadaika"])
def ugadaika(message):
    ugadaika_kondratev(message, bot)



@bot.message_handler(commands=["test"])
def klyew(message):
    test_klyuew(message, bot, types)


@bot.message_handler(commands=['wiki'])
def wiki(message):
    wiki_Sukhanov(message, bot)
    get_wiki_Sukhanov(message)



bot.infinity_polling()