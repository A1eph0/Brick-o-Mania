import time
import os
import colorama as clr
from Screen import Screen
from Paddle import Paddle
from Ball import Ball
from Blocks import Block
from Parameters import *
from Input import Get

clr.init()

# os.system('clear')
class Game:
    screen = Screen()
    paddle = Paddle()
    ball = Ball()
    block = Block()

    get = Get()

    def __init__(self):
        os.system("stty -echo")

    def run (self):
        while (True):
            if self.screen.life: 
                key = self.get.input_to() 
                self.screen.render()

                self.ball.move_ball(self.paddle, self.block)

                for i in (self.block, self.paddle, self.ball):
                    i.render(self.screen)

                if key == 'd':
                    self.paddle.move(True)
                    # print(self.ball.held)
                    if self.ball.held and self.ball.position[0]==DIMENSIONS["height"]-12 and self.ball.move_state==False:
                        self.ball.move(True, self.paddle)

                if key == 'a':
                    self.paddle.move(False)
                    # print(self.ball.held)
                    if self.ball.held and self.ball.position[0]==DIMENSIONS["height"]-12 and self.ball.move_state==False:
                        self.ball.move(False, self.paddle)
                
                if key == 'r':
                    self.reset()

                if key == 'q':
                    os.system("stty echo")
                    os._exit(0)
                
                if key == 'p':
                    self.ball.held=False
                    self.ball.move_state = True-(self.ball.move_state)
        
                self.screen.out()
                if self.ball.position[0]==DIMENSIONS["height"]-10:
                    self.screen.life-=1
                    self.paddle = Paddle()
                    self.ball = Ball()
            else:
                key = self.get.input_to() 
                self.screen.render()
                self.screen.render_on_screen((9, 47), OVER, clr.Fore.LIGHTRED_EX)
                self.screen.out()

                if key == 'r':
                    self.reset()

                if key == 'q':
                    os.system("stty echo")
                    os._exit(0)



    
    def reset(self):
        self.screen = Screen()
        self.paddle = Paddle()
        self.ball = Ball()
        self.block = Block()
