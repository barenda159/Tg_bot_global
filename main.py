import telebot
import config
from help import help
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")
@bot.message_handler(commands=['help'])
def command_help(message):
    help(message)
bot.infinity_polling()