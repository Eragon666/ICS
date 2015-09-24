#!/usr/bin/python

import ast

import mosquito as m
import human as h

import numpy as np
import random


class simulation():

    def __init__(self, config):
        """ Initialize the class and save the config """
        self.config = config

    def initalizeGrid(self):
        """ Initialize the grid and the human and mosquito classes """
        config = self.config

        # Get the numbers of humans and mosquitos in the initial state
        popHuman = int(config['pop-human'])
        popMosq = int(config['pop-mosq'])

        nrinfected = popHuman*config['init-distr-human']

        # Generate a list with randomly chosen infected humans based on
        # init-distr-human config value
        infected = random.sample(xrange(popHuman), int(nrinfected))

        # Numpy array with the size of the grix
        grid = np.ndarray(shape=(config['grid-x'] +1, config['grid-y'] + 1), dtype=object)

        for i in range(1, popHuman):
            if i in infected:
                status = 1 #Infected
            else:
                status = 0 #Not infected

            coordinates = self.getCoordinates()
            x = coordinates[0]
            y = coordinates[1]

            grid[x][y] = h.human(x, y,status)

        nrinfected = popMosq*config['init-distr-mosq']

        infected = random.sample(xrange(popMosq), int(nrinfected))

        for i in range(1, popMosq):
            if i in infected:
                status = 1 #infected
            else:
                status = 0

            coordinates = self.getCoordinates()
            x = coordinates[0]
            y = coordinates[1]

            m.mosquito(1,2,status)

    def getCoordinates(self):
        x = random.randint(0, self.config['grid-x'])
        y = random.randint(0, self.config['grid-y'])

        return (x, y)

if __name__ == '__main__':

    with open('config.txt', 'r') as inf:
        config = ast.literal_eval(inf.read())

    sim = simulation(config)

    sim.initalizeGrid()
