def help(message):
    bot.send_message(message.chat.id, "Команды боты:\n"
                                      "/edit_message - Команда редактирования сообщения.\n"
                                      "/edit_link - Команда редактирования ссылки.\n"
                                      "/show_message - Показать сообщение.\n"
                                      "/send_message - Начать рассылку.\n"
                                      "/help - Помощь")
