#!/usr/bin/python

import numpy as np

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

    def step(self, maxX, maxY, t):
        """ Move the mosquito to a new place. Return tuple.  """
        # If already moved this T, stay in this cell
        if self.t >= t:
            return (self.x, self.y)
        else:
            # move in a random direction (hor., vert. or diag.), and do step
            # if it is stays within boundaries
            # newY = self.y + np.random.randint(2) -1 
            # newX = self.x + np.random.randint(2) -1 
            # if 0 <= newY < maxY:
            #     self.y = newY
            # if 0 <= newX < maxX:
            #     self.x = newX

            move = np.random.randint(4)
            # Check the direction, 0 = stay on same place. Also check if it's
            # within the grid boundaries.
            if move == 0 and self.y + 1 < maxY:
                self.y += 1 #Move North
            elif move == 1 and self.x + 1 < maxX:
                self.x += 1 # Move East
            elif move == 2 and self.y - 1 >= 0:
                self.y -= 1 # Move South
            elif move == 3 and self.x - 1 >= 0:
                self.x -= 1 # Move West

        self.t = t
        self.age += 1

        # return tuple of new location
        return (self.x, self.y)

