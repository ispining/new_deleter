
import telebot, pickle

import remover

bot = telebot.TeleBot("")
bot.parse_mode = 'HTML'

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

class bots:
    def __init__(self, token=None):
        self.token = token

    def list_all(self):
        return unpick("data")

    def add(self):
        unp = unpick("data")
        unp.append(self.token)
        pick("data", unp)

    def remove(self):
        unp = unpick("data")
        unp.remove(self.token)
        pick("data", unp)




def loop_bots_threads():
    for b in bots().list_all():
        th = remover.threading.Thread(target=remover.starter, args=(b, ))
        th.daemon = True
        th.start()
        remover.threading.main_thread()

