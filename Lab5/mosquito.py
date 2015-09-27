#!/usr/bin/python

import numpy as np
from globalFunctions import decision, decisionLogarithmic
import math
import random

class mosquito:

    # 0 = not infected = grey, 1 = infected = black
    colorList = ['#ECEAE5','black']

    def __init__(self, x, y, t, infected, hungry, age, config, ovi=False, egg=True):
        """ Set the basic parameters for the mosquito """
        self.x = x
        self.y = y
        self.t = t
        self.infected = infected
        self.hungry = hungry  # 0 not hungry, 1 hungry
        self.age = age
        self.egg = False
        self.oviposition = 0
        self.config = config
        self.prevX = 0 
        self.prevY = 0

        if (egg == True):
            self.egg = True
        elif (ovi == True):
            self.oviposition = random.randint(1, 4)

    def getColor(self):
        return self.colorList[self.infected]


    def checkDeath(self,maxAge):
        # If mosquito dies False
        if decisionLogarithmic(self.age / float(maxAge)):
            return True

        return False

    def step(self, maxX, maxY, t):
        """ Move the mosquito to a new place. Return tuple.  """

        # If still an egg
        if self.egg == True:

            # Check if a new mosquito must be born
            if self.age > 5 and decisionLogarithmic(self.config['mosq-egg-time']/self.age) == True:
                self.age = 1
                self.egg = False
            else:
                self.age += 1

            return (self.x, self.y)
        else: 

            # If already moved this T, stay in this cell
            if self.t >= t:
                return (self.x, self.y)
            else:
                # find new location if it is the previous block
                while (self.prevX == self.x and self.prevY == self.y):
                    # move horizontal if staysbetween borders
                    if np.random.randint(2) == 0:
                        newX = self.x + np.random.randint(-1,2)
                        if 0 <= newX < maxX:
                            self.x = newX
                    else:
                        # move veritcal if it stays between borders
                        newY = self.y + np.random.randint(-1,2) 
                        if 0 <= newY < maxY:
                            self.y = newY

                #print "previous xy:",self.prevX , ",", self.prevY, " new:",self.x,",",self.y

                # safe previous direction
                self.prevX = self.x
                self.prevY = self.y

            self.t = t
            self.age += 1

            # return tuple of new location
            return (self.x, self.y)

    def getToHumanStep(self, x, y):
        """ We found a human in the neighbourhoud, go to it """
        self.x = x
        self.y = y
        self.t = t
        self.age += 1
        return (self.x, self.y)
