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

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Numpy array with the size of the grid
        self.grid = np.ndarray(shape=(config['grid-x'],
            config['grid-y']), dtype=object)

        # Add a grid instance to the array
        for (x,y), value in np.ndenumerate(self.grid):
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

        for i in range(0, popHuman-1):
            status = infected[i]

            found = False

            # Make sure that every grid place has only one human
            while (not found):
                (x,y) = self.getCoordinates()

                if (grid[x][y].checkFreedom() == True):
                    found = True

            grid[x][y].moveIn(h.human(x, y,status))

    def addMosquitos(self):
        """ Add the mosquitos to the grid, there can be humans and mosquitos on
        the same field and even multiple mosquitos on one field. """

        config = self.config
        grid = self.grid

        # Get the numbers of mosquitos in the initial state
        popMosq = int(config['pop-mosq'])

        # Generate for each mosquito if it's infected or not in the initial
        # state. Based on the initial distribution.
        infected = (np.random.rand(popMosq) > config['init-distr-mosq']).astype(int)

        for i in range(1, popMosq-1):
            status = infected[i]

            (x,y) = self.getCoordinates()

            grid[x][y].flyIn(m.mosquito(x,y,status))

    def getCoordinates(self):
        """ Generate a pair of coordinates, return it as a tuple"""
        x = random.randint(0, self.config['grid-x'] - 1)
        y = random.randint(0, self.config['grid-y'] - 1)

        return (x, y)

if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    start = time.clock()
    sim.initalizeGrid()
    end = time.clock()
    print end-start
