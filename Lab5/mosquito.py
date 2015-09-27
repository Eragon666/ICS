#!/usr/bin/python

import numpy as np
from globalFunctions import decision, decisionLogarithmic

class mosquito:

    # 0 = infected = black, 1 = not infected = grey
    colorList = ['black','grey']

    def __init__(self, x, y, t, infected, hungry, age):
        """ Set the basic parameters for the mosquito """
        self.x = x
        self.y = y
        self.t = t
        self.infected = infected
        self.hungry = hungry
        self.age = age

    def getColor(self):
        return self.colorList[self.infected]

    def step(self, maxX, maxY, t, maxAge):
        """ Move the mosquito to a new place. Return tuple.  """

        # If mosquito dies return -1, -1
        if decisionLogarithmic(self.age / float(maxAge)):
            return (-1, -1)

        # If already moved this T, stay in this cell
        if self.t >= t:
            return (self.x, self.y)
        else:
            # move in a random direction (hor., vert. or diag.), and do step
            # if it is stays within boundaries
            newY = self.y + np.random.randint(2) -1 
            newX = self.x + np.random.randint(2) -1 
            if 0 <= newY < maxY:
                self.y = newY
            if 0 <= newX < maxX:
                self.x = newX

        self.t = t
        self.age += 1

        # return tuple of new location
        return (self.x, self.y)

