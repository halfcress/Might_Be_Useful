from pygame import mixer
import time

mixer.init()
mixer.music.load('C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/kuzi.mp3')

y = ""
log = "C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/Client.txt"
def ses_cal():
    mixer.music.play()

def satir_oku():
    with open(log, 'r', encoding='utf8') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        return last_line

while True:

    time.sleep(1)
    satir = satir_oku()
    x = satir.split(" ")

    satir = satir_oku()

    x = satir.split(" ")

    if x[-1] == y:
        ses_cal()
        if x[-1] == y:
            y = "random"
            time.sleep(1)
    elif x[-1] != "Hideout.":
        y = "Hideout."
        time.sleep(1)





















