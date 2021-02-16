
class Brick:
    
    total = 0


    def __init__(self, x, y, stage):
        self.x = x
        self.y = y
        self.stage = stage

        if (stage > 0):
            Brick.total += 1


    def update_stage(self):
        self.stage -= 1


    @classmethod
    def set_speed(cls, speed):
        cls.speed = speed
