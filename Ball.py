import numpy as np
import random
from Parameters import *

class Ball:

    position = [DIMENSIONS['height']-12, 87]

    xspeed = 0
    yspeed = 1
    mult = 1

    angle = False

    move_state = False

    def __init__(self):
        pos=random.choice(range(-6,7))
        self.position = [DIMENSIONS['height']-12, 87+pos]


    def move_ball(self, paddle, block):

        # print( self.yspeed)
        col=self.__checkcol(block)
        
        if col == False and self.move_state and self.position[0] < DIMENSIONS['height']-10:
            if self.position[0] == DIMENSIONS['height']-12:

                
                if (self.position[1]==((paddle.x)%121+26)):
                    self.xspeed=0
                    self.yspeed=-1
                    self.position[0] = DIMENSIONS['height']-12
                    

                else:
                    for i in range(1, paddle.size+1):
                        if (self.position[1]==((paddle.x+i-1)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed+=1
                            self.xspeed= np.sign(self.xspeed)*(int((i-1)/4)+1)
                            self.position[0]
                            self.position[0] = DIMENSIONS['height']-12
                        
                        elif (self.position[1]+1==((paddle.x-i+1)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed-=1
                            self.xspeed= np.sign(self.xspeed)*(int((i-1)/4)+1)
                            self.position[0] = DIMENSIONS['height']-12

            self.position[0]+= self.mult*self.yspeed
            self.position[1]+= 1*self.xspeed

            if self.position[0] == DIMENSIONS['height']-12:
                
                if (self.position[1]==((paddle.x)%121+26)):
                    self.xspeed=0
                    self.yspeed=-1

                else:
                    for i in range(1, paddle.size+1):
                        if (self.position[1]==((paddle.x+i-1)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed+=1
                            self.xspeed= np.sign(self.xspeed)*(int((i-1)/4)+1)
                        
                        elif (self.position[1]+1==((paddle.x-i+1)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed-=1
                            self.xspeed= np.sign(self.xspeed)*(int((i-1)/4)+1)
                        
                        # else:
                        #     print(self.position, (paddle.x+1+i+121)%26, (paddle.x-i+121)%26)

                # print("here:", self.position, (paddle.x)%26)
                # self.move_state = False
                # return 0

            if self.position[0] <= 2 :
                self.yspeed = -self.yspeed
                self.position[0] = 3
            
            if self.position[1] <= 25 :
                self.xspeed = - self.xspeed
                self.position[1] = 26

            if self.position[1] >= DIMENSIONS['width']-3 -25 :
                self.xspeed = - self.xspeed
                self.position[1] = DIMENSIONS['width']-3-25


            if self.position[0] == DIMENSIONS['height']-11:

                
                if (self.position[1]==((paddle.x)%121+26)):
                    self.xspeed=0
                    self.yspeed=-1
                    self.position[0] = DIMENSIONS['height']-12
                    

                else:
                    for i in range(1, paddle.size+1):
                        if (self.position[1]==((paddle.x+i-1)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed+=1
                            self.xspeed= np.sign(self.xspeed)*(int((i-1)/4)+1)
                            self.position[0]
                            self.position[0] = DIMENSIONS['height']-12
                        
                        elif (self.position[1]+1==((paddle.x-i+1)%121+26)):
                            self.yspeed=-1
                            if self.xspeed==0:
                                self.xspeed-=1
                            self.xspeed= np.sign(self.xspeed)*(int((i-1)/4)+1)
                            self.position[0] = DIMENSIONS['height']-12
            
            if self.position[0] >= DIMENSIONS['height']-10 :
                self.move_state = False
                return 0

            if block.position_checker(self.position[0], self.position[1]) or block.position_checker(self.position[0], self.position[1]+1):
                print(self.xspeed, self.yspeed)
                return 0

            # if self.position[0] == DIMENSIONS['height']-11:
            #         print(self.position, (paddle.x)%121+26, (paddle.x)%121+26)
            
                     
    def __checkcol(self, block):
        
        if self.yspeed==abs(self.yspeed):
            first_check= block.position_checker(self.position[0]+1, self.position[1])
            second_check= block.position_checker(self.position[0]+1, self.position[1]+1)

            if first_check or second_check:
                self.yspeed=-self.yspeed
                return True
                # print("here8")

        if self.yspeed==-abs(self.yspeed):
            
            first_check= block.position_checker(self.position[0]-1, self.position[1])
            second_check= block.position_checker(self.position[0]-1, self.position[1]+1)

            if first_check or second_check:
                # print("here: ", self.yspeed)
                self.yspeed=-self.yspeed
                # print("here again: ", self.yspeed)
                return True
                

        if self.xspeed==abs(self.xspeed):
            check=False
            for i in range(abs(self.xspeed)):
                check = check or block.position_checker(self.position[0], self.position[1]+2+i)

            if check:
                self.xspeed=-self.xspeed
                return True
                # print("here6")

        if self.xspeed==-abs(self.xspeed):
            check=False
            for i in range(abs(self.xspeed)):
                check = check or block.position_checker(self.position[0], self.position[1]-1-i)

            if check:
                self.xspeed=-self.xspeed
                return True
                # print("here5")

        if self.xspeed==abs(self.xspeed) and self.yspeed==abs(self.yspeed):
            check=False
            for i in range(abs(self.xspeed)):
                check=check or block.position_checker(self.position[0]+1, self.position[1]+2+i)

            if check:
                self.xspeed=-self.xspeed
                return True
                # print("here4")
        
        if self.xspeed==abs(self.xspeed) and self.yspeed==-abs(self.yspeed):
            check=False
            for i in range(abs(self.xspeed)):
                check= check or block.position_checker(self.position[0]-1, self.position[1]+2+i)

            if check:
                self.xspeed=-self.xspeed
                return True
                # print("here3")

        if self.xspeed==-abs(self.xspeed) and self.yspeed==abs(self.yspeed):
            check=False
            for i in range(abs(self.xspeed)):
                check = check or block.position_checker(self.position[0]+1, self.position[1]-1-i)

            if check:
                self.xspeed=-self.xspeed
                return True
                # print("here2")

        if self.xspeed==-abs(self.xspeed) and self.yspeed==-abs(self.yspeed):
            check=False
            for i in range(abs(self.xspeed)):
                check= check or block.position_checker(self.position[0]-1, self.position[1]-1-i)

            if check:
                self.xspeed=-self.xspeed
                return True
                # print("here1")
                
        return False

        
    def render(self, screen):
        screen.render_on_screen((self.position[0], self.position[1]), '⬤' )

# ⬤