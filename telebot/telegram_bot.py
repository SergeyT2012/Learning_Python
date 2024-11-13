import telebot
from telebot import types
from random import *
from time import *
bot = telebot.TeleBot("7799596122:AAHvRyuachHNG6vubSArXNV0hnelLOKknEc")
@bot.message_handler(commands = ["start"])
def bot_buttons_setup(message):
    buttons_array = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = "Meme", callback_data = "a")
    buttons_array.add(button1)
    button2 = types.InlineKeyboardButton(text = "music", callback_data = "b")
    buttons_array.add(button2)
    button3 = types.InlineKeyboardButton(text = "flip a coin", callback_data = "c")
    buttons_array.add(button3)
    button4 = types.InlineKeyboardButton(text = "video link", callback_data = "d")
    buttons_array.add(button4)
    button5 = types.InlineKeyboardButton(text = "secret (A LOT OF ACTION)", callback_data = "e")
    buttons_array.add(button5)
    bot.send_message(message.chat.id, "what do you want me to do?", reply_markup = buttons_array)
@bot.callback_query_handler(func = lambda call: True)
def button(call):
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
def auto_responder_to_specific_text(message):
    bot.send_message(message.chat.id, "yeah")
@bot.message_handler(commands = ["nospam"])
def respond_to_specific_message(message):
    bot.send_message(message.chat.id, "ok")
spam_toggle = False
random_player_number = randint(1,6)
random_bot_number = randint(1,6)
@bot.message_handler(content_types = ["text"])
def text(message):
    global spam_toggle
    if message.text == "Hello" or message.text == "hello":
        button_setup_under_entry = types.ReplyKeyboardMarkup(resize_keyboard = True)
        entry_button_1 = types.KeyboardButton(text = "Link to YouTube")
        entry_button_2 = types.KeyboardButton(text = "GIF")
        entry_button_3 = types.KeyboardButton(text = "Guess the number (NOT FINISHED)")
        entry_button_4 = types.KeyboardButton(text = "spam11!!!!1!")
        entry_button_5 = types.KeyboardButton(text = "Dice")
        button_setup_under_entry.add(entry_button_1,entry_button_2,entry_button_3,entry_button_4,entry_button_5)
        bot.send_message(message.chat.id, "Hi! Im your bot! How are you doing?", reply_markup = button_setup_under_entry)
    elif message.text == "spam11!!!!1!":
        while spam_toggle == False:
            bot.send_message(message.chat.id,"You won a fre iFone 17 pro max ultra!!!11!11!")
            sleep(2)
    elif message.text == "Dice":
        random_player_number = randint(1,6)
        random_bot_number = randint(1,6)
        if random_player_number == 1:
            bot.send_message(message.chat.id," You got 1 dot!")
        elif random_player_number == 2:
            bot.send_message(message.chat.id," You got 2 dots!")
        elif random_player_number == 3:
            bot.send_message(message.chat.id," You got 3 dots!")
        elif random_player_number == 4:
            bot.send_message(message.chat.id," You got 4 dots!")
        elif random_player_number == 5:
            bot.send_message(message.chat.id," You got 5 dots!")
        elif random_player_number == 6:
            bot.send_message(message.chat.id," You got 6 dots!")
        if random_bot_number == 1:
            bot.send_message(message.chat.id," I got 1 dot!")
        elif random_bot_number == 2:
            bot.send_message(message.chat.id," I got 2 dots!")
        elif random_bot_number == 3:
            bot.send_message(message.chat.id," I got 3 dots!")
        elif random_bot_number == 4:
            bot.send_message(message.chat.id," I got 4 dots!")
        elif random_bot_number == 5:
            bot.send_message(message.chat.id," I got 5 dots!")
        elif random_bot_number == 6:
            bot.send_message(message.chat.id," I got 6 dots!")
        if random_bot_number == random_player_number:
            bot.send_message(message.chat.id," It's a tie!")
        if random_bot_number > random_player_number:
            bot.send_message(message.chat.id," I won!")
        if random_bot_number < random_player_number:
            bot.send_message(message.chat.id," You won!")
    elif message.text == "Stop":
        spam_toggle = True
        bot.send_message(message.chat.id, "Stopped!")
    elif message.text == "Link to Youtube":
        bot.send_message(message.chat.id,"https://www.youtube.com/")
    elif message.text == "GIF":
        bot.send_document(message.chat.id, open("cat-shocked.gif","rb"))
    elif message.text == "Guess the number":
        global random_guess_number
        random_guess_number = randint(1,10)
        bot.send_message(message.chat.id, "Enter a number from 1 to 10")
        sleep(10)
        if message.text == random_guess_number:
            bot.send_message(message.chat.id, "Great! You guessed it! The number was " + str(random_guess_number))
        else:
            bot.send_message(message.chat.id, "You didn't guess it right. Shame! The number was " + str(random_guess_number))
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
def photo_respond(message):
    bot.send_message(message.chat.id, "brhu, im blind!111!!1!!!")

bot.polling()