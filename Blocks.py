from Objects import Objects as Object
import numpy as np
import random
import colorama as clr
from Parameters import *
clr.init()

class Block(Object):
    block_space = np.full( (12,  99) ,' ', dtype="<U20")
    is_there = np.full((12, 11), False)
    h_golden=5
    w_golden=5

    def __init__(self):
        self.block_space = np.full( (12,  99) ,' ', dtype="<U20")
        self.is_there = np.full((12, 11), False)
        for i in range(12):
            for j in range(11):
                should=random.choice([True, False, False, False])
                if should:
                    blk_type=random.choice([1, 2, 3, 4])
                    
                    if blk_type == 1 :
                        self.is_there[i][j]=True
                        hor = np.full( ( 1,  9) , clr.Back.GREEN + ' ' + RESET, dtype="<U20")
                        self.block_space[i, (j*9):(j*9)+9]  = hor[0]

                    if blk_type == 2 :
                        self.is_there[i][j]=True
                        hor = np.full( ( 1,  9) , clr.Back.BLUE + ' ' + RESET, dtype="<U20")
                        self.block_space[i, (j*9):(j*9)+9]  = hor[0]
                    
                    if blk_type == 3 :
                        self.is_there[i][j]=True
                        hor = np.full( ( 1,  9) , clr.Back.RED + ' ' + RESET, dtype="<U20")
                        self.block_space[i, (j*9):(j*9)+9]  = hor[0]

                    if blk_type == 4 :
                        self.is_there[i][j]=True
                        hor = np.full( ( 1,  9) , clr.Back.LIGHTWHITE_EX + ' ' + RESET, dtype="<U20")
                        self.block_space[i, (j*9):(j*9)+9]  = hor[0]
        
        self.h_golden=random.choice(range(1, 10))
        self.w_golden=random.choice(range(1, 4))

        for i in range(6):
            self.is_there[self.h_golden][self.w_golden+i]=True
            hor = np.full( ( 1,  9) , clr.Back.LIGHTYELLOW_EX + ' ' + RESET, dtype="<U20")
            self.block_space[self.h_golden, ((self.w_golden+i)*9):((self.w_golden+i)*9)+9]  = hor[0]


    
    # def change_state(self, coords):
    #     pass
    
    def position_checker(self, h, w):
        if h>16 or h<5 or w<37 or w>135: 
            return False
        else:
            temp_width=int((w-37)/9)
            temp_height=int((h-5))
            return(self.is_there[temp_height][temp_width])

    def render(self, screen):
        screen.render_on_screen((5, 37), self.block_space, False, True)

    def is_over(self, screen):
        flag = True
        for i in range(12):
            for j in range(11):
                if self.block_space[i][j*9]!= ' ' and self.block_space[i][j*9] != clr.Back.LIGHTWHITE_EX + ' ' + RESET:
                    flag = False
        if flag:
            screen.life=0
    
    def hit(self, h, w, screen):
        
        i= int((h-5))
        j = int((w-37)/9)

        if self.block_space[i][j*9] == clr.Back.GREEN + ' ' + RESET:
            self.is_there[i][j]=False
            hor = np.full( ( 1,  9) , ' ', dtype="<U20")
            self.block_space[i, (j*9):(j*9)+9]  = hor[0]
            screen.score+=500
        
        elif self.block_space[i][j*9] == clr.Back.BLUE + ' ' + RESET:
            hor = np.full( ( 1,  9) , clr.Back.GREEN + ' ' + RESET, dtype="<U20")
            self.block_space[i, (j*9):(j*9)+9]  = hor[0]
            screen.score+=300
        
        elif self.block_space[i][j*9] == clr.Back.RED + ' ' + RESET:
            hor = np.full( ( 1,  9) , clr.Back.BLUE + ' ' + RESET, dtype="<U20")
            self.block_space[i, (j*9):(j*9)+9]  = hor[0]
            screen.score+=200

        elif self.block_space[i][j*9] == clr.Back.LIGHTYELLOW_EX + ' ' + RESET:
            for j in range(3):
                for i in range(8):
                    self.is_there[self.h_golden-1+j][self.w_golden+i-1]=False
                    hor = np.full( ( 1,  9) , ' ', dtype="<U20")
                    self.block_space[self.h_golden-1+j, ((self.w_golden+i-1)*9):((self.w_golden+i-1)*9)+9]  = hor[0]
            screen.score+=2000
        
# block=Block()
# # block.render()
# block.position_checker(7,135)