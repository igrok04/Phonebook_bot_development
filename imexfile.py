
import telebot
from telebot import TeleBot, types
import crud as cr
token = cr.get_token()
bot = telebot.TeleBot(token, parse_mode='MARKDOWN')

import logger as lg


print('\nВас приветствует программа импорта и экспорта файлов телефонной книги')

print('Переходи в бот и вводи /9 - импорт файла, /10 - экспорт файла.') 
                 
       
@bot.message_handler()
def answer(msg: types.Message):

    text = msg.text
    
    if text == '/9':
        bot.register_next_step_handler(msg, answer)
        lg.logging.info('User entered: /9')
        bot.send_message(chat_id=msg.from_user.id, text='Отправьте файл')
        lg.logging.info('User imported the file')
        
    elif text == '/10':
        lg.logging.info('User entered: /10')
        bot.send_document(chat_id=msg.from_user.id, document = open('base_phone.csv', 'rb'))
        lg.logging.info('User exported file "base_phone.csv"')

    else:
        lg.logging.info('User entered an invalid menu value: {n}')
        print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

@bot.message_handler(commands=['start'])

    
        

#@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')



print('server start')
bot.infinity_polling()

    
   