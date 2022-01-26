import random

class Player:

    def __init__(self,name):
        self.name = name

    def scorePoints(self):
        return random.choice([0,1,0,0,1,0,0,1,0,1,0,1,0,1])