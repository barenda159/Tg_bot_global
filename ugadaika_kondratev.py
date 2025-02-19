num = False
game = False

def ugadaika_kondratev(message, bot):
    global num, game
    if message.text == "Угадайка":
        game = True
        num = random.randint(1, 5)
        reply_markup = types.ReplyKeyboardMarkup()
        btn_1 = types.KeyboardButton("1")
        btn_2 = types.KeyboardButton("2")
        btn_3 = types.KeyboardButton("3")
        btn_4 = types.KeyboardButton("4")
        btn_5 = types.KeyboardButton("5")
        reply_markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
        bot.send_message(message.chat.id, "Я загадал число угадай число", reply_markup=reply_markup)
    elif str(num) == message.text and game:
        game = False
        bot.send_message(message.chat.id, "Ты угадал!")
    elif str(num) != message.text and message.text in ["1", "2", "3", "4", "5"] and game:
        game = False
        bot.send_message(message.chat.id, "Ты не угадал!")
