#!/usr/bin/python

import ast
import time

import mosquito as m
import human as h
import grid as g

import numpy as np
import random


class simulation():

    def __init__(self, config):
        """ Initialize the class and save the config """
        self.config = config
        self.t = 0

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Numpy array with the size of the grid
        self.grid = np.ndarray(shape=(config['grid-x'],
            config['grid-y']), dtype=object)

        # Add a grid instance to the array
        for x in xrange(0, config['grid-y']):
            for y in xrange(0, config['grid-x']):
                self.grid[x][y] = g.grid(x, y)

        self.addHumans()
        self.addMosquitos()

    def addHumans(self):
        """Add humans to the grid, only one human can be on each field"""

        config = self.config
        grid = self.grid

        # Get the numbers of humans in the initial state
        popHuman = int(config['pop-human'])

        # Generate a list with randomly chosen infected humans based on
        # init-distr-human config value
        infected = (np.random.rand(popHuman) > config['init-distr-human']).astype(int)

        for i in xrange(0, popHuman-1):
            found = False

            # Make sure that every grid place has only one human
            while (not found):
                (x,y) = self.getCoordinates()

                if (grid[x][y].checkFreedom() == True):
                    found = True

            grid[x][y].moveIn(h.human(x, y, infected[i]))

    def addMosquitos(self):
        """ Add the mosquitos to the grid, there can be humans and mosquitos on
        the same field and even multiple mosquitos on one field. """

        config = self.config
        grid = self.grid

        # Get the numbers of mosquitos in the initial state
        popMosq = int(config['pop-mosq'])

        # Generate for each mosquito if it's infected or not and if it's hungry 
        # in the initial state. Based on the initial distribution.
        infected = (np.random.rand(popMosq) > config['init-distr-mosq']).astype(int)
        hungry = (np.random.rand(popMosq) > config['init-hungry-mosq']).astype(int)

        for i in xrange(1, popMosq-1):
            (x,y) = self.getCoordinates()

            grid[x][y].flyIn(m.mosquito(x, y, self.t, infected[i], hungry[i]))

    def getCoordinates(self):
        """ Generate a pair of coordinates, return it as a tuple"""
        x = random.randint(0, self.config['grid-x'] - 1)
        y = random.randint(0, self.config['grid-y'] - 1)

        return (x, y)

    def step(self):
        """ Do all the steps """

        self.t += 1

        for x in xrange(0, config['grid-y']):
            for y in xrange(0, config['grid-x']):
                self.stepMosquitos(x, y)

    def stepMosquitos(self, x, y):
        """ Calculate the step for the mosquitos """
        #mosquitos = self.grid[x][y].getMosquitos()
        #self.grid[x][y].clearMosquitos()

        #for mosquito in mosquitos:
        #    (x, y) = mosquito.step(config['grid-x'] - 1, config['grid-y'] - 1, self.t)
        #    self.grid[x][y].flyIn(mosquito)

        # Loop through the list of mosquitos and remove the mosquito from the
        # list if checkMosquito returns False
        self.grid[x][y].mosquitos[:] = [ z for z in self.grid[x][y].mosquitos
                if self.checkMosquito(z, (x,y)) ]


    def checkMosquito(self, mosquito, current):
        """ Check if the mosquitos stays in the same place """

        # Do the calculations for the next position of the mosquito
        (x, y) = mosquito.step(config['grid-x'] - 1, config['grid-y'] - 1, self.t)

        # If the mosquito did not move, return True
        if current == (x, y):
            return True

        # Else place the mosquito in another cell and return False so the
        # mosquitos gets removed from the current field
        self.grid[x][y].flyIn(mosquito)
        return False


if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    start = time.time()
    sim.initalizeGrid()
    end = time.time()
    print end-start

    startSteps = time.time()

    for i in xrange(10):
        sim.step()

    endSteps = time.time()

    print (endSteps-startSteps)/10

