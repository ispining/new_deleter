
import iluxaMod as ilm

import remover

main_tg_bot = ilm.tgBot('')
bot = main_tg_bot.bot
bot.parse_mode = 'HTML'

pickle = ilm.tools.pickle

class bots:
    def __init__(self, token=None):
        self.token = token

    def list_all(self):
        return pickle('data').unpick()

    def add(self):
        unp = pickle('data').unpick()
        unp.append(self.token)
        pickle('data').pick(unp)

    def remove(self):
        unp = pickle('data').unpick()
        unp.remove(self.token)
        pickle('data').pick(unp)




def loop_bots_threads():
    for b in bots().list_all():
        th = remover.threading.Thread(target=remover.starter, args=(b, ))
        th.daemon = True
        th.start()
        remover.threading.main_thread()

