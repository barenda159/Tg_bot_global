
def inline_kinzhagaleev(message, bot, types):
    reply_markup = types.InlineKeyboardMarkup()
    btn_yes = types.InlineKeyboardButton("Да")
    btn_no = types.InlineKeyboardButton("Нет")
    reply_markup.add(btn_yes, btn_no)

