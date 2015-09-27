#!/usr/bin/python

import numpy as np

class mosquito:

    # 0 = infected = black, 1 = not infected = grey
    colorList = ['black','grey']

    def __init__(self, x, y, t, infected, hungry, size):
        """ Set the basic parameters for the mosquito """
        self.x = x
        self.y = y
        self.t = t
        self.infected = infected
        self.hungry = hungry
        self.age = np.random.randint(21)
        self.size = size

    def getColor(self):
        return self.colorList[self.infected]

    def step(self, maxX, maxY, t):
        """ Move the mosquito to a new place. Return tuple.  """

        #print 'Current T = ' + str(self.t) + ' & new t = ' + str(t)

        # If already moved this T, stay in this cell
        if self.t >= t:
            return (self.x, self.y)
        else:
            # move in a random direction, and do step
            # if it is stays within boundaries
            newY = self.y + np.random.randint(2) -1 
            newX = self.x + np.random.randint(2) -1 
            if 0 <= newY < maxY:
                self.y = newY
            if 0 <= newX < maxX:
                self.x = newX

        #print 'Moving from ' + str(self.x) + ', ' + str(self.y)
        
        # move = np.random.randint(5)
        # # Check the direction, 0 = stay on same place. Also check if it's
        # # within the grid boundaries.
        # if move == 1 and self.y + 1 < maxY:
        #     self.y += 1 #Move North
        # elif move == 2 and self.x + 1 < maxX:
        #     self.x += 1 # Move East
        # elif move == 3 and self.y - 1 >= 0:
        #     self.y -= 1 # Move South
        # elif move == 4 and self.x - 1 >= 0:
        #     self.x -= 1 # Move West

        self.t = t
        self.age += 1
        # the musquitos becomes hungry every step
        if self.hungry != 0: 
            self.hungry = 1

        #print 'To ' + str(self.x) + ', ' + str(self.y)

        # return tuple of new location
        return (self.x, self.y)

