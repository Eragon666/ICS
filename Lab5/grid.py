#!/usr/bin/pythony

import numpy as np

class grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.human = None
        self.mosquitos = []

    def checkFreedom(self):
        """Check if the human can live here or that there is already an
        inhabitant on this grid"""
        if self.human == None:
            return True
        else:
            return False

    def moveIn(self, human):
        """Add a human to this cell"""
        self.human = human

    def moveOut(self):
        """Remove the human from the cell"""
        self.human = None

    def flyIn(self, mosquito):
        """Fly the mosquito into the cell, multiple mosquitos can be in one
        cell"""
        self.mosquitos.append(mosquito)

    def getMosquitos(self):
        """ return the list of mosquitos in this cell """
        return self.mosquitos

    def clearMosquitos(self):
        """ Clear the list of mosquitos in this cell """
        self.mosquitos = []

    def getInhabitants(self):
        """ return inhabitants in current cell """

        if self.human != None:
            return self.human.getColor()
        elif not self.mosquitos:
            return False
        else:
            return self.mosquitos[0].getColor()

