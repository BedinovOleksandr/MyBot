from time import sleep
import telebot
import DBfunctions
import logging

logging.basicConfig(filename='messegesLog.log', filemode='w', level='INFO')


bot = telebot.TeleBot('YOUR_TOKEN')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Стикер', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    logging.info(message.text)
    DBfunctions.insert_user(list(vars(message.from_user).values()))
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def bot_send_text(message):
    logging.info(message.text)
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока мой создатель')
    elif message.text.lower() == 'стикер':
        bot.send_sticker(message.chat.id, 'CAADAgADfgAD9wLID-usD1lCSOuqFgQ')
    else:
        bot.send_message(message.chat.id, 'Я понимаю только кнопки')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        sleep(15)