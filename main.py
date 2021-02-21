import os
from Game import Game
from Parameters import *

h, w = os.popen('stty size', 'r').read().split()


if (DIMENSIONS['width'] <= int(w)) and (DIMENSIONS['height'] <= int(h)):
    game=Game()
    game.run()
else:
    print("ERR!: Terminal size too small!"+'\n'+ "Terminal size needs to be atleast " + str(DIMENSIONS['height']) + " x " + str(DIMENSIONS['width']) + " (height x width)")
    os._exit(0)

