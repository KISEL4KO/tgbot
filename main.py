from telebot import types

import telebot

bot = telebot.TeleBot('6093434977:AAG-o0AxGHGmyYm-RaMq4vXvMe67J1zeB8o')

name = ''

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.reply_to(message, 'Привет бро если хочешь начать напиши /start')
    bot.register_next_step_handler(message, start)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.reply_to(message,'Добров пожаловать в мир Викингов Valhalla, а теперь назовись:')
        bot.register_next_step_handler(message, get_name)
    else: bot.reply_to(message,'Я тебе не понимаю ,напиши /start для начала')

@bot.message_handler(content_types=['text'])
def get_name(message):
    name = message.text
    bot.reply_to(message,f'Хах Хорошее имечко {name}')
    bot.reply_to(message,'Ну что ты решился начаться приключение?')
    bot.register_next_step_handler(message, check)


def check(message):
    if message.text == 'Да':
        bot.reply_to(message,'Хорошо')
        bot.register_next_step_handler(message,prolog)
    else: bot.reply_to(message,'Ну что до встречи тогда')





@bot.message_handler(content_types=['text'])
def prolog(message):
    bot.reply_to(message,'Итак для начала я расскажу предысторию')





bot.polling(none_stop=True, interval=0)
