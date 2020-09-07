import telebot
from telebot import types
from random import choice

bot = telebot.TeleBot("1245162998:AAHYtCvVRrszidXcERn-4o8tySA55CSUm_I", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "!g or -g: Googles stuff for you i.e: !g Telegram Bot" \
                "\n!y or -y: Searches Youtube for you i.e: !y My name is Jeff" \
                "\n!say or -say: Says something i.e: !say Hello there!" \
                "\n/soosmaz: Sends Soosmaz for you i.e: /soosmaz 2")

@bot.message_handler(func=lambda m: True if m.text != None and m.text.split(":")[0] == "!سنگ کاغذ قیچی" else False)
def RPS(message):
    try:
        m = message.text.split(":")
        botMove = choice(["سنگ", "کاغذ", "قیچی"])
        if m[1] == "سنگ":
            if botMove == "سنگ":
                bot.send_message(message.chat.id, "من سنگ رو انتخاب کردم. مساوی شدیم")
            elif botMove == "کاغذ":
                bot.send_message(message.chat.id, "من کاغذ رو انتخاب کردم. من بردم!")
            elif botMove == "قیچی":
                bot.send_message(message.chat.id, "من قیچی رو انتخاب کردم. تو بردی!")
        elif m[1] == "کاغذ":
            if botMove == "سنگ":
                bot.send_message(message.chat.id, "من سنگ رو انتخاب کردم. تو بردی!")
            elif botMove == "کاغذ":
                bot.send_message(message.chat.id, "من کاغذ رو انتخاب کردم. مساوی شدیم")
            elif botMove == "قیچی":
                bot.send_message(message.chat.id, "من قیچی رو انتخاب کردم. من بردم!")
        elif m[1] == "قیچی":
            if botMove == "سنگ":
                bot.send_message(message.chat.id, "من سنگ رو انتخاب کردم. من بردم!")
            elif botMove == "کاغذ":
                bot.send_message(message.chat.id, "من کاغذ رو انتخاب کردم. تو بردی!")
            elif botMove == "قیچی":
                bot.send_message(message.chat.id, "من قیچی رو انتخاب کردم. مساوی شدیم")
        else:
            bot.send_message(message.chat.id, "از بین سنگ و کاغذ و قیچی یکی رو انتخاب کن")
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and (m.text.split(" ")[0] == "!g" or m.text.split(" ")[0] == "-g") else False)
def google(message):
    try:
        search = message.text[3:].replace(" ", "+")
        bot.reply_to(message, f"http://www.google.com/search?q={search}")
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and (m.text.split(" ")[0] == "!y" or m.text.split(" ")[0] == "-y") else False)
def youtube(message):
    try:
        search = message.text[3:].replace(" ", "+")
        bot.reply_to(message, f"https://www.youtube.com/results?search_query={search}")
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and (m.text.split(" ")[0] == "!say" or m.text.split(" ")[0] == "-say") else False)
def say(message):
    try:
        m = message.text[4:]
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, m)
    except:
        pass

@bot.message_handler(commands=['soosmaz'])
def send_season_one(message):
    try:
        m = message.text.split(" ")
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
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and "ب3" in m.text else False)
def BalBalBal(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,"بل بل بل")

@bot.message_handler(func=lambda m: True if m.text != None and (m.text == "ضیغمی 1") else False)
def zeyghami_khosgel(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,"خوشگل!")

@bot.message_handler(func=lambda m: True if m.text != None and (m.text == "ضیغمی 2") else False)
def zeyghami_pnb(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,"پس نمه بابا!")

try:
    bot.polling(none_stop=True)
except:
    pass

