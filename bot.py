import re
import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN", parse_mode=None)

user = bot.get_me()





@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Thanks for using me! I'm Navid's test bot, a bot designed by Navid, to test if he can make a telegram bot" \
"\nYou can tell me your name and I welcome you, or..." \
"\nYeah, that's all I do for now" \
"\nAnyway, see you later!" \
"\n(P.S: If I'm not responding, Navid has turned me off)")

@bot.message_handler(commands=['soosmaz'])
def send_song_w_command(message):
    m = message.text.split(" ")
    print(type(m), "\"", m, "\"")
    if len(m) > 1:
        if m[1] == '1':
            bot.send_message(message.chat.id, m[1])
            bot.forward_message(message.chat.id, -1001308027908, 4)
        elif m[1] == '2':
            bot.send_message(message.chat.id, m[1])
            bot.forward_message(message.chat.id, -1001308027908, 7)
        elif m[1] == '3':
            bot.send_message(message.chat.id, m[1])
            bot.forward_message(message.chat.id, -1001308027908, 9)
        elif m[1] == '4':
            bot.send_message(message.chat.id, m[1])
            bot.forward_message(message.chat.id, -1001308027908, 11)
        elif m[1] == '5':
            bot.send_message(message.chat.id, m[1])
            bot.forward_message(message.chat.id, -1001308027908, 14)
        elif m[1] == '6':
            bot.send_message(message.chat.id, m[1])
            bot.forward_message(message.chat.id, -1001308027908, 16)
        else:
            print("Error")
    else:
        pass

try:
    bot.polling(none_stop=True)
except:
    pass

