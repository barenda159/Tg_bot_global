import telebot
from telebot.util import content_type_media

import config
from inline_kinzhagaleev import inline_kinzhagaleev

from help import help


from test_klyuew import test_klyuew
from telebot import types

from wiki_Sukhanov import wiki_Sukhanov, get_wiki_Sukhanov



bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")
@bot.message_handler(commands=['inline'])

def inline(message):
    inline_kinzhagaleev(message, bot, types)







@bot.message_handler(commands=['help'])
def command_help(message):
    help(message)



@bot.message_handler(content_types=['text'])
def feedback(message):
    bot.reply_to(message, "К вашим услугам")


@bot.message_handler(commands=["test"])
def klyew(message):
    test_klyuew(message, bot, types)


@bot.message_handler(commands=['wiki'])
def wiki(message):
    wiki_Sukhanov(message, bot)
    get_wiki_Sukhanov(message)




bot.infinity_polling()

