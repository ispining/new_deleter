import os
import threading
import time
import config
from config import bot
import pickle
from config import pick, unpick



config.loop_bots_threads()



while True:
    try:

        os.system('clear')
        sessions = len(unpick("data"))
        print(f"[+] Sessions: {str(sessions)}")
        time.sleep(3)
    except KeyboardInterrupt:
        exit()
