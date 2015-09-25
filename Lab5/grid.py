#!/usr/bin/pythony

class grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.human = None
        self.mosquito = []

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
        self.mosquito.append(mosquito)
