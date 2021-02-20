import numpy as np
import random
import colorama as clr
from Parameters import *
clr.init()

class Block:
    block_space = np.full( (12,  99) ,' ', dtype="<U20")
    is_there = np.full((12, 11), False)

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
    
    def change_state(self, coords):
        pass

    def render(self, screen):
        screen.render_on_screen((5, 37), self.block_space, False, True)
        
# block=Block()
# block.render()

        
    
    
        
        
