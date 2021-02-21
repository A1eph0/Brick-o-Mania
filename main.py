import os
from Game import Game
from Parameters import *

rows, columns = os.popen('stty size', 'r').read().split()
rows, columns = int(rows), int(columns)

if (DIMENSIONS['width'] <= columns) and (DIMENSIONS['height'] <= rows):
    game=Game()
    game.run()
else:
    print("Terminal size needs to be atleast \
            240 x 60 (columns x rows)")
    os._exit(0)

