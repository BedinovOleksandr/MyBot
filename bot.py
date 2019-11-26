import telebot
import DBfunctions

bot = telebot.TeleBot('YOUR_TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    DBfunctions.insert_user(list(vars(message.from_user).values()))
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
bot.polling()
