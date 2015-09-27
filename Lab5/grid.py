#!/usr/bin/pythony

import numpy as np
import random

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
        #self.devourHumans(mosquito)

    def devourHumans(self,mosquito):
        """ eat a human if there is one and the mosquito hungry """
        if self.human != None and mosquito.hungry == 1:
            # if the human is infected, so is the mosquito based on probability
            if self.human.status == 1 and decision(0.9):
                mosquito.infected = 1
            # if the human is not immune and mosq is infected, infect human based on probability
            elif self.human.status != 2 and mosquito.infected == 1 and decision(0.8):
                self.human.status = 1

    def decision(probability):
        return random.random() < probability

    def getMosquitos(self):
        """ return the list of mosquitos in this cell """
        return self.mosquitos

    def clearMosquitos(self):
        """ Clear the list of mosquitos in this cell """
        self.mosquitos = []

    def getInhabitants(self):
        """ return inhabitants in current cell """

        if self.human != None:
            return (self.human.getColor(), self.human.size)
        elif not self.mosquitos:
            return (False, False)
        else:
            return (self.mosquitos[0].getColor(), self.mosquitos[0].size)

