import telebot
from telebot import types
from datetime import datetime
import threading

token = ''
bot = telebot.TeleBot(token=token)
reminder_dct = {}
on_off_spam_switch = False

@bot.message_handler(commands=['start'])
def main_func(message):
    user = bot.send_message(
        message.chat.id,
        text='Hello!',
        reply_markup=keyboard()
    )
    bot.register_next_step_handler(user, option_func)


def option_func(message):
    if message.text == 'Reminders':
        set_reminder(message)
    if message.text == 'Show All Reminders':
        bot.send_message(message.chat.id, text=str(reminder_dct))
        main_func(message)




def set_reminder(message):
    bot.reply_to(message, text='Enter date and time in format: YYYY-MM-DD HH:MM')
    bot.register_next_step_handler(message, set_reminder_key_func)


def set_reminder_key_func(message):
    try:
        reminder_datetime = datetime.strptime(message.text, '%Y-%m-%d %H:%M')
        if reminder_datetime < datetime.now():
            bot.reply_to(message, text="BUY A CALENDAR STOOPID!!!!")
        else:
            reminder_key = message.text
            reminder_dct[reminder_key] = ""
            bot.send_message(message.chat.id, text=f'Reminder set for: {reminder_key}, now enter reminder name')
            bot.register_next_step_handler(message, set_reminder_name_func, reminder_key)
    except ValueError:
        bot.reply_to(message, text="Wrong format! Try again: YYYY-MM-DD HH:MM")
        main_func(message)


def set_reminder_name_func(message, reminder_key):
    reminder_dct[reminder_key] = message.text
    bot.send_message(message.chat.id, text=f'Reminder "{reminder_dct[reminder_key]}" set for {reminder_key}.')
    main_func(message)

    delay = (datetime.strptime(reminder_key, '%Y-%m-%d %H:%M') - datetime.now()).total_seconds()
    threading.Timer(delay, start_spam, args=[message.chat.id, reminder_key]).start()


def start_spam(message, reminder_key):
    global on_off_spam_switch
    on_off_spam_switch = True
    while on_off_spam_switch:
        bot.send_message(message, text=f"Reminder: {reminder_dct[reminder_key]}! Type 'stop {reminder_key}' to stop.")
    bot.register_next_step_handler(message, stop_spam)


def stop_spam(message, reminder_key):
    del reminder_dct[reminder_key]
    global on_off_spam_switch
    if message.text.lower() == 'stop':
        on_off_spam_switch = False
        bot.send_message(message.chat.id, text=f"Reminder {reminder_key} stopped.")
        main_func(message)
    else:
        start_spam(message, reminder_key)



def keyboard():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(text='Reminders')
    button2 = types.KeyboardButton(text='Show All Reminders')
    button3 = types.KeyboardButton(text='Remove Reminder')
    buttons.add(button1, button2, button3)
    return buttons


if __name__ == '__main__':
    bot.polling(none_stop=True)
