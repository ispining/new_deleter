import os
import threading
import time
import config
from config import bot, pickle



config.loop_bots_threads()



while True:
    try:
        try:
            os.system('cls')
        except:
            os.system('clear')
        sessions = len(unpick("data"))
        print(f"[+] Sessions: {str(sessions)}")
        time.sleep(3)
    except KeyboardInterrupt:
        exit()
