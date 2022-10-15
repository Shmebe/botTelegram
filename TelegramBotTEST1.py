import telebot
from telebot import types

bot = telebot.TeleBot('5765388677:AAF0qS9u9Rz8MpepM4wKKiiSxUYrChAkEIo')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'HI, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("text on button", url="https://www.python.org/downloads/release/python-3108/"))
    bot.send_message(message.chat.id, "website", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_info(message):
    if message.text == "id":
        bot.send_message(message.chat.id, f"your id - {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('photo.bmp', 'rb')
        bot.send_photo(message.chat.id, photo)


#@bot.message_handler(content_types=[])
#bot.polling(none_stop=True)
