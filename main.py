import telebot
import config
from inline_kinzhagaleev import inline_kinzhagaleev

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")
@bot.message_handler(commands=['inline'])

def inline(message):
    inline_kinzhagaleev(message, bot, types)


bot.infinity_polling()


