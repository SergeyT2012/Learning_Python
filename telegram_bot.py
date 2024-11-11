import telebot
from telebot import types
from random import *
from time import *
bot = telebot.TeleBot("7799596122:AAHvRyuachHNG6vubSArXNV0hnelLOKknEc")
@bot.message_handler(commands = ["start"])
def f1(message):
    k = types.InlineKeyboardMarkup()
    k1 = types.InlineKeyboardButton(text = "Meme", callback_data = "a")
    k.add(k1)
    k2 = types.InlineKeyboardButton(text = "music", callback_data = "b")
    k.add(k2)
    k3 = types.InlineKeyboardButton(text = "flip a coin", callback_data = "c")
    k.add(k3)
    k4 = types.InlineKeyboardButton(text = "video link", callback_data = "d")
    k.add(k4)
    k5 = types.InlineKeyboardButton(text = "secret (A LOT OF ACTION)", callback_data = "e")
    k.add(k5)
    bot.send_message(message.chat.id, "what do you want me to do?", reply_markup = k)
@bot.callback_query_handler(func = lambda call: True)
def knopka(call):
    if call.data == "a":
        bot.send_photo(call.message.chat.id, open("e.jpeg","rb"))
    if call.data == "b":
        bot.send_audio(call.message.chat.id, open("spongebob.mp3","rb"))
    if call.data == "c":
        coin = randint(1,2)
        if coin == 1:
            bot.send_message(call.message.chat.id, text = "It's heads!")
            bot.send_photo(call.message.chat.id, open("Orel.gif","rb"))
        if coin == 2:
            bot.send_message(call.message.chat.id, text = "It's tails!")
            bot.send_photo(call.message.chat.id, open("Reshka.gif","rb"))
    if call.data == "d":
        bot.send_message(call.message.chat.id, text = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs")
    if call.data == "e":
        bot.send_document(call.message.chat.id, open("copy_9DDF8921-3668-49DE-A55B-AE9B71C280CC.mov","rb"))
@bot.message_handler(commands = ["awesome"])
def f2(message):
    bot.send_message(message.chat.id, "yeah")
@bot.message_handler(commands = ["nospam"])
def f3(message):
    bot.send_message(message.chat.id, "ok")
gg = False
igrok = randint(1,6)
rr = randint(1,6)
@bot.message_handler(content_types = ["text"])
def text(message):
    global gg
    if message.text == "Hello" or message.text == "hello":
        t = types.ReplyKeyboardMarkup(resize_keyboard = True)
        t1 = types.KeyboardButton(text = "Link to YouTube")
        t2 = types.KeyboardButton(text = "GIF")
        t3 = types.KeyboardButton(text = "Guess the number")
        t4 = types.KeyboardButton(text = "spam11!!!!1!")
        t5 = types.KeyboardButton(text = "Dice")
        t.add(t1,t2,t3,t4,t5)
        bot.send_message(message.chat.id, "Hi! Im your bot! How are you doing?", reply_markup = t)
    elif message.text == "spam11!!!!1!":
        while gg == False:
            bot.send_message(message.chat.id,"You won a fre iFone 17 pro max ultra!!!11!11!")
            sleep(2)
    elif message.text == "Dice":
        igrok = randint(1,6)
        rr = randint(1,6)
        if igrok == 1:
            bot.send_message(message.chat.id," You got 1 dot!")
        elif igrok == 2:
            bot.send_message(message.chat.id," You got 2 dots!")
        elif igrok == 3:
            bot.send_message(message.chat.id," You got 3 dots!")
        elif igrok == 4:
            bot.send_message(message.chat.id," You got 4 dots!")
        elif igrok == 5:
            bot.send_message(message.chat.id," You got 5 dots!")
        elif igrok == 6:
            bot.send_message(message.chat.id," You got 6 dots!")
        if rr == 1:
            bot.send_message(message.chat.id," I got 1 dot!")
        elif rr == 2:
            bot.send_message(message.chat.id," I got 2 dots!")
        elif rr == 3:
            bot.send_message(message.chat.id," I got 3 dots!")
        elif rr == 4:
            bot.send_message(message.chat.id," I got 4 dots!")
        elif rr == 5:
            bot.send_message(message.chat.id," I got 5 dots!")
        elif rr == 6:
            bot.send_message(message.chat.id," I got 6 dots!")
        if rr == igrok:
            bot.send_message(message.chat.id," It's a tie!")
        if rr > igrok:
            bot.send_message(message.chat.id," I won!")
        if rr < igrok:
            bot.send_message(message.chat.id," You won!")
    elif message.text == "Stop":
        gg = True
        bot.send_message(message.chat.id, "Stopped!")
    elif message.text == "Link to Youtube":
        bot.send_message(message.chat.id,"https://www.youtube.com/")
    elif message.text == "GIF":
        bot.send_document(message.chat.id, open("cat-shocked.gif","rb"))
    elif message.text == "Guess the number":
        global x
        x = randint(1,10)
        bot.send_message(message.chat.id, "Enter a number from 1 to 10")
        sleep(10)
        if message.text == x:
            bot.send_message(message.chat.id, "Great! You guessed it! The number was " + str(x))
        else:
            bot.send_message(message.chat.id, "You didn't guess it right. Shame! The number was " + str(x))
    elif message.text == "Good" or message.text == "good":
        bot.send_message(message.chat.id, "Great! What are you doing at the moment?")
    elif message.text == "Coding" or message.text == "coding":
        bot.send_message(message.chat.id, "What are you coding?")
    elif message.text == "You" or message.text == "you":
        bot.send_message(message.chat.id, "Woah! That's cool!")
    elif message.text == "I know" or message.text == "i know":
        bot.send_message(message.chat.id, "Well then, go back to work dev >:)!")
    elif message.text == "Hello" or "hello" or "Hi" or "hi":
        bot.send_message(message.chat.id, "hi! Im your bot!")
    else:
        bot.send_message(message.chat.id, "Sorry, didn't catch that! Can you repeat please?")
@bot.message_handler(content_types = ["photo"])
def p(message):
    bot.send_message(message.chat.id, "brhu, im blind!111!!1!!!")

bot.polling()