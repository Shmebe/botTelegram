import telebot

bot = telebot.TeleBot('5765388677:AAF0qS9u9Rz8MpepM4wKKiiSxUYrChAkEIo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, i love pizza")

bot.polling(none_stop=True)