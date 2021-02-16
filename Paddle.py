import colorama as clr
from Parameters import *
clr.init()


class Paddle:
    size = 15
    x = 55
    speed = 1

    def __init__(self):
        pass
    
    def render(self, screen):
        screen.render_on_screen((DIMENSIONS['height']-11, (self.x%121)+26), '◖' )
        for i in range(1, self.size-1):
            screen.render_on_screen((DIMENSIONS['height']-11, ((self.x + i)%121)+26), '▮', clr.Back.LIGHTBLUE_EX )
        screen.render_on_screen((DIMENSIONS['height']-11, ((self.x+self.size-1)%121)+26), '◗' )
    
    def move(self, dir):
        if dir:
            self.x+=self.speed
        else:
            self.x-=self.speed
