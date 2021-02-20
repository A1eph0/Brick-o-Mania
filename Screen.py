import numpy as np
import time 
import sys
import colorama as clr
from Parameters import *
clr.init()

def make_borders():
        array = np.full( ( DIMENSIONS["height"], DIMENSIONS["width"] ) ,' ', dtype="<U20")
        vert = BORDERS['vertical']
        hori = BORDERS['horizontal']

        for i in vert:
            col = np.full( ( i[2]-i[1]+1, 1 ) , clr.Back.WHITE + ' ' + RESET, dtype="<U20")
            array[i[1]:i[2]+1,i[0]]= col[:,0]

        for i in hori:
            hor = np.full( ( 1,  i[2]-i[1]+1) , clr.Back.WHITE + ' ' + RESET, dtype="<U20")
            array[i[0], i[1]:i[2]+1]  = hor[0]
        return (array)

static_screen = make_borders()

class Screen:
    screen_array = static_screen
    T = 1/FPS

    def __init__(self):
        self.render_on_screen(TITLE['coord'], TITLE['text'], clr.Fore.LIGHTGREEN_EX)
        self.render_on_screen((TITLE['coord'][0]+2, TITLE['coord'][1]+88), MISC)

    def out(self):
        np.savetxt(sys.stdout,
                   self.screen_array,
                   fmt='%s',
                   delimiter='')

        time.sleep(self.T)
        print('\u001b[{}A'.format(DIMENSIONS["height"]), end='')

    def __string_to_array(self, str):
        return list(str)
    
    def __color_text(self, a, col):
        if (col):
            a = col + a + RESET
        return a
    
    def render_on_screen (self, coord, text, col=False, already=False):
        if already:
            for i in range(12):
                self.screen_array[coord[0]+i, coord[1]:coord[1]+text[i].size]  = text[i]
        else:
            text = text.split('\n')
            text = np.array(text)

            # print(text.size)

            for i in range(text.size):
                text_array=self.__string_to_array(text[i])
                text_array= np.array(text_array,  dtype="<U20")
                color_fn = np.vectorize(self.__color_text, otypes=["<U20"])
                text_array=color_fn(text_array, col)
                self.screen_array[coord[0]+i, coord[1]:coord[1]+text_array.size]  = text_array
    
    def reset_screen(self):
        self.render_on_screen((3, 26), EMPTY)
            
