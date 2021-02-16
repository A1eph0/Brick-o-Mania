import time
import os
import colorama as clr
from Screen import Screen
from Paddle import Paddle
from Parameters import *
from Input import Get

clr.init()

# os.system('clear')
screen = Screen()
paddle = Paddle()

score = "0"
time = "--:--"
life = 5
get = Get()
while (True): 
    score_string = "Score: " + score
    time_string = "Time: " + time
    life_string = "❤ "*5

    key = get.input_to() 

    screen.reset_screen()
    screen.render_on_screen((1, 25), score_string)
    screen.render_on_screen((1, 86-life), life_string, clr.Fore.RED)
    screen.render_on_screen((1, 135), time_string)
    paddle.render(screen)
    if key == 'd':
        paddle.move(True)
    if key == 'a':
        paddle.move(False)
    
    screen.out()
    