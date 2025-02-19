from otbetka import text

def text(text, bot, message):
    if text == "привет" or text == "Привет" or text == "прив" or text == "Пgрив":
        bot.send_message(message.From_user.id, "Привет кожаный")
    if text == "Пока" or text == "пока" or text == "досвидания" or text == "Досвидания":
        bot.send_message(message.From_user.id, "бот выключен, привет реальность")
    if text == "мне грустно" or text == "Мне гнрустно":
        bot.send_message(message.From_user.id, "https://youtu.be/dQw4w9WgXcQ?si=ZgtbGoKQ2NRZWa9a")


