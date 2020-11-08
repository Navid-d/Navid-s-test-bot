import telebot
from telebot import types
from random import choice

def rps(player1, player2):
    if player1 == "rock 🗻":
        if player2 == "rock 🗻":
            return "tie"
        elif player2 == "paper 📄":
            return "player2"
        elif player2 == "scissor ✂️":
            return "player1"

    elif player1 == "paper 📄":
        if player2 == "rock 🗻":
            return "player1"
        elif player2 == "paper 📄":
            return "tie"
        elif player2 == "scissor ✂️":
            return "player2"

    elif player1 == "scissor ✂️":
        if player2 == "rock 🗻":
            return "player2"
        elif player2 == "paper 📄":
            return "player1"
        elif player2 == "scissor ✂️":
            return "tie"
    else:
        return "error"

bot = telebot.TeleBot("1245162998:AAHYtCvVRrszidXcERn-4o8tySA55CSUm_I", parse_mode=None)

letter = {
    "ا": "h",
    "ب": "f",
    "پ": "\\",
    "ت": "j",
    "ث": "e",
    "ج": "[",
    "چ": "]",
    "ح": "p",
    "خ": "o",
    "د": "n",
    "ذ": "b",
    "ر": "v",
    "ز": "c",
    "ژ": "C",
    "س": "s",
    "ش": "a",
    "ص": "w",
    "ض": "q",
    "ط": "x",
    "ظ": "z",
    "ع": "u",
    "غ": "y",
    "ف": "t",
    "ق": "r",
    "ک": ";",
    "گ": "'",
    "ل": "g",
    "م": "l",
    "ن": "k",
    "و": ",",
    "ه": "i",
    "ی": "d",
    "h": "ا",
    "f": "ب",
    "\\": "پ",
    "j": "ت",
    "e": "ث",
    "[": "ج",
    "]": "چ",
    "p": "ح",
    "o": "خ",
    "n": "د",
    "b": "ذ",
    "v": "ر",
    "c": "ز",
    "C": "ژ",
    "s": "س",
    "a": "ش",
    "w": "ص",
    "q": "ض",
    "x": "ط",
    "z": "ظ",
    "u": "ع",
    "y": "غ",
    "t": "ف",
    "r": "ق",
    ";": "ک",
    "'": "گ",
    "g": "ل",
    "l": "م",
    "k": "ن",
    ",": "و",
    "i": "ه",
    "d": "ی",
    "H": "آ",
    "?": "؟",
    "؟": "?",
}


def shift(code):
    finale = []
    for i in code:
        if i in letter:
            finale.append(letter[i])
        else:
            finale.append(i)
    return "".join(finale)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "!g or -g: Googles stuff for you i.e: !g Telegram Bot" \
                "\n!y or -y: Searches Youtube for you i.e: !y My name is Jeff" \
                "\n!say or -say: Says something i.e: !say Hello there!" \
                "\n/soosmaz: Sends Soosmaz for you i.e: /soosmaz 2")

@bot.message_handler(func=lambda m: True if m.text != None and m.text.split(":")[0] == "!سنگ کاغذ قیچی" else False)
def RPS(message):
    try:
        m = message.text.split(":")[1]
        botMove = choice(["سنگ", "کاغذ", "قیچی"])

        matchRes = rps(m, botMove)

        if matchRes == "tie":
            bot.send_message(message.chat.id, f"من {botMove} رو انتخاب کردم. مساوی شدیم")
        elif matchRes == "bot":
            bot.send_message(message.chat.id, f"من {botMove} رو انتخاب کردم. من بردم!")
        elif matchRes == "mem":
            bot.send_message(message.chat.id, f"من {botMove} رو انتخاب کردم. تو بردی!")
        else:
            bot.send_message(message.chat.id, "از بین سنگ و کاغذ و قیچی یکی رو انتخاب کن")
    except:
        pass

players = []
player_moves = [None, None]
@bot.message_handler(func=lambda m: True if m.text != None and m.text.split(":")[0].lower() == "!rps" else False)
def RPS_multi(message):
    try:
        global players
        global player_moves

        # Declaring Second Player
        player2 = message.text.split(":")[1]

        # If input is a username
        if player2[0] == "@" and message.chat.type == "group":
            if "@" + message.from_user.username.lower() == player2.lower():
                bot.send_message(message.chat.id, "Error: Two players are the same")
                return 0
            else:
                players = []
                player_moves = [None, None]
                players.append(message.from_user.username.lower())
                players.append(player2.lower()[1:])
                bot.send_message(message.chat.id, f"{player2} has been challenged!")
            # bot.send_message(message.chat.id, players[0] + ", " + players[1])

        # If it's not a username, it must be a move
        else:
            if message.chat.type == "private" and message.from_user.username.lower() in players:
                move = message.text.split(":")[1].lower()
                if move == "r":
                    player_moves[players.index(message.from_user.username.lower())] = "rock 🗻"
                elif move == "p":
                    player_moves[players.index(message.from_user.username.lower())] = "paper 📄"
                elif move == "s":
                    player_moves[players.index(message.from_user.username.lower())] = "scissor ✂️"
                else:
                    bot.send_message(message.chat.id, "Error: Not a valid move")

                if player_moves[0] != None and player_moves[1] != None:
                    if rps(player_moves[0], player_moves[1]) == "player1":
                        bot.send_message(-218047352, f"{players[0]}  :  {player_moves[0]}\n\n{players[1]}  :  {player_moves[1]}")
                        bot.send_message(-218047352, f"\"{players[0]}\" is the winner")

                    elif rps(player_moves[0], player_moves[1]) == "player2":
                        bot.send_message(-218047352, f"{players[0]}  :  {player_moves[0]}\n\n{players[1]}  :  {player_moves[1]}")
                        bot.send_message(-218047352, f"\"{players[1]}\" is the winner")

                    elif rps(player_moves[0], player_moves[1]) == "tie":
                        bot.send_message(-218047352, f"{players[0]}  :  {player_moves[0]}\n\n{players[1]}  :  {player_moves[1]}")
                        bot.send_message(-218047352, f"Tie")

                    else:
                        bot.send_message(-218047352, "Error")
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and m.text == "!bowl" or m.text == "-bowl" else False)
def bowl(message):
    try:
        hit = choice([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10])

        if hit == 1:
            response = choice(["نیازمند تلاش بیشتر", "آفا شما ضعیف هستید", "عمه من بهتر از تو می تونه امتیاز بیاره"])
        elif hit == 2:
            response = choice(["بهتر از 1ـه، ولی بازم ریدی", "2تا؟ خجالت بکش", "تو بولینگ رو ببوس بزار کنار"])
        elif hit == 3:
            response = choice(["آقا شما تمرین کافی ندارید", "چرا انقدر کم؟", "بهتر از 2 تا"])
        elif hit == 4:
            response = choice(["داری بهتر میشی", "می تونی بهتر بزنی", "دوباره امتحان کن", "یکم بهتر"])
        elif hit == 5:
            response = choice(["نصفشو زدی", "نصفش ریخت", "داری بهتر میشی", "توپو پرت کنی فکر کنم تعداد بیشتری رو بزنی", "50/50"])
        elif hit == 6:
            response = choice(["نصف بیشترشو زدی", "بالاخره بیشتر از نصفشو زدی", "ایول، 6 تاش افتاد!", "عجب مسابقه ای", "من به تواناییات شک داشتم، هنوزم دارم", "من چشم بسته بیشتر از تو میزدم"])
        elif hit == 7:
            response = choice(["سه تا مونده بود", "بدک نیست", "آقا شما مهارت دارید", "زمین کج بود", "واقعا چطور 7 تا زدی؟", "به به", "یدونه از 6 تا بیشتر", "عجب ضربه ای"])
        elif hit == 8:
            response = choice(["دوتا مونده", "این یکی رو شانس آوردی", "تو این مهارت های بولینگو از کجات در آوردی؟", "همش شانسه", "داور به نفع تیم حریف گرفت"])
        elif hit == 9:
            response = choice(["یدونه مونده تا امتیاز کامل!", "اگه مهارت منو داشتی، الان امتیاز کامل گرفته بودی", "خیلی نزدیک شدی", "میل آخر داشت می افتاد، ولی یهو صاف شد", "عه امتیاز کامل رفت امتیاز کامل خودافیظ"])
        elif hit == 10:
            response = choice(["آقا تبریک میگم، ما بولینگ بازان حرفه ای، به شما افتخار می کنیم", "امتیاز کاملو گرفتی!", "تبریک میگم! امتیاز همه میل ها رو زدی"])

        bot.send_message(message.chat.id, f"`شما {hit} میل انداختید`", parse_mode="markdown")
        bot.send_message(message.chat.id, response)
    except:
        pass

@bot.message_handler(commands=["g"])
def google(message):
    try:
        search = message.text[3:].replace(" ", "+")
        bot.reply_to(message, f"http://www.google.com/search?q={search}")
    except:
        pass

@bot.message_handler(commands=["y"])
def youtube(message):
    try:
        search = message.text[3:].replace(" ", "+")
        bot.reply_to(message, f"https://www.youtube.com/results?search_query={search}")
    except:
        pass

@bot.message_handler(commands=["say"])
def say(message):
    try:
        m = message.text[4:]
        bot.delete_message(message.chat.id, message.message_id)
        if message.reply_to_message == None:
            bot.send_message(message.chat.id, m)
        else:
            bot.reply_to(message.reply_to_message, m)

    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and (m.text.split(" ")[0].lower() == "soosmaz" or m.text.split(" ")[0] == "سوسماز") else False)
def send_season_one(message):
    try:
        m = message.text.split(" ")
        if len(m) > 1:
            if m[1] == '1' or m[1] == '۱':
                bot.forward_message(message.chat.id, -1001410450666, 2)
            elif m[1] == '2' or m[1] == '۲':
                bot.forward_message(message.chat.id, -1001410450666, 3)
            elif m[1] == '3' or m[1] == '۳':
                bot.forward_message(message.chat.id, -1001410450666, 4)
            elif m[1] == '4' or m[1] == '۴':
                bot.forward_message(message.chat.id, -1001410450666, 5)
            elif m[1] == '5' or m[1] == '۵':
                bot.forward_message(message.chat.id, -1001410450666, 8)
            elif m[1] == '6' or m[1] == '۶':
                bot.forward_message(message.chat.id, -1001410450666, 10)
            elif m[1] == '7' or m[1] == '۷':
                bot.forward_message(message.chat.id, -1001410450666, 12)
            elif m[1] == '8' or m[1] == '۸':
                bot.forward_message(message.chat.id, -1001410450666, 14)
            elif m[1] == '9' or m[1] == '۹':
                bot.forward_message(message.chat.id, -1001410450666, 16)
            elif m[1] == '10' or m[1] == '۱۰':
                bot.forward_message(message.chat.id, -1001410450666, 17)
            elif m[1] == '11' or m[1] == '۱۱':
                bot.forward_message(message.chat.id, -1001410450666, 19)
            elif m[1] == '12' or m[1] == '۱۲':
                bot.forward_message(message.chat.id, -1001410450666, 23)
            elif m[1] == '13' or m[1] == '۱۳':
                bot.forward_message(message.chat.id, -1001410450666, 25)
            elif m[1] == '14' or m[1] == '۱۴':
                bot.forward_message(message.chat.id, -1001410450666, 26)
            elif m[1] == '15' or m[1] == '۱۵':
                bot.forward_message(message.chat.id, -1001410450666, 28)
            else:
                pass
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and "ب3" in m.text else False)
def BalBalBal(message):
    bot.delete_message(message.chat.id, message.message_id)
    if message.reply_to_message == None:
        bot.send_message(message.chat.id, "بل بل بل")
    else:
        bot.reply_to(message.reply_to_message, "بل بل بل")

@bot.message_handler(func=lambda m: True if m.text != None and (m.text == "ضیغمی 1" or m.text == "ضیغمی1") else False)
def zeyghami_khosgel(message):
    bot.delete_message(message.chat.id, message.message_id)
    if message.reply_to_message == None:
        bot.send_message(message.chat.id, "خوشگل!")
    else:
        bot.reply_to(message.reply_to_message, "خوشگل!")

@bot.message_handler(func=lambda m: True if m.text != None and (m.text == "ضیغمی 2" or m.text == "ضیغمی2") else False)
def zeyghami_pnb(message):
    bot.delete_message(message.chat.id, message.message_id)
    if message.reply_to_message == None:
        bot.send_message(message.chat.id, "پس نمه بابا!")
    else:
        bot.reply_to(message.reply_to_message, "پس نمه بابا!")

@bot.message_handler(commands=["kill", "vote"])
def kill(message):
    try:
        bot.send_message(message.chat.id, f"{message.text[5:]} {choice(['was', 'was not'])} an impostor")
    except:
        pass

banned_stickers = ["khas0111", "Emamkhomeyni_rah", "HamenabaGp"]
@bot.message_handler(content_types=["sticker"])
def ban(message):
    if message.sticker.set_name in banned_stickers:
        # bot.delete_message(message.chat.id, message.message_id)
        pass
    elif message.sticker.set_name == "Shpooky":
        bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAEBgOZfl9FCGjYq5NOakbIb3t16JgZtngACswADj-aFB1be__PTiwZoGwQ")

@bot.message_handler(func=lambda m: True if m.text != None and ("میو" in m.text.split(" ") or "meow" in m.text.split(" ")) else False)
def dog(message):
    pass

@bot.message_handler(commands=["translate"])
def translate(message):
    try:
        bot.reply_to(message.reply_to_message, shift(message.reply_to_message.text.lower()))
    except:
        pass

@bot.message_handler(func=lambda m: True if m.text != None and (m.text.split(" ")[0] == "تدوخ" or m.text.split(" ")[0] == "تدی") else False)
def teddy(message):
    bot.send_message(message.chat.id, "🧸بله")

@bot.message_handler(func=lambda m: True if m.text != None and (m.text == "چی میگی تو" or m.text == "چی میگی تو؟" or m.text == "چی می گی تو" or m.text == "چی می گی تو؟") else False)
def gorbe_1(message):
    bot.reply_to(message, "چی میگی تو یعنی چی؟")
@bot.message_handler(func=lambda m: True if m.text != None and (m.text == "عن آقا" or m.text == "عن اقا") else False)
def gorbe_2(message):
    bot.reply_to(message, "درست صحبت کن\nعن آقا چیه؟")
    bot.send_message(message.chat.id, "`کف گرگی`", parse_mode="markdown")

@bot.message_handler(func=lambda m: True if m.text != None and ("یوبی سافت" in m.text or "یوبیسافت" in m.text) else False)
def ubibug(message):
    bot.reply_to(message, "*یوبی باگ")

@bot.message_handler(func=lambda m: True if m.text != None and ("ترامپ" in m.text) and ("ترام" not in m.text or "تُرام" not in m.text) else False)
def toram(message):
    bot.reply_to(message, "*تُرام")


@bot.message_handler(commands=['soosmazstats'])
def soosmazStats(message):
    for i in range(29):
        bot.send_message(message.chat.id, i)
        try:
            bot.forward_message(message.chat.id, -1001410450666, i)
        except:
            pass

try:
    bot.polling(none_stop=True)
except:
    pass
