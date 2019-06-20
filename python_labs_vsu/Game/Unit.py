from random import *
from Game.Color import *
#import random

class Unit(object):
    def __init__(self, color_count):
        self.color = Color(randint(1, color_count))

    @property
    def what_color(self):
        return self.color