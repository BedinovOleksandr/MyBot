from time import sleep

import telebot
import DBfunctions

bot = telebot.TeleBot('915271863:AAHpmWLQOEsHPbz226tceUMGetyfBQoCNCs')



@bot.message_handler(commands=['start'])
def start_message(message):
    DBfunctions.insert_user(list(vars(message.from_user).values()))
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.infinity_polling(True)
'''try:
    bot.polling()
except OSError as e:
    print(e)
    bot.stop_polling()
    sleep(5)
    bot.polling()'''