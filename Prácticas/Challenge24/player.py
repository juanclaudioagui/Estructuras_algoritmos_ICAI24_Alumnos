import os
import random
import time
import random
from pygame import mixer
mixer.init()
path='./Mp3/'
files = os.listdir(path)
for i in range(300):
    sel1 = random.choice(files)
    sel2=path+sel1
    print(sel2)
    mixer.music.load(sel2) # you may use .mp3 but support is limited
    mixer.music.play()
    time.sleep(5) 
    mixer.music.stop()
