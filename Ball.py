import numpy as np
from Parameters import *

class Ball:

    position = [DIMENSIONS['height']-13, 87]

    xspeed = 0
    yspeed = 1

    angle = False

    move_state = False

    def __init__(self):
        self.position = [DIMENSIONS['height']-13, 87]


    def move_ball(self, paddle):

        if self.move_state and self.position[0] < DIMENSIONS['height']-10:
            self.position[0]+= 1*self.yspeed
            self.position[1]+= 1*self.xspeed

            if self.position[0] == DIMENSIONS['height']-12:

                
                if (self.position[1]==((paddle.x)%121+26)):
                    self.xspeed=0
                    self.yspeed=-1

                else:
                    for i in range(1, paddle.size-1):
                        if (self.position[1]==((paddle.x+1+i)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed+=1
                            self.xspeed= np.sign(self.xspeed)*(int(i-1/4))
                        
                        elif (self.position[1]+1==((paddle.x-i)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed-=1
                            self.xspeed= np.sign(self.xspeed)*(int(i-1/4))
                        
                        # else:
                        #     print(self.position, (paddle.x+1+i+121)%26, (paddle.x-i+121)%26)

                # print("here:", self.position, (paddle.x)%26)
                # self.move_state = False
                # return 0

            if self.position[0] <= 2 :
                self.yspeed = -self.yspeed
                self.position[0] = 3+(2-self.position[0])
            
            if self.position[0] >= DIMENSIONS['height']-10 :
                self.move_state = False
                return 0
            
            if self.position[1] <= 25 :
                self.xspeed = - self.xspeed
                self.position[1] = 26+(25-self.position[1])

            if self.position[1] >= DIMENSIONS['width']-3 -25 :
                self.xspeed = - self.xspeed
                self.position[1] = DIMENSIONS['width']-3-25-(self.position[1]-(DIMENSIONS['width']-2-25))


            if self.position[0] == DIMENSIONS['height']-12:
                
                if (self.position[1]==paddle.x):
                    self.xspeed=0
                    self.yspeed=-1

                for i in range(1, paddle.size-1):
                    if (self.position[1]==paddle.x+1+i):
                        self.yspeed=-1
                        self.xspeed= int(self.xspeed/abs(self.xspeed))*int(i-1/3)
                    
                    if (self.position[1]+1==paddle.x-i):
                        self.yspeed=-1
                        self.xspeed= int(self.xspeed/abs(self.xspeed))*int(i-1/3)
                    
                     

        
    def render(self, screen):
        screen.render_on_screen((self.position[0], self.position[1]), '⬤' )

# ⬤