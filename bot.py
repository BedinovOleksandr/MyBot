from time import sleep

import telebot
import DBfunctions

bot = telebot.TeleBot('YOUR TOKEN')



@bot.message_handler(commands=['start'])
def start_message(message):
    DBfunctions.insert_user(list(vars(message.from_user).values()))
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        sleep(15)