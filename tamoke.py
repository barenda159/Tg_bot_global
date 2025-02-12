




def tamoke(message,bot,types):
    chat.id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton(text="tegvtrfbt")
    button1 = telebot.types.KeyboardButton(text="донат")
    button2 = telebot.types.KeyboardButton(text="👍👍👍👍👍")
    keyboard.add(button_support)
    bot.send_message(chat_id,
    reply_markup = keyboard)
