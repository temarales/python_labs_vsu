from Game.Field import Field
from enum import Enum

class GameState(Enum):
    PLAYING = 0  # game is still going
    END = 1  # game is ended

class Game(object):
    def __init__(self, level, size):
        self.field = Field(size, level) #Размер?
        self.size = size

    def change_positions(self, row1, column1, row2, column2):
        self.field.change_positions(row1, column1, row2, column2)





