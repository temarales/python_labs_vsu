import math


class Point(object):

    def __init__(self, x_new, y_new):
        self.x = x_new
        self.y = y_new

    @property
    def getX(self):
        return self.x

    @property
    def getY(self):
        return self.y

    def setX(self, x_new):
        self.x = x_new

    def setY(self, y_new):
        self.y = y_new
