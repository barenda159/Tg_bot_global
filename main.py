import telebot
import config
from tamoke import tamoke , get_tamoke
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")

def tamoke(message,types):
    get_tamoke()
bot.infinity_polling()