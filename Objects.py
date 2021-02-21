import numpy as np
from Parameters import *

class Objects:

    string = ""
    array=np.full( ( DIMENSIONS["height"], DIMENSIONS["width"] ) ,' ', dtype="<U20")
    coords=[0,0]

    def __init__(self):
        pass

    def _array_to_string(self):
        temp_list=[]
        for i in self.array:
            temp = i
            temp=''.join(temp)
            temp_list.append(temp)
        return ('\n'.join(temp_list))


    def render(self,screen):
        self.string = self._array_to_string()
        screen.render_on_screen(self.coords, self.string)
