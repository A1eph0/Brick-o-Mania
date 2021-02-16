import time
import os
import colorama as clr
from Screen import Screen
from Paddle import Paddle
from Parameters import *
from Input import Get

clr.init()

# os.system('clear')
class Game:
    screen = Screen()
    paddle = Paddle()

    score = "0"
    time = "--:--"
    life = 5
    get = Get()

    def __init__(self):
        os.system("stty -echo")

    def run (self):
        while (True): 
            score_string = "Score: " + self.score
            time_string = "Time: " + self.time
            life_string = "❤ "*5

            key = self.get.input_to() 

            self.screen.reset_screen()
            self.screen.render_on_screen((1, 25), score_string)
            self.screen.render_on_screen((1, 86-self.life), life_string, clr.Fore.RED)
            self.screen.render_on_screen((1, 135), time_string)
            self.paddle.render(self.screen)
            if key == 'd':
                self.paddle.move(True)
            if key == 'a':
                self.paddle.move(False)
            
            if key == 'r':
                self.reset()

            if key == 'q':
                os.system("stty echo")
                os._exit(0)
    
            self.screen.out()
    
    def reset(self):
        self.screen = Screen()
        self.paddle = Paddle()

        self.score = "0"
        self.time = "--:--"
        self.life = 5
        self.get = Get()
