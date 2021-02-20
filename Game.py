import os, time
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
    stime = time.time()
    paused = True
    ttime = 0
    ptime = 0
    started=False

    get = Get()

    def __init__(self):
        os.system("stty -echo")

    def run (self):
        while (True):
            if self.screen.life: 
                key = self.get.input_to() 
                if self.paused:
                    self.screen.render(False)
                else:
                    self.screen.render(self.stime+self.ptime)

                self.ball.move_ball(self.paddle, self.block, self.screen)

                for i in (self.block, self.paddle, self.ball):
                    i.render(self.screen)

                if self.paused==False or self.started==False:
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
                    
                    if self.started==False:
                        self.ttime=time.time()
                
                else:
                    self.ttime=time.time()
                    
                if key == 'r':
                    self.reset()

                if key == 'q':
                    os.system("stty echo")
                    os._exit(0)
                
                if key == 'p':
                    self.ball.held=False
                    self.started=True
                    self.ball.move_state = True-(self.ball.move_state)
                    if self.paused == True:
                        self.ptime+= time.time()-self.ttime
                    self.paused= True-(self.paused)
        
                self.screen.out()
                if self.ball.position[0]==DIMENSIONS["height"]-10:
                    self.screen.life-=1
                    self.paddle = Paddle()
                    self.ball = Ball()
                    self.started=False
                    self.paused=True

                self.block.is_over(self.screen)

            else:
                key = self.get.input_to() 
                self.screen.render(False)
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

        self.ptime=0
        self.stime=time.time()
        self.started=False
        self.paused = True
