import telebot
import config
from wiki_Sukhanov import wiki_Sukhanov, get_wiki_Sukhanov

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую вас!")
    bot.send_message(message.chat.id, "Чего желаете?")

def wiki_Sukhanov(message, bot):
    global wiki
    if wiki:
        bot.send_message(message.chat.id, get_wiki_Sukhanov(message.text))
        wiki = False
    if message.text == "Википедия":
        bot.send_message(message.chat.id, "Напиши, что ты хочешь найти?")
        wiki = True

wikipedia.set_lang("ru")
def get_wiki_Sukhanov(word):
    try:
        w = wikipedia.page(word)  # Ищем статью
        wikitext = w.content[:400]
        wikimas = wikitext.split(".")  # разделяем предложение
        wikimas = wikimas[:-1]  # удаляем последний элемент из списка
        wikiresult = ""
        for i in wikimas:
            if not ("==" in i):
                wikiresult = wikiresult + i + "."
            else:
                break
        wikiresult = re.sub('\([^()]*\)', "----", wikiresult)
        wikiresult = re.sub('\{[^\{\}]*\}', "----", wikiresult)
        return wikiresult
    except Exception as e:
        return "Такой статьи нет"

bot.infinity_polling()