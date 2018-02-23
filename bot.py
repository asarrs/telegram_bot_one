
import telebot
import config
import botan
import random
bot = telebot.TeleBot(config.token)
random.seed()
import os
from telebot import types

@bot.message_handler(commands=['start'])
def start(message,):
    keyboard = types.InlineKeyboardMarkup(True)
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Часто задаваемые вопросы 🤔', 'Где мы находимся ? 🤔', 'Остались вопросы ? 🙄', 'Наши акции 💕', 'Прайс 💰',]])
    bot.send_message(message.chat.id, 'Здравствуй, меня зовут Анна.🖐\n'
                                      'Я сотрудница и поклоница студии красоты <b>S Studio</b>.\n'
                                      'И я немного раскажу про нашу студию 😉\n'
                                      '\n'
                                      'Команду <b>S Studio</b> очень волнует безопаность нашего клиента '
                                      'думаю вам известно что многие салоны красоты как и частные мастера '
                                      'использют многоразыве инструменты такие как пилки, бафики из за этого '
                                      'велика вероятность получить различные заболевания такие как <b>"Гипатит С","Герпес","Грибок"</b> \n'
                                      'и сказать по правде список довольно огромен. '
                                      'У нас для каждого клиента имеется одноразовый инструмент, это снижает возможность заражения до 0%.\n'
                                      '\n'
                                      'Также мы очень ценим ваше время, поэтому ввели услугу <b>"Экспресс"</b> вы сможете одновремено нарасти ногти и сделать чудный педикюр\n'
                                      '                <pre>Все для вас</pre>😉'
                                      , reply_markup=keyboard, parse_mode='HTML')
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == '👈 назад в меню':
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Часто задаваемые вопросы 🤔', 'Где мы находимся ? 🤔', 'Остались вопросы ? 🙄', 'Наши акции 💕', 'Прайс 💰']])
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Анекдот дня: Парень хотел стать геем но не смог у него слишком тонкая кишка !',
            reply_markup=keyboard
        )
    elif c.data == '👈 назад':
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Наши работы 💅','Наши мастера', 'Как записастя ?', 'Материалы которые мы используем', '👈 назад в меню']])
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Анекдот дня: Парень хотел стать геем но не смог у него слишком тонкая кишка !',
            reply_markup=keyboard
        )
    elif c.data == 'Прайс 💰':
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['👈 назад в меню']])
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='<b>МАНИКЮР|ПЕДИКЮР</b>\n'
                 'Аппаратный маникюр - <b>300р.</b>\n'
                 'Педикюр - <b>650р.</b>\n'
                 'Коррекция гелем - <b>1000</b>\n'
                 'Маникюр <b>+</b> Наращивание гелем - <b>1300р.</b>\n'
                 'Маникюр <b>+</b> коррекция гелем - <b>1000р.</b>\n'
                 'Маникюр <b>+</b> покрытие гель-лкаом - <b>900р.</b>\n'
                 'Педикюр <b>+</b> коррекция гелем - <b>1300р.</b>\n'
                 'Оформление бровей нитью - <b>200р.</b>\n'
                 'Окрашивание бровей - <b>100р.</b>\n'
                 'Оформление <b>+</b> окрашивание хной - <b>500р.</b>\n'
                 '<b>РЕСНИЦЫ</b>\n'
                 'Наращивание ресниц классика - <b>1000р.</b>\n'
                 'Наращивание ресниц 2D - <b>1200р.</b>\n'
                 'Наращивание ресниц 3D - <b>1400р.</b>\n'
                 'Голивуд - <b>1600р.</b>'
            ,
            reply_markup=keyboard,
            parse_mode='HTML'
        )
    elif c.data == 'Остались вопросы ? 🙄':
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Написать администратору','👈 назад в меню']])
        keyboard2 = types.ReplyKeyboardMarkup()
        keyboard2.add(types.KeyboardButton('Позвонить', request_contact=True))
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Если у вас остались какие либо вопросы вы можете написать нашему администратору прямо в телеграме или же позвонить, мы с радостью ответим на все ваши вопросы !😁\n'
                 'По вопросам сотрудничества можете написать нам на почту saulestudio@yandex.ru либо связатся с администратором !',
            reply_markup=keyboard,
        )

    elif c.data == 'Где мы находимся ? 🤔':
        bot.delete_message(chat_id=c.message.chat.id,
                           message_id=c.message.message_id)
        bot.send_location(c.from_user.id, 48.7706069, 44.559990500000026)
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['👈 назад в меню']])
        bot.send_message(
            text='Мы находимся по адресу : <b>Краснооктябрьский р-н, ул. Богунская, д.8, офис 320</b>',
            chat_id=c.message.chat.id,
            reply_markup=keyboard,
            parse_mode='HTML'
        )
    elif c.data == 'Часто задаваемые вопросы 🤔':
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name, url='https://www.instagram.com/askarishchanov/')for name in ['Наши работы 💅', ]])
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Наши мастера', 'Как записастя ?', 'Материалы которые мы используем', '👈 назад в меню']])
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Самые частые вопросы которые нам задают, надеемся вы надете ответ на свой вопрос ! 😁',
            reply_markup=keyboard,
        )
    elif c.data == 'Наши мастера':
        bot.delete_message(chat_id=c.message.chat.id,
                           message_id=c.message.message_id)
        directory = 'C:/Users/Askar/Pictures/test foto instagram/12'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(c.from_user.id, 'upload_photo')
        bot.send_photo(c.from_user.id, img)
        img.close()
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name)for name in ['>', '👈 назад в меню' ]])
        bot.send_message(
            chat_id=c.message.chat.id,
            text='Наши мастера',
            reply_markup=keyboard,
        )
    elif c.data == '>':
        bot.delete_message(chat_id=c.message.chat.id,message_id=c.message.message_id)
        directory = 'C:/Users/Askar/Pictures/test foto instagram/12'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(c.from_user.id, 'upload_photo')
        bot.send_photo(c.from_user.id, img)
        img.close()
        keyboard = types.InlineKeyboardMarkup(True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['>', '👈 назад в меню']])
        bot.send_message(c.from_user.id, 'dfg', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'Остались вопросы ? 🙄':
        keyboard2 = types.ReplyKeyboardMarkup()
        keyboard2.add(types.KeyboardButton('Позвонить', request_contact=True))
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Е',
            reply_markup=keyboard2,
        )


if __name__ == '__main__':
     bot.polling(none_stop=True)



