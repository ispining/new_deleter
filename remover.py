import re, pickle
import threading


import telebot.apihelper
import telebot



def pick(filename, data):
    file = open(filename, 'wb')

    # dump information to that file
    pickle.dump(data, file)

    # close the file
    file.close()


def unpick(filename):
    with open(filename, 'rb') as file:

        # dump information to that file
        return pickle.load(file)
    

# ilm.tools.pickle('data').pick(['5057064705:AAFgeeBBlTIjyEynVyo9fn_UAKBsrX3KtIE'])

def get_admins(bot, chat_id):
    result = []
    for i in bot.get_chat_administrators(chat_id):
        result.append(i.user.id)
    return result


def del_all_start(bot, message):
    user_id = message.from_user.id

    for m_id in range(1, message.message_id):
        try:
            bot.delete_message(message.chat.id, m_id)
        except:
            pass

    bot.send_message(user_id, "<b>Все сообщения в группе {} ({}) были удалены успешно!</b>".format(*[bot.get_chat(message.chat.id).title, str(message.chat.id)]))


def starter(t):
    bot = telebot.TeleBot(t)
    bot.parse_mode = 'HTML'


    @bot.message_handler(commands=["start"])
    def start_msg(message):
        chat_id = message.chat.id

        bot.send_message(chat_id, """
<b>Бот удаления сервисных сообщений</b>

Чтобы этот бот начал удалять системные сообщения - достаточно просто добавить его в свою группу и наделить правами Администратора.


<b>Клонирование бота</b>

Хотите такой же бот, только свой, при чем бесплатно?
1. Перейдите к боту @BotFather и введите команду /newbot
2. Выберите любое название и уникальный юзернейм для вашего нового бота.
3. В знак завершения регистрации - вы получите сообщение с токеном нового бота. Отправьте сюда сообщение с токеном сюда.
4. Ну как бы все;) Ваш бот самостоятельно удаляет сервисные сообщения о присоединившихся или покинувших группу участниках!


<b>Очистка чата</b>

Хочешь удалить все из своего чата? 
Нет проблем! Введи команду /del_all и все сообщения удалятся.
Работает только с сообщениями, посланными после того, как бот стал у вас в группе Администратором

        """)


    @bot.message_handler(commands=['del_all'])
    def del_all(message):
        chat_id = message.chat.id
        user_id = message.from_user.id

        if user_id in get_admins(bot, chat_id):
            bot.send_message(user_id, "<b>Начало удаления сообщений...</b>")

            th = threading.Thread(target=del_all_start, args=(bot, message, ))
            th.daemon = True
            th.start()
            threading.main_thread()



    @bot.message_handler(content_types=['text'])
    def text_messages(message):
        r = re.search(r"\d\d\d\d\d\d\d\d\d\d:\S+", message.text)
        if r != None:
            token = r.group(0)

            unp = unpick('data')
            if token not in unp:
                unp.append(token)
                pick('data', unp)
                th = threading.Thread(target=starter, args=(token, ))
                th.daemon = True
                th.start()
                threading.main_thread()

                bot.send_message(message.chat.id, """<b>Бот клонирован успешно!</b>
Теперь ваш бот работает самостоятельно и может очищать ваши группы.

                """)


            else:
                bot.send_message(message.chat.id, """<b>ОШИБКА!</b>
Бот уже был клонирован ранее, и все еще числится в базе клонированным.

                
                """)



    @bot.message_handler(chat_types=['group', 'supergroup'])
    def delete_msg(message):
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass





    while True:
        try:
            bot.polling()

        except telebot.apihelper.ApiTelegramException:
            try:
                bot.stop_polling()

            except:
                pass
            unp = unpick('data')
            unp.remove(t)
            pick('data', unp)
            break

        except Exception as ex:

            if ex != None:
                if "Description: Not Found" in str(ex):
                    try:
                        bot.stop_polling()

                    except:
                        pass
                    unp = unpick('data')
                    unp.remove(t)
                    pick('data', unp)
                    break
