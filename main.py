import telebot
import config
from ugadaika_kondratev import ugadaika_kondratev


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")

@bot.message_handler(commands=["ugadaika"])
def ugadaika(message):
    ugadaika_kondratev(message, bot)



bot.infinity_polling()