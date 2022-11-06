import os
import threading
import time
import config
import window
from config import bot, pickle



config.loop_bots_threads()

th = threading.Thread(target=window.start_window)
th.daemon = True
th.start()
threading.main_thread()

while True:
    try:
        os.system('cls')
        sessions = len(unpick("data"))
        print(f"[+] Sessions: {str(sessions)}")
        time.sleep(3)
    except KeyboardInterrupt:
        exit()
